import sqlite3
from textwrap import dedent

from llm_benchmark.config import DB_PATH


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
            return len(cur.fetchall()) > 0

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            cur.execute(
                dedent(
                    """\
                    SELECT 
                        t.Name AS TrackName, (
                            SELECT a2.Title 
                            FROM Album a2 
                            WHERE a2.AlbumId = t.AlbumId
                        ) AS AlbumName, 
                        (
                            SELECT ar.Name 
                            FROM Artist ar
                            JOIN Album a3 ON a3.ArtistId = ar.ArtistId
                            WHERE a3.AlbumId = t.AlbumId
                        ) AS ArtistName
                    FROM 
                        Track t
                    """
                )
            )
            return cur.fetchall()

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            cur.execute(
                dedent(
                    """\
                    SELECT 
                        i.InvoiceId, 
                        i.CustomerId, 
                        i.Total
                    FROM 
                        Invoice i
                    ORDER BY i.Total DESC
                    LIMIT 10
                    """
                )
            )
            return cur.fetchall()
