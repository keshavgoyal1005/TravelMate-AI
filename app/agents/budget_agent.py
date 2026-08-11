from app.graph.state import TravelState
from app.tools.budget_validation import validate_budget
from app.tools.cost_estimation import estimate_cost


def budget_agent(state: TravelState) -> TravelState:

    # Temporary costs based on the current mock research tools.
    flight_cost = 30000.0
    hotel_cost = 20000.0
    activity_cost = 10000.0
    restaurant_cost = 10000.0

    estimated_cost = estimate_cost.invoke(
        {
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "activity_cost": activity_cost,
            "restaurant_cost": restaurant_cost,
        }
    )

    within_budget = validate_budget.invoke(
        {
            "estimated_cost": estimated_cost,
            "budget": state["budget"],
        }
    )

    return {
        **state,
        "budget_result": {
            "estimated_cost": estimated_cost,
            "within_budget": within_budget,
        },
    }