from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 10),
        (1, 10),
        (5, 10),
        (10, 5),
        (100, 50),
    ],
)
def test_random_list(n: int, m: int) -> None:
    result = GenList.random_list(n, m)
    
    # Check that the length is correct
    assert len(result) == n
    
    # Check that all values are within the expected range [0, m]
    for value in result:
        assert 0 <= value <= m
        assert isinstance(value, int)


def test_benchmark_random_list(benchmark) -> None:
    benchmark(GenList.random_list, 100, 50)


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 10),
        (1, 10),
        (5, 10),
        (10, 5),
        (20, 30),
    ],
)
def test_random_matrix(n: int, m: int) -> None:
    result = GenList.random_matrix(n, m)
    
    # Check that the matrix has the correct number of rows
    assert len(result) == n
    
    # Check each row
    for row in result:
        # Check that each row has the correct length
        assert len(row) == n
        
        # Check that all values are within the expected range [0, m]
        for value in row:
            assert 0 <= value <= m
            assert isinstance(value, int)


def test_benchmark_random_matrix(benchmark) -> None:
    benchmark(GenList.random_matrix, 10, 50)
