# Control Flow Module

This module contains functions that benchmark control flow structures, particularly for-loop constructs with varying levels of nesting.

## Files

### single.py

Single for-loop operations for benchmarking basic iteration.

**Class: `SingleForLoop`**

#### Methods

##### `sum_range(n: int) -> int`
Calculates the sum of numbers from 0 to n-1.

- **Args**: `n` - Upper bound (exclusive)
- **Returns**: Sum of range [0, n)
- **Complexity**: O(n)

```python
from llm_benchmark.control.single import SingleForLoop

SingleForLoop.sum_range(10)  # Returns 45 (0+1+2+...+9)
```

##### `max_list(v: List[int]) -> int`
Finds the maximum value in a list.

- **Args**: `v` - List of integers
- **Returns**: Maximum value in the list
- **Complexity**: O(n)
- **Note**: Assumes non-empty list

```python
SingleForLoop.max_list([1, 5, 3, 9, 2])  # Returns 9
```

##### `sum_modulus(n: int, m: int) -> int`
Calculates the sum of all numbers divisible by m in range [0, n).

- **Args**:
  - `n` - Upper bound (exclusive)
  - `m` - Modulus divisor
- **Returns**: Sum of all multiples of m less than n
- **Complexity**: O(n)

```python
SingleForLoop.sum_modulus(100, 3)  # Returns sum of 0, 3, 6, 9, ..., 99
```

---

### double.py

Nested for-loop operations for benchmarking more complex iteration patterns.

**Class: `DoubleForLoop`**

#### Methods

##### `sum_square(n: int) -> int`
Calculates the sum of squares using nested loops.

- **Args**: `n` - Upper bound (exclusive)
- **Returns**: Sum of i² for i in [0, n)
- **Complexity**: O(n²)
- **Note**: Uses nested loops to identify when i == j

```python
from llm_benchmark.control.double import DoubleForLoop

DoubleForLoop.sum_square(10)  # Returns 285 (0²+1²+2²+...+9²)
```

##### `sum_triangle(n: int) -> int`
Calculates a triangular sum pattern.

- **Args**: `n` - Upper bound (exclusive)
- **Returns**: Sum of triangular pattern
- **Complexity**: O(n²)

```python
DoubleForLoop.sum_triangle(5)
# Computes: (0) + (0+1) + (0+1+2) + (0+1+2+3) + (0+1+2+3+4)
```

##### `count_pairs(arr: List[int]) -> int`
Counts the number of pairs in an array.

A pair is defined as exactly two occurrences of the same value.

- **Args**: `arr` - List of integers
- **Returns**: Number of pairs found
- **Complexity**: O(n²)

```python
DoubleForLoop.count_pairs([1, 2, 2, 3, 3, 4])  # Returns 2 (pair of 2s and pair of 3s)
```

##### `count_duplicates(arr0: List[int], arr1: List[int]) -> int`
Counts duplicate values at matching indices between two arrays.

- **Args**:
  - `arr0` - First list of integers
  - `arr1` - Second list of integers
- **Returns**: Count of matching values at same indices
- **Complexity**: O(n²)

```python
DoubleForLoop.count_duplicates([1, 2, 3], [1, 5, 3])  # Returns 2
```

##### `sum_matrix(m: List[List[int]]) -> int`
Calculates the sum of all elements in a 2D matrix.

- **Args**: `m` - Matrix (list of lists) of integers
- **Returns**: Sum of all matrix elements
- **Complexity**: O(n * m) for n×m matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
DoubleForLoop.sum_matrix(matrix)  # Returns 45
```

## Benchmarking Purpose

This module tests:
- **Loop optimization**: Single vs. nested loop performance
- **Algorithm efficiency**: O(n) vs. O(n²) complexity
- **Control flow understanding**: Proper use of loop constructs
- **Memory patterns**: Iteration over linear vs. 2D data structures

Run benchmarks with:
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/control/
```

## Notes

Some functions are intentionally implemented with suboptimal algorithms to provide diverse benchmarking scenarios for testing LLM code generation and optimization capabilities.
