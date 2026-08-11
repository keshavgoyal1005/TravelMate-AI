from app.tools.flight_search import search_flight


def test_search_flight():
    result = search_flight.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert result == ["Flight 1", "Flight 2", "Flight 3"]


def test_search_flight_returns_list():
    result = search_flight.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert isinstance(result, list)