"""Regression test for the DsList class bug.

Bug: dslist.py defined standalone module-level functions instead of methods on a
DsList class. All other modules in the benchmark follow the class-based pattern
(e.g. Sort, Primes, DoubleForLoop), and the existing tests in test_dslist.py
already import ``DsList`` — meaning every test there raised an ImportError
before the fix.

This file adds explicit tests for the two methods that had NO coverage at all
(rotate_list and merge_lists), so there is a clear before/after signal:

    BEFORE patch: ``from llm_benchmark.datastructures.dslist import DsList``
                  raises ImportError → all tests below FAIL.
    AFTER  patch: DsList is a proper class → all tests below PASS.
"""

from typing import List

import pytest

from llm_benchmark.datastructures.dslist import DsList


# ---------------------------------------------------------------------------
# rotate_list
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "v, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # full rotation = no-op
        ([1, 2, 3], 1, [2, 3, 1]),
        ([], 3, []),                              # empty list
    ],
)
def test_rotate_list(v: List[int], n: int, expected: List[int]) -> None:
    """DsList.rotate_list rotates a list left by n positions."""
    assert DsList.rotate_list(v, n) == expected


# ---------------------------------------------------------------------------
# merge_lists
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2]),
        ([], [], []),
        ([7], [8], [7, 8]),
    ],
)
def test_merge_lists(v1: List[int], v2: List[int], expected: List[int]) -> None:
    """DsList.merge_lists concatenates two lists into one."""
    assert DsList.merge_lists(v1, v2) == expected


# ---------------------------------------------------------------------------
# Smoke-test that the class itself is importable (catches the original bug
# where only module-level functions existed and there was no DsList symbol)
# ---------------------------------------------------------------------------

def test_dslist_class_exists() -> None:
    """DsList must be a class, not a module-level function collection."""
    assert isinstance(DsList, type), "DsList should be a class"


def test_dslist_has_expected_methods() -> None:
    """DsList must expose all six expected static methods."""
    for method_name in (
        "modify_list",
        "search_list",
        "sort_list",
        "reverse_list",
        "rotate_list",
        "merge_lists",
    ):
        assert hasattr(DsList, method_name), f"DsList is missing method: {method_name}"
