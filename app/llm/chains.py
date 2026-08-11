from app.llm.prompts import travel_prompt
from app.llm.client import llm
from app.llm.client import structured_llm


travel_chain = travel_prompt | llm
structured_travel_chain = travel_prompt | structured_llm