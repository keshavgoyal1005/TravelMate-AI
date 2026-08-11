from app.graph.state import TravelState
from app.llm.client import planner_llm


def planner_agent(state: TravelState) -> TravelState:

    user_request = state["user_request"]

    prompt = f"""
You are a travel planning agent.

Analyze the user's travel request and extract the travel requirements.

User request:
{user_request}

Extract:

- destination
- number of days
- maximum budget
- special requirements or preferences

If the user does not specify the number of days,
use 5 days.

If the user does not specify a budget,
use 100000.

Do not perform research.
Do not search for hotels.
Do not check weather.
Do not create an itinerary.

Only understand and structure the user's request.
"""

    plan = planner_llm.invoke(prompt)

    return {
        **state,
        "plan": plan,
        "destination": plan.destination,
        "days": plan.days,
        "budget": plan.budget,
        "needs_tool": state.get("needs_tool", True),
    }