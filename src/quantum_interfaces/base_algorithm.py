from abc import ABC, abstractmethod
from typing import Generic

from .exceptions import ValidationError
from .types import TParams, TResult


class BaseAlgorithm(ABC, Generic[TParams, TResult]):
    """
    Abstract base class for all quantum algorithms.
    It is generic and must be parameterized with input and output types.

    Example:
        class VQEParams(AlgorithmParams):
            operator: str

        class VQEResult(AlgorithmResult):
            energy: float

        class VQEAlgorithm(BaseAlgorithm[VQEParams, VQEResult]):
            ...
    """

    @abstractmethod
    def validate_params(self, params: TParams) -> None:
        """
        Validate the input parameters for the algorithm.
        Should raise a `ValidationError` if the parameters are invalid.
        Pydantic models handle this automatically on instantiation,
        but this method is here for custom, more complex validation logic.
        """
        # Default implementation can be empty if Pydantic validation is sufficient
        pass

    @abstractmethod
    def execute(self, params: TParams) -> TResult:
        """
        Execute the quantum algorithm with the given parameters.
        """
        pass 