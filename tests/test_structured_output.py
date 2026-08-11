from app.llm.chains import structured_travel_chain
from app.llm.schemas import TravelPlan


def test_structured_travel_plan():
    response = structured_travel_chain.invoke(
        {
            "user_request": (
                "Plan a 5-day trip to Goa with a budget of 30000 rupees."
            )
        }
    )

    print("\nRESPONSE:")
    print(response)

    # Verify structured output type
    assert isinstance(response, TravelPlan)

    # Verify destination
    assert response.destination

    # Verify dates
    assert response.start_date
    assert response.end_date

    # Verify activities
    assert isinstance(response.activities, list)
    assert len(response.activities) > 0

    # Verify budget
    assert response.budget > 0

    # Verify travel details
    assert response.transportation
    assert response.accommodation
    assert response.food
    assert response.tips