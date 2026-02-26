"""Control flow module with single and double loop implementations.

This module contains intentionally inefficient loop patterns used for benchmarking.
"""

from llm_benchmark.control.double import (
    count_duplicates,
    count_pairs,
    sum_matrix,
    sum_square,
    sum_triangle,
)
from llm_benchmark.control.single import max_list, sum_modulus, sum_range

__all__ = [
    # From single.py
    "sum_range",
    "max_list",
    "sum_modulus",
    # From double.py
    "sum_square",
    "sum_triangle",
    "count_pairs",
    "count_duplicates",
    "sum_matrix",
]
