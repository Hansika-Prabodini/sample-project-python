# Generator Module

This module contains utilities for generating test data and random structures.

## GenList Class

The `GenList` class provides static methods for generating lists and matrices of random integers. This is useful for creating test data and benchmarking purposes.

### Methods

#### `random_list(n: int, m: int) -> List[int]`

Generates a list of random integers.

**Parameters:**
- `n` (int): Number of integers to generate
- `m` (int): Maximum value of integers (exclusive, range is [0, m))

**Returns:**
- `List[int]`: A list containing `n` random integers, each in the range [0, m)

**Example:**
```python
from llm_benchmark.generator.gen_list import GenList

# Generate a list of 5 random integers with maximum value 100
random_ints = GenList.random_list(5, 100)
# Output: [42, 17, 89, 5, 63]
```

#### `random_matrix(n: int, m: int) -> List[List[int]]`

Generates a matrix of random integers with specified dimensions.

**Parameters:**
- `n` (int): Number of rows
- `m` (int): Number of columns

**Returns:**
- `List[List[int]]`: A matrix (list of lists) with `n` rows and `m` columns, where each element is a random integer in the range [0, m)

**Example:**
```python
from llm_benchmark.generator.gen_list import GenList

# Generate a 3x4 matrix of random integers
matrix = GenList.random_matrix(3, 4)
# Output: [[2, 3, 1, 2], [0, 3, 2, 1], [3, 1, 0, 2]]
```

## Usage

```python
from llm_benchmark.generator.gen_list import GenList

# Create a list of 10 random integers (values 0-99)
my_list = GenList.random_list(10, 100)

# Create a 5x5 matrix of random integers (values 0-5)
my_matrix = GenList.random_matrix(5, 5)
```

## Testing

Unit tests for the GenList class are located in `tests/llm_benchmark/generator/test_gen_list.py`.

Run tests with:
```bash
poetry run pytest tests/llm_benchmark/generator/test_gen_list.py
```
