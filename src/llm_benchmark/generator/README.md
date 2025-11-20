# Generator Module

This module provides utilities for generating random data for benchmarking.

## Classes

### GenList
Provides methods for generating random data:
- `random_list(n, m)`: Generate a list of n random integers between 0 and m
- `random_matrix(n, m)`: Generate an n×n matrix of random integers between 0 and m

## Purpose

These generators are used to create test data for benchmarking algorithms and operations with various input sizes and ranges.

## Usage

```python
from llm_benchmark.generator import GenList

# Generate a list of 100 random integers between 0 and 1000
data = GenList.random_list(100, 1000)

# Generate a 10x10 matrix of random integers between 0 and 100
matrix = GenList.random_matrix(10, 100)
```
