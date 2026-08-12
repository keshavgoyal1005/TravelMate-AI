from app.graph.workflow import graph


def test_research_success_goes_directly_to_budget():

    result = graph.invoke(
        {
            "user_request": (
                "Plan a 5 day trip to Paris "
                "with a budget of 100000"
            )
        }
    )

    # Research succeeded
    assert result["research_success"] is True

    # No retry was needed
    assert result["research_retry_count"] == 0

    # Workflow continued to Budget
    assert "budget_result" in result

    # Workflow continued to Itinerary
    assert "itinerary" in result

    assert result["itinerary"].destination == "Paris"