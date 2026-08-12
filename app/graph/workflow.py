from langgraph.graph import StateGraph, START, END
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
    END,
)

checkpointer = InMemorySaver()


graph = builder.compile(
    checkpointer=checkpointer,
)