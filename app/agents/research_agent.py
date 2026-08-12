from app.graph.state import TravelState
from app.tools.activity_search import search_activity
from app.tools.flight_search import search_flight
from app.tools.hotel_search import search_hotel
from app.tools.restaurant_search import search_restaurant


def research_agent(state: TravelState) -> TravelState:

    destination = state["destination"]

    # We currently don't have dates in PlannerOutput.
    # Use placeholder dates for the existing search-tool interface.
    start_date = "Not specified"
    end_date = "Not specified"

    flights = search_flight.invoke(
        {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
        }
    )

    hotels = search_hotel.invoke(
        {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
        }
    )

    activities = search_activity.invoke(
        {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
        }
    )

    restaurants = search_restaurant.invoke(
        {
            "destination": destination,
        }
    )

    research = {
        "flights": flights,
        "hotels": hotels,
        "activities": activities,
        "restaurants": restaurants,
    }

    return {
        **state,
        "research": research,
        "research_success": True,
        "research_retry_count": state.get("research_retry_count", 0),
    }