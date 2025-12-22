# Strings Module

This module contains functions for benchmarking string manipulation operations.

## Files

### strops.py

String operation implementations using manual iteration for benchmarking purposes.

**Class: `StrOps`**

#### Methods

##### `str_reverse(s: str) -> str`
Reverses a string character by character.

- **Args**: `s` - String to reverse
- **Returns**: Reversed string
- **Complexity**: O(n)

```python
from llm_benchmark.strings.strops import StrOps

StrOps.str_reverse("hello")    # Returns "olleh"
StrOps.str_reverse("Python")   # Returns "nohtyP"
StrOps.str_reverse("a")        # Returns "a"
StrOps.str_reverse("")         # Returns ""
```

**Implementation**: Uses manual string concatenation in a loop (not the most efficient approach, but useful for benchmarking).

##### `palindrome(s: str) -> bool`
Checks if a string is a palindrome (reads the same forwards and backwards).

- **Args**: `s` - String to check
- **Returns**: `True` if palindrome, `False` otherwise
- **Complexity**: O(n)

```python
StrOps.palindrome("racecar")   # True
StrOps.palindrome("hello")     # False
StrOps.palindrome("level")     # True
StrOps.palindrome("Python")    # False
StrOps.palindrome("a")         # True
StrOps.palindrome("")          # True (empty string is palindrome)
```

**Implementation**: Compares characters from both ends moving inward. Checks all positions rather than stopping at the middle (intentionally less efficient for benchmarking).

## Usage Examples

### Basic String Reversal

```python
from llm_benchmark.strings.strops import StrOps

# Reverse various strings
original = "The quick brown fox"
reversed_str = StrOps.str_reverse(original)
print(f"{original} -> {reversed_str}")
# Output: The quick brown fox -> xof nworb kciuq ehT
```

### Palindrome Detection

```python
# Check multiple strings
test_words = ["racecar", "hello", "madam", "python", "noon", "world"]

for word in test_words:
    is_pal = StrOps.palindrome(word)
    print(f"{word:10s}: {'✓ Palindrome' if is_pal else '✗ Not a palindrome'}")

# Output:
# racecar   : ✓ Palindrome
# hello     : ✗ Not a palindrome
# madam     : ✓ Palindrome
# python    : ✗ Not a palindrome
# noon      : ✓ Palindrome
# world     : ✗ Not a palindrome
```

### Combined Operations

```python
# Find palindromes by reversing and comparing
def is_reversible_palindrome(s: str) -> bool:
    """Check if string equals its reverse using StrOps"""
    return s == StrOps.str_reverse(s)

# Compare with built-in palindrome checker
test_str = "racecar"
print(f"Using reverse: {is_reversible_palindrome(test_str)}")
print(f"Using palindrome: {StrOps.palindrome(test_str)}")
```

## Implementation Notes

### Manual String Concatenation

The `str_reverse` function uses string concatenation in a loop:
```python
ret = ""
for i in range(len(s)):
    ret += s[len(s) - 1 - i]
```

This is **less efficient** than:
- Using slicing: `s[::-1]`
- Using `reversed()`: `''.join(reversed(s))`

**Purpose**: This intentional inefficiency serves benchmarking goals:
1. Test LLM understanding of basic string operations
2. Compare manual vs. built-in performance
3. Identify optimization opportunities

### Character-by-Character Comparison

The `palindrome` function checks every character position:
```python
for i in range(len(s)):
    if s[i] != s[len(s) - 1 - i]:
        return False
```

This checks **more positions than necessary** (could stop at `len(s) // 2`).

**Purpose**: Provides additional benchmarking scenarios for optimization detection.

## Benchmarking

This module tests:
- **String traversal**: Forward and backward iteration
- **String building**: Concatenation patterns and efficiency
- **Algorithm optimization**: Early exit vs. full traversal
- **Built-in alternatives**: When to use Python's string methods

Run benchmarks with:
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/strings/
```

## Performance Characteristics

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| `str_reverse` | O(n²) | O(n) | String concatenation in loop creates intermediate strings |
| `palindrome` | O(n) | O(1) | Character comparison with no extra storage |

**Note**: Python strings are immutable, so each `+=` operation creates a new string object, making `str_reverse` quadratic in time.

## Optimization Opportunities

For production code, consider:

```python
# Efficient string reversal
def fast_reverse(s: str) -> str:
    return s[::-1]

# Efficient palindrome check (early exit)
def fast_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Or even simpler
def simplest_palindrome(s: str) -> bool:
    return s == s[::-1]
```

These optimizations are **intentionally not used** in this module to provide diverse benchmarking scenarios.
