# llm-benchmark

A collection of Python functions and utilities designed to benchmark Large Language Model (LLM) projects. This library provides various computational tasks, algorithms, and data structure operations that can be used to evaluate and measure the performance of LLM-generated code.

## Overview

This benchmarking suite contains implementations of common programming patterns and algorithms across multiple domains:

- **Algorithms**: Prime number operations, sorting algorithms
- **Control Structures**: Single and nested loop patterns
- **Data Structures**: List operations including search, sort, reverse, rotate, and merge
- **String Operations**: String manipulation and palindrome detection
- **SQL Queries**: Database query operations
- **Generators**: Utility functions for generating test data

## Features

### Algorithms Module
- **Primes**: Prime number checking, sum of primes, prime factorization
- **Sort**: Sorting algorithms, Dutch flag partition, finding max N elements

### Control Structures Module
- **Single For Loops**: Sum range, find max in list, sum with modulus
- **Double For Loops**: Sum of squares, triangle sums, pair counting, matrix operations

### Data Structures Module
- **DsList**: Comprehensive list operations including:
  - Modify, search, sort, reverse operations
  - List rotation by N positions
  - List merging

### String Operations Module
- **StrOps**: String reversal and palindrome checking

### SQL Module
- **SqlQuery**: Album queries, join operations, invoice queries

### Generator Module
- **GenList**: Random list and matrix generation for testing

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Prerequisites
- Python 3.8 or higher
- Poetry

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd llm-benchmark
```

2. Install dependencies:
```bash
poetry install
```

## Usage

### Running the Main Demo

Execute all benchmark examples:

```bash
poetry run main
```

### Using as a Library

```python
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.strings.strops import StrOps

# Prime number operations
print(Primes.is_prime_ineff(17))  # True
print(Primes.sum_primes(20))      # Sum of primes up to 20

# List operations
test_list = [1, 2, 3, 4, 5]
rotated = DsList.rotate_list(test_list, 2)  # [3, 4, 5, 1, 2]
reversed_list = DsList.reverse_list(test_list)  # [5, 4, 3, 2, 1]

# String operations
print(StrOps.palindrome("racecar"))  # True
print(StrOps.str_reverse("hello"))   # "olleh"
```

## Testing

### Run Unit Tests

Execute all unit tests without benchmarking:

```bash
poetry run pytest --benchmark-skip tests/
```

### Run Benchmarks

Execute performance benchmarks:

```bash
poetry run pytest --benchmark-only tests/
```

### Run All Tests

Run both unit tests and benchmarks:

```bash
poetry run pytest tests/
```

## Project Structure

```
llm-benchmark/
├── src/
│   └── llm_benchmark/
│       ├── algorithms/      # Prime and sorting algorithms
│       ├── control/         # Loop control structures
│       ├── datastructures/  # List and data structure operations
│       ├── strings/         # String manipulation functions
│       ├── sql/             # SQL query operations
│       └── generator/       # Test data generators
├── tests/                   # Unit tests and benchmarks
├── main.py                  # Demo script
├── pyproject.toml          # Poetry configuration
└── README.md               # This file
```

## Development

### Code Formatting

This project uses `black` and `isort` for code formatting:

```bash
poetry run black .
poetry run isort .
```

### Running Tests During Development

```bash
poetry run pytest -v tests/
```

## Contributing

Contributions are welcome! Please ensure that:

1. All tests pass before submitting a pull request
2. New features include appropriate unit tests
3. Code follows the project's formatting standards (black, isort)
4. Documentation is updated for new features

## License

This project is maintained by TurinTech AI.

## Authors

- Matthew Truscott (matthew.truscott@turintech.ai)
```
