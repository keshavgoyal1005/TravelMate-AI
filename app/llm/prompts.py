from langchain_core.prompts import ChatPromptTemplate


travel_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are TravelMate, an AI travel assistant. "
            "Help users plan practical and useful trips."
        ),
        (
            "human",
            "{user_request}"
        ),
    ]
)