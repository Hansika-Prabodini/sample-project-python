# Generator Module

This module provides utility functions for generating random test data used throughout the benchmark suite.

## Files

### gen_list.py

Random data generation for testing and benchmarking purposes.

**Class: `GenList`**

#### Methods

##### `random_list(n: int, m: int) -> List[int]`
Generates a list of random integers.

- **Args**:
  - `n` - Number of integers to generate (length of list)
  - `m` - Maximum value (exclusive) - values will be in range [0, m)
- **Returns**: List of n random integers in range [0, m-1]
- **Complexity**: O(n)

```python
from llm_benchmark.generator.gen_list import GenList

# Generate 10 random integers from 0 to 99
random_data = GenList.random_list(10, 100)

# Generate 5 random integers from 0 to 4
small_data = GenList.random_list(5, 5)

# Generate 100 random booleans (0 or 1)
binary_data = GenList.random_list(100, 2)
```

**Important**: The parameter `m` is **exclusive**. Values generated will be in the range `[0, m)`, meaning:
- `GenList.random_list(10, 1)` generates 10 zeros
- `GenList.random_list(10, 5)` generates integers from 0 to 4 (inclusive)
- `GenList.random_list(10, 100)` generates integers from 0 to 99 (inclusive)

##### `random_matrix(n: int, m: int) -> List[List[int]]`
Generates a matrix (2D list) of random integers.

- **Args**:
  - `n` - Number of rows in the matrix
  - `m` - Maximum value (exclusive) for each element
- **Returns**: n×n matrix with random integers in range [0, m-1]
- **Complexity**: O(n²)

```python
# Generate a 5×5 matrix with values 0-9
matrix = GenList.random_matrix(5, 10)

# Result structure:
# [[3, 7, 1, 9, 2],
#  [4, 0, 8, 5, 6],
#  [2, 9, 3, 1, 7],
#  [8, 4, 6, 0, 5],
#  [1, 3, 9, 2, 4]]
```

**Note**: The matrix is square (n rows × n columns), with each element in range [0, m).

## Usage Examples

### Generating Test Data for Benchmarks

```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.algorithms.sort import Sort

# Create random data for testing
test_data = GenList.random_list(1000, 100)

# Use in sorting benchmarks
Sort.sort_list(test_data)

# Use in nested loop operations
pairs = DoubleForLoop.count_pairs(test_data)

# Create matrix for 2D operations
test_matrix = GenList.random_matrix(50, 10)
total = DoubleForLoop.sum_matrix(test_matrix)
```

### Different Data Distributions

```python
# Large lists with small value range (many duplicates)
GenList.random_list(1000, 10)

# Small lists with large value range (few duplicates)
GenList.random_list(10, 1000)

# Square matrix with binary values
GenList.random_matrix(100, 2)

# Large matrix with diverse values
GenList.random_matrix(100, 1000)
```

## Implementation Details

- Uses Python's `random.randint()` for random number generation
- List comprehension for efficient list creation
- Each call produces different random values (non-deterministic)
- No seed setting by default (use `random.seed()` externally if needed)

## Testing

The generator module includes comprehensive tests to verify:
- Correct range boundaries (exclusive upper bound)
- Proper list/matrix dimensions
- Value distributions

Run tests with:
```bash
poetry run pytest tests/llm_benchmark/generator/
```

## Design Rationale

This module exists separately to:
1. Provide consistent test data generation across all benchmarks
2. Avoid mixing I/O or randomness into benchmark measurements
3. Enable reproducible testing when needed (via external seed setting)
4. Simplify benchmark function signatures (they receive pre-generated data)
