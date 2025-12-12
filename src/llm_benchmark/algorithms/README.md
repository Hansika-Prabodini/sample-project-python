# Algorithms Module

This module contains algorithm implementations for benchmarking LLM code generation capabilities.

## Modules

### Primes (`primes.py`)

Prime number operations and utilities.

#### Methods

- **`is_prime(n: int) -> bool`**
  - Check if a number is prime
  - Args: `n` - Number to check
  - Returns: `True` if the number is prime, `False` otherwise
  - Example:
    ```python
    from llm_benchmark.algorithms.primes import Primes
    Primes.is_prime(17)  # Returns: True
    Primes.is_prime(18)  # Returns: False
    ```

- **`is_prime_ineff(n: int) -> bool`**
  - Inefficient implementation for benchmarking purposes
  - Includes unnecessary calculations to demonstrate performance differences
  - Args: `n` - Number to check
  - Returns: `True` if the number is prime, `False` otherwise

- **`sum_primes(n: int) -> int`**
  - Calculate the sum of all prime numbers from 0 to n (exclusive)
  - Args: `n` - Upper bound (exclusive)
  - Returns: Sum of all primes less than n
  - Example:
    ```python
    Primes.sum_primes(10)  # Returns: 17 (2 + 3 + 5 + 7)
    ```

- **`prime_factors(n: int) -> List[int]`**
  - Get the prime factorization of a number
  - Args: `n` - Number to factorize
  - Returns: List of prime factors
  - Example:
    ```python
    Primes.prime_factors(840)  # Returns: [2, 2, 2, 3, 5, 7]
    ```

### Sort (`sort.py`)

Sorting algorithms and array partitioning operations.

#### Methods

- **`sort_list(v: List[int]) -> None`**
  - Sort a list of integers in-place using bubble sort
  - Args: `v` - List of integers to sort
  - Returns: None (modifies list in-place)
  - Example:
    ```python
    from llm_benchmark.algorithms.sort import Sort
    nums = [5, 3, 2, 1, 4]
    Sort.sort_list(nums)
    print(nums)  # [1, 2, 3, 4, 5]
    ```

- **`dutch_flag_partition(v: List[int], pivot_value: int) -> None`**
  - Partition a list using the Dutch National Flag algorithm
  - Elements less than pivot come first, then equal to pivot, then greater
  - Args:
    - `v` - List of integers to partition
    - `pivot_value` - Value to partition around
  - Returns: None (modifies list in-place)
  - Example:
    ```python
    nums = [5, 3, 2, 1, 4, 3, 3]
    Sort.dutch_flag_partition(nums, 3)
    print(nums)  # [2, 1, 3, 3, 3, 5, 4]
    ```

- **`max_n(v: List[int], n: int) -> List[int]`**
  - Find the N largest elements in a list
  - Args:
    - `v` - List of integers
    - `n` - Number of maximum values to find
  - Returns: List of the N largest values
  - Example:
    ```python
    Sort.max_n([5, 3, 2, 1, 4], 3)  # Returns: [5, 4, 3]
    ```

## Usage Example

```python
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.algorithms.sort import Sort

# Prime number operations
print(Primes.is_prime(17))  # True
print(Primes.sum_primes(100))  # Sum of primes < 100
print(Primes.prime_factors(60))  # [2, 2, 3, 5]

# Sorting operations
numbers = [9, 3, 7, 1, 5]
Sort.sort_list(numbers)
print(numbers)  # [1, 3, 5, 7, 9]

print(Sort.max_n([9, 3, 7, 1, 5], 2))  # [9, 7]
```

## Performance Notes

- The `is_prime_ineff` method is intentionally inefficient for benchmarking comparisons
- The `sort_list` method uses a simple bubble sort algorithm
- The `max_n` method uses a selection-based approach rather than full sorting
