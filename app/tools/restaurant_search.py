from langchain_core.tools import tool

@tool
def search_restaurant(
    destination: str
) -> list[str]:
    """
    Search for a restaurant based on the destination
    """
    return ["Restaurant 1", "Restaurant 2", "Restaurant 3"]
    
    