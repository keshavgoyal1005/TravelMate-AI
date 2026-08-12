from app.graph.workflow import graph
from langgraph.types import Command


def test_graph_pauses_for_human_approval():
    config = {
        "configurable": {
            "thread_id": "hitl-test-1"
        }
    }

    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        },
        config=config,
    )

    assert "__interrupt__" in result

    interrupts = result["__interrupt__"]

    assert len(interrupts) == 1

    approval_request = interrupts[0].value

    assert approval_request["type"] == "approval"
    assert approval_request["message"] == "Do you approve this travel plan?"


def test_graph_pauses_before_final_state():
    config = {
        "configurable": {
            "thread_id": "hitl-pause-test"
        }
    }

    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        },
        config=config,
    )

    assert "__interrupt__" in result

    interrupts = result["__interrupt__"]

    assert len(interrupts) == 1

    approval_request = interrupts[0].value

    assert approval_request["type"] == "approval"

    # The graph must be waiting for human input.
    assert "approval" not in result


def test_graph_resumes_after_human_approval():
    config = {
        "configurable": {
            "thread_id": "hitl-approval-test"
        }
    }

    # First execution pauses at human approval.
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        },
        config=config,
    )

    assert "__interrupt__" in result

    # Human approves the plan.
    result = graph.invoke(
        Command(
            resume={
                "action": "approve"
            }
        ),
        config=config,
    )

    # Graph should now finish.
    assert "__interrupt__" not in result

    # Human decision should be stored.
    assert result["approval"] == "approve"








def test_graph_handles_human_rejection():
    config = {
        "configurable": {
            "thread_id": "hitl-rejection-test"
        }
    }

    # First execution pauses at human approval.
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        },
        config=config,
    )

    assert "__interrupt__" in result

    # Human rejects the plan.
    result = graph.invoke(
        Command(
            resume={
                "action": "reject",
                "reason": "The budget is too high",
            }
        ),
        config=config,
    )

    # Graph should finish.
    assert "__interrupt__" not in result

    # Rejection should be recorded.
    assert result["approval"] == "reject"
    assert result["approval_reason"] == "The budget is too high"
    assert result["rejection_reason"] == "The budget is too high"




def test_graph_handles_human_changes():
    config = {
        "configurable": {
            "thread_id": "hitl-change-test"
        }
    }

    # First execution pauses for approval.
    result = graph.invoke(
        {
            "user_request": "Plan a trip to Paris"
        },
        config=config,
    )

    assert "__interrupt__" in result

    # Human requests a budget change.
    result = graph.invoke(
        Command(
            resume={
                "action": "change",
                "changes": {
                    "budget": 80000
                }
            }
        ),
        config=config,
    )

    # The graph should run again and reach another approval checkpoint.
    assert "__interrupt__" in result

    approval_request = result["__interrupt__"][0].value

    assert approval_request["type"] == "approval"
    assert approval_request["budget"] == 80000