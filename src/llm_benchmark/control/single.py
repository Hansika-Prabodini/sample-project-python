"""Single loop control flow operations.

This module provides optimized implementations of single-loop algorithms
with comprehensive input validation and type safety.
"""

from typing import List


def sum_range(n: int) -> int:
    """Sum of range of numbers from 0 to n-1.
    
    Uses the mathematical formula n*(n-1)//2 for O(1) performance
    instead of O(n) array creation.

    Args:
        n: Upper bound for the range (exclusive), must be non-negative

    Returns:
        Sum of integers from 0 to n-1

    Raises:
        TypeError: If n is None or not an integer
        ValueError: If n is negative
        
    Examples:
        >>> sum_range(0)
        0
        >>> sum_range(5)
        10
    """
    if n is None:
        raise TypeError("Parameter 'n' cannot be None")
    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Parameter 'n' must be non-negative, got {n}")
    
    return n * (n - 1) // 2


def max_list(v: List[int]) -> int:
    """Find maximum value in a list.
    
    Efficient O(n) single-pass implementation.

    Args:
        v: List of integers, must not be None or empty

    Returns:
        Maximum value in the list

    Raises:
        TypeError: If v is None or not a list
        ValueError: If v is empty
        
    Examples:
        >>> max_list([1, 2, 3])
        3
        >>> max_list([-5, -1, -10])
        -1
    """
    if v is None:
        raise TypeError("Parameter 'v' cannot be None")
    if not isinstance(v, list):
        raise TypeError(f"Parameter 'v' must be a list, got {type(v).__name__}")
    if len(v) == 0:
        raise ValueError("Parameter 'v' cannot be empty")
    
    max_val = v[0]
    for i in range(1, len(v)):
        if v[i] > max_val:
            max_val = v[i]
    return max_val


def sum_modulus(n: int, m: int) -> int:
    """Sum all numbers divisible by m in range [0, n).
    
    Optimized to accumulate sum directly without array creation.

    Args:
        n: Upper bound for the range (exclusive), must be non-negative
        m: Modulus divisor, must be non-zero

    Returns:
        Sum of all integers i where 0 <= i < n and i % m == 0

    Raises:
        TypeError: If n or m is None or not an integer
        ValueError: If n is negative or m is zero
        
    Examples:
        >>> sum_modulus(10, 2)
        20
        >>> sum_modulus(10, 3)
        18
    """
    if n is None:
        raise TypeError("Parameter 'n' cannot be None")
    if m is None:
        raise TypeError("Parameter 'm' cannot be None")
    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}")
    if not isinstance(m, int):
        raise TypeError(f"Parameter 'm' must be an integer, got {type(m).__name__}")
    if n < 0:
        raise ValueError(f"Parameter 'n' must be non-negative, got {n}")
    if m == 0:
        raise ValueError("Parameter 'm' cannot be zero")
    
    total = 0
    for i in range(n):
        if i % m == 0:
            total += i
    return total
