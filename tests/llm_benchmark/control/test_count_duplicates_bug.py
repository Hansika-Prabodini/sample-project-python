"""Unit test that demonstrates the count_duplicates bug.

This test would FAIL with the buggy implementation that uses set intersection:
    return len(set(arr0) & set(arr1))

But PASSES with the correct implementation that counts matching positions:
    count = 0
    for i in range(min(len(arr0), len(arr1))):
        if arr0[i] == arr1[i]:
            count += 1
    return count

The bug: The old implementation counted unique values that appear in both arrays,
instead of counting positions where the arrays have matching values.
"""

import pytest
from llm_benchmark.control.double import DoubleForLoop


def test_count_duplicates_bug_case_1():
    """Test case that clearly shows the bug: arrays with same values in different positions.
    
    Arrays [1,2,3] and [2,3,1] contain the same unique values {1,2,3},
    but NO positions have matching values:
    - Position 0: 1 != 2
    - Position 1: 2 != 3  
    - Position 2: 3 != 1
    
    Buggy implementation (set intersection): returns 3 (counts unique common values)
    Correct implementation (position matching): returns 0 (no matching positions)
    """
    arr0 = [1, 2, 3]
    arr1 = [2, 3, 1]
    
    # Expected: 0 matches (no position has same value in both arrays)
    assert DoubleForLoop.count_duplicates(arr0, arr1) == 0


def test_count_duplicates_bug_case_2():
    """Test case showing duplicate values issue.
    
    Arrays [1,1,2,2] and [1,1,2,2] are identical, so ALL 4 positions match:
    - Position 0: 1 == 1 ✓
    - Position 1: 1 == 1 ✓
    - Position 2: 2 == 2 ✓
    - Position 3: 2 == 2 ✓
    
    Buggy implementation (set intersection): returns 2 (unique values {1,2})
    Correct implementation (position matching): returns 4 (all positions match)
    """
    arr0 = [1, 1, 2, 2]
    arr1 = [1, 1, 2, 2]
    
    # Expected: 4 matches (all positions have same values)
    assert DoubleForLoop.count_duplicates(arr0, arr1) == 4


def test_count_duplicates_bug_case_3():
    """Test case with partial matches.
    
    Arrays [5,3,7,9] and [5,8,7,2] share values at positions 0 and 2:
    - Position 0: 5 == 5 ✓
    - Position 1: 3 != 8
    - Position 2: 7 == 7 ✓
    - Position 3: 9 != 2
    
    Buggy implementation: returns 2 (unique common values {5,7})
    Correct implementation: returns 2 (positions 0 and 2 match)
    
    Note: This case happens to give the same answer by coincidence,
    but for the wrong reason!
    """
    arr0 = [5, 3, 7, 9]
    arr1 = [5, 8, 7, 2]
    
    # Expected: 2 matches (positions 0 and 2)
    assert DoubleForLoop.count_duplicates(arr0, arr1) == 2


def test_count_duplicates_bug_case_4():
    """Test case with repeated values showing clear difference.
    
    Arrays [1,1,1] and [1,1,1] are identical with repeated values:
    - Position 0: 1 == 1 ✓
    - Position 1: 1 == 1 ✓
    - Position 2: 1 == 1 ✓
    
    Buggy implementation (set intersection): returns 1 (unique value {1})
    Correct implementation (position matching): returns 3 (all positions match)
    """
    arr0 = [1, 1, 1]
    arr1 = [1, 1, 1]
    
    # Expected: 3 matches (all positions have value 1)
    assert DoubleForLoop.count_duplicates(arr0, arr1) == 3


def test_count_duplicates_bug_case_5():
    """Test case with different lengths.
    
    Arrays [1,2,3,4,5] and [1,2,3] where first 3 positions match:
    - Position 0: 1 == 1 ✓
    - Position 1: 2 == 2 ✓
    - Position 2: 3 == 3 ✓
    
    Buggy implementation: returns 3 (unique common values {1,2,3})
    Correct implementation: returns 3 (first 3 positions match)
    
    Note: Another coincidental match, but shows the implementation should
    only compare up to min(len(arr0), len(arr1))
    """
    arr0 = [1, 2, 3, 4, 5]
    arr1 = [1, 2, 3]
    
    # Expected: 3 matches (first 3 positions)
    assert DoubleForLoop.count_duplicates(arr0, arr1) == 3
