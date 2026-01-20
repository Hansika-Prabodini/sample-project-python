"""Test cases for single loop operations.

This module contains unit tests and benchmark tests for the SingleForLoop class,
which implements various algorithms using single loop structures.
"""

from typing import List

import pytest

from llm_benchmark.control.single import sum_range, max_list, sum_modulus


@pytest.mark.parametrize("n, S", [(0, 0), (1, 0), (2, 1), (3, 3), (4, 6), (10, 45)])
def test_sum_range(n: int, S: int) -> None:
    """Test sum_range function which calculates the sum of all integers from 0 to n-1.
    
    Tests the calculation: sum(range(n)) = 0 + 1 + 2 + ... + (n-1)
    This is equivalent to the formula: n * (n - 1) / 2
    
    Args:
        n: Upper bound for the range (exclusive)
        S: Expected sum result
        
    Test cases:
        - n=0: Empty range, sum = 0
        - n=1: Only 0, sum = 0
        - n=2: 0+1 = 1
        - n=3: 0+1+2 = 3
        - n=4: 0+1+2+3 = 6
        - n=10: 0+1+...+9 = 45
    """
    assert sum_range(n) == S


def test_benchmark_sum_range(benchmark) -> None:
    """Benchmark the performance of sum_range with n=100.
    
    Measures execution time for summing all integers from 0 to 99
    using a single loop iteration.
    """
    benchmark(sum_range, 100)


@pytest.mark.parametrize(
    "v, M",
    [([0], 0), ([1, 2, 3, 4, 5], 5), ([1, 1, 1, 1, 0], 1), ([-1, -1, -1, -1, 0], 0)],
)
def test_max_list(v: List[int], M: int) -> None:
    """Test max_list function which finds the maximum value in a list.
    
    Iterates through the list once to find the largest element.
    
    Args:
        v: List of integers to search
        M: Expected maximum value
        
    Test cases:
        - [0]: Single element, max = 0
        - [1,2,3,4,5]: Ascending order, max = 5
        - [1,1,1,1,0]: Repeated values with smaller element, max = 1
        - [-1,-1,-1,-1,0]: All negative except one zero, max = 0
    """
    assert max_list(v) == M


def test_benchmark_max_list(benchmark) -> None:
    """Benchmark the performance of max_list.
    
    Measures execution time for finding the maximum value in a
    5-element list [1, 2, 3, 4, 5].
    """
    benchmark(max_list, [1, 2, 3, 4, 5])


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
    """Test sum_modulus function which sums all integers divisible by m in range [0, n).
    
    Iterates from 0 to n-1 and sums only the numbers that are divisible by m
    (i.e., where i % m == 0).
    
    Args:
        n: Upper bound for the range (exclusive)
        m: Modulus divisor to check
        S: Expected sum result
        
    Test cases:
        - n=0, m=2: Empty range, sum = 0
        - n=1, m=2: Only 0 (0%2==0), sum = 0
        - n=2, m=2: 0 (0%2==0), sum = 0
        - n=3, m=2: 0, 2 (both divisible by 2), sum = 2
        - n=4, m=2: 0, 2, sum = 2
        - n=10, m=2: 0+2+4+6+8 = 20
        - n=10, m=3: 0+3+6+9 = 18
        - n=10, m=4: 0+4+8 = 12
    """
    assert sum_modulus(n, m) == S


def test_benchmark_sum_modulus(benchmark) -> None:
    """Benchmark the performance of sum_modulus.
    
    Measures execution time for summing all numbers divisible by 2
    in the range [0, 100).
    """
    benchmark(sum_modulus, 100, 2)
