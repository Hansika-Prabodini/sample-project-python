"""Test cases for list generator operations.

This module contains unit tests for the GenList class,
which implements random list and matrix generation.
"""

import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that random_list respects the exclusive upper bound.
    
    The docstring for random_list states that m is the maximum value (exclusive).
    This means all generated values should be in the range [0, m), i.e., 0 <= value < m.
    
    Test approach:
        - Generate many random numbers with m=1
        - With m=1 (exclusive), only valid value is 0
        - If bug exists, randint(0, 1) can return 1, violating the exclusive bound
        - If fixed, randint(0, 0) only returns 0, respecting the exclusive bound
    """
    # Generate a large list to ensure we'd see the bug if it exists
    result = GenList.random_list(100, 1)
    
    # All values should be less than m (which is 1)
    for value in result:
        assert value < 1, f"Value {value} should be less than m=1 (exclusive bound)"
    
    # More specifically, all values should be 0 when m=1
    assert all(v == 0 for v in result), "All values should be 0 when m=1 (exclusive)"


def test_random_list_max_exclusive_larger():
    """Test that random_list respects the exclusive upper bound for larger m.
    
    Test with m=5 to ensure no values equal to 5 are generated.
    """
    # Generate many random numbers to increase probability of hitting boundary
    result = GenList.random_list(1000, 5)
    
    # All values should be less than m (which is 5)
    for value in result:
        assert value < 5, f"Value {value} should be less than m=5 (exclusive bound)"
        assert value >= 0, f"Value {value} should be >= 0"


def test_random_list_length():
    """Test that random_list generates the correct number of elements."""
    result = GenList.random_list(10, 5)
    assert len(result) == 10, "Should generate exactly n elements"


@pytest.mark.parametrize("n,m", [(0, 1), (5, 10), (10, 100)])
def test_random_list_bounds(n: int, m: int):
    """Parametrized test to verify bounds for various n and m values.
    
    Args:
        n: Number of integers to generate
        m: Maximum value (exclusive)
    """
    result = GenList.random_list(n, m)
    assert len(result) == n, f"Should generate exactly {n} elements"
    
    if n > 0:
        assert all(0 <= v < m for v in result), f"All values should be in range [0, {m})"
