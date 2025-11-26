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
    """Test querying for album existence in the database.
    
    This test verifies that the query_album method correctly identifies whether
    an album exists in the database. It uses parameterized queries to prevent
    SQL injection vulnerabilities.
    
    Test cases:
    - "Presence": An album that exists in the database (expected: True)
    - "Roundabout": An album that does not exist in the database (expected: False)
    
    Args:
        name: The name of the album to search for
        expected: The expected boolean result (True if album exists, False otherwise)
    """
    assert SqlQuery.query_album(name) == expected


def test_benchmark_query_album(benchmark) -> None:
    """Benchmark the performance of the query_album method.
    
    This benchmark test measures the execution time of querying for an album
    in the database. It uses "Presence" as a test album that exists in the
    database to benchmark realistic query performance.
    
    Args:
        benchmark: Pytest-benchmark fixture for performance measurement
    """
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums() -> None:
    """Test joining Album, Artist, and Track tables.
    
    This test verifies that the join_albums method correctly performs a join
    operation across the Track, Album, and Artist tables, returning track names
    with their corresponding album and artist information.
    
    The test validates the first result tuple, which should contain:
    - Track name: "For Those About To Rock (We Salute You)"
    - Album name: "For Those About To Rock We Salute You"
    - Artist name: "AC/DC"
    """
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    """Benchmark the performance of the join_albums method.
    
    This benchmark test measures the execution time of performing a complex
    join operation across the Track, Album, and Artist tables. This helps
    track query performance for multi-table joins with subqueries.
    
    Args:
        benchmark: Pytest-benchmark fixture for performance measurement
    """
    benchmark(SqlQuery.join_albums)


def test_top_invoices() -> None:
    """Test retrieving the top 10 invoices ordered by total amount.
    
    This test verifies that the top_invoices method correctly retrieves and
    orders the top 10 invoices by total amount in descending order. The test
    validates:
    - The first invoice has a total of 25.86
    - The third invoice has a total of 21.86
    - Exactly 10 invoices are returned
    
    The query joins the Invoice and Customer tables to include customer names.
    """
    top = SqlQuery.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    """Benchmark the performance of the top_invoices method.
    
    This benchmark test measures the execution time of retrieving and ordering
    the top 10 invoices. This helps track query performance for operations
    involving joins, ordering, and result limiting.
    
    Args:
        benchmark: Pytest-benchmark fixture for performance measurement
    """
    benchmark(SqlQuery.top_invoices)
