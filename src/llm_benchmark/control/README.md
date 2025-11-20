# Control Module

This module contains implementations of control flow operations for performance benchmarking.

## Classes

### SingleForLoop
Provides operations with single loop control flow:
- `sum_range(n)`: Calculate the sum of numbers from 0 to n
- `max_list(v)`: Find the maximum value in a list
- `sum_modulus(n, m)`: Sum numbers divisible by m in range 0 to n

### DoubleForLoop
Provides operations with nested loop control flow:
- `sum_square(n)`: Sum of squares from 0 to n using nested loops
- `sum_triangle(n)`: Sum of triangle pattern from 0 to n
- `count_pairs(arr)`: Count pairs of equal numbers in an array
- `count_duplicates(arr0, arr1)`: Count common elements between two arrays
- `sum_matrix(m)`: Sum all elements in a 2D matrix

## Purpose

These implementations demonstrate performance characteristics of single vs. nested loops, useful for understanding algorithmic complexity and optimization.

## Usage

```python
from llm_benchmark.control import SingleForLoop, DoubleForLoop

# Single loop operations
sum_vals = SingleForLoop.sum_range(100)
max_val = SingleForLoop.max_list([3, 1, 4, 1, 5, 9])

# Nested loop operations
square_sum = DoubleForLoop.sum_square(10)
pair_count = DoubleForLoop.count_pairs([1, 2, 2, 3, 3, 3])
```
