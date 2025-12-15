"""Test cases for SQL query operations.

This module contains unit tests and benchmark tests for the SqlQuery class,
which performs various database operations on the Chinook SQLite database.
The tests verify album queries, table joins, and invoice analysis.
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
    """Test query_album function which checks if an album exists in the database.
    
    Queries the Album table in the Chinook database to verify if an album
    with the given name exists.
    
    Args:
        name: Album name to search for
        expected: Expected boolean result (True if exists, False otherwise)
        
    Test cases:
        - "Presence": Known album in the database, should return True
        - "Roundabout": Not an album name in the database, should return False
    """
    sql_query = SqlQuery()
    assert sql_query.query_album(name) == expected


def test_benchmark_query_album(benchmark) -> None:
    """Benchmark the performance of query_album.
    
    Measures execution time for querying an album that exists in the
    database ("Presence").
    """
    sql_query = SqlQuery()
    benchmark(sql_query.query_album, "Presence")


def test_join_albums() -> None:
    """Test join_albums function which performs a multi-table join operation.
    
    Joins the Album, Artist, and Track tables to retrieve complete album
    information including track name, album title, and artist name.
    Tests that the first result matches the expected tuple.
    
    Expected first result:
        - Track: "For Those About To Rock (We Salute You)"
        - Album: "For Those About To Rock We Salute You"
        - Artist: "AC/DC"
    """
    sql_query = SqlQuery()
    assert sql_query.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    """Benchmark the performance of join_albums.
    
    Measures execution time for performing a three-table join operation
    across Album, Artist, and Track tables in the Chinook database.
    """
    sql_query = SqlQuery()
    benchmark(sql_query.join_albums)


def test_top_invoices() -> None:
    """Test top_invoices function which retrieves the top 10 invoices by total amount.
    
    Queries the Invoice table, orders by total amount in descending order,
    and returns the top 10 results. Tests verify:
    - First invoice total is 25.86
    - Third invoice total is 21.86
    - Exactly 10 invoices are returned
    
    Each invoice tuple contains: (InvoiceId, CustomerId, Total)
    where CustomerId is the integer ID of the customer who made the invoice.
    """
    sql_query = SqlQuery()
    top = sql_query.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    """Benchmark the performance of top_invoices.
    
    Measures execution time for querying and sorting the top 10 invoices
    by total amount from the Invoice table.
    """
    sql_query = SqlQuery()
    benchmark(sql_query.top_invoices)
