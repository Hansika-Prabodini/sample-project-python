import logging
import os
import sqlite3
from textwrap import dedent

logger = logging.getLogger(__name__)


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        try:
            logger.debug("Connecting to DB at %s", os.path.abspath("data/chinook.db"))
            with sqlite3.connect("data/chinook.db") as conn:
                cur = conn.cursor()

                cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
                rows = cur.fetchall()
                logger.debug("query_album(%r) returned %d rows", name, len(rows))
                return len(rows) > 0
        except sqlite3.Error as e:
            raise RuntimeError(f"DB query failed in query_album: {e}") from e

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        try:
            logger.debug("Connecting to DB at %s", os.path.abspath("data/chinook.db"))
            with sqlite3.connect("data/chinook.db") as conn:
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
                rows = cur.fetchall()
                logger.debug("join_albums() returned %d rows", len(rows))
                return rows
        except sqlite3.Error as e:
            raise RuntimeError(f"DB query failed in join_albums: {e}") from e

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        try:
            logger.debug("Connecting to DB at %s", os.path.abspath("data/chinook.db"))
            with sqlite3.connect("data/chinook.db") as conn:
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
                rows = cur.fetchall()
                logger.debug("top_invoices() returned %d rows", len(rows))
                return rows
        except sqlite3.Error as e:
            raise RuntimeError(f"DB query failed in top_invoices: {e}") from e
