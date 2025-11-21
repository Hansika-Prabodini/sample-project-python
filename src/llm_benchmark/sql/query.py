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
            ValueError: If name is None or empty string
            sqlite3.OperationalError: If database file is not accessible
            sqlite3.Error: For other database-related errors
        """
        # Input validation
        if name is None:
            raise ValueError("Album name cannot be None")
        if not isinstance(name, str):
            raise TypeError(f"Album name must be a string, got {type(name).__name__}")
        if not name.strip():
            raise ValueError("Album name cannot be empty")
        
        try:
            with sqlite3.connect("data/chinook.db") as conn:
                cur = conn.cursor()

                cur.execute(f"SELECT * FROM Album WHERE Title = '{name}'")
                return len(cur.fetchall()) > 0
        except sqlite3.OperationalError as e:
            raise sqlite3.OperationalError(
                f"Failed to access database: {str(e)}"
            ) from e
        except sqlite3.Error as e:
            raise sqlite3.Error(
                f"Database error while querying album: {str(e)}"
            ) from e

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list: List of tuples containing (TrackName, AlbumName, ArtistName)
            
        Raises:
            sqlite3.OperationalError: If database file is not accessible
            sqlite3.Error: For other database-related errors
        """
        try:
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
        except sqlite3.OperationalError as e:
            raise sqlite3.OperationalError(
                f"Failed to access database: {str(e)}"
            ) from e
        except sqlite3.Error as e:
            raise sqlite3.Error(
                f"Database error while joining album tables: {str(e)}"
            ) from e

    @staticmethod
    def top_invoices(n: int = 10) -> list:
        """Get the top n invoices by total

        Args:
            n (int): Number of top invoices to return (default: 10)

        Returns:
            list: List of tuples containing (InvoiceId, CustomerName, Total)
            
        Raises:
            ValueError: If n is None, not positive, or not an integer
            TypeError: If n is not an integer type
            sqlite3.OperationalError: If database file is not accessible
            sqlite3.Error: For other database-related errors
        """
        # Input validation
        if n is None:
            raise ValueError("Parameter 'n' cannot be None")
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}")
        if n <= 0:
            raise ValueError(f"Parameter 'n' must be a positive integer, got {n}")
        
        try:
            with sqlite3.connect("data/chinook.db") as conn:
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
                        """
                    )
                )
                return cur.fetchall()[:n]
        except sqlite3.OperationalError as e:
            raise sqlite3.OperationalError(
                f"Failed to access database: {str(e)}"
            ) from e
        except sqlite3.Error as e:
            raise sqlite3.Error(
                f"Database error while fetching top invoices: {str(e)}"
            ) from e
