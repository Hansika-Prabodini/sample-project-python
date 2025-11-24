#!/usr/bin/env python3
"""Quick verification script for the random_matrix bug fix"""

from src.llm_benchmark.generator.gen_list import GenList

# Test 1: Verify dimensions with n=3, m=5
print("Test 1: random_matrix(3, 5)")
matrix = GenList.random_matrix(3, 5)
print(f"  Number of rows: {len(matrix)} (expected 3)")
print(f"  Number of columns in each row: {[len(row) for row in matrix]} (expected [5, 5, 5])")
assert len(matrix) == 3, f"Expected 3 rows, got {len(matrix)}"
assert all(len(row) == 5 for row in matrix), "Not all rows have 5 columns"
print("  ✓ PASS\n")

# Test 2: Verify with different dimensions n=2, m=4
print("Test 2: random_matrix(2, 4)")
matrix = GenList.random_matrix(2, 4)
print(f"  Number of rows: {len(matrix)} (expected 2)")
print(f"  Number of columns in each row: {[len(row) for row in matrix]} (expected [4, 4])")
assert len(matrix) == 2, f"Expected 2 rows, got {len(matrix)}"
assert all(len(row) == 4 for row in matrix), "Not all rows have 4 columns"
print("  ✓ PASS\n")

# Test 3: Verify with n=1, m=1
print("Test 3: random_matrix(1, 1)")
matrix = GenList.random_matrix(1, 1)
print(f"  Number of rows: {len(matrix)} (expected 1)")
print(f"  Number of columns in row 0: {len(matrix[0])} (expected 1)")
assert len(matrix) == 1, f"Expected 1 row, got {len(matrix)}"
assert len(matrix[0]) == 1, f"Expected 1 column, got {len(matrix[0])}"
print("  ✓ PASS\n")

print("All tests passed! Bug fix verified.")
