from app.graph.retry import research_fallback


def test_research_fallback():

    state = {
        "user_request": "Plan a trip to Paris",
        "destination": "Paris",
        "days": 5,
        "budget": 100000,
        "research_success": False,
        "research_retry_count": 2,
    }

    result = research_fallback(state)

    assert result["fallback_used"] is True

    assert result["research_success"] is False

    assert "research" in result

    assert result["research"]["flights"]
    assert result["research"]["hotels"]
    assert result["research"]["activities"]
    assert result["research"]["restaurants"]