from app.graph.state import TravelState
from app.llm.client import structured_llm


def itinerary_agent(state: TravelState) -> TravelState:

    plan = state["plan"]
    research = state["research"]
    budget_result = state["budget_result"]

    prompt = f"""
You are the final itinerary planning agent.

Create a complete travel plan using the information below.

PLANNER INFORMATION:
{plan}

RESEARCH INFORMATION:
{research}

BUDGET INFORMATION:
{budget_result}

Create a practical travel plan.

Return:
- destination
- start date
- end date
- activities
- budget
- transportation
- accommodation
- food
- tips

Do not invent information that contradicts the research.
Keep the plan within the user's budget when possible.
"""

    itinerary = structured_llm.invoke(prompt)

    return {
        **state,
        "itinerary": itinerary,
    }