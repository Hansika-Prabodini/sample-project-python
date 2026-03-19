"""Test case to demonstrate the DsList class import bug.

This test demonstrates a bug where the test file test_dslist.py tries to import
a DsList class from llm_benchmark.datastructures.dslist, but the module only
contains standalone functions, not a class.

BEFORE THE FIX:
- This test would fail with ImportError: cannot import name 'DsList'

AFTER THE FIX:
- The DsList class exists and can be imported
- The class has static methods that work correctly
"""

import pytest


def test_dslist_class_exists():
    """Test that DsList class can be imported and used.
    
    This test would fail before the bug fix because DsList class doesn't exist.
    After the fix, DsList should be a class with static methods.
    """
    # This import would fail before the fix
    from llm_benchmark.datastructures.dslist import DsList
    
    # Verify it's a class
    assert isinstance(DsList, type), "DsList should be a class"
    
    # Verify the class has the expected static methods
    assert hasattr(DsList, 'modify_list'), "DsList should have modify_list method"
    assert hasattr(DsList, 'search_list'), "DsList should have search_list method"
    assert hasattr(DsList, 'sort_list'), "DsList should have sort_list method"
    assert hasattr(DsList, 'reverse_list'), "DsList should have reverse_list method"
    assert hasattr(DsList, 'rotate_list'), "DsList should have rotate_list method"
    assert hasattr(DsList, 'merge_lists'), "DsList should have merge_lists method"


def test_dslist_modify_list_works():
    """Test that DsList.modify_list works correctly.
    
    This verifies that the DsList class methods actually function correctly
    after the bug fix.
    """
    from llm_benchmark.datastructures.dslist import DsList
    
    # Test basic functionality
    result = DsList.modify_list([1, 2, 3])
    assert result == [2, 3, 4], "modify_list should increment each element by 1"


def test_dslist_search_list_works():
    """Test that DsList.search_list works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    result = DsList.search_list([1, 2, 3, 2, 5], 2)
    assert result == [1, 3], "search_list should return all indices where value appears"


def test_dslist_sort_list_works():
    """Test that DsList.sort_list works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    result = DsList.sort_list([3, 1, 2])
    assert result == [1, 2, 3], "sort_list should return a sorted copy"


def test_dslist_reverse_list_works():
    """Test that DsList.reverse_list works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    result = DsList.reverse_list([1, 2, 3])
    assert result == [3, 2, 1], "reverse_list should return a reversed copy"


def test_dslist_rotate_list_works():
    """Test that DsList.rotate_list works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    result = DsList.rotate_list([1, 2, 3, 4, 5], 2)
    assert result == [3, 4, 5, 1, 2], "rotate_list should rotate by n positions"


def test_dslist_merge_lists_works():
    """Test that DsList.merge_lists works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    result = DsList.merge_lists([1, 2], [3, 4])
    assert result == [1, 2, 3, 4], "merge_lists should concatenate two lists"
