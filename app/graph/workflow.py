from langgraph.graph import StateGraph, START, END

from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent

from app.graph.state import TravelState

from app.graph.nodes import (
    tool_node,
    finalize_node,
    route_after_planning,
)


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
    "tool",
    tool_node,
)

builder.add_node(
    "finalize",
    finalize_node,
)


# -------------------------
# Starting point
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
# Research routing
# -------------------------

builder.add_conditional_edges(
    "research",
    route_after_planning,
    {
        "tool": "tool",
        "finalize": "finalize",
    },
)


# -------------------------
# Tool → Finalize
# -------------------------

builder.add_edge(
    "tool",
    "finalize",
)


# -------------------------
# Finalize → END
# -------------------------

builder.add_edge(
    "finalize",
    END,
)


graph = builder.compile()