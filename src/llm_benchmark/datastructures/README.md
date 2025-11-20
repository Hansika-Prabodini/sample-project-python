# Data Structures Module

This module contains implementations of common list operations for benchmarking.

## Classes

### DsList
Provides various list manipulation operations:
- `modify_list(v)`: Add 1 to each element in a list
- `search_list(v, n)`: Find all indices where a value occurs
- `sort_list(v)`: Sort a list of integers (returns a copy)
- `reverse_list(v)`: Reverse a list (returns a copy)
- `rotate_list(v, n)`: Rotate a list by n positions
- `merge_lists(v1, v2)`: Merge two lists

## Purpose

These operations demonstrate various list manipulation patterns and their performance characteristics under different conditions.

## Usage

```python
from llm_benchmark.datastructures import DsList

# List operations
modified = DsList.modify_list([1, 2, 3, 4])
indices = DsList.search_list([1, 2, 1, 3, 1], 1)
sorted_list = DsList.sort_list([3, 1, 4, 1, 5])
reversed_list = DsList.reverse_list([1, 2, 3, 4, 5])
rotated = DsList.rotate_list([1, 2, 3, 4, 5], 2)
merged = DsList.merge_lists([1, 2], [3, 4])
```
