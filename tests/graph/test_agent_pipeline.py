from app.graph.workflow import graph


def test_full_agent_pipeline():

    result = graph.invoke(
        {
            "user_request": (
                "Plan a 5 day trip to Paris "
                "with a budget of 100000"
            )
        }
    )

    # Planner
    assert result["destination"] == "Paris"
    assert result["days"] == 5
    assert result["budget"] == 100000

    # Research
    assert "research" in result
    assert result["research"]["flights"]
    assert result["research"]["hotels"]
    assert result["research"]["activities"]
    assert result["research"]["restaurants"]

    # Budget
    assert "budget_result" in result
    assert result["budget_result"]["estimated_cost"] == 70000
    assert result["budget_result"]["within_budget"] is True

    # Itinerary
    assert "itinerary" in result

    itinerary = result["itinerary"]

    assert itinerary.destination == "Paris"
    assert itinerary.budget > 0
    assert itinerary.activities
    assert itinerary.transportation
    assert itinerary.accommodation
    assert itinerary.food
    assert itinerary.tips