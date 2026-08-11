from langchain_core.tools import tool

@tool
def search_hotel(
    destination: str,
    start_date: str,
    end_date: str,
) -> list[str]:
    """
    Search for a hotel based on the destination, start date, and end date.
    """
    return ["Hotel 1", "Hotel 2", "Hotel 3"]
    
    