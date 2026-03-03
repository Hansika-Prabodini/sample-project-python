"""Test cases for string operations.

This module contains unit tests and benchmark tests for the StrOps class,
which implements various string manipulation operations including reversal
and palindrome checking.
"""

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
        ("hello world", "dlrow olleh"),
    ],
)
def test_str_reverse(s: str, expected: str) -> None:
    """Test str_reverse function which reverses a string.
    
    Args:
        s: String to reverse
        expected: Expected reversed string
        
    Test cases:
        - Empty string reverses to empty string
        - Single character reverses to itself
        - "ab" reverses to "ba"
        - "abc" reverses to "cba"
        - "hello" reverses to "olleh"
        - "racecar" (palindrome) reverses to itself
        - "hello world" reverses to "dlrow olleh"
    """
    assert StrOps.str_reverse(s) == expected


def test_benchmark_str_reverse(benchmark) -> None:
    """Benchmark the performance of str_reverse.
    
    Measures execution time for reversing the string "hello world".
    """
    benchmark(StrOps.str_reverse, "hello world")


@pytest.mark.parametrize(
    "s, is_palindrome",
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("11211", True),
    ],
)
def test_palindrome(s: str, is_palindrome: bool) -> None:
    """Test palindrome function which checks if a string is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards.
    The function performs a two-pointer comparison from both ends of the string.
    
    Args:
        s: String to check
        is_palindrome: Expected boolean result
        
    Test cases:
        - Empty string is a palindrome
        - Single character is a palindrome
        - "aa" is a palindrome
        - "ab" is not a palindrome
        - "aba" is a palindrome
        - "abc" is not a palindrome
        - "racecar" is a palindrome
        - "hello" is not a palindrome
        - "madam" is a palindrome
        - "11211" is a palindrome
    """
    assert StrOps.palindrome(s) == is_palindrome


def test_benchmark_palindrome(benchmark) -> None:
    """Benchmark the performance of palindrome.
    
    Measures execution time for checking if "racecar" is a palindrome.
    """
    benchmark(StrOps.palindrome, "racecar")
