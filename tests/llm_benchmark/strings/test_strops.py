"""Test cases for string operations.

This module contains unit tests and benchmark tests for the StrOps class,
which implements string manipulation utilities including reversal and
palindrome detection.
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
        ("racecar", "racecar"),
        ("hello", "olleh"),
        ("12345", "54321"),
    ],
)
def test_str_reverse(s: str, expected: str) -> None:
    """Test str_reverse function which reverses a string character by character.

    The function iterates from the end of the string to the beginning,
    building the reversed result one character at a time.

    Args:
        s: Input string to reverse
        expected: Expected reversed string

    Test cases:
        - "": Empty string returns ""
        - "a": Single character returns itself
        - "ab": Two characters swapped
        - "abc": Three characters fully reversed
        - "racecar": Palindrome — reversed equals original
        - "hello": Normal word reversed
        - "12345": Numeric string reversed
    """
    assert StrOps.str_reverse(s) == expected


def test_benchmark_str_reverse(benchmark) -> None:
    """Benchmark the performance of str_reverse.

    Measures execution time for reversing a moderately long string.
    """
    benchmark(StrOps.str_reverse, "benchmarkstring")


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("racecar", True),
        ("level", True),
        ("hello", False),
        ("abcba", True),
        ("abcd", False),
        ("A", True),
        ("Aba", False),   # case-sensitive: 'A' != 'a'
    ],
)
def test_palindrome(s: str, expected: bool) -> None:
    """Test palindrome function which checks if a string reads the same forwards and backwards.

    Compares characters at symmetric positions from both ends. The check is
    case-sensitive (e.g. "Aba" is NOT a palindrome because 'A' != 'a').

    Args:
        s: Input string to check
        expected: True if the string is a palindrome, False otherwise

    Test cases:
        - "": Empty string is trivially a palindrome
        - "a": Single character is always a palindrome
        - "aa": Two identical characters
        - "ab": Two different characters — not a palindrome
        - "racecar": Classic odd-length palindrome
        - "level": Another odd-length palindrome
        - "hello": Non-palindrome word
        - "abcba": Symmetric around centre 'c'
        - "abcd": No symmetry
        - "A": Single uppercase letter
        - "Aba": Case mismatch — 'A' != 'a', not a palindrome
    """
    assert StrOps.palindrome(s) == expected


def test_benchmark_palindrome(benchmark) -> None:
    """Benchmark the performance of palindrome.

    Measures execution time for checking a known palindrome.
    """
    benchmark(StrOps.palindrome, "racecar")
