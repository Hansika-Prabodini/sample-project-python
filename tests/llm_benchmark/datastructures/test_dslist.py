"""Test suite for list data structure operations.

This module contains tests for the DsList class, which implements various
list manipulation algorithms including element modification, searching,
sorting, and reversal operations.
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
    """Test in-place modification of list elements.
    
    Validates that modify_list correctly increments each element in the
    list by 1, returning a new list with modified values.
    
    Args:
        v: The input list to modify.
        ref: The expected result list with each element incremented by 1.
    
    Test cases:
        - [0]: Single element, becomes [1]
        - [1,2,3]: Sequential values, becomes [2,3,4]
        - [1,1,1]: Repeated values, becomes [2,2,2]
        - [1,1,2]: Mixed repeated values, becomes [2,2,3]
        - [1,2,3,4,5]: Longer sequential list, becomes [2,3,4,5,6]
    """
    assert DsList.modify_list(v) == ref


def test_benchmark_modify_list(benchmark) -> None:
    """Benchmark the list modification operation.
    
    Measures the performance of incrementing all elements in a 5-element list.
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
    """Test searching for value indices in a list.
    
    Validates that search_list correctly finds and returns all indices
    where the search value appears in the list.
    
    Args:
        v: The list to search in.
        search_value: The value to search for.
        ref: The expected list of indices where the value is found.
    
    Test cases:
        - Search for 1 in [1,2,3,4,5]: Found at index 0
        - Search for 2 in [1,2,3,4,5]: Found at index 1
        - Search for 9 in [1,2,3,4,5]: Not found, empty list
    """
    assert DsList.search_list(v, search_value) == ref


def test_benchmark_search_list(benchmark) -> None:
    """Benchmark the list search operation.
    
    Measures the performance of searching for value 2 in a 5-element list.
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
    """Test sorting a list in ascending order.
    
    Validates that sort_list correctly sorts a list of integers in
    ascending order, handling both unique and duplicate values.
    
    Args:
        v: The unsorted input list.
        ref: The expected sorted list in ascending order.
    
    Test cases:
        - [5,4,3,2,1]: Reverse order, becomes [1,2,3,4,5]
        - [3,3,2,2,4,3,0,5]: Mixed with duplicates, becomes [0,2,2,3,3,3,4,5]
    """
    assert DsList.sort_list(v) == ref


def test_benchmark_sort_list(benchmark) -> None:
    """Benchmark the list sorting operation.
    
    Measures the performance of sorting a reverse-ordered 5-element list.
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
    """Test reversing the order of list elements.
    
    Validates that reverse_list correctly reverses the order of elements
    in a list, creating a new list with elements in reverse order.
    
    Args:
        v: The input list to reverse.
        ref: The expected list with elements in reverse order.
    
    Test cases:
        - [1,2,3,4,5]: Sequential forward, becomes [5,4,3,2,1]
        - [1,3,2,0]: Mixed order, becomes [0,2,3,1]
        - [1,1,1,1,1]: All same values, remains [1,1,1,1,1]
    """
    assert DsList.reverse_list(v) == ref


def test_benchmark_reverse_list(benchmark) -> None:
    """Benchmark the list reversal operation.
    
    Measures the performance of reversing a 5-element list.
    """
    benchmark(DsList.reverse_list, [1, 2, 3, 4, 5])
