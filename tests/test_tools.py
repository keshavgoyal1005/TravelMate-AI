import pytest

from app.tools.travel_tools import calculate_trip_budget


def test_calculate_trip_budget():
    result = calculate_trip_budget.invoke(
        {
            "base_budget": 30000,
            "additional_expenses": 5000,
        }
    )

    assert result == 35000


def test_calculate_trip_budget_rejects_negative_budget():
    with pytest.raises(
        ValueError, 
        match="Base budget cannot be negative",
    ):
        calculate_trip_budget.invoke(
            {
                "base_budget": -30000,
                "additional_expenses": 5000,
            }
        )