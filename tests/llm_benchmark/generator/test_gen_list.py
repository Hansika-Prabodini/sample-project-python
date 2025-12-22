import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that random_list respects the exclusive upper bound for m.
    
    The documentation states that m is the maximum value (exclusive),
    so all generated values should be < m.
    """
    # Test with m=1, so only 0 should be possible (0 <= value < 1)
    result = GenList.random_list(100, 1)
    
    # All values should be strictly less than m=1 (i.e., only 0)
    assert all(val < 1 for val in result), f"Found values >= 1 in result: {result}"
    assert all(val == 0 for val in result), f"Expected all 0s, got: {result}"


def test_random_list_max_exclusive_range():
    """Test that random_list generates values in correct range [0, m)."""
    # Test with m=5, values should be in [0, 1, 2, 3, 4]
    result = GenList.random_list(1000, 5)
    
    # All values should be in range [0, 5)
    assert all(0 <= val < 5 for val in result), f"Found values outside [0, 5): {result}"
    
    # None should be >= 5
    assert not any(val >= 5 for val in result), f"Found values >= 5: {[v for v in result if v >= 5]}"


def test_random_list_basic():
    """Test basic functionality of random_list."""
    result = GenList.random_list(10, 10)
    
    # Should have correct length
    assert len(result) == 10
    
    # All values should be in valid range [0, 10)
    assert all(0 <= val < 10 for val in result)


def test_random_matrix_max_exclusive():
    """Test that random_matrix also respects exclusive upper bound."""
    result = GenList.random_matrix(5, 1)
    
    # Should be 5x5 matrix
    assert len(result) == 5
    assert all(len(row) == 5 for row in result)
    
    # All values should be 0 (since m=1 is exclusive)
    for row in result:
        assert all(val == 0 for val in row), f"Expected all 0s in row: {row}"
