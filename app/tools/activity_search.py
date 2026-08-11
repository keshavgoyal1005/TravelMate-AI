from langchain_core.tools import tool

@tool
def search_activity(
    destination: str,
    start_date: str,
    end_date: str,
) -> list[str]:
    """
    Search for an activity based on the destination, start date, and end date.
    """
    return ["Activity 1", "Activity 2", "Activity 3"]
    
    