from langgraph.types import Command

from app.graph.workflow import graph


from langgraph.types import Command

from app.graph.workflow import graph


def test_travel_graph():
    config = {
        "configurable": {
            "thread_id": "test-travel-graph"
        }
    }

    # Start the graph
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
            "needs_tool": True,
        },
        config=config,
    )

    # Graph should pause for human approval
    assert "__interrupt__" in result

    # Human approves the plan
    result = graph.invoke(
        Command(
            resume={
                "action": "approve"
            }
        ),
        config=config,
    )

    # Approved path should complete successfully
    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000
    assert result["approval"] == "approve"


def test_travel_graph_without_tool():
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
            "needs_tool": False,
        },
        config={
            "configurable": {
                "thread_id": "test-travel-graph-without-tool"
            }
        }
    )

    assert result["plan"].destination == "Paris"