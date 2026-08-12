from app.tools.executor import execute_tool_safely
from app.tools.travel_tools import calculate_trip_budget


def test_safe_tool_execution_success():
    result = execute_tool_safely(
        calculate_trip_budget,
        {
            "base_budget": 30000,
            "additional_expenses": 5000,
        },
    )

    assert result == 35000


def test_safe_tool_execution_failure():
    result = execute_tool_safely(
        calculate_trip_budget,
        {
            "base_budget": -30000,
            "additional_expenses": 5000,
        },
    )

    assert result == (
        "Tool execution failed: Base budget cannot be negative"
    )