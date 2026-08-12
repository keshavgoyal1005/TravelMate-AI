from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from langgraph.checkpoint.memory import InMemorySaver

from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent
from app.agents.budget_agent import budget_agent
from app.agents.itinerary_agent import itinerary_agent

from app.graph.retry import retry_research, research_fallback

from app.graph.nodes import (
    route_after_research,
    route_after_budget,
)

from app.graph.state import TravelState

def human_approval_node(state):
    decision = interrupt(
        {
            "type": "approval",
            "message": "Do you approve this travel plan?",
            "destination": state.get("destination"),
            "days": state.get("days"),
            "budget": state.get("budget"),
        }
    )

    return {
        "approval": decision["action"],
        "approval_reason": decision.get("reason"),
        "requested_changes": decision.get("changes", {}),
    }

def route_after_approval(state):
    if state.get("approval") == "approve":
        return "approved"

    if state.get("approval") == "reject":
        return "rejected"

    if state.get("approval") == "change":
        return "changed"

    raise ValueError(
        f"Unknown approval decision: {state.get('approval')}"
    )


def rejection_node(state):
    return {
        "rejection_reason": state.get("approval_reason")
    }

def apply_human_changes(state):
    changes = state.get("requested_changes", {})

    updated_state = {}

    if "budget" in changes:
        updated_state["budget"] = changes["budget"]

    if "days" in changes:
        updated_state["days"] = changes["days"]

    if "destination" in changes:
        updated_state["destination"] = changes["destination"]

    return updated_state

builder = StateGraph(TravelState)


# -------------------------
# Nodes
# -------------------------

builder.add_node(
    "planner",
    planner_agent,
)

builder.add_node(
    "research",
    research_agent,
)

builder.add_node(
    "retry_research",
    retry_research,
)

builder.add_node(
    "fallback",
    research_fallback,
)

builder.add_node(
    "budget",
    budget_agent,
)

builder.add_node(
    "itinerary",
    itinerary_agent,
)

builder.add_node(
    "human_approval", 
    human_approval_node,
)

builder.add_node(
    "rejection",
    rejection_node,
)

builder.add_node(
    "apply_human_changes",
    apply_human_changes,
)
# -------------------------
# START → Planner
# -------------------------

builder.add_edge(
    START,
    "planner",
)


# -------------------------
# Planner → Research
# -------------------------

builder.add_edge(
    "planner",
    "research",
)


# -------------------------
# Research Routing
# -------------------------

builder.add_conditional_edges(
    "research",
    route_after_research,
    {
        "budget": "budget",
        "retry_research": "retry_research",
        "fallback": "fallback",
    },
)


# -------------------------
# Retry → Research
# -------------------------

builder.add_edge(
    "retry_research",
    "research",
)


# -------------------------
# Fallback → Budget
# -------------------------

builder.add_edge(
    "fallback",
    "budget",
)


# -------------------------
# Budget Routing
# -------------------------

builder.add_conditional_edges(
    "budget",
    route_after_budget,
    {
        "itinerary": "itinerary",
    },
)


# -------------------------
# Itinerary → END
# -------------------------

builder.add_edge(
    "itinerary",
    "human_approval",
)

builder.add_conditional_edges(
    "human_approval",
    route_after_approval,
    {
        "approved": END,
        "rejected": "rejection",
        "changed": "apply_human_changes",
    },
)

builder.add_edge(
    "apply_human_changes",
    "itinerary",
)

builder.add_edge(
    "rejection",
    END,
)

checkpointer = InMemorySaver()


graph = builder.compile(
    checkpointer=checkpointer,
)