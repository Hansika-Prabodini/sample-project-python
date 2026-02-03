# Author

This project was developed as part of an LLM benchmark testing suite.

## Bug Fix Contribution

### Fixed: Infinite Loop in `prime_factors` Function

**Bug Description:**
The `prime_factors` function in `src/llm_benchmark/algorithms/primes.py` had an infinite loop bug when called with `n=0`.

**Root Cause:**
When `n=0`, the condition `while n % 2 == 0:` evaluates to `True` (since `0 % 2 == 0`), and the statement `n = n // 2` keeps `n` at `0` (since `0 // 2 == 0`), causing the loop to run indefinitely.

**Solution:**
Added an early return check at the beginning of the function:
```python
if n <= 1:
    return []
```

This fix:
- Prevents the infinite loop for `n=0`
- Correctly handles `n=1` (which has no prime factors by definition)
- Handles negative numbers appropriately

**Testing:**
Created comprehensive unit tests in `tests/llm_benchmark/algorithms/test_prime_factors_bugfix.py` that would fail (hang) before the patch and pass after the patch.
