"""Test cases for sorting algorithms.

This module contains unit tests for the Sort class,
which implements various sorting and selection algorithms.
"""

from typing import List

import pytest

from llm_benchmark.algorithms.sort import Sort


@pytest.mark.parametrize(
    "v, expected",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 5, 5], [5, 5, 5]),
    ],
)
def test_sort_list(v: List[int], expected: List[int]) -> None:
    """Test sort_list function which sorts a list in place.
    
    Args:
        v: List to sort
        expected: Expected sorted list
    """
    Sort.sort_list(v)
    assert v == expected


@pytest.mark.parametrize(
    "v, pivot, expected_less, expected_equal",
    [
        ([3, 1, 2, 3, 4, 5, 3], 3, 2, 3),
        ([5, 4, 3, 2, 1], 3, 2, 1),
        ([1, 1, 1], 1, 0, 3),
    ],
)
def test_dutch_flag_partition(
    v: List[int], pivot: int, expected_less: int, expected_equal: int
) -> None:
    """Test dutch_flag_partition function.
    
    After partitioning, all elements less than pivot should come first,
    followed by elements equal to pivot, then elements greater than pivot.
    
    Args:
        v: List to partition
        pivot: Pivot value
        expected_less: Expected count of elements less than pivot
        expected_equal: Expected count of elements equal to pivot
    """
    Sort.dutch_flag_partition(v, pivot)
    
    # Count elements in each partition
    less_count = sum(1 for x in v[:expected_less] if x < pivot)
    equal_start = expected_less
    equal_end = expected_less + expected_equal
    equal_count = sum(1 for x in v[equal_start:equal_end] if x == pivot)
    greater_count = sum(1 for x in v[equal_end:] if x > pivot)
    
    assert less_count == expected_less
    assert equal_count == expected_equal
    assert greater_count == len(v) - expected_less - expected_equal


@pytest.mark.parametrize(
    "v, n, expected",
    [
        ([1, 2, 3, 4, 5], 3, [5, 4, 3]),
        ([5, 3, 2, 1, 4], 2, [5, 4]),
        ([1], 1, [1]),
        ([3, 3, 3], 2, [3, 3]),
        # Edge case: n larger than list length
        ([1, 2, 3], 5, [3, 2, 1, -(2**63), -(2**63)]),
        # Edge case: empty list
        ([], 3, [-(2**63), -(2**63), -(2**63)]),
    ],
)
def test_max_n(v: List[int], n: int, expected: List[int]) -> None:
    """Test max_n function which finds the n largest elements.
    
    When n is greater than the length of the list, the function should
    return all elements sorted in descending order, followed by default
    values (-sys.maxsize - 1) to fill the remaining positions.
    
    Args:
        v: Input list
        n: Number of maximum values to find
        expected: Expected list of n maximum values
    """
    result = Sort.max_n(v, n)
    assert result == expected


def test_benchmark_sort_list(benchmark) -> None:
    """Benchmark the performance of sort_list."""
    v = [5, 4, 3, 2, 1]
    benchmark(Sort.sort_list, v.copy())


def test_benchmark_dutch_flag_partition(benchmark) -> None:
    """Benchmark the performance of dutch_flag_partition."""
    v = [3, 1, 2, 3, 4, 5, 3]
    benchmark(Sort.dutch_flag_partition, v.copy(), 3)


def test_benchmark_max_n(benchmark) -> None:
    """Benchmark the performance of max_n."""
    benchmark(Sort.max_n, [5, 3, 2, 1, 4], 3)
