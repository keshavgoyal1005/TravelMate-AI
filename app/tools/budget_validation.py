from langchain_core.tools import tool


@tool
def validate_budget(
    estimated_cost: float,
    budget: float,
) -> bool:
    """
    Validate whether the estimated trip cost fits within the budget.
    """
    return estimated_cost <= budget