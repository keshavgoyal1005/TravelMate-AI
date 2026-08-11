from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.llm.schemas import TravelPlan, PlannerOutput
from app.tools.travel_tools import calculate_trip_budget



llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=settings.openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)


structured_llm = llm.with_structured_output(TravelPlan)
planner_llm = llm.with_structured_output(PlannerOutput)

tool_llm = llm.bind_tools([calculate_trip_budget])