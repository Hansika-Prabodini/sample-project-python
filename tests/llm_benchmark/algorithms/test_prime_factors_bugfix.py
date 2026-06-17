"""Test case for the prime_factors bug fix.

This test specifically validates the fix for the infinite loop bug that occurred
when calling prime_factors with n=0 or n=1.

BUG DESCRIPTION:
----------------
Before the fix, calling Primes.prime_factors(0) would cause an infinite loop because:
1. The function starts with: while n % 2 == 0
2. When n=0: 0 % 2 == 0 evaluates to True
3. Inside the loop: n = n // 2 results in n = 0 // 2 = 0
4. Since n remains 0, the while condition stays True, causing an infinite loop

THE FIX:
--------
Added an early return check at the beginning of prime_factors:
    if n <= 1:
        return []

This prevents the infinite loop for n=0 and correctly handles n=1 (which also has no prime factors).

This test would FAIL (hang forever) before the patch was applied.
After the patch, it passes immediately, returning [] for both edge cases.
"""

import pytest
from llm_benchmark.algorithms.primes import Primes


def test_prime_factors_zero_no_infinite_loop():
    """Test that prime_factors(0) returns [] without hanging.
    
    Before the bug fix, this would cause an infinite loop because:
    - while n % 2 == 0 is True when n=0
    - n = n // 2 keeps n at 0
    - Loop never exits
    
    After the fix, it immediately returns [] due to the n <= 1 check.
    """
    result = Primes.prime_factors(0)
    assert result == [], "prime_factors(0) should return an empty list"


def test_prime_factors_one_edge_case():
    """Test that prime_factors(1) returns [] correctly.
    
    The number 1 has no prime factors by definition.
    Before the fix, this worked correctly (didn't enter the while loop).
    After the fix, it's handled by the explicit n <= 1 check for clarity.
    """
    result = Primes.prime_factors(1)
    assert result == [], "prime_factors(1) should return an empty list"


def test_prime_factors_negative_numbers():
    """Test that prime_factors handles negative numbers correctly.
    
    Prime factorization is typically only defined for positive integers > 1.
    The fix ensures that any n <= 1 (including negatives) returns [].
    """
    assert Primes.prime_factors(-1) == []
    assert Primes.prime_factors(-5) == []
    assert Primes.prime_factors(-100) == []


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (12, [2, 2, 3]),
    ],
)
def test_prime_factors_comprehensive(n: int, expected: list):
    """Comprehensive test including the edge cases fixed by the patch.
    
    This parametrized test covers:
    - Edge cases: 0 and 1 (would fail before the fix)
    - Prime numbers: 2, 3
    - Composite numbers: 4, 6, 12
    """
    assert Primes.prime_factors(n) == expected
