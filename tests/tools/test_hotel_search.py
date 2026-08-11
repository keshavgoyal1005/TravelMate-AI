from app.tools.hotel_search import search_hotel


def test_search_hotel():
    result = search_hotel.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert result == ["Hotel 1", "Hotel 2", "Hotel 3"]


def test_search_hotel_returns_list():
    result = search_hotel.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert isinstance(result, list)