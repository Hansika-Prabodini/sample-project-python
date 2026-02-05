import sqlite3
from textwrap import dedent


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
            
        Raises:
            ValueError: If name is None, empty, not a string, or exceeds maximum length
        """
        # Input validation for security and data integrity
        if name is None:
            raise ValueError("Album name cannot be None")
        
        if not isinstance(name, str):
            raise ValueError("Album name must be a string")
        
        # Strip leading/trailing whitespace
        name = name.strip()
        
        if not name:
            raise ValueError("Album name cannot be empty")
        
        # Reasonable maximum length for album titles (most album titles are under 200 chars)
        MAX_ALBUM_TITLE_LENGTH = 255
        if len(name) > MAX_ALBUM_TITLE_LENGTH:
            raise ValueError(f"Album name cannot exceed {MAX_ALBUM_TITLE_LENGTH} characters")
        
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()

            cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
            return len(cur.fetchall()) > 0

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
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
            return cur.fetchall()

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
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
            return cur.fetchall()
