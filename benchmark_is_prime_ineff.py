#!/usr/bin/env python3
"""Micro-benchmark for is_prime_ineff optimization.

This script compares the performance and correctness of the optimized
is_prime_ineff function against a reference implementation (the old inefficient
version) to demonstrate the improvement in runtime performance.

The old implementation had O(n * 11000) complexity due to:
- Nested loops doing n * 10000 pointless multiplications
- 1000 extra iterations per divisibility check
- Checking all divisors from 2 to n

The new implementation has O(sqrt(n)) complexity by:
- Removing all unnecessary loops
- Only checking divisors up to sqrt(n)
- Skipping even numbers after 2
"""

import time
from typing import Callable, List, Tuple


def is_prime_old_ineff(n: int) -> bool:
    """Original inefficient implementation for comparison.
    
    This is the OLD version with intentional performance issues.
    Time complexity: O(n * 11000)
    """
    if n < 2:
        return False

    # Bottleneck 1: Nested loops doing pointless work
    for j in range(1, n):
        for k in range(1, 10000):
            _ = k * j

    # Bottleneck 2: Check divisibility with extra iterations
    for i in range(2, n):
        for _ in range(1000):
            pass
        if n % i == 0:
            return False

    return True


def is_prime_optimized(n: int) -> bool:
    """Optimized implementation.
    
    This is the NEW version with performance improvements.
    Time complexity: O(sqrt(n))
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


def benchmark_function(func: Callable[[int], bool], n: int, iterations: int = 1) -> Tuple[float, bool]:
    """Benchmark a primality testing function.
    
    Args:
        func: Function to benchmark
        n: Number to test for primality
        iterations: Number of times to run the function
        
    Returns:
        Tuple of (average_time_seconds, result)
    """
    start = time.perf_counter()
    result = None
    for _ in range(iterations):
        result = func(n)
    end = time.perf_counter()
    
    avg_time = (end - start) / iterations
    return avg_time, result


def verify_correctness(test_cases: List[Tuple[int, bool]]) -> None:
    """Verify that both implementations produce correct results.
    
    Args:
        test_cases: List of (n, expected_is_prime) tuples
    """
    print("Verifying correctness...")
    print("-" * 60)
    
    all_correct = True
    for n, expected in test_cases:
        result_opt = is_prime_optimized(n)
        
        if result_opt != expected:
            print(f"❌ FAILED for n={n}: expected {expected}, got {result_opt}")
            all_correct = False
        else:
            print(f"✓ n={n}: {result_opt} (correct)")
    
    print()
    if all_correct:
        print("✅ All correctness tests passed!")
    else:
        print("❌ Some tests failed!")
    print()


def run_performance_comparison(test_values: List[int]) -> None:
    """Run performance comparison between old and new implementations.
    
    Args:
        test_values: List of values to test
    """
    print("Performance Comparison")
    print("=" * 60)
    print()
    
    for n in test_values:
        print(f"Testing n={n}:")
        print("-" * 60)
        
        # Benchmark optimized version (more iterations since it's fast)
        time_opt, result_opt = benchmark_function(is_prime_optimized, n, iterations=1000)
        print(f"Optimized version:  {time_opt*1000:.6f} ms (avg over 1000 runs)")
        print(f"Result: {result_opt}")
        
        # Only benchmark old version for small values (it's too slow for large ones)
        if n <= 100:
            time_old, result_old = benchmark_function(is_prime_old_ineff, n, iterations=1)
            print(f"Old version:        {time_old*1000:.2f} ms (1 run)")
            print(f"Result: {result_old}")
            
            speedup = time_old / time_opt
            print(f"\n🚀 Speedup: {speedup:.1f}x faster!")
            
            # Verify both give same result
            if result_old != result_opt:
                print("⚠️  WARNING: Results differ!")
        else:
            print(f"Old version:        SKIPPED (too slow for n={n})")
            print(f"\n💡 The old implementation would take approximately:")
            # Estimate based on O(n * 11000) complexity
            estimated_time = n * 11000 / 1_000_000  # rough estimate in seconds
            if estimated_time < 60:
                print(f"   ~{estimated_time:.1f} seconds")
            elif estimated_time < 3600:
                print(f"   ~{estimated_time/60:.1f} minutes")
            else:
                print(f"   ~{estimated_time/3600:.1f} hours")
        
        print()


def main():
    """Main benchmark execution."""
    print("=" * 60)
    print("Micro-Benchmark: is_prime_ineff Optimization")
    print("=" * 60)
    print()
    
    # Test correctness first
    test_cases = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (10, False),
        (17, True),
        (26, False),
        (97, True),
        (100, False),
        (1699, True),
        (1700, False),
    ]
    
    verify_correctness(test_cases)
    
    # Performance comparison
    print("\n")
    
    # Test with increasing sizes
    test_values = [17, 97, 1700, 10007, 100003]
    run_performance_comparison(test_values)
    
    # Memory improvement note
    print("=" * 60)
    print("Memory Improvement:")
    print("-" * 60)
    print("Old version: O(1) space but with massive constant overhead")
    print("New version: O(1) space with minimal overhead")
    print()
    print("The optimized version also has better cache efficiency due to:")
    print("- Fewer loop iterations")
    print("- No unnecessary variable assignments")
    print("- Better branch prediction")
    print("=" * 60)


if __name__ == "__main__":
    main()
