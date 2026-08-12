from app.graph.workflow import graph


def test_budget_agent_in_graph():

    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
            "needs_tool": False,
        },
        config={
            "configurable": {
                "thread_id": "test-budget-graph"
            }
        }
    )

    assert "budget_result" in result

    budget_result = result["budget_result"]

    assert budget_result["estimated_cost"] == 70000
    assert budget_result["within_budget"] is True