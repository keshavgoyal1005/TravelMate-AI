from app.graph.state import TravelState


MAX_RESEARCH_RETRIES = 3


def retry_research(state: TravelState) -> TravelState:

    current_count = state.get("research_retry_count", 0)

    return {
        **state,
        "research_retry_count": current_count + 1,
    }

def research_fallback(state: TravelState) -> TravelState:

    fallback_research = {
        "flights": [
            "No flight data available. Use a standard flight option."
        ],
        "hotels": [
            "No hotel data available. Use a standard accommodation option."
        ],
        "activities": [
            "No activity data available. Use standard destination activities."
        ],
        "restaurants": [
            "No restaurant data available. Use standard local restaurants."
        ],
    }

    return {
        **state,
        "research": fallback_research,
        "research_success": False,
        "fallback_used": True,
    }
