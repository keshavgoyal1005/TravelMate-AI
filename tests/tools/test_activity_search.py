from app.tools.activity_search import search_activity


def test_search_activity():
    result = search_activity.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert result == ["Activity 1", "Activity 2", "Activity 3"]


def test_search_activity_returns_list():
    result = search_activity.invoke({"destination": "Paris", "start_date": "2026-01-01", "end_date": "2026-01-05"})

    assert isinstance(result, list)