from typing import Any, TypedDict

from app.llm.schemas import PlannerOutput, ResearchOutput, BudgetOutput, TravelPlan


class TravelState(TypedDict, total=False):
    user_request: str

    destination: str
    days: int
    budget: float

    needs_tool: bool
    tool_result: Any

    itinerary: TravelPlan

    plan: PlannerOutput
    research: ResearchOutput
    budget_result: BudgetOutput

    research_retry_count: int
    research_success: bool
    fallback_used: bool