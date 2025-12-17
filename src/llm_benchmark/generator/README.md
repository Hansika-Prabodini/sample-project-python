# Generator Module

This module contains utilities for generating random test data used in benchmarking operations.

## Modules

### GenList (`gen_list.py`)

Random data generation for lists and matrices.

#### Methods

- **`random_list(n: int, m: int) -> List[int]`**
  - Generate a list of random integers
  - Args:
    - `n` - Number of integers to generate (list length)
    - `m` - Maximum value of integers (exclusive upper bound)
  - Returns: List of `n` random integers in the range [0, m-1]
  - Example:
    ```python
    from llm_benchmark.generator.gen_list import GenList
    
    # Generate 10 random numbers from 0 to 100
    random_numbers = GenList.random_list(10, 100)
    print(random_numbers)  # e.g., [45, 23, 78, 12, 90, 34, 56, 67, 89, 1]
    
    # Generate 5 random numbers from 0 to 10
    small_list = GenList.random_list(5, 10)
    print(small_list)  # e.g., [3, 7, 2, 9, 4]
    ```

- **`random_matrix(n: int, m: int) -> List[List[int]]`**
  - Generate a matrix (2D list) of random integers
  - Args:
    - `n` - Number of rows in the matrix
    - `m` - Number of columns in the matrix (also used as max value)
  - Returns: Matrix of `n x m` random integers, each in range [0, m-1]
  - Example:
    ```python
    # Generate a 3x3 matrix with values from 0 to 3
    matrix = GenList.random_matrix(3, 3)
    print(matrix)
    # e.g., [[1, 2, 0],
    #        [3, 1, 2],
    #        [0, 3, 1]]
    
    # Generate a 5x5 matrix
    large_matrix = GenList.random_matrix(5, 5)
    ```

## Usage Example

```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.datastructures.dslist import DsList

# Generate random test data
test_list = GenList.random_list(20, 50)
print(f"Random list: {test_list}")

# Use generated data with other modules
sorted_list = DsList.sort_list(test_list)
print(f"Sorted list: {sorted_list}")

max_value = max(test_list)
print(f"Maximum value: {max_value}")

# Generate matrix data
test_matrix = GenList.random_matrix(4, 4)
print(f"\nRandom 4x4 matrix:")
for row in test_matrix:
    print(row)

# Use matrix with other operations
matrix_sum = DoubleForLoop.sum_matrix(test_matrix)
print(f"Matrix sum: {matrix_sum}")

# Generate data for pair counting
pairs_list = GenList.random_list(30, 10)
pair_count = DoubleForLoop.count_pairs(pairs_list)
print(f"Number of pairs: {pair_count}")
```

## Common Use Cases

### Testing Algorithm Performance
```python
# Generate large dataset for performance testing
large_dataset = GenList.random_list(10000, 1000)
# Test sorting performance
# Sort.sort_list(large_dataset)
```

### Comparing Two Lists
```python
# Generate two lists for comparison operations
list1 = GenList.random_list(100, 50)
list2 = GenList.random_list(100, 50)
duplicates = DoubleForLoop.count_duplicates(list1, list2)
```

### Matrix Operations
```python
# Generate matrices for testing
small_matrix = GenList.random_matrix(3, 3)
medium_matrix = GenList.random_matrix(10, 10)
large_matrix = GenList.random_matrix(100, 100)

# Test matrix sum performance
for matrix in [small_matrix, medium_matrix, large_matrix]:
    total = DoubleForLoop.sum_matrix(matrix)
    print(f"Matrix sum: {total}")
```

## Performance Notes

- Uses Python's `random.randint()` for number generation
- Random values are in the range [0, m-1] (inclusive of 0, exclusive of m)
- Matrix generation creates independent random values for each cell
- Useful for creating reproducible test cases when seeded
- Designed to support benchmarking and testing of other modules

## Implementation Details

- `random_list()` uses list comprehension for efficient generation
- `random_matrix()` internally calls `random_list()` for each row
- No validation is performed on input parameters (assumes valid positive integers)
