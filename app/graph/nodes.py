from app.graph.state import TravelState
from app.tools.travel_tools import calculate_trip_budget
from app.tools.executor import execute_tool_safely


def planner_node(state: TravelState) -> TravelState:
    print("Running planner node")

    state["destination"] = "Paris"
    state["days"] = 5
    state["budget"] = 100000
    if "needs_tool" not in state:
        state["needs_tool"] = True

    return state


def tool_node(state: TravelState) -> TravelState:
    print("Running tool node")

    arguments = {
        "base_budget": state["budget"],
        "additional_expenses": 5000,
    }

    result = execute_tool_safely(
        calculate_trip_budget,
        arguments,
    )

    state["tool_result"] = result

    return state


def finalize_node(state: TravelState) -> TravelState:
    print("Running finalize node")

    destination = state["destination"]
    days = state["days"]
    budget = state["budget"]
    total_budget = state.get("tool_result", budget)

    state["itinerary"] = (
        f"{days}-day trip to {destination} "
        f"with a base budget of ₹{budget:.0f}. "
        f"Total budget including additional expenses: "
        f"₹{total_budget:.0f}"
    )

    return state


def route_after_planning(state: TravelState) -> str:
    if state.get("needs_tool", False):
        return "tool"

    return "finalize"