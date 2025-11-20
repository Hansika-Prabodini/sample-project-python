# Strings Module

This module contains string manipulation implementations for benchmarking.

## Classes

### StrOps
Provides various string operations:
- `str_reverse(s)`: Reverse a string
- `palindrome(s)`: Check if a string is a palindrome

## Purpose

These implementations demonstrate string manipulation patterns and their performance characteristics for benchmarking purposes.

## Usage

```python
from llm_benchmark.strings import StrOps

# Reverse a string
reversed_str = StrOps.str_reverse("hello")

# Check if a string is a palindrome
is_palindrome = StrOps.palindrome("racecar")
is_palindrome = StrOps.palindrome("hello")
```
