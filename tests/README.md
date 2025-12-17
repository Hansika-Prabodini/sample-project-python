# Tests

This directory contains the comprehensive test suite for the `llm_benchmark` project. The tests include both unit tests to verify correctness and performance benchmarks to measure execution speed.

## Structure

The test directory mirrors the source code structure:

```
tests/
├── README.md              # This file
└── llm_benchmark/        # Test modules matching src structure
    ├── algorithms/       # Tests for algorithm implementations
    ├── control/          # Tests for control flow operations
    ├── datastructures/   # Tests for data structure operations
    ├── generator/        # Tests for data generators
    ├── sql/             # Tests for SQL queries
    └── strings/         # Tests for string operations
```

## Running Tests

### Run All Tests

To run all unit tests and benchmarks:

```bash
poetry run pytest tests/
```

### Run Unit Tests Only

To skip performance benchmarks and only run functional tests:

```bash
poetry run pytest --benchmark-skip tests/
```

This is useful for quick validation during development.

### Run Benchmarks Only

To run only the performance benchmarks:

```bash
poetry run pytest --benchmark-only tests/
```

This will measure and compare execution times of different implementations.

### Run Specific Test Files

To run tests for a specific module:

```bash
# Test algorithms
poetry run pytest tests/llm_benchmark/algorithms/

# Test control flow
poetry run pytest tests/llm_benchmark/control/

# Test a specific file
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py
```

### Verbose Output

For detailed test output:

```bash
poetry run pytest -v tests/
```

## Test Coverage

The test suite covers:

### Algorithms
- **Primes**: Prime detection (efficient and inefficient), prime summation, prime factorization
- **Sort**: List sorting, Dutch flag partitioning, finding max N elements

### Control Flow
- **Single Loop**: Range summation, list maximum, modulus filtering
- **Double Loop**: Square summation, triangular sums, pair counting, matrix operations

### Data Structures
- **Lists**: Modification, searching, sorting, reversing, rotating, merging

### Generators
- **Random Data**: List generation, matrix generation, boundary conditions

### SQL
- **Queries**: Album searches, table joins, invoice analysis

### Strings
- **Operations**: String reversal, palindrome detection

## Benchmark Tests

Benchmark tests use the `pytest-benchmark` plugin to measure performance. They typically:
- Run the function multiple times to get accurate measurements
- Report statistics including min, max, mean, and standard deviation
- Compare performance of different implementations (e.g., `is_prime` vs `is_prime_ineff`)

Example benchmark output:
```
Name (time in us)                 Min       Max      Mean    StdDev
test_benchmark_is_prime         10.50     25.30    12.40      1.20
test_benchmark_is_prime_ineff  500.20  1,250.80   650.45     85.30
```

## Writing New Tests

When adding new functionality:

1. Create test files matching the module structure
2. Include both unit tests and benchmark tests
3. Use parametrize for testing multiple scenarios:
   ```python
   @pytest.mark.parametrize("input,expected", [
       (5, True),
       (4, False),
   ])
   def test_function(input, expected):
       assert function(input) == expected
   ```

4. Add benchmarks for performance-critical code:
   ```python
   def test_benchmark_function(benchmark):
       result = benchmark(function, arg1, arg2)
       assert result == expected_value
   ```

## Dependencies

The test suite requires:
- `pytest` - Testing framework
- `pytest-benchmark` - Performance benchmarking plugin

These are included in the `dev` dependencies in `pyproject.toml`.
