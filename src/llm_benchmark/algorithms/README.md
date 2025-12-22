# Algorithms Module

This module contains algorithm implementations designed to benchmark computational complexity and algorithmic thinking in LLM-generated code.

## Files

### primes.py

Prime number operations for testing mathematical algorithm generation.

**Class: `Primes`**

#### Methods

##### `is_prime(n: int) -> bool`
Checks if a number is prime using trial division.

- **Args**: `n` - Number to check
- **Returns**: `True` if prime, `False` otherwise
- **Complexity**: O(n) - checks all divisors up to n

```python
from llm_benchmark.algorithms.primes import Primes

Primes.is_prime(17)  # True
Primes.is_prime(12)  # False
```

##### `is_prime_ineff(n: int) -> bool`
Intentionally inefficient prime checking for benchmarking optimization detection.

- **Args**: `n` - Number to check
- **Returns**: `True` if prime, `False` otherwise
- **Complexity**: O(n²) with significant constant factors
- **Note**: Contains unnecessary nested loops for performance testing

##### `sum_primes(n: int) -> int`
Calculates the sum of all prime numbers from 0 to n (exclusive).

- **Args**: `n` - Upper bound (exclusive)
- **Returns**: Sum of all primes less than n
- **Complexity**: O(n²)

```python
Primes.sum_primes(10)  # Returns 17 (2 + 3 + 5 + 7)
```

##### `prime_factors(n: int) -> List[int]`
Finds the prime factorization of a number.

- **Args**: `n` - Number to factorize
- **Returns**: List of prime factors
- **Complexity**: O(n²)

```python
Primes.prime_factors(12)  # Returns [2, 2, 3]
Primes.prime_factors(15)  # Returns [3, 5]
```

---

### sort.py

Sorting and array manipulation algorithms.

**Class: `Sort`**

#### Methods

##### `sort_list(v: List[int]) -> None`
Sorts a list in-place using bubble sort.

- **Args**: `v` - List of integers to sort
- **Returns**: None (modifies list in-place)
- **Complexity**: O(n²)

```python
from llm_benchmark.algorithms.sort import Sort

numbers = [5, 3, 2, 1, 4]
Sort.sort_list(numbers)
print(numbers)  # [1, 2, 3, 4, 5]
```

##### `dutch_flag_partition(v: List[int], pivot_value: int) -> None`
Partitions a list around a pivot value (Dutch National Flag problem).

- **Args**:
  - `v` - List of integers to partition
  - `pivot_value` - Pivot value for partitioning
- **Returns**: None (modifies list in-place)
- **Complexity**: O(n)
- **Result**: Elements < pivot, then == pivot, then > pivot

```python
numbers = [5, 3, 2, 1, 4]
Sort.dutch_flag_partition(numbers, 3)
print(numbers)  # [2, 1, 3, 5, 4] (< 3, == 3, > 3)
```

##### `max_n(v: List[int], n: int) -> List[int]`
Finds the n largest values in a list.

- **Args**:
  - `v` - List of integers
  - `n` - Number of maximum values to find
- **Returns**: List of n largest values in descending order
- **Complexity**: O(n * m) where m is the list length

```python
Sort.max_n([5, 3, 8, 1, 9, 2], 3)  # Returns [9, 8, 5]
```

## Benchmarking

These algorithms are implemented with varying levels of efficiency to test:
- Algorithm optimization capabilities
- Time complexity understanding
- In-place vs. copy operations
- Edge case handling

Run benchmarks with:
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/algorithms/
```
