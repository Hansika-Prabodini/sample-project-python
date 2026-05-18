"""Test cases demonstrating the DsList class bug fix.

This test file would FAIL before the fix because the DsList class did not exist.
The bug was that test_dslist.py imported DsList as a class with static methods,
but the dslist.py module only contained standalone functions without a class wrapper.

After the fix, the DsList class is properly defined with static methods that
wrap the standalone functions, allowing all tests to pass.
"""

import pytest
from llm_benchmark.datastructures.dslist import DsList


def test_dsList_class_exists():
    """Test that the DsList class exists and is importable.
    
    This test would fail with:
    ImportError: cannot import name 'DsList' from 'llm_benchmark.datastructures.dslist'
    
    Before the fix when DsList class did not exist.
    """
    assert DsList is not None
    assert hasattr(DsList, 'modify_list')
    assert hasattr(DsList, 'search_list')
    assert hasattr(DsList, 'sort_list')
    assert hasattr(DsList, 'reverse_list')
    assert hasattr(DsList, 'rotate_list')
    assert hasattr(DsList, 'merge_lists')


def test_dsList_modify_list_is_callable():
    """Test that DsList.modify_list is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.modify_list([1, 2, 3])
    assert result == [2, 3, 4]
    assert isinstance(result, list)


def test_dsList_search_list_is_callable():
    """Test that DsList.search_list is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.search_list([1, 2, 3, 2, 4], 2)
    assert result == [1, 3]


def test_dsList_sort_list_is_callable():
    """Test that DsList.sort_list is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.sort_list([3, 1, 4, 1, 5])
    assert result == [1, 1, 3, 4, 5]


def test_dsList_reverse_list_is_callable():
    """Test that DsList.reverse_list is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.reverse_list([1, 2, 3])
    assert result == [3, 2, 1]


def test_dsList_rotate_list_is_callable():
    """Test that DsList.rotate_list is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.rotate_list([1, 2, 3, 4, 5], 2)
    assert result == [3, 4, 5, 1, 2]


def test_dsList_merge_lists_is_callable():
    """Test that DsList.merge_lists is callable as a static method.
    
    Before the fix, DsList did not exist, so this would raise AttributeError.
    """
    result = DsList.merge_lists([1, 2], [3, 4])
    assert result == [1, 2, 3, 4]
