from langchain_core.tools import tool


@tool
def calculate_trip_budget(
    base_budget: float,
    additional_expenses: float
) -> float:
    """
    Calculate the total trip budget including additional expenses.
    """

    if base_budget < 0:
        raise ValueError("Base budget cannot be negative")

    if additional_expenses < 0:
        raise ValueError("Additional expenses cannot be negative")
        
    return base_budget + additional_expenses