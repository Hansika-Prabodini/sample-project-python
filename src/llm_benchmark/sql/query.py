import sqlite3
from textwrap import dedent


class SqlQuery:
    @staticmethod
    def _ro_connection() -> sqlite3.Connection:
        """Open a read-only SQLite connection using URI mode.
        Ensures the database cannot be mutated by queries in this project.
        """
        # Use a read-only URI to prevent accidental writes and improve safety
        return sqlite3.connect("file:data/chinook.db?mode=ro", uri=True)

    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        # Parameterized query to avoid SQL injection and context manager for cleanup
        with SqlQuery._ro_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM Album WHERE Title = ?", (name,))
            return cur.fetchone() is not None

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        with SqlQuery._ro_connection() as conn:
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
        with SqlQuery._ro_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                dedent(
                    """\
                    SELECT 
                        i.InvoiceId, 
                        c.FirstName || ' ' || c.LastName AS CustomerName, 
                        i.Total
                    FROM 
                        Invoice i
                    JOIN Customer c ON c.CustomerId = i.CustomerId
                    ORDER BY i.Total DESC
                    LIMIT 10
                    """
                )
            )
            return cur.fetchall()
