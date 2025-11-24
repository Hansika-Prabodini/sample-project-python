#!/usr/bin/env python3
"""Simple test to verify the rotate_list bug fix"""

from src.llm_benchmark.datastructures.dslist import DsList


def test_negative_rotation():
    """Test that negative rotation works correctly"""
    v = [1, 2, 3, 4, 5]
    result = DsList.rotate_list(v, -1)
    expected = [5, 1, 2, 3, 4]
    assert result == expected, f"Expected {expected}, got {result}"
    assert len(result) == len(v), f"Length mismatch: expected {len(v)}, got {len(result)}"
    print("✓ Negative rotation test passed")


def test_large_rotation():
    """Test that rotation > len(v) works correctly"""
    v = [1, 2, 3, 4, 5]
    result = DsList.rotate_list(v, 6)
    expected = [2, 3, 4, 5, 1]
    assert result == expected, f"Expected {expected}, got {result}"
    assert len(result) == len(v), f"Length mismatch: expected {len(v)}, got {len(result)}"
    print("✓ Large rotation test passed")


def test_empty_list():
    """Test that empty list is handled correctly"""
    v = []
    result = DsList.rotate_list(v, 5)
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Empty list test passed")


def test_basic_rotation():
    """Test basic rotation"""
    v = [1, 2, 3, 4, 5]
    result = DsList.rotate_list(v, 2)
    expected = [3, 4, 5, 1, 2]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic rotation test passed")


if __name__ == "__main__":
    print("Testing rotate_list bug fix...")
    print()
    
    test_basic_rotation()
    test_negative_rotation()
    test_large_rotation()
    test_empty_list()
    
    print()
    print("All tests passed! ✓")
    print()
    print("Summary:")
    print("--------")
    print("Bug fixed: rotate_list now correctly handles:")
    print("  - Negative rotation values (wrap around)")
    print("  - Rotation values larger than list length (wrap around)")
    print("  - Empty lists")
    print("  - All basic rotation cases")
