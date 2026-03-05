#!/usr/bin/env python3
"""Demonstration of the count_duplicates bug and fix.

This script demonstrates the bug that was found and fixed in the
count_duplicates function in src/llm_benchmark/control/double.py.

Run this script to see:
1. How the buggy implementation (set intersection) behaves
2. How the correct implementation (position matching) behaves
3. Test cases that clearly show the difference
"""

from typing import List


def count_duplicates_buggy(arr0: List[int], arr1: List[int]) -> int:
    """BUGGY implementation using set intersection.
    
    This counts unique values that appear in both arrays,
    NOT positions where values match.
    """
    return len(set(arr0) & set(arr1))


def count_duplicates_fixed(arr0: List[int], arr1: List[int]) -> int:
    """FIXED implementation using position matching.
    
    This counts positions where arr0[i] == arr1[i].
    """
    count = 0
    for i in range(min(len(arr0), len(arr1))):
        if arr0[i] == arr1[i]:
            count += 1
    return count


def demonstrate_case(case_name: str, arr0: List[int], arr1: List[int], expected: int):
    """Demonstrate a specific test case."""
    buggy_result = count_duplicates_buggy(arr0, arr1)
    fixed_result = count_duplicates_fixed(arr0, arr1)
    
    print(f"\n{case_name}")
    print(f"  Array 0: {arr0}")
    print(f"  Array 1: {arr1}")
    print(f"  Expected result: {expected}")
    print(f"  Buggy implementation: {buggy_result} {'❌ WRONG' if buggy_result != expected else '✓'}")
    print(f"  Fixed implementation: {fixed_result} {'✓ CORRECT' if fixed_result == expected else '❌ WRONG'}")
    
    # Show position-by-position comparison
    print("  Position-by-position comparison:")
    for i in range(min(len(arr0), len(arr1))):
        match = "✓" if arr0[i] == arr1[i] else "✗"
        print(f"    [{i}]: {arr0[i]} vs {arr1[i]} {match}")


def main():
    """Run all demonstration cases."""
    print("=" * 70)
    print("COUNT_DUPLICATES BUG DEMONSTRATION")
    print("=" * 70)
    print("\nThis demonstrates a bug where the function counted unique common")
    print("values instead of counting matching positions.")
    
    # Case 1: Same values, different positions
    demonstrate_case(
        "Case 1: Same values in different positions",
        arr0=[1, 2, 3],
        arr1=[2, 3, 1],
        expected=0
    )
    
    # Case 2: Identical arrays with duplicates
    demonstrate_case(
        "Case 2: Identical arrays with duplicate values",
        arr0=[1, 1, 2, 2],
        arr1=[1, 1, 2, 2],
        expected=4
    )
    
    # Case 3: Repeated single value
    demonstrate_case(
        "Case 3: Repeated single value",
        arr0=[1, 1, 1],
        arr1=[1, 1, 1],
        expected=3
    )
    
    # Case 4: Partial matches
    demonstrate_case(
        "Case 4: Partial matches",
        arr0=[5, 3, 7, 9],
        arr1=[5, 8, 7, 2],
        expected=2
    )
    
    # Case 5: No matches at all
    demonstrate_case(
        "Case 5: No matching positions",
        arr0=[1, 2, 3, 4],
        arr1=[5, 6, 7, 8],
        expected=0
    )
    
    # Case 6: Different lengths
    demonstrate_case(
        "Case 6: Different length arrays",
        arr0=[1, 2, 3, 4, 5],
        arr1=[1, 2, 3],
        expected=3
    )
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nThe bug was in using: return len(set(arr0) & set(arr1))")
    print("The fix is to use a loop that counts matching positions:")
    print("""
    count = 0
    for i in range(min(len(arr0), len(arr1))):
        if arr0[i] == arr1[i]:
            count += 1
    return count
    """)
    print("\nSee BUG_FIX_SUMMARY.md for complete documentation.")
    print("See tests/llm_benchmark/control/test_count_duplicates_bug.py for unit tests.")
    print("=" * 70)


if __name__ == "__main__":
    main()
