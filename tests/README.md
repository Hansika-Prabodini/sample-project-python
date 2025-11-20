# Tests

This directory contains unit tests and benchmarks for the llm_benchmark module.

## Structure

The test structure mirrors the source module structure under `src/llm_benchmark/`:

- `llm_benchmark/algorithms/` - Tests for algorithm implementations
- `llm_benchmark/control/` - Tests for control flow operations
- `llm_benchmark/datastructures/` - Tests for data structure operations
- `llm_benchmark/generator/` - Tests for data generation utilities
- `llm_benchmark/sql/` - Tests for SQL operations
- `llm_benchmark/strings/` - Tests for string operations

## Running Tests

### Unit Tests Only

```shell
poetry run pytest --benchmark-skip tests/
```

### Benchmark Tests Only

```shell
poetry run pytest --benchmark-only tests/
```

### All Tests

```shell
poetry run pytest tests/
```

## Test Framework

Tests use `pytest` with `pytest-benchmark` for performance measurement. Each test includes both correctness validation and performance benchmarking.
