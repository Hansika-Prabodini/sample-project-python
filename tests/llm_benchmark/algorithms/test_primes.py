from typing import List

import pytest

from llm_benchmark.algorithms.primes import Primes


@pytest.mark.parametrize(
    "number, expected_is_prime",
    [
        pytest.param(0, False, id="zero-is-not-prime"),
        pytest.param(1, False, id="one-is-not-prime"),
        pytest.param(2, True, id="smallest-prime"),
        pytest.param(3, True, id="odd-prime"),
        pytest.param(4, False, id="even-composite"),
        pytest.param(10, False, id="larger-even-composite"),
        pytest.param(17, True, id="larger-prime"),
        pytest.param(26, False, id="prime-multiple"),
    ],
)
def test_is_prime_identifies_prime_and_composite_numbers(
    number: int, expected_is_prime: bool
) -> None:
    actual_is_prime = Primes.is_prime(number)

    assert actual_is_prime is expected_is_prime


@pytest.mark.parametrize(
    "number, expected_is_prime",
    [
        pytest.param(-10, False, id="negative-even"),
        pytest.param(-1, False, id="negative-one"),
        pytest.param(0, False, id="zero"),
        pytest.param(1, False, id="one"),
        pytest.param(2, True, id="smallest-prime"),
        pytest.param(3, True, id="odd-prime"),
        pytest.param(4, False, id="even-composite"),
        pytest.param(10, False, id="larger-even-composite"),
        pytest.param(17, True, id="larger-prime"),
        pytest.param(26, False, id="prime-multiple"),
    ],
)
def test_square_root_primality_check_handles_all_integer_categories(
    number: int, expected_is_prime: bool
) -> None:
    actual_is_prime = Primes.is_prime_ineff(number)

    assert actual_is_prime is expected_is_prime


def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)


@pytest.mark.parametrize(
    "exclusive_upper_bound, expected_sum",
    [(0, 0), (1, 0), (2, 0), (3, 2), (4, 5), (10, 17), (100, 1060)],
    ids=["empty-range", "below-primes", "excludes-two", "includes-two", "two-primes", "below-ten", "below-one-hundred"],
)
def test_sum_primes_adds_primes_below_exclusive_upper_bound(
    exclusive_upper_bound: int, expected_sum: int
) -> None:
    actual_sum = Primes.sum_primes(exclusive_upper_bound)

    assert actual_sum == expected_sum


def test_benchmark_sum_primes(benchmark) -> None:
    benchmark(Primes.sum_primes, 20)


@pytest.mark.parametrize(
    "number, expected_factors",
    [
        pytest.param(0, [], id="zero-has-no-factors"),
        pytest.param(1, [], id="one-has-no-factors"),
        pytest.param(2, [2], id="smallest-prime"),
        pytest.param(3, [3], id="odd-prime"),
        pytest.param(4, [2, 2], id="repeated-factor"),
        pytest.param(10, [2, 5], id="two-distinct-factors"),
        pytest.param(17, [17], id="larger-prime"),
        pytest.param(84, [2, 2, 3, 7], id="multiple-prime-factors"),
    ],
)
def test_prime_factors_returns_factors_in_ascending_order(
    number: int, expected_factors: List[int]
) -> None:
    actual_factors = Primes.prime_factors(number)

    assert actual_factors == expected_factors


def test_benchmark_prime_factors(benchmark) -> None:
    benchmark(Primes.prime_factors, 84)
