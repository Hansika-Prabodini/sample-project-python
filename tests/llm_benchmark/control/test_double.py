"""Test suite for double nested for-loop control structures.

This module contains tests for the DoubleForLoop class, which implements
various algorithms using nested for-loop iteration patterns. Tests cover
2D summations, pair counting, duplicate detection, and matrix operations.
"""

from typing import List

import pytest

from llm_benchmark.control.double import DoubleForLoop


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 5), (10, 285)])
def test_sum_square(n: int, S: int) -> None:
    """Test summation over a square grid pattern.
    
    Validates that sum_square correctly computes the sum using nested loops
    over a square range [0,n) x [0,n), typically summing i*j for all pairs.
    
    Args:
        n: The dimension of the square grid (both width and height).
        S: The expected sum over all grid positions.
    
    Test cases:
        - n=1: 1x1 grid, sum is 0
        - n=2: 2x2 grid, sum is 1
        - n=3: 3x3 grid, sum is 5
        - n=10: 10x10 grid, sum is 285
    """
    assert DoubleForLoop.sum_square(n) == S


def test_benchmark_sum_square(benchmark) -> None:
    """Benchmark the square grid summation operation.
    
    Measures the performance of nested loop summation over a 100x100 grid.
    """
    benchmark(DoubleForLoop.sum_square, 100)


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 4), (10, 165)])
def test_sum_triangle(n: int, S: int) -> None:
    """Test summation over a triangular pattern.
    
    Validates that sum_triangle correctly computes the sum using nested loops
    where the inner loop range depends on the outer loop variable, creating
    a triangular iteration pattern.
    
    Args:
        n: The base dimension of the triangle.
        S: The expected sum over the triangular pattern.
    
    Test cases:
        - n=1: Minimal triangle, sum is 0
        - n=2: Small triangle, sum is 1
        - n=3: Triangle with 3 levels, sum is 4
        - n=10: Larger triangle, sum is 165
    """
    assert DoubleForLoop.sum_triangle(n) == S


def test_benchmark_sum_triangle(benchmark) -> None:
    """Benchmark the triangular pattern summation operation.
    
    Measures the performance of nested loop summation over a triangular
    pattern with base 100.
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
    """Test counting of equal value pairs at different indices.
    
    Validates that count_pairs correctly counts pairs (i,j) where i < j
    and arr[i] == arr[j] using nested loops.
    
    Args:
        arr: The list to search for matching pairs.
        count: The expected number of pairs found.
    
    Test cases:
        - [0]: Single element, no pairs possible
        - [1,2,3]: All distinct values, no matching pairs
        - [1,1,1]: All same value but counting unique pairs (i<j)
        - [1,1,2]: Two 1's form one pair
        - [1,1,2,2]: Two 1's form one pair, two 2's form one pair
    """
    assert DoubleForLoop.count_pairs(arr) == count


def test_benchmark_count_pairs(benchmark) -> None:
    """Benchmark the pair counting operation.
    
    Measures the performance of counting pairs in a list with duplicates.
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
    """Test counting matching elements between two arrays.
    
    Validates that count_duplicates correctly counts pairs (i,j) where
    arr0[i] == arr1[j] at the same index using nested loops.
    
    Args:
        arr0: The first list to compare.
        arr1: The second list to compare.
        count: The expected number of matching index pairs.
    
    Test cases:
        - [0], [0]: Single matching element
        - [1,2,3], [2,3,1]: No matches at same indices
        - [1,1,1], [1,2,3]: Only first elements match
        - [1,1,2], [1,2,2]: Two matching index pairs
        - [1,1,2,2], [1,1,2,2]: Four matching index pairs
    """
    assert DoubleForLoop.count_duplicates(arr0, arr1) == count


def test_benchmark_count_duplicates(benchmark) -> None:
    """Benchmark the duplicate counting operation between two arrays.
    
    Measures the performance of counting matching elements at same indices.
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
    """Test summation of all elements in a 2D matrix.
    
    Validates that sum_matrix correctly computes the sum of all elements
    in a 2D matrix using nested loops to iterate over rows and columns.
    
    Args:
        matrix: The 2D list (matrix) to sum.
        S: The expected sum of all matrix elements.
    
    Test cases:
        - [[0]]: 1x1 matrix with single zero element
        - [[0,1],[2,3]]: 2x2 matrix, sum is 0+1+2+3 = 6
        - [[0,1,2],[3,4,5],[6,7,8]]: 3x3 matrix, sum is 0+1+...+8 = 36
    """
    assert DoubleForLoop.sum_matrix(matrix) == S


def test_benchmark_sum_matrix(benchmark) -> None:
    """Benchmark the matrix summation operation.
    
    Measures the performance of summing all elements in a 3x3 matrix.
    """
    benchmark(DoubleForLoop.sum_matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
