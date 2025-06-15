# Quantum Interfaces

Base interfaces and types for quantum algorithms in the Quantopus ecosystem.

## Overview

This package provides the foundational interfaces and data structures used across all quantum algorithm implementations:

- `BaseAlgorithm[TParams, TResult]` - Generic base class for quantum algorithms
- Parameter and result types with Pydantic validation
- Common quantum computing utilities

## Installation

```bash
make dev-install
```

## Usage

```python
from quantum_interfaces import BaseAlgorithm, BaseParams, BaseResult

# Implement your quantum algorithm
class MyAlgorithm(BaseAlgorithm[MyParams, MyResult]):
    def execute(self, params: MyParams) -> MyResult:
        # Your implementation here
        pass
```

## Development

```bash
make test     # Run tests
make lint     # Check code quality
make format   # Format code
```

Part of the [Quantopus](https://github.com/quantopus) quantum computing ecosystem.
