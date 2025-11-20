# Algorithms

This module contains implementations of common algorithms used for benchmarking.

## Modules

### primes.py

Prime number operations:
- `Primes.is_prime(n)` - Check if a number is prime
- `Primes.is_prime_ineff(n)` - Check if a number is prime (intentionally inefficient for benchmarking)
- `Primes.sum_primes(n)` - Sum all prime numbers from 0 to n
- `Primes.prime_factors(n)` - Get all prime factors of a number

### sort.py

Sorting and selection operations:
- `Sort.sort_list(v)` - Sort a list in place using bubble sort
- `Sort.dutch_flag_partition(v, pivot)` - Partition list using Dutch flag algorithm
- `Sort.max_n(v, n)` - Find the maximum n numbers in a list
