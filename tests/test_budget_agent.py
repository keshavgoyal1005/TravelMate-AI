from app.agents.budget_agent import budget_agent


def test_budget_agent():

    state = {
        "user_request": "Plan a trip to Paris",
        "destination": "Paris",
        "days": 5,
        "budget": 100000,
    }

    result = budget_agent(state)

    assert "budget_result" in result

    budget_result = result["budget_result"]

    assert budget_result["estimated_cost"] == 70000
    assert budget_result["within_budget"] is True