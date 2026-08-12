from langgraph.graph import StateGraph, START, END

from app.graph.nodes import route_after_research
from app.graph.retry import retry_research, research_fallback
from app.graph.state import TravelState


def test_research_failure_triggers_retries():

    call_count = 0

    def failing_research_agent(state: TravelState) -> TravelState:
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
        "end",
        lambda state: state,
    )

    builder.add_edge(
        START,
        "research",
    )

    builder.add_conditional_edges(
        "research",
        route_after_research,
        {
            "retry_research": "retry_research",
            "fallback": "fallback",
            "budget": "end",
        },
    )

    builder.add_edge(
        "retry_research",
        "research",
    )

    builder.add_edge(
        "fallback",
        END,
    )

    builder.add_edge(
        "end",
        END,
    )

    test_graph = builder.compile()

    result = test_graph.invoke(
        {
            "user_request": (
                "Plan a 5 day trip to Paris "
                "with a budget of 100000"
            )
        }
    )

    # Initial attempt + 2 retries
    assert call_count == 3

    # Two retries were performed
    assert result["research_retry_count"] == 2

    # Research ultimately failed
    assert result["research_success"] is False