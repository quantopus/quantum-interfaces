# src/quantum_interfaces/exceptions.py

class AlgorithmError(Exception):
    """Base exception for all algorithm-related errors."""
    pass


class ValidationError(AlgorithmError):
    """Raised when algorithm parameters fail validation."""
    pass


class ExecutionError(AlgorithmError):
    """Raised when an error occurs during algorithm execution."""
    pass 