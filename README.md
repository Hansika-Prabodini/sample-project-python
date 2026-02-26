# LLM Benchmark

A collection of Python functions to benchmark LLM projects with intentionally inefficient implementations for performance testing.

## Overview

This project provides a suite of benchmark functions across multiple domains, designed to test and measure the performance of code analysis and optimization tools, particularly those powered by Large Language Models (LLMs).

## Installation

```bash
poetry install
```

## Modules

### Control Flow (`llm_benchmark.control`)

The control module contains intentionally inefficient loop implementations for benchmarking purposes.

#### Single Loop Functions

Functions that use single loop constructs:

```python
from llm_benchmark.control import sum_range, max_list, sum_modulus

# Sum of range [0, n)
result = sum_range(10)  # Returns 45

# Find maximum value in a list
max_val = max_list([1, 2, 3, 4, 5])  # Returns 5

# Sum of numbers divisible by m in range [0, n)
sum_val = sum_modulus(100, 3)  # Returns sum of 0, 3, 6, ..., 99
```

**Intentional Inefficiencies:**
- `sum_range`: Creates intermediate list instead of direct summation
- `max_list`: Manual iteration instead of using built-in `max()`
- `sum_modulus`: Creates intermediate list for filtered values

#### Double Loop Functions

Functions that use nested loop constructs:

```python
from llm_benchmark.control import (
    sum_square,
    sum_triangle,
    count_pairs,
    count_duplicates,
    sum_matrix
)

# Sum of squares using inefficient nested loops
result = sum_square(10)

# Sum of triangular pattern
result = sum_triangle(10)

# Count elements that appear exactly twice
pairs = count_pairs([1, 1, 2, 2, 3])  # Returns 2

# Count common elements between two arrays
common = count_duplicates([1, 2, 3], [2, 3, 4])  # Returns 2

# Sum all elements in a 2D matrix
total = sum_matrix([[1, 2], [3, 4]])  # Returns 10
```

**Intentional Inefficiencies:**
- `sum_square`: O(n²) nested loops with conditional check
- `sum_triangle`: Nested loops for triangular summation
- `count_pairs`: O(n²) duplicate counting algorithm

### Algorithms (`llm_benchmark.algorithms`)

Prime number operations and sorting algorithms.

**Modules:**
- `llm_benchmark.algorithms.primes`: Prime checking, prime summation, and factorization
- `llm_benchmark.algorithms.sort`: Sorting and partitioning algorithms

### Data Structures (`llm_benchmark.datastructures`)

List manipulation operations.

**Module:**
- `llm_benchmark.datastructures.dslist`: List operations like modify, search, sort, reverse, rotate, and merge

### Strings (`llm_benchmark.strings`)

String manipulation functions.

**Module:**
- `llm_benchmark.strings.strops`: String reversal and palindrome checking

### SQL (`llm_benchmark.sql`)

Database query operations using the Chinook database.

**Module:**
- `llm_benchmark.sql.query`: Album queries, joins, and invoice operations

### Generator (`llm_benchmark.generator`)

Random data generation utilities.

**Module:**
- `llm_benchmark.generator.gen_list`: Generate random lists and matrices

## Usage Example

```python
from llm_benchmark.control import sum_range, count_pairs
from llm_benchmark.generator.gen_list import GenList

# Use control flow functions
total = sum_range(100)
print(f"Sum of range(100): {total}")

# Generate random data and count pairs
random_list = GenList.random_list(30, 10)
pairs = count_pairs(random_list)
print(f"Number of pairs: {pairs}")
```

## Running the Demo

```bash
poetry run main
```

Or:

```bash
python main.py
```

## Development

### Dependencies

- Python ^3.8
- Development tools: pytest, pytest-benchmark, black, isort

### Testing

```bash
poetry run pytest
```

### Benchmarking

The project includes benchmark tests using `pytest-benchmark`:

```bash
poetry run pytest --benchmark-only
```

## Purpose

This benchmark suite is designed to:

1. **Test Code Analysis Tools**: Provide deliberately inefficient code patterns for optimization tools to detect
2. **Benchmark LLM Performance**: Measure how well LLMs can identify and suggest improvements to inefficient code
3. **Performance Testing**: Establish baseline performance metrics for various algorithms

## License

See project metadata for license information.

## Authors

- Matthew <matthew.truscott@turintech.ai>
