"""Test cases for list data structure operations.

This module contains unit tests and benchmark tests for the DsList class,
which implements various list manipulation operations including modification,
searching, sorting, and reversal.
"""

from typing import List

import pytest

from llm_benchmark.datastructures.dslist import DsList


@pytest.mark.parametrize(
    "v, ref",
    [
        ([0], [1]),
        ([1, 2, 3], [2, 3, 4]),
        ([1, 1, 1], [2, 2, 2]),
        ([1, 1, 2], [2, 2, 3]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]),
    ],
)
def test_modify_list(v: List[int], ref: List[int]) -> None:
    """Test modify_list function which increments each element by 1.
    
    Creates a new list where each element is the original element plus 1.
    The function does not modify the original list.
    
    Args:
        v: Input list of integers
        ref: Expected output list with each element incremented
        
    Test cases:
        - [0]: Single element, becomes [1]
        - [1,2,3]: Becomes [2,3,4]
        - [1,1,1]: Repeated values, becomes [2,2,2]
        - [1,1,2]: Mixed values, becomes [2,2,3]
        - [1,2,3,4,5]: Sequential values, becomes [2,3,4,5,6]
    """
    assert DsList.modify_list(v) == ref


def test_benchmark_modify_list(benchmark) -> None:
    """Benchmark the performance of modify_list.
    
    Measures execution time for incrementing each element in a
    5-element list [1, 2, 3, 4, 5].
    """
    benchmark(DsList.modify_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "v, search_value, ref",
    [
        ([1, 2, 3, 4, 5], 1, [0]),
        ([1, 2, 3, 4, 5], 2, [1]),
        ([1, 2, 3, 4, 5], 9, []),
    ],
)
def test_search_list(v: List[int], search_value: int, ref: List[int]) -> None:
    """Test search_list function which finds all indices of a value in a list.
    
    Searches through the list and returns a list of all indices where the
    search value appears. Returns an empty list if the value is not found.
    
    Args:
        v: List to search through
        search_value: Value to search for
        ref: Expected list of indices where the value appears
        
    Test cases:
        - Search for 1 in [1,2,3,4,5]: Found at index 0
        - Search for 2 in [1,2,3,4,5]: Found at index 1
        - Search for 9 in [1,2,3,4,5]: Not found, returns []
    """
    assert DsList.search_list(v, search_value) == ref


def test_benchmark_search_list(benchmark) -> None:
    """Benchmark the performance of search_list.
    
    Measures execution time for searching for value 2 in the list
    [1, 2, 3, 4, 5].
    """
    benchmark(DsList.search_list, [1, 2, 3, 4, 5], 2)


@pytest.mark.parametrize(
    "v, ref",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 3, 2, 2, 4, 3, 0, 5], [0, 2, 2, 3, 3, 3, 4, 5]),
    ],
)
def test_sort_list(v: List[int], ref: List[int]) -> None:
    """Test sort_list function which sorts a list in ascending order.
    
    Returns a new sorted list, leaving the original list unchanged.
    Handles duplicate values correctly.
    
    Args:
        v: Input list to sort
        ref: Expected sorted output list
        
    Test cases:
        - [5,4,3,2,1]: Reverse order, becomes [1,2,3,4,5]
        - [3,3,2,2,4,3,0,5]: Mixed with duplicates, becomes [0,2,2,3,3,3,4,5]
    """
    assert DsList.sort_list(v) == ref


def test_benchmark_sort_list(benchmark) -> None:
    """Benchmark the performance of sort_list.
    
    Measures execution time for sorting a 5-element list in reverse order
    [5, 4, 3, 2, 1].
    """
    benchmark(DsList.sort_list, [5, 4, 3, 2, 1])


@pytest.mark.parametrize(
    "v, ref",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 3, 2, 0], [0, 2, 3, 1]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ],
)
def test_reverse_list(v: List[int], ref: List[int]) -> None:
    """Test reverse_list function which reverses the order of elements.
    
    Returns a new list with elements in reverse order, leaving the original
    list unchanged.
    
    Args:
        v: Input list to reverse
        ref: Expected reversed output list
        
    Test cases:
        - [1,2,3,4,5]: Becomes [5,4,3,2,1]
        - [1,3,2,0]: Becomes [0,2,3,1]
        - [1,1,1,1,1]: All same values, remains [1,1,1,1,1]
    """
    assert DsList.reverse_list(v) == ref


def test_benchmark_reverse_list(benchmark) -> None:
    """Benchmark the performance of reverse_list.
    
    Measures execution time for reversing a 5-element list [1, 2, 3, 4, 5].
    """
    benchmark(DsList.reverse_list, [1, 2, 3, 4, 5])


@pytest.mark.parametrize(
    "v, n, ref",
    [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),
        ([], 0, []),
        ([], 5, []),
        ([1], 0, [1]),
        ([1], 1, [1]),
        ([1], 5, [1]),
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    """Test rotate_list with various rotation amounts including edge cases.
    
    This test verifies that the function correctly handles:
    - Normal rotations (0 < n < len(v))
    - Rotation by length (n == len(v))
    - Rotation by more than length (n > len(v))
    - Empty lists
    - Single-element lists
    """
    assert DsList.rotate_list(v, n) == ref


def test_benchmark_rotate_list(benchmark) -> None:
    benchmark(DsList.rotate_list, [1, 2, 3, 4, 5], 2)
