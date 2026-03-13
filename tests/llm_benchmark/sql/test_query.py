"""Test suite for SQL query operations.

This module contains tests for the SqlQuery class, which performs various
database query operations including album searches, table joins, and
invoice analysis.
"""

import pytest

from llm_benchmark.sql.query import SqlQuery


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Presence", True),
        ("Roundabout", False),
    ],
)
def test_query_album(name: str, expected: bool) -> None:
    """Test album existence query in the database.
    
    Validates that the query_album method correctly identifies whether
    an album with the given name exists in the database.
    
    Args:
        name: The album name to search for.
        expected: Whether the album should exist (True) or not (False).
    
    Test cases:
        - "Presence": Album that exists in the database
        - "Roundabout": Album that does not exist in the database
    """
    assert SqlQuery.query_album(name) == expected


def test_benchmark_query_album(benchmark) -> None:
    """Benchmark the album query operation.
    
    Measures the performance of querying for an album by name.
    Uses "Presence" as the test album.
    """
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums() -> None:
    """Test joining albums with tracks and artists.
    
    Validates that the join_albums method correctly performs a multi-table
    join operation and returns the expected data structure with album name,
    track name, and artist name.
    
    Verifies that the first result is:
        - Album: "For Those About To Rock (We Salute You)"
        - Track: "For Those About To Rock We Salute You"
        - Artist: "AC/DC"
    """
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    """Benchmark the album join operation.
    
    Measures the performance of joining albums, tracks, and artists tables.
    """
    benchmark(SqlQuery.join_albums)


def test_top_invoices() -> None:
    """Test retrieval of top invoices by total amount.
    
    Validates that the top_invoices method returns the correct set of
    invoices ordered by total amount in descending order.
    
    Verifies:
        - First invoice total is 25.86
        - Third invoice total is 21.86
        - Exactly 10 invoices are returned
    """
    top = SqlQuery.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    """Benchmark the top invoices query.
    
    Measures the performance of retrieving and sorting top invoices.
    """
    benchmark(SqlQuery.top_invoices)
