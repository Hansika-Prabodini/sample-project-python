# Data Structures Module

This module contains functions for benchmarking common data structure operations, with a focus on list manipulation.

## Files

### dslist.py

List data structure operations implemented using explicit loops for benchmarking purposes.

**Class: `DsList`**

#### Methods

##### `modify_list(v: List[int]) -> List[int]`
Creates a modified copy of a list by adding 1 to each element.

- **Args**: `v` - List of integers
- **Returns**: New list with each element incremented by 1
- **Complexity**: O(n)

```python
from llm_benchmark.datastructures.dslist import DsList

DsList.modify_list([1, 2, 3])  # Returns [2, 3, 4]
```

##### `search_list(v: List[int], n: int) -> List[int]`
Searches for all occurrences of a value in a list.

- **Args**:
  - `v` - List of integers
  - `n` - Value to search for
- **Returns**: List of indices where the value is found
- **Complexity**: O(n)

```python
DsList.search_list([1, 5, 3, 5, 2], 5)  # Returns [1, 3]
DsList.search_list([1, 2, 3], 4)        # Returns []
```

##### `sort_list(v: List[int]) -> List[int]`
Sorts a list of integers and returns a sorted copy.

- **Args**: `v` - List of integers
- **Returns**: New sorted list (original unchanged)
- **Complexity**: O(n²) - uses bubble sort
- **Note**: Returns a copy, does not modify original

```python
original = [5, 3, 2, 1, 4]
sorted_list = DsList.sort_list(original)
print(sorted_list)  # [1, 2, 3, 4, 5]
print(original)     # [5, 3, 2, 1, 4] (unchanged)
```

##### `reverse_list(v: List[int]) -> List[int]`
Reverses a list and returns a reversed copy.

- **Args**: `v` - List of integers
- **Returns**: New list with elements in reverse order
- **Complexity**: O(n)

```python
DsList.reverse_list([1, 2, 3, 4, 5])  # Returns [5, 4, 3, 2, 1]
```

##### `rotate_list(v: List[int], n: int) -> List[int]`
Rotates a list by n positions to the left.

- **Args**:
  - `v` - List of integers
  - `n` - Number of positions to rotate
- **Returns**: New list rotated n positions left
- **Complexity**: O(n)

```python
DsList.rotate_list([1, 2, 3, 4, 5], 2)  # Returns [3, 4, 5, 1, 2]
DsList.rotate_list([1, 2, 3, 4, 5], 0)  # Returns [1, 2, 3, 4, 5]
```

##### `merge_lists(v1: List[int], v2: List[int]) -> List[int]`
Merges two lists by concatenation.

- **Args**:
  - `v1` - First list of integers
  - `v2` - Second list of integers
- **Returns**: New list containing all elements from v1 followed by v2
- **Complexity**: O(n + m)

```python
DsList.merge_lists([1, 2, 3], [4, 5, 6])  # Returns [1, 2, 3, 4, 5, 6]
```

## Implementation Notes

All functions in this module are implemented using explicit for-loops rather than built-in Python functions or list comprehensions. This design choice serves several benchmarking purposes:

1. **Performance comparison**: Compare manual implementations vs. built-in operations
2. **Code generation testing**: Test LLM understanding of basic data structure manipulation
3. **Optimization opportunities**: Identify when built-ins would be more efficient
4. **Educational value**: Clear algorithmic implementations for learning

## Benchmarking

These operations test:
- List traversal patterns
- In-place vs. copy operations
- Memory allocation patterns
- Time/space complexity trade-offs

Run benchmarks with:
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/datastructures/
```

## Example Usage

```python
from llm_benchmark.datastructures.dslist import DsList

# Work with a list
data = [1, 2, 3, 4, 5]

# Transform
doubled = DsList.modify_list(data)  # [2, 3, 4, 5, 6]

# Search
indices = DsList.search_list(data, 3)  # [2]

# Reorganize
sorted_data = DsList.sort_list(data)
reversed_data = DsList.reverse_list(data)
rotated_data = DsList.rotate_list(data, 2)

# Combine
merged = DsList.merge_lists(data, [6, 7, 8])
```
