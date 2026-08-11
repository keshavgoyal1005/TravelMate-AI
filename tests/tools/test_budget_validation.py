from app.tools.budget_validation import validate_budget


def test_budget_is_valid():
    result = validate_budget.invoke({
        "estimated_cost": 95000,
        "budget": 100000,
    })

    assert result is True


def test_budget_is_exceeded():
    result = validate_budget.invoke({
        "estimated_cost": 120000,
        "budget": 100000,
    })

    assert result is False


def test_cost_equals_budget():
    result = validate_budget.invoke({
        "estimated_cost": 100000,
        "budget": 100000,
    })

    assert result is True