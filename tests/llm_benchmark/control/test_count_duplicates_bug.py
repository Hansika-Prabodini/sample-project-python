"""Test case that demonstrates the count_duplicates bug fix.

This test would fail with the buggy implementation (which only counted
matches at the same index position) but passes with the corrected 
implementation (which counts all element matches between arrays).
"""

import pytest
from llm_benchmark.control.double import DoubleForLoop


def test_count_duplicates_different_positions():
    """Test that count_duplicates correctly counts elements that appear in both arrays,
    regardless of their position.
    
    This test demonstrates the bug: with the condition 'i == j', the function only
    counted matches at the same index. For example, [1, 2, 3] vs [2, 3, 1] would
    return 0 because:
    - Position 0: arr0[0]=1 != arr1[0]=2
    - Position 1: arr0[1]=2 != arr1[1]=3  
    - Position 2: arr0[2]=3 != arr1[2]=1
    
    But actually, all three elements (1, 2, 3) appear in both arrays, so the
    count should be 3 (each element in arr0 matches exactly one in arr1).
    
    Before fix: Returns 0 (only checks same positions)
    After fix: Returns 3 (correctly counts all matches)
    """
    # Test case where elements exist in both arrays but at different positions
    arr0 = [1, 2, 3]
    arr1 = [2, 3, 1]
    
    # Each element in arr0 appears exactly once in arr1, so we expect 3 matches:
    # - arr0[0]=1 matches arr1[2]=1
    # - arr0[1]=2 matches arr1[0]=2
    # - arr0[2]=3 matches arr1[1]=3
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == 3, f"Expected 3 matches but got {result}"


def test_count_duplicates_with_repetitions():
    """Test count_duplicates with repeated elements to ensure it counts all matches.
    
    When an element appears multiple times in both arrays, each occurrence in arr0
    should match each occurrence in arr1.
    
    Before fix: Would only count 1 (position 0 where both have value 1)
    After fix: Correctly counts 3 (each of 3 ones in arr0 matches the one 1 in arr1)
    """
    arr0 = [1, 1, 1]
    arr1 = [1, 2, 3]
    
    # Each of the three 1's in arr0 matches the single 1 in arr1 = 3 matches
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == 3, f"Expected 3 matches but got {result}"


def test_count_duplicates_multiple_duplicates():
    """Test with multiple duplicate values across both arrays.
    
    Before fix: Would return 2 (positions 0 and 2 where values match)
    After fix: Returns 4 (all matches counted)
    """
    arr0 = [1, 1, 2]
    arr1 = [1, 2, 2]
    
    # arr0[0]=1 matches arr1[0]=1 (1 match)
    # arr0[1]=1 matches arr1[0]=1 (1 match)
    # arr0[2]=2 matches arr1[1]=2 (1 match)
    # arr0[2]=2 matches arr1[2]=2 (1 match)
    # Total: 4 matches
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == 4, f"Expected 4 matches but got {result}"
