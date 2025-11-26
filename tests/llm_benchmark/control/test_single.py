"""Test suite for single for-loop control structures.

This module contains tests for the SingleForLoop class, which implements
various algorithms using single for-loop iteration patterns. Tests cover
range summation, list operations, and conditional summation.
"""

from typing import List

import pytest

from llm_benchmark.control.single import SingleForLoop


@pytest.mark.parametrize("n, S", [(0, 0), (1, 0), (2, 1), (3, 3), (4, 6), (10, 45)])
def test_sum_range(n: int, S: int) -> None:
    """Test summation of integers from 0 to n-1.
    
    Validates that sum_range correctly computes the sum of all integers
    in the range [0, n). This tests basic single loop iteration and
    accumulation.
    
    Args:
        n: The upper bound (exclusive) of the range to sum.
        S: The expected sum of integers from 0 to n-1.
    
    Test cases:
        - n=0: Empty range, sum should be 0
        - n=1: Range [0], sum is 0
        - n=2: Range [0,1], sum is 1
        - n=3: Range [0,1,2], sum is 3
        - n=4: Range [0,1,2,3], sum is 6
        - n=10: Range [0..9], sum is 45
    """
    assert SingleForLoop.sum_range(n) == S


def test_benchmark_sum_range(benchmark) -> None:
    """Benchmark the range summation operation.
    
    Measures the performance of summing integers from 0 to 99.
    """
    benchmark(SingleForLoop.sum_range, 100)


@pytest.mark.parametrize(
    "v, M",
    [([0], 0), ([1, 2, 3, 4, 5], 5), ([1, 1, 1, 1, 0], 1), ([-1, -1, -1, -1, 0], 0)],
)
def test_max_list(v: List[int], M: int) -> None:
    """Test finding the maximum value in a list.
    
    Validates that max_list correctly identifies the maximum element
    in a list of integers using a single loop iteration.
    
    Args:
        v: The list of integers to search.
        M: The expected maximum value in the list.
    
    Test cases:
        - [0]: Single element list
        - [1,2,3,4,5]: Ascending order, max at end
        - [1,1,1,1,0]: Repeated values with smaller value at end
        - [-1,-1,-1,-1,0]: Negative numbers with zero at end
    """
    assert SingleForLoop.max_list(v) == M


def test_benchmark_max_list(benchmark) -> None:
    """Benchmark the maximum value search operation.
    
    Measures the performance of finding the maximum in a 5-element list.
    """
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
    """Test conditional summation based on modulus operation.
    
    Validates that sum_modulus correctly sums integers from 0 to n-1
    that are divisible by m (i.e., where i % m == 0).
    
    Args:
        n: The upper bound (exclusive) of the range.
        m: The modulus divisor.
        S: The expected sum of values divisible by m.
    
    Test cases:
        - n=0, m=2: Empty range
        - n=1, m=2: Only 0, which is divisible by 2, but sum is 0
        - n=2, m=2: Only 0 is divisible, sum is 0
        - n=3, m=2: 0 and 2 divisible, sum is 2
        - n=4, m=2: 0 and 2 divisible, sum is 2
        - n=10, m=2: 0,2,4,6,8 divisible, sum is 20
        - n=10, m=3: 0,3,6,9 divisible, sum is 18
        - n=10, m=4: 0,4,8 divisible, sum is 12
    """
    assert SingleForLoop.sum_modulus(n, m) == S


def test_benchmark_sum_modulus(benchmark) -> None:
    """Benchmark the conditional modulus summation operation.
    
    Measures the performance of summing values divisible by 2 in range [0,100).
    """
    benchmark(SingleForLoop.sum_modulus, 100, 2)
