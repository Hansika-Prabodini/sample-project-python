# Changes

## Bug Fixes

### `max_list()` Function - Edge Case Handling

**File**: `src/llm_benchmark/control/single.py`

**Issue**: The `max_list()` function would crash with `IndexError` when given an empty list, and `AttributeError` when given `None`, due to directly accessing `v[0]` without validation.

**Changes Made**:
- Added input validation at function entry to check for `None` parameter
- Added validation to check for empty list before accessing elements
- Function now raises `ValueError` with descriptive error messages instead of crashing:
  - `ValueError("List cannot be None")` when `v` is `None`
  - `ValueError("List cannot be empty")` when `v` is an empty list `[]`

**Impact**:
- Function now fails fast with clear, user-friendly error messages
- Existing functionality for valid inputs (non-empty lists) remains unchanged
- Improves code robustness and debugging experience

**Code Changes**:
```python
# Added validation at lines 30-33
if v is None:
    raise ValueError("List cannot be None")
if len(v) == 0:
    raise ValueError("List cannot be empty")
```

**Behavior**:
- Before: `max_list([])` → `IndexError: list index out of range`
- After: `max_list([])` → `ValueError: List cannot be empty`
- Before: `max_list(None)` → `TypeError: 'NoneType' object is not subscriptable`
- After: `max_list(None)` → `ValueError: List cannot be None`
