"""Input validation utilities module.

This module provides reusable validation functions for common input types
across the codebase. All functions raise appropriate exceptions (ValueError
or TypeError) with descriptive, actionable error messages.

Usage:
    >>> from llm_benchmark.validation import validate_list, validate_numeric, validate_string
    >>> validate_list([1, 2, 3], allow_empty=False)
    >>> validate_numeric(42, min_value=0, max_value=100)
    >>> validate_string("hello", allow_empty=False)
"""

import math
from typing import Any, List, Optional, Union


def validate_list(
    value: Any, allow_empty: bool = True
) -> List[Any]:
    """Validate that a value is a list and check if empty lists are acceptable.

    This function validates that the input is a list type and optionally
    ensures the list is not empty. Raises appropriate exceptions with
    descriptive error messages for invalid inputs.

    Args:
        value: The value to validate.
        allow_empty: If False, raises ValueError when the list is empty.
                    Defaults to True (empty lists are allowed).

    Returns:
        List[Any]: The validated list (returned for chaining validation calls).

    Raises:
        TypeError: If value is not a list.
        ValueError: If allow_empty is False and the list is empty.

    Examples:
        >>> validate_list([1, 2, 3])
        [1, 2, 3]

        >>> validate_list([], allow_empty=True)
        []

        >>> validate_list([], allow_empty=False)
        Traceback (most recent call last):
            ...
        ValueError: List cannot be empty when allow_empty is False

        >>> validate_list("not a list")
        Traceback (most recent call last):
            ...
        TypeError: Expected list, got str

        >>> validate_list(None)
        Traceback (most recent call last):
            ...
        TypeError: Expected list, got NoneType
    """
    if not isinstance(value, list):
        actual_type = type(value).__name__
        raise TypeError(
            f"Expected list, got {actual_type}. "
            f"Please provide a list type value."
        )

    if not allow_empty and len(value) == 0:
        raise ValueError(
            "List cannot be empty when allow_empty is False. "
            "Please provide a non-empty list."
        )

    return value


def validate_numeric(
    value: Any,
    min_value: Optional[Union[int, float]] = None,
    max_value: Optional[Union[int, float]] = None,
) -> Union[int, float]:
    """Validate that a value is numeric and within an optional range.

    This function validates that the input is an int or float, and optionally
    checks that it falls within a specified range (min_value to max_value).
    Handles edge cases like negative numbers, zero, and None values.

    Args:
        value: The value to validate.
        min_value: Minimum allowed value (inclusive). If None, no lower bound
                   is enforced. Defaults to None.
        max_value: Maximum allowed value (inclusive). If None, no upper bound
                   is enforced. Defaults to None.

    Returns:
        Union[int, float]: The validated numeric value.

    Raises:
        TypeError: If value is not an int or float.
        ValueError: If value is outside the specified range.

    Examples:
        >>> validate_numeric(42)
        42

        >>> validate_numeric(3.14)
        3.14

        >>> validate_numeric(0)
        0

        >>> validate_numeric(-5)
        -5

        >>> validate_numeric(50, min_value=0, max_value=100)
        50

        >>> validate_numeric(-10, min_value=0, max_value=100)
        Traceback (most recent call last):
            ...
        ValueError: Value -10 is below the minimum allowed value of 0

        >>> validate_numeric(150, min_value=0, max_value=100)
        Traceback (most recent call last):
            ...
        ValueError: Value 150 exceeds the maximum allowed value of 100

        >>> validate_numeric("not a number")
        Traceback (most recent call last):
            ...
        TypeError: Expected int or float, got str

        >>> validate_numeric(None)
        Traceback (most recent call last):
            ...
        TypeError: Expected int or float, got NoneType
    """
    # Check type (bool is technically a subclass of int, so we exclude it)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        actual_type = type(value).__name__
        raise TypeError(
            f"Expected int or float, got {actual_type}. "
            f"Please provide a numeric value."
        )

    # Reject NaN: all comparisons with NaN return False in Python, so NaN
    # would silently bypass every range check below and be returned as if it
    # were a valid number.  NaN is never a meaningful numeric value.
    if isinstance(value, float) and math.isnan(value):
        raise ValueError(
            "Value is NaN, which is not a valid numeric value. "
            "Please provide a real numeric value."
        )

    # Check range constraints
    if min_value is not None and value < min_value:
        raise ValueError(
            f"Value {value} is below the minimum allowed value of {min_value}. "
            f"Please provide a value >= {min_value}."
        )

    if max_value is not None and value > max_value:
        raise ValueError(
            f"Value {value} exceeds the maximum allowed value of {max_value}. "
            f"Please provide a value <= {max_value}."
        )

    return value


def validate_string(
    value: Any, allow_empty: bool = True
) -> str:
    """Validate that a value is a string and check if empty strings are acceptable.

    This function validates that the input is a string type and optionally
    ensures the string is not empty. Handles None values and provides
    descriptive error messages.

    Args:
        value: The value to validate.
        allow_empty: If False, raises ValueError when the string is empty.
                    Defaults to True (empty strings are allowed).

    Returns:
        str: The validated string (returned for chaining validation calls).

    Raises:
        TypeError: If value is not a string.
        ValueError: If allow_empty is False and the string is empty.

    Examples:
        >>> validate_string("hello")
        'hello'

        >>> validate_string("", allow_empty=True)
        ''

        >>> validate_string("", allow_empty=False)
        Traceback (most recent call last):
            ...
        ValueError: String cannot be empty when allow_empty is False

        >>> validate_string(42)
        Traceback (most recent call last):
            ...
        TypeError: Expected str, got int

        >>> validate_string(None)
        Traceback (most recent call last):
            ...
        TypeError: Expected str, got NoneType
    """
    if not isinstance(value, str):
        actual_type = type(value).__name__
        raise TypeError(
            f"Expected str, got {actual_type}. "
            f"Please provide a string type value."
        )

    if not allow_empty and len(value) == 0:
        raise ValueError(
            "String cannot be empty when allow_empty is False. "
            "Please provide a non-empty string."
        )

    return value
