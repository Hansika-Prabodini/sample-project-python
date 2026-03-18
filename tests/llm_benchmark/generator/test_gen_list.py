"""Test cases for random list and matrix generation.

This module contains unit tests for the GenList class,
which generates random lists and matrices for testing purposes.
"""

import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that random_list respects m as exclusive maximum.
    
    This test verifies the bug fix where randint(0, m) was incorrectly
    including m as a possible value, when the documentation states m
    should be exclusive (i.e., values should be in range [0, m)).
    
    Before fix: randint(0, m) could return values 0, 1, 2, ..., m
    After fix: randint(0, m-1) returns values 0, 1, 2, ..., m-1
    """
    # Generate a large sample to increase confidence
    n = 1000
    m = 5
    
    result = GenList.random_list(n, m)
    
    # Check all values are in range [0, m)
    assert all(0 <= val < m for val in result), \
        f"All values should be in range [0, {m}), but got values: {set(result)}"
    
    # Check that the maximum possible value is m-1, not m
    assert all(val <= m - 1 for val in result), \
        f"No value should be >= {m}, but got values: {set(result)}"
    
    # Check that values can reach m-1 (to ensure we're not overly restrictive)
    # With 1000 samples from [0, 4], we should see 4 at least once
    assert max(result) == m - 1, \
        f"Maximum value should reach {m-1}, but got max: {max(result)}"


def test_random_list_basic():
    """Test basic functionality of random_list."""
    n = 10
    m = 3
    
    result = GenList.random_list(n, m)
    
    # Check correct length
    assert len(result) == n, f"Expected length {n}, got {len(result)}"
    
    # Check all values are integers
    assert all(isinstance(val, int) for val in result), \
        "All values should be integers"
    
    # Check all values are in valid range [0, m)
    assert all(0 <= val < m for val in result), \
        f"All values should be in range [0, {m})"


def test_random_matrix_basic():
    """Test basic functionality of random_matrix."""
    n_rows = 5
    n_cols = 4
    
    result = GenList.random_matrix(n_rows, n_cols)
    
    # Check correct number of rows
    assert len(result) == n_rows, \
        f"Expected {n_rows} rows, got {len(result)}"
    
    # Check each row has correct number of columns
    for i, row in enumerate(result):
        assert len(row) == n_cols, \
            f"Row {i} should have {n_cols} columns, got {len(row)}"
        
        # Check all values are in valid range [0, n_cols)
        # Note: random_matrix uses m as both column count and max value
        assert all(0 <= val < n_cols for val in row), \
            f"All values in row {i} should be in range [0, {n_cols})"


def test_random_list_edge_case_m_equals_1():
    """Test edge case where m=1, should only generate 0s."""
    n = 50
    m = 1
    
    result = GenList.random_list(n, m)
    
    # With m=1 (exclusive), only valid value is 0
    assert all(val == 0 for val in result), \
        f"With m=1, all values should be 0, but got: {set(result)}"


def test_benchmark_random_list(benchmark):
    """Benchmark the performance of random_list generation."""
    benchmark(GenList.random_list, 1000, 100)


def test_benchmark_random_matrix(benchmark):
    """Benchmark the performance of random_matrix generation."""
    benchmark(GenList.random_matrix, 100, 100)
