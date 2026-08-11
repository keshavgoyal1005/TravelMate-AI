from app.tools.cost_estimation import estimate_cost


def test_estimate_cost():
    result = estimate_cost.invoke({
        "flight_cost": 40000,
        "hotel_cost": 30000,
        "activity_cost": 10000,
        "restaurant_cost": 15000,
    })

    assert result == 95000


def test_estimate_cost_returns_number():
    result = estimate_cost.invoke({
        "flight_cost": 40000,
        "hotel_cost": 30000,
        "activity_cost": 10000,
        "restaurant_cost": 15000,
    })

    assert isinstance(result, (int, float))


def test_estimate_cost_with_zero_values():
    result = estimate_cost.invoke({
        "flight_cost": 0,
        "hotel_cost": 0,
        "activity_cost": 0,
        "restaurant_cost": 0,
    })

    assert result == 0