import pytest

from llm_benchmark.sql.query import SqlQuery


def test_sql_injection_attempt_does_not_match_or_modify_db():
    # Common injection payload that would break naive string formatting queries
    payload = "Presence'; DROP TABLE Album; --"

    # Should not match; should not raise; should not modify DB (DB is read-only as extra protection)
    assert SqlQuery.query_album(payload) is False

    # Normal behavior still works afterwards
    assert SqlQuery.query_album("Presence") is True


@pytest.mark.benchmark(group="security")
def test_benchmark_query_album_injection(benchmark):
    benchmark(SqlQuery.query_album, "Presence'; DROP TABLE Album; --")
