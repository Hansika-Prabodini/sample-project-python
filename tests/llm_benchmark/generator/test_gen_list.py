from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


@pytest.mark.parametrize(
    "n, m, rows, cols",
    [
        (1, 1, 1, 1),
        (2, 3, 2, 3),
        (3, 5, 3, 5),
        (4, 2, 4, 2),
        (5, 10, 5, 10),
    ],
)
def test_random_matrix_dimensions(n: int, m: int, rows: int, cols: int) -> None:
    """Test that random_matrix generates a matrix with correct dimensions.
    
    This test verifies that random_matrix(n, m) returns a matrix with:
    - n rows
    - m columns in each row
    
    This test fails with the current buggy implementation because
    random_matrix ignores the 'm' parameter and creates an n×n matrix
    instead of an n×m matrix.
    """
    matrix = GenList.random_matrix(n, m)
    
    # Check number of rows
    assert len(matrix) == rows, f"Expected {rows} rows, got {len(matrix)}"
    
    # Check number of columns in each row
    for i, row in enumerate(matrix):
        assert len(row) == cols, f"Row {i} has {len(row)} columns, expected {cols}"
