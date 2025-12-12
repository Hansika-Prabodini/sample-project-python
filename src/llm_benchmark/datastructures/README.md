# Data Structures Module

This module contains data structure operations focusing on list manipulations for benchmarking purposes.

## Modules

### DsList (`dslist.py`)

List manipulation operations implemented using explicit loops.

#### Methods

- **`modify_list(v: List[int]) -> List[int]`**
  - Create a new list with 1 added to each element
  - Args: `v` - List of integers
  - Returns: New list with each element incremented by 1
  - Example:
    ```python
    from llm_benchmark.datastructures.dslist import DsList
    DsList.modify_list([1, 2, 3])  # Returns: [2, 3, 4]
    ```

- **`search_list(v: List[int], n: int) -> List[int]`**
  - Find all indices where a value appears in a list
  - Args:
    - `v` - List of integers to search
    - `n` - Value to search for
  - Returns: List of indices where the value is found
  - Example:
    ```python
    DsList.search_list([1, 2, 3, 2, 4], 2)  # Returns: [1, 3]
    ```

- **`sort_list(v: List[int]) -> List[int]`**
  - Sort a list and return a new sorted copy
  - Original list is not modified
  - Args: `v` - List of integers to sort
  - Returns: New sorted list
  - Example:
    ```python
    original = [5, 3, 1, 4, 2]
    sorted_list = DsList.sort_list(original)
    print(sorted_list)  # [1, 2, 3, 4, 5]
    print(original)     # [5, 3, 1, 4, 2] (unchanged)
    ```

- **`reverse_list(v: List[int]) -> List[int]`**
  - Reverse a list and return a new reversed copy
  - Original list is not modified
  - Args: `v` - List of integers to reverse
  - Returns: New reversed list
  - Example:
    ```python
    DsList.reverse_list([1, 2, 3, 4, 5])  # Returns: [5, 4, 3, 2, 1]
    ```

- **`rotate_list(v: List[int], n: int) -> List[int]`**
  - Rotate a list by n positions to the left
  - Args:
    - `v` - List of integers to rotate
    - `n` - Number of positions to rotate
  - Returns: New rotated list
  - Example:
    ```python
    DsList.rotate_list([1, 2, 3, 4, 5], 2)  # Returns: [3, 4, 5, 1, 2]
    ```

- **`merge_lists(v1: List[int], v2: List[int]) -> List[int]`**
  - Merge two lists by concatenating them
  - Args:
    - `v1` - First list of integers
    - `v2` - Second list of integers
  - Returns: New list containing all elements from v1 followed by v2
  - Example:
    ```python
    DsList.merge_lists([1, 2, 3], [4, 5, 6])  # Returns: [1, 2, 3, 4, 5, 6]
    ```

## Usage Example

```python
from llm_benchmark.datastructures.dslist import DsList

# List modifications
original = [1, 2, 3, 4, 5]
print(DsList.modify_list(original))  # [2, 3, 4, 5, 6]

# Search operations
numbers = [10, 20, 30, 20, 40]
print(DsList.search_list(numbers, 20))  # [1, 3]

# Sorting (returns copy)
unsorted = [5, 2, 8, 1, 9]
sorted_list = DsList.sort_list(unsorted)
print(sorted_list)  # [1, 2, 5, 8, 9]
print(unsorted)     # [5, 2, 8, 1, 9] (unchanged)

# Reversing
print(DsList.reverse_list([1, 2, 3]))  # [3, 2, 1]

# Rotating
print(DsList.rotate_list([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]

# Merging
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(DsList.merge_lists(list1, list2))  # [1, 2, 3, 4, 5, 6]
```

## Performance Notes

- All methods use explicit loops rather than built-in Python functions
- Operations return new lists, preserving the original (except where noted)
- Designed to benchmark LLM code generation for list operations
- The sort implementation uses a simple bubble sort algorithm (O(n²))
