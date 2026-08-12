from langgraph.graph import StateGraph, START, END

from app.graph.nodes import (
    route_after_research,
    route_after_budget,
)

from app.graph.retry import (
    retry_research,
    research_fallback,
)

from app.graph.state import TravelState

from app.agents.budget_agent import budget_agent

from app.llm.schemas import TravelPlan


def fake_itinerary_agent(state: TravelState) -> TravelState:

    itinerary = TravelPlan(
        destination=state["destination"],
        start_date="Not specified",
        end_date="Not specified",
        activities=[
            "Visit Paris",
        ],
        budget=state["budget"],
        transportation="Metro",
        accommodation="Hotel",
        food="Local food",
        tips="Book attractions in advance",
    )

    return {
        **state,
        "itinerary": itinerary,
    }


def test_fallback_continues_to_budget_and_itinerary():

    call_count = 0

    # --------------------------------
    # Fake Research Agent
    # --------------------------------

    def failing_research_agent(
        state: TravelState,
    ) -> TravelState:

        nonlocal call_count

        call_count += 1

        return {
            **state,
            "research_success": False,
            "research_retry_count": state.get(
                "research_retry_count",
                0,
            ),
        }

    # --------------------------------
    # Build isolated test graph
    # --------------------------------

    builder = StateGraph(TravelState)

    builder.add_node(
        "research",
        failing_research_agent,
    )

    builder.add_node(
        "retry_research",
        retry_research,
    )

    builder.add_node(
        "fallback",
        research_fallback,
    )

    builder.add_node(
        "budget",
        budget_agent,
    )

    builder.add_node(
        "itinerary",
        fake_itinerary_agent,
    )

    # --------------------------------
    # START → Research
    # --------------------------------

    builder.add_edge(
        START,
        "research",
    )

    # --------------------------------
    # Research Routing
    # --------------------------------

    builder.add_conditional_edges(
        "research",
        route_after_research,
        {
            "budget": "budget",
            "retry_research": "retry_research",
            "fallback": "fallback",
        },
    )

    # --------------------------------
    # Retry → Research
    # --------------------------------

    builder.add_edge(
        "retry_research",
        "research",
    )

    # --------------------------------
    # Fallback → Budget
    # --------------------------------

    builder.add_edge(
        "fallback",
        "budget",
    )

    # --------------------------------
    # Budget → Itinerary
    # --------------------------------

    builder.add_conditional_edges(
        "budget",
        route_after_budget,
        {
            "itinerary": "itinerary",
        },
    )

    # --------------------------------
    # Itinerary → END
    # --------------------------------

    builder.add_edge(
        "itinerary",
        END,
    )

    test_graph = builder.compile()

    # --------------------------------
    # Initial State
    # --------------------------------

    result = test_graph.invoke(
        {
            "user_request": (
                "Plan a 5 day trip to Paris "
                "with a budget of 100000"
            ),

            "destination": "Paris",

            "days": 5,

            "budget": 100000,

            "plan": {
                "destination": "Paris",
                "days": 5,
                "budget": 100000,
                "requirements": [],
            },
        }
    )

    # --------------------------------
    # Research was attempted 3 times
    # --------------------------------

    assert call_count == 3

    # --------------------------------
    # Fallback was used
    # --------------------------------

    assert result["fallback_used"] is True

    # --------------------------------
    # Fallback research exists
    # --------------------------------

    assert result["research"]["flights"]

    assert result["research"]["hotels"]

    assert result["research"]["activities"]

    assert result["research"]["restaurants"]

    # --------------------------------
    # Budget Agent ran
    # --------------------------------

    assert "budget_result" in result

    # --------------------------------
    # Itinerary Agent ran
    # --------------------------------

    assert "itinerary" in result

    assert result["itinerary"].destination == "Paris"