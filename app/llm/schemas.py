from pydantic import BaseModel, Field


class TravelPlan(BaseModel):
    destination: str = Field(
        ...,
        description="The destination of the trip",
    )

    start_date: str = Field(
        ...,
        description="The start date of the trip",
    )

    end_date: str = Field(
        ...,
        description="The end date of the trip",
    )

    activities: list[str] = Field(
        ...,
        description="The activities to do in the trip",
    )

    budget: float = Field(
        ...,
        description="The budget for the trip",
    )

    transportation: str = Field(
        ...,
        description="The transportation to use for the trip",
    )

    accommodation: str = Field(
        ...,
        description="The accommodation to use for the trip",
    )

    food: str = Field(
        ...,
        description="The food to eat in the trip",
    )

    tips: str = Field(
        ...,
        description="The tips to follow in the trip",
    )


class PlannerOutput(BaseModel):
    destination: str = Field(
        ...,
        description="The destination of the trip",
    )

    days: int = Field(
        ...,
        description="Number of days for the trip",
    )

    budget: float = Field(
        ...,
        description="Maximum budget for the trip",
    )

    requirements: list[str] = Field(
        default_factory=list,
        description="Special requirements or preferences from the user",
    )


class ResearchOutput(BaseModel):
    flights: list[str] = Field(
        default_factory=list,
        description="Available flight options",
    )

    hotels: list[str] = Field(
        default_factory=list,
        description="Available hotel options",
    )

    activities: list[str] = Field(
        default_factory=list,
        description="Available activity options",
    )

    restaurants: list[str] = Field(
        default_factory=list,
        description="Available restaurant options",
    )

class BudgetOutput(BaseModel):
    estimated_cost: float = Field(
        ...,
        description="The estimated cost of the trip",
    )

    within_budget: bool = Field(
        ...,
        description="Whether the estimated cost is within the budget",
    )