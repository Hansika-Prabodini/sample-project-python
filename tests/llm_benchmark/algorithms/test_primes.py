"""Test suite for prime number algorithms.

This module contains tests for the Primes class, which implements various
prime number related algorithms including primality testing, prime summation,
and prime factorization.
"""

from typing import List

import pytest

from llm_benchmark.algorithms.primes import Primes


@pytest.mark.parametrize(
    "n, is_prime",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (10, False),
        (17, True),
        (26, False),
    ],
)
def test_is_prime(n: int, is_prime: bool) -> None:
    """Test primality checking for integers.
    
    Validates that is_prime correctly determines whether a given integer
    is a prime number. Tests cover edge cases (0, 1), small primes,
    composite numbers, and larger values.
    
    Args:
        n: The integer to test for primality.
        is_prime: Whether n should be identified as prime (True) or not (False).
    
    Test cases:
        - n=0: Not prime by definition
        - n=1: Not prime by definition
        - n=2: Smallest prime number
        - n=3: Small prime number
        - n=4: Composite (2×2)
        - n=10: Composite (2×5)
        - n=17: Larger prime number
        - n=26: Larger composite (2×13)
    """
    assert Primes.is_prime(n) == is_prime


def test_benchmark_is_prime(benchmark) -> None:
    """Benchmark the primality test operation.
    
    Measures the performance of checking if 17 is prime.
    """
    benchmark(Primes.is_prime, 17)


@pytest.mark.parametrize(
    "n, S", [(0, 0), (1, 0), (2, 0), (3, 2), (4, 5), (10, 17), (100, 1060)]
)
def test_sum_primes(n: int, S: int) -> None:
    """Test summation of prime numbers below n.
    
    Validates that sum_primes correctly computes the sum of all prime
    numbers less than n. This tests both primality checking and accumulation
    over a range.
    
    Args:
        n: The upper bound (exclusive) for prime summation.
        S: The expected sum of all primes less than n.
    
    Test cases:
        - n=0: No primes, sum is 0
        - n=1: No primes, sum is 0
        - n=2: No primes less than 2, sum is 0
        - n=3: Prime 2, sum is 2
        - n=4: Primes 2,3, sum is 5
        - n=10: Primes 2,3,5,7, sum is 17
        - n=100: Sum of all primes less than 100 is 1060
    """
    assert Primes.sum_primes(n) == S


def test_benchmark_sum_primes(benchmark) -> None:
    """Benchmark the prime summation operation.
    
    Measures the performance of summing all primes less than 20.
    """
    benchmark(Primes.sum_primes, 20)


@pytest.mark.parametrize(
    "n, factors",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (10, [2, 5]),
        (17, [17]),
        (84, [2, 2, 3, 7]),
    ],
)
def test_prime_factors(n: int, factors: List[int]) -> None:
    """Test prime factorization of integers.
    
    Validates that prime_factors correctly computes the complete prime
    factorization of an integer, returning factors in ascending order
    with repetitions for powers.
    
    Args:
        n: The integer to factorize.
        factors: The expected list of prime factors (with repetitions).
    
    Test cases:
        - n=0: No prime factors (empty list)
        - n=1: No prime factors (empty list)
        - n=2: Prime itself, factors = [2]
        - n=3: Prime itself, factors = [3]
        - n=4: 2², factors = [2, 2]
        - n=10: 2×5, factors = [2, 5]
        - n=17: Prime itself, factors = [17]
        - n=84: 2²×3×7, factors = [2, 2, 3, 7]
    """
    assert Primes.prime_factors(n) == factors


def test_benchmark_prime_factors(benchmark) -> None:
    """Benchmark the prime factorization operation.
    
    Measures the performance of factorizing 84 (2²×3×7).
    """
    benchmark(Primes.prime_factors, 84)
