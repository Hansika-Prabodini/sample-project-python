# LLM Benchmark Modules

This package contains a collection of Python functions designed to benchmark LLM (Large Language Model) code generation capabilities. Each module focuses on different aspects of programming to test various code generation scenarios.

## Module Overview

### 📊 [algorithms/](algorithms/)
Algorithm implementations for benchmarking computational complexity:
- **primes.py**: Prime number operations (primality testing, prime factorization, prime summation)
- **sort.py**: Sorting algorithms (bubble sort, Dutch flag partition, max-n finder)

### 🔄 [control/](control/)
Control flow benchmarks testing loop constructs:
- **single.py**: Single for-loop operations (sum range, max value, modulus sum)
- **double.py**: Nested for-loop operations (matrix operations, pair counting, duplicates)

### 📦 [datastructures/](datastructures/)
Data structure manipulation benchmarks:
- **dslist.py**: List operations (modify, search, sort, reverse, rotate, merge)

### 🎲 [generator/](generator/)
Random data generation utilities:
- **gen_list.py**: Generate random lists and matrices for testing

### 🗄️ [sql/](sql/)
SQL query execution benchmarks:
- **query.py**: Database operations using SQLite (album queries, joins, invoice aggregations)

### 🔤 [strings/](strings/)
String manipulation benchmarks:
- **strops.py**: String operations (reverse, palindrome checking)

## Usage

All modules are designed with static methods for easy benchmarking. Example:

```python
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.generator.gen_list import GenList

# Test prime operations
result = Primes.is_prime(17)
prime_sum = Primes.sum_primes(100)

# Generate test data
random_data = GenList.random_list(1000, 100)
```

## Benchmarking

This project uses `pytest-benchmark` for performance testing. Run benchmarks with:

```bash
poetry run pytest --benchmark-only tests/
```

## Purpose

These functions are intentionally implemented with varying levels of efficiency to provide diverse benchmarking scenarios for testing LLM code generation, optimization, and understanding capabilities.
