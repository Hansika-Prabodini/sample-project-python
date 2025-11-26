"""Test cases for prime number algorithms.

This module contains unit tests and benchmark tests for the Primes class,
which implements various prime number related algorithms including primality
testing, prime summation, and prime factorization.
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
    """Test is_prime function which determines if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself. The function checks divisibility up to
    the square root of n for efficiency.
    
    Args:
        n: Number to check for primality
        is_prime: Expected boolean result
        
    Test cases:
        - n=0: Not prime (not a natural number > 1)
        - n=1: Not prime (by definition)
        - n=2: Prime (smallest prime number)
        - n=3: Prime
        - n=4: Not prime (divisible by 2)
        - n=10: Not prime (divisible by 2 and 5)
        - n=17: Prime
        - n=26: Not prime (divisible by 2 and 13)
    """
    assert Primes.is_prime(n) == is_prime


def test_benchmark_is_prime(benchmark) -> None:
    """Benchmark the performance of is_prime.
    
    Measures execution time for checking if 17 is a prime number.
    Uses a moderately small prime to test the algorithm efficiency.
    """
    benchmark(Primes.is_prime, 17)


@pytest.mark.parametrize(
    "n, S", [(0, 0), (1, 0), (2, 0), (3, 2), (4, 5), (10, 17), (100, 1060)]
)
def test_sum_primes(n: int, S: int) -> None:
    """Test sum_primes function which calculates the sum of all primes less than n.
    
    Iterates through all numbers from 0 to n-1, checks each for primality,
    and sums all prime numbers found.
    
    Args:
        n: Upper bound (exclusive) for finding primes
        S: Expected sum of all primes in range [0, n)
        
    Test cases:
        - n=0: No numbers to check, sum = 0
        - n=1: Only 0, which is not prime, sum = 0
        - n=2: Only 0 and 1, neither prime, sum = 0
        - n=3: Includes 2 (prime), sum = 2
        - n=4: Includes 2, 3 (both prime), sum = 5
        - n=10: Primes are 2,3,5,7, sum = 17
        - n=100: Sum of all primes up to 99 = 1060
    """
    assert Primes.sum_primes(n) == S


def test_benchmark_sum_primes(benchmark) -> None:
    """Benchmark the performance of sum_primes.
    
    Measures execution time for finding and summing all prime numbers
    less than 20.
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
    """Test prime_factors function which computes the prime factorization of n.
    
    Returns a list of prime factors (with repetition) such that their product
    equals n. For example, 84 = 2 × 2 × 3 × 7.
    
    Args:
        n: Number to factorize
        factors: Expected list of prime factors (in ascending order with repetition)
        
    Test cases:
        - n=0: No prime factors, returns []
        - n=1: No prime factors, returns []
        - n=2: Prime itself, returns [2]
        - n=3: Prime itself, returns [3]
        - n=4: 2², returns [2, 2]
        - n=10: 2 × 5, returns [2, 5]
        - n=17: Prime itself, returns [17]
        - n=84: 2² × 3 × 7, returns [2, 2, 3, 7]
    """
    assert Primes.prime_factors(n) == factors


def test_benchmark_prime_factors(benchmark) -> None:
    """Benchmark the performance of prime_factors.
    
    Measures execution time for computing the prime factorization of 84,
    which equals 2 × 2 × 3 × 7.
    """
    benchmark(Primes.prime_factors, 84)
