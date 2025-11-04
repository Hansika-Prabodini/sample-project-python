from typing import List

import pytest

from llm_benchmark.algorithms.sort import Sort


@pytest.mark.parametrize(
    "v, expected",
    [
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 3, 2, 2, 4, 3, 0, 5], [0, 2, 2, 3, 3, 3, 4, 5]),
    ],
)
def test_sort_list(v: List[int], expected: List[int]) -> None:
    v_copy = v.copy()
    Sort.sort_list(v_copy)
    assert v_copy == expected


def test_benchmark_sort_list(benchmark) -> None:
    benchmark(lambda: Sort.sort_list([5, 4, 3, 2, 1]))


@pytest.mark.parametrize(
    "v, pivot, expected",
    [
        ([], 1, []),
        ([1], 1, [1]),
        ([0, 1, 2, 0, 2, 1, 1], 1, [0, 0, 1, 1, 1, 2, 2]),
        ([3, 5, 2, 5, 3, 2, 5, 3], 3, [2, 2, 3, 3, 3, 5, 5, 5]),
    ],
)
def test_dutch_flag_partition(v: List[int], pivot: int, expected: List[int]) -> None:
    v_copy = v.copy()
    Sort.dutch_flag_partition(v_copy, pivot)
    # Verify three-way partition properties:
    # 1) All < pivot are first
    # 2) Then == pivot
    # 3) Then > pivot
    # Also stable in counts, though not stable order-wise
    less = [x for x in v_copy if x < pivot]
    equal = [x for x in v_copy if x == pivot]
    greater = [x for x in v_copy if x > pivot]
    assert len(less) + len(equal) + len(greater) == len(v_copy)
    assert all(x < pivot for x in less)
    assert all(x == pivot for x in equal)
    assert all(x > pivot for x in greater)
    # And compare against a canonical expected arrangement for determinism
    assert v_copy == expected


def test_benchmark_dutch_flag_partition(benchmark) -> None:
    benchmark(lambda: Sort.dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 1))


@pytest.mark.parametrize(
    "v, n, expected",
    [
        ([1, 2, 3, 4, 5], 1, [5]),
        ([1, 2, 3, 4, 5], 2, [5, 4]),
        ([5, 1, 5, 3], 2, [5, 5]),
        ([3, 3, 3], 2, [3, 3]),
    ],
)
def test_max_n(v: List[int], n: int, expected: List[int]) -> None:
    assert Sort.max_n(v, n) == expected


def test_benchmark_max_n(benchmark) -> None:
    benchmark(Sort.max_n, [1, 2, 3, 4, 5], 3)
