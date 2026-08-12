from app.graph.workflow import graph


def test_research_results_are_added_to_state():
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
            "needs_tool": False,
        }
    )

    assert "research" in result

    research = result["research"]

    assert research["flights"]
    assert research["hotels"]
    assert research["activities"]
    assert research["restaurants"]