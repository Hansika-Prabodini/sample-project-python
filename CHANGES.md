# Changes to `rotate_list()` Function

## Overview
Fixed the `rotate_list()` function in `src/llm_benchmark/datastructures/dslist.py` to handle rotation parameter bounds and edge cases properly.

## Changes Made

### 1. Added Parameter Validation
- **None Check**: Added validation to ensure the `v` parameter is not `None`
  - Raises `ValueError` with message: `"List cannot be None"`
- **Non-negative Rotation**: Added validation to ensure `n >= 0`
  - Raises `ValueError` with message: `"Rotation count must be non-negative"`

### 2. Edge Case Handling
- **Empty List**: Added graceful handling for empty lists
  - `rotate_list([], n)` now returns `[]` for any valid `n >= 0`
- **Oversized Rotation**: Implemented modulo arithmetic for `n > len(v)`
  - `n` is normalized using `n % len(v)` to handle rotations larger than list length
  - Example: `rotate_list([1,2,3], 10)` effectively rotates by `10 % 3 = 1`, returning `[2,3,1]`

### 3. Updated Documentation
- Added `Raises` section to docstring documenting `ValueError` conditions
- Improved clarity on parameter requirements

## Examples

### Valid Usage
```python
# Normal rotation
DsList.rotate_list([1, 2, 3, 4, 5], 2)  # Returns: [3, 4, 5, 1, 2]

# No rotation
DsList.rotate_list([1, 2, 3], 0)  # Returns: [1, 2, 3]

# Empty list
DsList.rotate_list([], 5)  # Returns: []

# Oversized rotation (uses modulo)
DsList.rotate_list([1, 2, 3], 10)  # Returns: [2, 3, 1] (equivalent to rotation by 1)

# Full rotation (returns to original)
DsList.rotate_list([1, 2, 3], 3)  # Returns: [1, 2, 3]
```

### Error Cases
```python
# None list
DsList.rotate_list(None, 1)  # Raises: ValueError("List cannot be None")

# Negative rotation
DsList.rotate_list([1, 2, 3], -1)  # Raises: ValueError("Rotation count must be non-negative")
```

## Benefits
1. **Robustness**: Function now validates inputs and handles edge cases gracefully
2. **User-Friendly**: Modulo arithmetic allows natural handling of large rotation values
3. **Clear Errors**: Descriptive error messages help users quickly identify and fix issues
4. **Backward Compatible**: Existing valid usage continues to work as expected

## Technical Details
- **Modulo Operation**: For non-empty lists, `n` is normalized to `n % len(v)` before rotation
- **Early Returns**: Empty lists return immediately after validation, avoiding unnecessary computation
- **Validation Order**: Checks are performed in logical order (None → negative → empty → modulo)
