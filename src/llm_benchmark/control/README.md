# Control Flow Module

This module contains control flow operations using single and nested loops for benchmarking purposes.

## Modules

### SingleForLoop (`single.py`)

Operations that use a single for loop.

#### Methods

- **`sum_range(n: int) -> int`**
  - Calculate the sum of numbers from 0 to n (exclusive)
  - Args: `n` - Upper bound (exclusive)
  - Returns: Sum of all numbers from 0 to n-1
  - Example:
    ```python
    from llm_benchmark.control.single import SingleForLoop
    SingleForLoop.sum_range(10)  # Returns: 45 (0+1+2+...+9)
    ```

- **`max_list(v: List[int]) -> int`**
  - Find the maximum value in a list
  - Args: `v` - List of integers
  - Returns: Maximum value in the list
  - Example:
    ```python
    SingleForLoop.max_list([1, 5, 3, 9, 2])  # Returns: 9
    ```

- **`sum_modulus(n: int, m: int) -> int`**
  - Calculate the sum of all numbers from 0 to n that are divisible by m
  - Args:
    - `n` - Upper bound (exclusive)
    - `m` - Divisor for modulus check
  - Returns: Sum of numbers divisible by m
  - Example:
    ```python
    SingleForLoop.sum_modulus(100, 3)  # Returns: 1683 (sum of 0,3,6,...,99)
    ```

### DoubleForLoop (`double.py`)

Operations that use nested for loops.

#### Methods

- **`sum_square(n: int) -> int`**
  - Calculate the sum of squares from 0 to n (exclusive)
  - Uses nested loops where i == j to compute i²
  - Args: `n` - Upper bound (exclusive)
  - Returns: Sum of squares
  - Example:
    ```python
    from llm_benchmark.control.double import DoubleForLoop
    DoubleForLoop.sum_square(5)  # Returns: 30 (0² + 1² + 2² + 3² + 4²)
    ```

- **`sum_triangle(n: int) -> int`**
  - Calculate the triangular sum using nested loops
  - Sums all numbers in a triangular pattern
  - Args: `n` - Upper bound (exclusive)
  - Returns: Triangular sum
  - Example:
    ```python
    DoubleForLoop.sum_triangle(5)  # Returns: 20
    ```

- **`count_pairs(arr: List[int]) -> int`**
  - Count the number of pairs in an array
  - A pair is defined as exactly two occurrences of the same number
  - Args: `arr` - List of integers
  - Returns: Number of pairs found
  - Example:
    ```python
    DoubleForLoop.count_pairs([1, 2, 2, 3, 3, 4])  # Returns: 2 (pairs: 2,2 and 3,3)
    ```

- **`count_duplicates(arr0: List[int], arr1: List[int]) -> int`**
  - Count duplicates between two arrays at matching indices
  - Only counts when i == j and arr0[i] == arr1[j]
  - Args:
    - `arr0` - First list of integers
    - `arr1` - Second list of integers
  - Returns: Number of matching elements at same positions
  - Example:
    ```python
    DoubleForLoop.count_duplicates([1, 2, 3], [1, 5, 3])  # Returns: 2
    ```

- **`sum_matrix(m: List[List[int]]) -> int`**
  - Calculate the sum of all elements in a matrix
  - Args: `m` - Matrix (2D list) of integers
  - Returns: Sum of all matrix elements
  - Example:
    ```python
    matrix = [[1, 2, 3], [4, 5, 6]]
    DoubleForLoop.sum_matrix(matrix)  # Returns: 21
    ```

## Usage Example

```python
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.control.double import DoubleForLoop

# Single loop operations
print(SingleForLoop.sum_range(100))  # Sum from 0 to 99
print(SingleForLoop.max_list([5, 2, 8, 1, 9]))  # Find maximum
print(SingleForLoop.sum_modulus(50, 5))  # Sum multiples of 5

# Nested loop operations
print(DoubleForLoop.sum_square(10))  # Sum of squares
print(DoubleForLoop.sum_triangle(10))  # Triangular sum
print(DoubleForLoop.count_pairs([1, 1, 2, 2, 3]))  # Count pairs

# Matrix operations
matrix = [[1, 2], [3, 4], [5, 6]]
print(DoubleForLoop.sum_matrix(matrix))  # Sum all elements
```

## Performance Notes

- These implementations intentionally use explicit loops rather than built-in functions
- Designed to benchmark LLM code generation for control flow structures
- The nested loop operations demonstrate O(n²) complexity patterns
