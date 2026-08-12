from app.graph.nodes import route_after_budget


def test_route_after_budget_within_budget():

    state = {
        "budget_result": {
            "estimated_cost": 70000,
            "within_budget": True,
        }
    }

    result = route_after_budget(state)

    assert result == "itinerary"


def test_route_after_budget_over_budget():

    state = {
        "budget_result": {
            "estimated_cost": 120000,
            "within_budget": False,
        }
    }

    result = route_after_budget(state)

    assert result == "itinerary"