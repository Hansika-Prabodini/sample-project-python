"""Test case to demonstrate the DsList class bug.

This test file demonstrates a bug where the implementation file dslist.py
only contains standalone functions, but the existing test file test_dslist.py
expects a DsList class with static methods.

This test will:
- FAIL before the patch (DsList class doesn't exist)
- PASS after the patch (DsList class is properly implemented)
"""

import pytest


def test_dslist_class_exists():
    """Test that DsList class can be imported.
    
    The existing test file test_dslist.py imports and uses DsList class,
    but the implementation only has standalone functions. This test
    verifies that the DsList class exists and can be imported.
    """
    from llm_benchmark.datastructures.dslist import DsList
    
    # Verify the class exists
    assert DsList is not None
    assert hasattr(DsList, '__name__')
    assert DsList.__name__ == 'DsList'


def test_dslist_class_has_static_methods():
    """Test that DsList class has the expected static methods.
    
    The existing tests call methods like DsList.modify_list(),
    DsList.search_list(), etc. This test verifies all expected
    static methods exist.
    """
    from llm_benchmark.datastructures.dslist import DsList
    
    # Check that all expected methods exist
    expected_methods = [
        'modify_list',
        'search_list',
        'sort_list',
        'reverse_list',
        'rotate_list',
        'merge_lists'
    ]
    
    for method_name in expected_methods:
        assert hasattr(DsList, method_name), f"DsList should have method {method_name}"
        # Verify it's a static method or class method (callable on the class)
        method = getattr(DsList, method_name)
        assert callable(method), f"{method_name} should be callable"


def test_dslist_modify_list_works():
    """Test that DsList.modify_list() works correctly.
    
    This test demonstrates that the DsList class methods work as expected,
    matching the behavior of the existing test cases.
    """
    from llm_benchmark.datastructures.dslist import DsList
    
    # Test case from existing tests
    result = DsList.modify_list([1, 2, 3])
    assert result == [2, 3, 4]
    
    result = DsList.modify_list([0])
    assert result == [1]


def test_dslist_search_list_works():
    """Test that DsList.search_list() works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    # Test case from existing tests
    result = DsList.search_list([1, 2, 3, 4, 5], 1)
    assert result == [0]
    
    result = DsList.search_list([1, 2, 3, 4, 5], 9)
    assert result == []


def test_dslist_sort_list_works():
    """Test that DsList.sort_list() works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    # Test case from existing tests
    result = DsList.sort_list([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_dslist_reverse_list_works():
    """Test that DsList.reverse_list() works correctly."""
    from llm_benchmark.datastructures.dslist import DsList
    
    # Test case from existing tests
    result = DsList.reverse_list([1, 2, 3, 4, 5])
    assert result == [5, 4, 3, 2, 1]
