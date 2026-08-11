from langchain_core.tools import tool


@tool
def estimate_cost(
    flight_cost: float,
    hotel_cost: float,
    activity_cost: float,
    restaurant_cost: float,
) -> float:
    """
    Estimate the total cost of a trip.
    """
    return (
        flight_cost
        + hotel_cost
        + activity_cost
        + restaurant_cost
    )