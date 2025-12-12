"""Test cases for sorting algorithms.

This module contains unit tests for the Sort class,
which implements various sorting and selection algorithms.
"""

from typing import List

import pytest

from llm_benchmark.algorithms.sort import Sort


@pytest.mark.parametrize(
    "v, n, expected",
    [
        ([5, 3, 2, 1, 4], 3, [5, 4, 3]),
        ([5, 3, 2, 1, 4], 1, [5]),
        ([5, 3, 2, 1, 4], 5, [5, 4, 3, 2, 1]),
        ([1, 2, 3], 5, [3, 2, 1, -9223372036854775808, -9223372036854775808]),  # n > len(v)
        ([10], 3, [10, -9223372036854775808, -9223372036854775808]),  # n > len(v)
        ([], 2, [-9223372036854775808, -9223372036854775808]),  # empty list
    ],
)
def test_max_n(v: List[int], n: int, expected: List[int]) -> None:
    """Test max_n function which finds the n largest elements in a list.
    
    The function should return the n largest elements in descending order.
    If n > len(v), the remaining positions should be filled with -maxsize - 1.
    
    Args:
        v: Input list of integers
        n: Number of maximum values to find
        expected: Expected list of n maximum values
        
    Test cases:
        - [5,3,2,1,4], n=3: Returns [5, 4, 3]
        - [5,3,2,1,4], n=1: Returns [5]
        - [5,3,2,1,4], n=5: Returns all elements [5, 4, 3, 2, 1]
        - [1,2,3], n=5: Returns [3, 2, 1, -maxsize-1, -maxsize-1]
        - [10], n=3: Returns [10, -maxsize-1, -maxsize-1]
        - [], n=2: Returns [-maxsize-1, -maxsize-1]
    """
    result = Sort.max_n(v, n)
    assert result == expected
