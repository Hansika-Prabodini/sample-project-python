"""Test cases for string operations."""

import pytest

from llm_benchmark.strings.strops import StrOps


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("abc", "cba"),
        ("hello", "olleh"),
        ("racecar", "racecar"),
    ],
)
def test_str_reverse(s: str, expected: str) -> None:
    """Test str_reverse function."""
    assert StrOps.str_reverse(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", False),  # case-sensitive, with spaces
    ],
)
def test_palindrome(s: str, expected: bool) -> None:
    """Test palindrome function."""
    assert StrOps.palindrome(s) == expected
