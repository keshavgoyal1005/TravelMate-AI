from typing import Any, TypedDict

from app.llm.schemas import PlannerOutput, ResearchOutput, BudgetOutput


class TravelState(TypedDict, total=False):
    user_request: str

    destination: str
    days: int
    budget: float

    needs_tool: bool
    tool_result: Any

    itinerary: str

    plan: PlannerOutput
    research: ResearchOutput
    budget_result: BudgetOutput