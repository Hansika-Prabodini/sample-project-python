import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_matrix_dimensions():
    """Test that random_matrix creates a matrix with correct dimensions.
    
    This test verifies that random_matrix(n, m) creates a matrix with
    n rows and m columns, not n rows and n columns.
    """
    # Test case 1: 3 rows, 5 columns
    matrix = GenList.random_matrix(3, 5)
    assert len(matrix) == 3, "Matrix should have 3 rows"
    for row in matrix:
        assert len(row) == 5, "Each row should have 5 columns"
    
    # Test case 2: 2 rows, 7 columns
    matrix = GenList.random_matrix(2, 7)
    assert len(matrix) == 2, "Matrix should have 2 rows"
    for row in matrix:
        assert len(row) == 7, "Each row should have 7 columns"
    
    # Test case 3: 4 rows, 2 columns
    matrix = GenList.random_matrix(4, 2)
    assert len(matrix) == 4, "Matrix should have 4 rows"
    for row in matrix:
        assert len(row) == 2, "Each row should have 2 columns"


def test_benchmark_random_matrix(benchmark):
    """Benchmark test for random_matrix."""
    benchmark(GenList.random_matrix, 10, 10)
