"""Algorithms module providing prime number and sorting functions."""

from llm_benchmark.algorithms.primes import (
    is_prime,
    is_prime_ineff,
    sum_primes,
    prime_factors,
)
from llm_benchmark.algorithms.sort import (
    sort_list,
    dutch_flag_partition,
    max_n,
)

__all__ = [
    # Prime number functions
    "is_prime",
    "is_prime_ineff",
    "sum_primes",
    "prime_factors",
    # Sorting functions
    "sort_list",
    "dutch_flag_partition",
    "max_n",
]
