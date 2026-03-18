"""Test cases for list generation operations.

This module contains unit tests for the GenList class,
which implements random list and matrix generation.
"""

import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_value_exclusive():
    """Test that random_list respects the exclusive upper bound.
    
    The docstring specifies that m is the maximum value (exclusive),
    so generated values should be in the range [0, m), not [0, m].
    This test generates many random values and verifies none are >= m.
    """
    n = 1000  # Generate many values to have high confidence
    m = 10    # Maximum value (exclusive)
    
    result = GenList.random_list(n, m)
    
    # Verify we generated the correct number of values
    assert len(result) == n
    
    # Verify all values are in the range [0, m)
    for value in result:
        assert 0 <= value < m, f"Generated value {value} is not in range [0, {m})"


def test_random_list_min_value_inclusive():
    """Test that random_list includes 0 as a possible value.
    
    Generates many random values and checks that 0 appears at least once,
    confirming the lower bound is inclusive.
    """
    n = 1000
    m = 10
    
    result = GenList.random_list(n, m)
    
    # With 1000 random values in range [0, 10), 0 should appear at least once
    # (probability of not getting 0 in 1000 tries is (9/10)^1000 ≈ 0)
    assert 0 in result, "Lower bound 0 should be inclusive"


def test_random_list_empty():
    """Test that random_list handles n=0 correctly."""
    result = GenList.random_list(0, 10)
    assert result == []


@pytest.mark.parametrize("n,m", [(5, 3), (10, 20), (100, 5)])
def test_random_list_size(n: int, m: int):
    """Test that random_list generates the correct number of elements.
    
    Args:
        n: Number of integers to generate
        m: Maximum value (exclusive)
    """
    result = GenList.random_list(n, m)
    assert len(result) == n


def test_random_matrix_dimensions():
    """Test that random_matrix generates the correct dimensions.
    
    The matrix should have n rows and m columns.
    """
    n = 5  # rows
    m = 3  # columns
    
    result = GenList.random_matrix(n, m)
    
    # Check number of rows
    assert len(result) == n
    
    # Check number of columns in each row
    for row in result:
        assert len(row) == m


def test_random_matrix_values_in_range():
    """Test that random_matrix generates values in the correct range.
    
    Since random_matrix calls random_list(m, m), values should be in [0, m).
    """
    n = 10
    m = 5
    
    result = GenList.random_matrix(n, m)
    
    # Check all values are in the range [0, m)
    for row in result:
        for value in row:
            assert 0 <= value < m, f"Generated value {value} is not in range [0, {m})"
