"""Unit tests for the validation utilities module.

Covers validate_list, validate_numeric, and validate_string, including
edge-cases such as NaN/Inf handling in validate_numeric.
"""

import math

import pytest

from llm_benchmark.validation import validate_list, validate_numeric, validate_string


# ---------------------------------------------------------------------------
# validate_list
# ---------------------------------------------------------------------------

class TestValidateList:
    def test_returns_list_unchanged(self):
        v = [1, 2, 3]
        assert validate_list(v) is v

    def test_allows_empty_list_by_default(self):
        assert validate_list([]) == []

    def test_rejects_empty_list_when_not_allowed(self):
        with pytest.raises(ValueError, match="empty"):
            validate_list([], allow_empty=False)

    def test_rejects_non_list_type(self):
        with pytest.raises(TypeError, match="Expected list"):
            validate_list("not a list")

    def test_rejects_none(self):
        with pytest.raises(TypeError, match="Expected list"):
            validate_list(None)


# ---------------------------------------------------------------------------
# validate_numeric
# ---------------------------------------------------------------------------

class TestValidateNumeric:
    def test_accepts_int(self):
        assert validate_numeric(42) == 42

    def test_accepts_float(self):
        assert validate_numeric(3.14) == pytest.approx(3.14)

    def test_accepts_zero(self):
        assert validate_numeric(0) == 0

    def test_accepts_negative(self):
        assert validate_numeric(-5) == -5

    def test_accepts_value_within_range(self):
        assert validate_numeric(50, min_value=0, max_value=100) == 50

    def test_rejects_value_below_min(self):
        with pytest.raises(ValueError, match="minimum"):
            validate_numeric(-10, min_value=0)

    def test_rejects_value_above_max(self):
        with pytest.raises(ValueError, match="maximum"):
            validate_numeric(150, max_value=100)

    def test_rejects_bool(self):
        with pytest.raises(TypeError, match="Expected int or float"):
            validate_numeric(True)

    def test_rejects_string(self):
        with pytest.raises(TypeError, match="Expected int or float"):
            validate_numeric("42")

    def test_rejects_none(self):
        with pytest.raises(TypeError, match="Expected int or float"):
            validate_numeric(None)

    def test_accepts_inf_without_range(self):
        """Positive infinity is a valid float when no range is constrained."""
        assert validate_numeric(math.inf) == math.inf

    def test_rejects_inf_above_max(self):
        """Positive infinity should violate any finite max_value."""
        with pytest.raises(ValueError):
            validate_numeric(math.inf, max_value=100)

    # ------------------------------------------------------------------
    # BUG: NaN bypasses range checks because all comparisons with NaN
    # evaluate to False in Python.  validate_numeric(float('nan'), ...)
    # should raise ValueError regardless of the range arguments.
    # ------------------------------------------------------------------
    def test_rejects_nan_no_range(self):
        """NaN is not a meaningful numeric value and must always be rejected."""
        with pytest.raises(ValueError, match="NaN"):
            validate_numeric(float("nan"))

    def test_rejects_nan_with_min(self):
        """NaN silently passes `value < min_value` (always False) — must be caught."""
        with pytest.raises(ValueError, match="NaN"):
            validate_numeric(float("nan"), min_value=0)

    def test_rejects_nan_with_max(self):
        """NaN silently passes `value > max_value` (always False) — must be caught."""
        with pytest.raises(ValueError, match="NaN"):
            validate_numeric(float("nan"), max_value=100)

    def test_rejects_nan_with_range(self):
        """NaN silently passes both range guards — must be caught."""
        with pytest.raises(ValueError, match="NaN"):
            validate_numeric(float("nan"), min_value=0, max_value=100)


# ---------------------------------------------------------------------------
# validate_string
# ---------------------------------------------------------------------------

class TestValidateString:
    def test_returns_string_unchanged(self):
        assert validate_string("hello") == "hello"

    def test_allows_empty_string_by_default(self):
        assert validate_string("") == ""

    def test_rejects_empty_string_when_not_allowed(self):
        with pytest.raises(ValueError, match="empty"):
            validate_string("", allow_empty=False)

    def test_rejects_non_string_type(self):
        with pytest.raises(TypeError, match="Expected str"):
            validate_string(42)

    def test_rejects_none(self):
        with pytest.raises(TypeError, match="Expected str"):
            validate_string(None)
