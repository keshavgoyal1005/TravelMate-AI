from langchain_core.tools import tool


@tool
def search_destination(
    query: str,
) -> list[str]:
    """
    Search for a destination based on a query.
    """
    return ["Paris", "London", "New York"] 



    