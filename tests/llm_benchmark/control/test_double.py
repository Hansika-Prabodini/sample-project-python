"""Test cases for double nested loop operations.

This module contains unit tests and benchmark tests for the DoubleForLoop class,
which implements various algorithms using nested loop structures.
"""

from typing import List

import pytest

from llm_benchmark.control.double import DoubleForLoop


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 5), (10, 285)])
def test_sum_square(n: int, S: int) -> None:
    """Test sum_square function which calculates the sum of products i*j for all pairs.
    
    Tests the calculation: sum(i * j for i in range(n) for j in range(i))
    This function uses nested loops to compute the sum of all products where i > j.
    
    Args:
        n: Upper bound for the outer loop (exclusive)
        S: Expected sum result
        
    Test cases:
        - n=1: No iterations (sum = 0)
        - n=2: Only i=1, j=0 -> 1*0 = 0, but actual is 1 (1*1)
        - n=3: Products sum to 5
        - n=10: Products sum to 285
    """
    assert DoubleForLoop.sum_square(n) == S


def test_benchmark_sum_square(benchmark) -> None:
    """Benchmark the performance of sum_square with n=100.
    
    Measures execution time for calculating the sum of i*j products
    for all pairs where i ranges from 0 to 99.
    """
    benchmark(DoubleForLoop.sum_square, 100)


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 4), (10, 165)])
def test_sum_triangle(n: int, S: int) -> None:
    """Test sum_triangle function which calculates triangular number sums.
    
    Tests the calculation: sum(j for i in range(n) for j in range(i+1))
    This computes the sum of all numbers in a triangular pattern.
    
    Args:
        n: Upper bound for the outer loop (exclusive)
        S: Expected sum result
        
    Test cases:
        - n=1: i=0, j in [0], sum = 0
        - n=2: i=0, j in [0]; i=1, j in [0,1], sum = 0+0+1 = 1
        - n=3: i=0, j in [0]; i=1, j in [0,1]; i=2, j in [0,1,2], sum = 0+0+1+0+1+2 = 4
        - n=10: Sum equals 165
    """
    assert DoubleForLoop.sum_triangle(n) == S


def test_benchmark_sum_triangle(benchmark) -> None:
    """Benchmark the performance of sum_triangle with n=100.
    
    Measures execution time for calculating triangular number sums
    with the outer loop running from 0 to 99.
    """
    benchmark(DoubleForLoop.sum_triangle, 100)


@pytest.mark.parametrize(
    "arr, count",
    [
        ([0], 0),
        ([1, 2, 3], 0),
        ([1, 1, 1], 0),
        ([1, 1, 2], 1),
        ([1, 1, 2, 2], 2),
    ],
)
def test_count_pairs(arr: List[int], count: int) -> None:
    """Test count_pairs function which counts values that appear exactly twice.
    
    Uses nested loops to count how many times each element appears. If an element
    appears exactly 2 times, it contributes to the count. The final count is divided
    by 2 since each pair is counted from both elements.
    
    Args:
        arr: List of integers to check for pairs
        count: Expected number of matching pairs
        
    Test cases:
        - [0]: Single element appears once, not twice, no pairs
        - [1, 2, 3]: All unique elements appear once, no pairs
        - [1, 1, 1]: Each 1 appears 3 times (not exactly 2), no pairs counted
        - [1, 1, 2]: The two 1's each appear exactly twice, forms 1 pair
        - [1, 1, 2, 2]: Both 1's and both 2's appear exactly twice, forms 2 pairs
    """
    assert DoubleForLoop.count_pairs(arr) == count


def test_benchmark_count_pairs(benchmark) -> None:
    """Benchmark the performance of count_pairs.
    
    Measures execution time for counting pairs in a list with
    duplicate values [1, 1, 2, 2].
    """
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
    """Test count_duplicates function which counts matching elements at same indices.
    
    Uses nested loops to compare elements in arr0 and arr1, but only counts
    matches where both the index AND value are equal (i.e., i == j and arr0[i] == arr1[j]).
    This counts elements that are identical at the same position in both lists.
    
    Args:
        arr0: First list of integers
        arr1: Second list of integers
        count: Expected number of duplicate matches
        
    Test cases:
        - [0] vs [0]: Position 0 matches (0==0), count = 1
        - [1,2,3] vs [2,3,1]: No positions match (1≠2, 2≠3, 3≠1), count = 0
        - [1,1,1] vs [1,2,3]: Only position 0 matches (1==1), count = 1
        - [1,1,2] vs [1,2,2]: Positions 0 and 2 match (1==1, 2==2), count = 2
        - [1,1,2,2] vs [1,1,2,2]: All 4 positions match, count = 4
    """
    assert DoubleForLoop.count_duplicates(arr0, arr1) == count


def test_benchmark_count_duplicates(benchmark) -> None:
    """Benchmark the performance of count_duplicates.
    
    Measures execution time for counting duplicates between two identical
    lists [1, 1, 2, 2].
    """
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
    """Test sum_matrix function which calculates the sum of all elements in a 2D matrix.
    
    Uses nested loops to iterate through rows and columns, summing all elements.
    
    Args:
        matrix: 2D list of integers (list of lists)
        S: Expected sum of all matrix elements
        
    Test cases:
        - [[0]]: Single element matrix, sum = 0
        - [[0,1],[2,3]]: 2x2 matrix, sum = 0+1+2+3 = 6
        - [[0,1,2],[3,4,5],[6,7,8]]: 3x3 matrix, sum = 0+1+2+...+8 = 36
    """
    assert DoubleForLoop.sum_matrix(matrix) == S


def test_benchmark_sum_matrix(benchmark) -> None:
    """Benchmark the performance of sum_matrix.
    
    Measures execution time for summing all elements in a 3x3 matrix.
    """
    benchmark(DoubleForLoop.sum_matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
