# Bug Fix Summary

## Bug Found

**Location:** `src/llm_benchmark/control/single.py` - `SingleForLoop.max_list()` method

**Type:** Missing edge case handling

**Description:**
The `max_list()` function fails when called with an empty list. It attempts to access `v[0]` without first checking if the list is non-empty, resulting in an `IndexError`.

### Before (Buggy Code):
```python
@staticmethod
def max_list(v: List[int]) -> int:
    """Maximum value in a vector"""
    max_val = v[0]  # IndexError if v is empty!
    for i in range(1, len(v)):
        if v[i] > max_val:
            max_val = v[i]
    return max_val
```

### Issue:
```python
>>> SingleForLoop.max_list([])
IndexError: list index out of range
```

This is inconsistent with Python's built-in `max()` function, which raises a `ValueError` with a descriptive message: `"max() arg is an empty sequence"`.

## Fix Applied

Added a check for empty lists and raise a proper `ValueError` with a descriptive error message, matching Python's standard library behavior.

### After (Fixed Code):
```python
@staticmethod
def max_list(v: List[int]) -> int:
    """Maximum value in a vector
    
    Raises:
        ValueError: If the list is empty
    """
    if not v:
        raise ValueError("max_list() arg is an empty sequence")
    
    max_val = v[0]
    for i in range(1, len(v)):
        if v[i] > max_val:
            max_val = v[i]
    return max_val
```

## Unit Test Added

**Location:** `tests/llm_benchmark/control/test_single.py`

```python
def test_max_list_empty() -> None:
    """Test max_list function with an empty list.
    
    The function should handle empty lists gracefully by raising a
    meaningful ValueError instead of an IndexError.
    """
    with pytest.raises(ValueError, match="empty"):
        SingleForLoop.max_list([])
```

### Test Behavior:
- **Before the fix:** The test would fail because the function raises `IndexError` instead of `ValueError`
- **After the fix:** The test passes because the function correctly raises `ValueError` with the expected message

## Benefits of the Fix

1. **Better error messages:** Users get a clear, descriptive error message instead of a generic index error
2. **Consistency:** Matches the behavior of Python's built-in `max()` function
3. **Defensive programming:** Validates input before processing
4. **Improved debugging:** Developers can quickly identify the issue when debugging
