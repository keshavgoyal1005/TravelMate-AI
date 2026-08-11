from app.tools.restaurant_search import search_restaurant

def test_search_restaurant():
    result = search_restaurant.invoke({"destination": "Paris"})

    assert result == ["Restaurant 1", "Restaurant 2", "Restaurant 3"]


def test_search_restaurant_returns_list():
    result = search_restaurant.invoke({"destination": "Paris"})

    assert isinstance(result, list)

def test_search_restaurant_returns_strings():
    result = search_restaurant.invoke({"destination": "Paris"})

    assert all(isinstance(restaurant, str) for restaurant in result)