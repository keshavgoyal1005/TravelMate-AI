from app.graph.workflow import graph


def test_travel_graph():
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        }
    )

    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000
    assert result["tool_result"] == 105000
    assert "Paris" in result["itinerary"]


def test_travel_graph_without_tool():
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris",
            "needs_tool": False,
        }
    )

    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000
    assert "itinerary" in result
    assert "Paris" in result["itinerary"]
    assert "tool_result" not in result