"""Test cases for random list generation.

This module contains unit tests for the GenList class,
which generates random lists and matrices of integers.
"""

import random
import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_value_exclusive():
    """Test that random_list respects the exclusive upper bound.
    
    The documentation states that m is the maximum value (exclusive),
    meaning generated values should be in the range [0, m).
    This test generates many random numbers and verifies that none
    of them equal or exceed m.
    """
    # Set seed for reproducibility
    random.seed(42)
    
    # Test with different values of m
    test_cases = [
        (100, 5),   # Generate 100 numbers with max value 5 (exclusive)
        (200, 10),  # Generate 200 numbers with max value 10 (exclusive)
        (500, 3),   # Generate 500 numbers with max value 3 (exclusive)
    ]
    
    for n, m in test_cases:
        result = GenList.random_list(n, m)
        
        # All values should be less than m (exclusive upper bound)
        assert all(val < m for val in result), \
            f"random_list generated values >= {m} (should be exclusive upper bound)"
        
        # All values should be >= 0 (inclusive lower bound)
        assert all(val >= 0 for val in result), \
            f"random_list generated values < 0 (should be >= 0)"


def test_random_list_boundary_values():
    """Test that random_list can generate boundary values 0 and m-1.
    
    With enough iterations, we should see both the minimum (0) and
    maximum (m-1) valid values.
    """
    random.seed(123)
    
    # Generate many numbers with small m to ensure we hit boundaries
    m = 3
    result = GenList.random_list(1000, m)
    
    # Should contain 0 (lower boundary)
    assert 0 in result, "random_list should be able to generate 0"
    
    # Should contain m-1 (upper boundary, inclusive)
    assert (m - 1) in result, f"random_list should be able to generate {m-1}"
    
    # Should NOT contain m or higher (exclusive upper bound)
    assert m not in result, f"random_list should not generate {m} (exclusive upper bound)"
    assert not any(val >= m for val in result), \
        f"random_list should not generate values >= {m}"


def test_random_list_length():
    """Test that random_list generates the correct number of elements."""
    random.seed(456)
    
    test_cases = [0, 1, 5, 10, 100]
    
    for n in test_cases:
        result = GenList.random_list(n, 10)
        assert len(result) == n, f"Expected list of length {n}, got {len(result)}"
