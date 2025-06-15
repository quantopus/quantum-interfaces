from typing import Any, Dict, TypeVar

from pydantic import BaseModel, Field

# Generic type for algorithm parameters
TParams = TypeVar("TParams", bound="AlgorithmParams")

# Generic type for algorithm results
TResult = TypeVar("TResult", bound="AlgorithmResult")


class AlgorithmParams(BaseModel):
    """Base model for algorithm input parameters."""

    class Config:
        extra = "forbid"  # Forbid any extra fields to ensure strict validation


class AlgorithmResult(BaseModel):
    """Base model for algorithm execution results."""

    meta: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the execution.") 