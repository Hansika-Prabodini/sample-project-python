import pytest

from llm_benchmark.sql.query import SqlQuery


@pytest.mark.parametrize(
    "album_title, expected_to_exist",
    [
        pytest.param("Presence", True, id="album-exists"),
        pytest.param("Roundabout", False, id="album-does-not-exist"),
    ],
)
def test_query_album_reports_whether_title_exists(
    album_title: str, expected_to_exist: bool
) -> None:
    album_exists = SqlQuery.query_album(album_title)

    assert album_exists is expected_to_exist


def test_benchmark_query_album(benchmark) -> None:
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums_returns_track_with_its_album_and_artist() -> None:
    joined_albums = SqlQuery.join_albums()

    first_track_name, first_album_title, first_artist_name = joined_albums[0]
    assert (
        first_track_name,
        first_album_title,
        first_artist_name,
    ) == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    benchmark(SqlQuery.join_albums)


def test_top_invoices_returns_ten_highest_totals_in_descending_order() -> None:
    top_invoices = SqlQuery.top_invoices()

    invoice_totals = [total for _, _, total in top_invoices]
    assert len(top_invoices) == 10
    assert invoice_totals == sorted(invoice_totals, reverse=True)

    highest_invoice_id, highest_customer_name, highest_total = top_invoices[0]
    assert (highest_invoice_id, highest_customer_name, highest_total) == (
        404,
        "Helena Holý",
        25.86,
    )


def test_benchmark_top_invoices(benchmark) -> None:
    benchmark(SqlQuery.top_invoices)
