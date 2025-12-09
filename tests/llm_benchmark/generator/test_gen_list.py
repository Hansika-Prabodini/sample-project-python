"""Test cases for random list and matrix generation.

This module contains unit tests for the GenList class,
which generates random lists and matrices for testing purposes.
"""

import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that random_list generates values less than m (exclusive).
    
    According to the documentation, m should be the exclusive upper bound,
    meaning generated values should be in the range [0, m).
    This test generates a large number of random values and verifies that
    none of them equal m.
    """
    n = 1000  # Generate many values to have high confidence
    m = 10
    
    # Generate multiple lists to increase coverage
    for _ in range(10):
        random_values = GenList.random_list(n, m)
        
        # Check that all values are in range [0, m)
        assert all(0 <= val < m for val in random_values), \
            f"random_list should generate values in [0, {m}), but got values: {set(random_values)}"
        
        # Specifically check that m is never in the generated values
        assert m not in random_values, \
            f"random_list with m={m} should never generate {m} (should be exclusive)"


def test_random_list_length():
    """Test that random_list generates the correct number of elements."""
    n = 15
    m = 20
    result = GenList.random_list(n, m)
    assert len(result) == n, f"Expected list of length {n}, got {len(result)}"


def test_random_list_min_inclusive():
    """Test that random_list can generate 0 as a value.
    
    The lower bound should be inclusive (>= 0).
    """
    n = 1000
    m = 10
    
    # Generate multiple lists
    all_values = []
    for _ in range(10):
        all_values.extend(GenList.random_list(n, m))
    
    # With high probability, 0 should appear at least once
    assert 0 in all_values, "random_list should be able to generate 0"


def test_random_matrix_dimensions():
    """Test that random_matrix generates correct dimensions."""
    n = 5  # rows
    m = 3  # columns
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    for row in matrix:
        assert len(row) == m, f"Expected {m} columns in each row, got {len(row)}"


def test_random_matrix_values_in_range():
    """Test that random_matrix generates values in correct range.
    
    Based on the implementation, random_matrix uses random_list(m, m),
    so values should be in range [0, m).
    """
    n = 5
    m = 7
    matrix = GenList.random_matrix(n, m)
    
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            assert 0 <= val < m, \
                f"Value at [{i}][{j}] = {val} is not in range [0, {m})"
