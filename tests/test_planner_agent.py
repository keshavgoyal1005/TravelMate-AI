from app.agents.planner_agent import planner_agent


def test_planner_agent():
    state = {
        "user_request": (
            "Plan a 5 day trip to Paris "
            "with a budget of 100000"
        )
    }

    result = planner_agent(state)

    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000
    assert result["plan"] is not None