from app.graph.nodes import route_after_research


def test_research_success_routes_to_budget():

    state = {
        "research_success": True,
        "research_retry_count": 0,
    }

    assert route_after_research(state) == "budget"


def test_research_failure_routes_to_retry():

    state = {
        "research_success": False,
        "research_retry_count": 0,
    }

    assert route_after_research(state) == "retry_research"


def test_research_failure_after_max_retries_routes_to_fallback():

    state = {
        "research_success": False,
        "research_retry_count": 2,
    }

    assert route_after_research(state) == "fallback"