from typing import List

import pytest

from llm_benchmark.control.single import SingleForLoop


@pytest.mark.parametrize(
    "exclusive_upper_bound, expected_sum",
    [(0, 0), (1, 0), (2, 1), (3, 3), (4, 6), (10, 45)],
    ids=["empty-range", "only-zero", "below-two", "below-three", "below-four", "below-ten"],
)
def test_sum_range_adds_integers_below_exclusive_upper_bound(
    exclusive_upper_bound: int, expected_sum: int
) -> None:
    actual_sum = SingleForLoop.sum_range(exclusive_upper_bound)

    assert actual_sum == expected_sum


def test_benchmark_sum_range(benchmark) -> None:
    benchmark(SingleForLoop.sum_range, 100)


@pytest.mark.parametrize(
    "values, expected_maximum",
    [
        pytest.param([0], 0, id="single-value"),
        pytest.param([1, 2, 3, 4, 5], 5, id="ascending-values"),
        pytest.param([1, 1, 1, 1, 0], 1, id="repeated-maximum"),
        pytest.param([-1, -1, -1, -1, 0], 0, id="zero-after-negatives"),
    ],
)
def test_max_list_returns_largest_value(
    values: List[int], expected_maximum: int
) -> None:
    actual_maximum = SingleForLoop.max_list(values)

    assert actual_maximum == expected_maximum


def test_benchmark_max_list(benchmark) -> None:
    benchmark(SingleForLoop.max_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "n, m, S",
    [
        (0, 2, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 2),
        (4, 2, 2),
        (10, 2, 20),
        (10, 3, 18),
        (10, 4, 12),
    ],
)
def test_sum_modulus(n: int, m: int, S: int) -> None:
    assert SingleForLoop.sum_modulus(n, m) == S


def test_benchmark_sum_modulus(benchmark) -> None:
    benchmark(SingleForLoop.sum_modulus, 100, 2)
