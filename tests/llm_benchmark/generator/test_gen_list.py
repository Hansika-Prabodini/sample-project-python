"""Test cases for random list generation.

This module contains unit tests for the GenList class,
which implements random list and matrix generation functions.
"""

from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_length() -> None:
    """Test that random_list generates the correct number of elements.
    
    Verifies that the generated list has exactly n elements.
    """
    n = 10
    m = 5
    result = GenList.random_list(n, m)
    assert len(result) == n


def test_random_list_max_value_exclusive() -> None:
    """Test that random_list respects the exclusive upper bound.
    
    The docstring states that m is the "Maximum value of integers (exclusive)",
    meaning generated values should be in the range [0, m), not [0, m].
    This test generates many random numbers and verifies that none equal m.
    
    This test will FAIL before the bug fix (because randint(0, m) includes m)
    and PASS after the bug fix (when changed to randint(0, m-1)).
    """
    n = 1000  # Generate many values to increase likelihood of hitting m if bug exists
    m = 10
    
    # Generate multiple lists to increase confidence
    for _ in range(10):
        result = GenList.random_list(n, m)
        
        # All values should be less than m (since m is exclusive)
        for value in result:
            assert value < m, f"Generated value {value} should be less than {m} (exclusive upper bound)"
            assert value >= 0, f"Generated value {value} should be >= 0"


def test_random_list_min_value() -> None:
    """Test that random_list generates values starting from 0.
    
    Verifies that the minimum possible value is 0 (inclusive lower bound).
    Since we can't deterministically test randomness, we generate many values
    and check they're all >= 0.
    """
    n = 100
    m = 5
    result = GenList.random_list(n, m)
    
    for value in result:
        assert value >= 0, f"Generated value {value} should be >= 0"


def test_random_matrix_dimensions() -> None:
    """Test that random_matrix generates the correct dimensions.
    
    Verifies that the matrix has n rows and m columns.
    """
    n = 5
    m = 3
    result = GenList.random_matrix(n, m)
    
    assert len(result) == n, f"Matrix should have {n} rows"
    for row in result:
        assert len(row) == m, f"Each row should have {m} elements"


def test_random_matrix_max_value_exclusive() -> None:
    """Test that random_matrix respects the exclusive upper bound.
    
    Since random_matrix uses random_list internally, if random_list has the bug,
    random_matrix will inherit it. This test verifies that all values in the
    matrix are less than m.
    """
    n = 10
    m = 5
    result = GenList.random_matrix(n, m)
    
    for row in result:
        for value in row:
            assert value < m, f"Generated value {value} should be less than {m} (exclusive upper bound)"
            assert value >= 0, f"Generated value {value} should be >= 0"


def test_benchmark_random_list(benchmark) -> None:
    """Benchmark the performance of random_list.
    
    Measures execution time for generating a list of 100 random integers
    with maximum value 50.
    """
    benchmark(GenList.random_list, 100, 50)


def test_benchmark_random_matrix(benchmark) -> None:
    """Benchmark the performance of random_matrix.
    
    Measures execution time for generating a 10x10 matrix of random integers.
    """
    benchmark(GenList.random_matrix, 10, 10)
