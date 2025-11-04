from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 0),
        (1, 1),
        (5, 3),
        (10, 10),
    ],
)
def test_random_list_shapes_and_bounds(n: int, m: int) -> None:
    lst = GenList.random_list(n, m)
    assert isinstance(lst, list)
    assert len(lst) == n
    for x in lst:
        assert isinstance(x, int)
        assert 0 <= x <= m


def test_random_matrix_shapes_and_bounds() -> None:
    n, m = 4, 7
    mat: List[List[int]] = GenList.random_matrix(n, m)
    assert isinstance(mat, list)
    assert len(mat) == n
    for row in mat:
        assert isinstance(row, list)
        assert len(row) == n  # square matrix per implementation
        for x in row:
            assert isinstance(x, int)
            assert 0 <= x <= m


# Avoid benchmarking random to keep CI stable; if needed, seed before measuring.
