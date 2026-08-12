from app.agents.research_agent import research_agent


def test_research_agent():

    state = {
        "user_request": "Plan a trip to Paris",
        "destination": "Paris",
        "days": 5,
        "budget": 100000,
    }

    result = research_agent(state)

    assert "research" in result

    assert result["research"]["flights"]
    assert result["research"]["hotels"]
    assert result["research"]["activities"]
    assert result["research"]["restaurants"]