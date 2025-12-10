from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_matrix_dimensions() -> None:
    """Test that random_matrix generates correct dimensions (n rows x m columns)
    
    This test demonstrates the bug where random_matrix generates n x n matrices
    instead of n x m matrices.
    """
    n = 3
    m = 5
    matrix = GenList.random_matrix(n, m)
    
    # Check number of rows
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    
    # Check number of columns in each row
    for i, row in enumerate(matrix):
        assert len(row) == m, f"Row {i} has {len(row)} columns, expected {m}"


def test_random_matrix_different_dimensions() -> None:
    """Test random_matrix with different n and m values"""
    n = 2
    m = 4
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n
    for row in matrix:
        assert len(row) == m


def test_random_matrix_single_element() -> None:
    """Test random_matrix with n=1, m=1"""
    matrix = GenList.random_matrix(1, 1)
    
    assert len(matrix) == 1
    assert len(matrix[0]) == 1
