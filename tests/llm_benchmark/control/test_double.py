from typing import List

import pytest

from llm_benchmark.control.double import DoubleForLoop


@pytest.mark.parametrize(
    "exclusive_upper_bound, expected_sum",
    [(1, 0), (2, 1), (3, 5), (10, 285)],
    ids=["zero-only", "includes-one", "includes-two", "below-ten"],
)
def test_sum_square_adds_squares_below_exclusive_upper_bound(
    exclusive_upper_bound: int, expected_sum: int
) -> None:
    actual_sum = DoubleForLoop.sum_square(exclusive_upper_bound)

    assert actual_sum == expected_sum


def test_benchmark_sum_square(benchmark) -> None:
    benchmark(DoubleForLoop.sum_square, 100)


@pytest.mark.parametrize(
    "exclusive_upper_bound, expected_sum",
    [(1, 0), (2, 1), (3, 4), (10, 165)],
    ids=["first-row", "two-rows", "three-rows", "ten-rows"],
)
def test_sum_triangle_adds_each_inclusive_row_below_upper_bound(
    exclusive_upper_bound: int, expected_sum: int
) -> None:
    actual_sum = DoubleForLoop.sum_triangle(exclusive_upper_bound)

    assert actual_sum == expected_sum


def test_benchmark_sum_triangle(benchmark) -> None:
    benchmark(DoubleForLoop.sum_triangle, 100)


@pytest.mark.parametrize(
    "values, expected_pair_count",
    [
        pytest.param([0], 0, id="single-value"),
        pytest.param([1, 2, 3], 0, id="all-distinct"),
        pytest.param([1, 1, 1], 0, id="three-equal-values-do-not-pair"),
        pytest.param([1, 1, 2], 1, id="one-value-occurs-exactly-twice"),
        pytest.param([1, 1, 2, 2], 2, id="two-values-occur-exactly-twice"),
    ],
)
def test_count_pairs_counts_values_occurring_exactly_twice(
    values: List[int], expected_pair_count: int
) -> None:
    actual_pair_count = DoubleForLoop.count_pairs(values)

    assert actual_pair_count == expected_pair_count


def test_benchmark_count_pairs(benchmark) -> None:
    benchmark(DoubleForLoop.count_pairs, [1, 1, 2, 2])


@pytest.mark.parametrize(
    "arr0, arr1, count",
    [
        ([0], [0], 1),
        ([1, 2, 3], [2, 3, 1], 0),
        ([1, 1, 1], [1, 2, 3], 1),
        ([1, 1, 2], [1, 2, 2], 2),
        ([1, 1, 2, 2], [1, 1, 2, 2], 4),
    ],
)
def test_count_duplicates(arr0: List[int], arr1: List[int], count: int) -> None:
    assert DoubleForLoop.count_duplicates(arr0, arr1) == count


def test_benchmark_count_duplicates(benchmark) -> None:
    benchmark(DoubleForLoop.count_duplicates, [1, 1, 2, 2], [1, 1, 2, 2])


@pytest.mark.parametrize(
    "matrix, S",
    [
        ([[0]], 0),
        ([[0, 1], [2, 3]], 6),
        ([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 36),
    ],
)
def test_sum_matrix(matrix: List[List[int]], S: int) -> None:
    assert DoubleForLoop.sum_matrix(matrix) == S


def test_benchmark_sum_matrix(benchmark) -> None:
    benchmark(DoubleForLoop.sum_matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
