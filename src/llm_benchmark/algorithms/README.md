# Algorithms Module

This module contains implementations of various algorithms for benchmarking purposes.

## Classes

### Primes
Provides methods for prime number operations:
- `is_prime(n)`: Check if a number is prime
- `is_prime_ineff(n)`: Inefficient prime check implementation for comparison
- `sum_primes(n)`: Calculate the sum of all primes up to n
- `prime_factors(n)`: Find all prime factors of a number

### Sort
Provides sorting and partitioning algorithms:
- `sort_list(v)`: Sort a list of integers in place using comparison sort
- `dutch_flag_partition(v, pivot_value)`: Dutch flag partitioning algorithm
- `max_n(v, n)`: Find the n largest numbers in a list

## Usage

```python
from llm_benchmark.algorithms import Primes, Sort

# Check if a number is prime
is_42_prime = Primes.is_prime(42)

# Sum primes up to 100
prime_sum = Primes.sum_primes(100)

# Sort a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
Sort.sort_list(numbers)
```
