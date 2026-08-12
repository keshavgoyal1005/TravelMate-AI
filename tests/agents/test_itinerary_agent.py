from app.agents.itinerary_agent import itinerary_agent


def test_itinerary_agent():

    state = {
        "user_request": "Plan a 5 day trip to Paris",

        "destination": "Paris",
        "days": 5,
        "budget": 100000,

        "plan": {
            "destination": "Paris",
            "days": 5,
            "budget": 100000,
            "requirements": [],
        },

        "research": {
            "flights": ["Flight 1", "Flight 2"],
            "hotels": ["Hotel 1", "Hotel 2"],
            "activities": ["Activity 1", "Activity 2"],
            "restaurants": ["Restaurant 1", "Restaurant 2"],
        },

        "budget_result": {
            "estimated_cost": 70000,
            "within_budget": True,
        },
    }

    result = itinerary_agent(state)

    assert "itinerary" in result

    itinerary = result["itinerary"]

    assert itinerary.destination == "Paris"
    assert itinerary.budget > 0
    assert itinerary.activities
    assert itinerary.transportation
    assert itinerary.accommodation
    assert itinerary.food
    assert itinerary.tips