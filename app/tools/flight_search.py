from langchain_core.tools import tool

@tool
def search_flight(
    destination: str,
    start_date: str,
    end_date: str,
) -> list[str]:
    """
    Search for a flight based on the destination, start date, and end date.
    """
    return ["Flight 1", "Flight 2", "Flight 3"]