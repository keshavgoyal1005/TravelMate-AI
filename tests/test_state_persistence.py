from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from app.graph.state import TravelState


def create_test_graph():

    def planner_node(state: TravelState) -> TravelState:
        return {
            **state,
            "destination": "Paris",
            "days": 5,
            "budget": 100000,
        }

    builder = StateGraph(TravelState)

    builder.add_node(
        "planner",
        planner_node,
    )

    builder.add_edge(
        START,
        "planner",
    )

    builder.add_edge(
        "planner",
        END,
    )

    checkpointer = InMemorySaver()

    return builder.compile(
        checkpointer=checkpointer,
    )


def test_graph_persists_state():

    graph = create_test_graph()

    config = {
        "configurable": {
            "thread_id": "test-trip-123",
        }
    }

    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
        },
        config=config,
    )

    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000

    saved_state = graph.get_state(config)

    assert saved_state.values["destination"] == "Paris"
    assert saved_state.values["days"] == 5
    assert saved_state.values["budget"] == 100000


def test_graph_recovers_state_from_thread():

    graph = create_test_graph()

    config = {
        "configurable": {
            "thread_id": "test-trip-456",
        }
    }

    graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
        },
        config=config,
    )

    saved_state = graph.get_state(config)

    assert saved_state.values["user_request"] == (
        "Plan a trip to Paris"
    )

    assert saved_state.values["destination"] == "Paris"
    assert saved_state.values["days"] == 5
    assert saved_state.values["budget"] == 100000