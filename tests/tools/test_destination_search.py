from app.tools.destination_search import search_destination


def test_search_destination():
    result = search_destination.invoke({"query": "Europe"})

    assert result == ["Paris", "London", "New York"]


def test_search_destination_returns_list():
    result = search_destination.invoke({"query": "Europe"})

    assert isinstance(result, list)


def test_search_destination_returns_strings():
    result = search_destination.invoke({"query": "Europe"})

    assert all(isinstance(destination, str) for destination in result)