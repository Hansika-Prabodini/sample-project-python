from typing import List

import pytest

from llm_benchmark.algorithms.primes import Primes


@pytest.mark.parametrize(
    "method, n, is_prime",
    [
        (Primes.is_prime, -10, False),
        (Primes.is_prime, -1, False),
        (Primes.is_prime, 0, False),
        (Primes.is_prime, 1, False),
        (Primes.is_prime, 2, True),
        (Primes.is_prime, 4, False),
        (Primes.is_prime, 17, True),
        (Primes.is_prime, 100, False),
        (Primes.is_prime, 997, True),
        (Primes.is_prime, 1000, False),
        (Primes.is_prime_ineff, -10, False),
        (Primes.is_prime_ineff, -1, False),
        (Primes.is_prime_ineff, 0, False),
        (Primes.is_prime_ineff, 1, False),
        (Primes.is_prime_ineff, 2, True),
        (Primes.is_prime_ineff, 4, False),
        (Primes.is_prime_ineff, 17, True),
        (Primes.is_prime_ineff, 100, False),
        (Primes.is_prime_ineff, 997, True),
        (Primes.is_prime_ineff, 1000, False),
    ],
)
def test_is_prime(method, n: int, is_prime: bool) -> None:
    assert method(n) == is_prime


def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)


@pytest.mark.parametrize(
    "n, S", [(0, 0), (1, 0), (2, 0), (3, 2), (4, 5), (10, 17), (100, 1060)]
)
def test_sum_primes(n: int, S: int) -> None:
    assert Primes.sum_primes(n) == S


def test_benchmark_sum_primes(benchmark) -> None:
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
    assert Primes.prime_factors(n) == factors


def test_benchmark_prime_factors(benchmark) -> None:
    benchmark(Primes.prime_factors, 84)
