# Tests Directory

This directory contains unit tests and benchmarks for the LLM Benchmark project.

## Structure

- `__init__.py`: Package initialization
- `llm_benchmark/`: Test modules for the llm_benchmark package
  - Subdirectories mirror the `src/llm_benchmark` module structure
  - Each module has corresponding test files for unit testing and benchmarking

## Running Tests

From the project root:

```bash
# Run all unit tests (skip benchmarks)
poetry run pytest --benchmark-skip tests/

# Run only benchmarks
poetry run pytest --benchmark-only tests/

# Run all tests including benchmarks
poetry run pytest tests/
```

## Test Types

- **Unit Tests**: Verify correctness of implementations
- **Benchmarks**: Measure performance using pytest-benchmark

## Adding Tests

When adding new functionality to the modules in `src/llm_benchmark`, corresponding test files should be added to `tests/llm_benchmark/` with the same directory structure.
