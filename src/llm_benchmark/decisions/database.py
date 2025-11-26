import sqlite3
from pathlib import Path
from typing import Optional


class DatabaseManager:
    """Static class for managing SQLite database initialization and connections.
    
    This class provides thread-safe database connection management for the
    decision-making system with idempotent initialization.
    """
    
    DEFAULT_DB_PATH = "data/decisions.db"
    
    @staticmethod
    def initialize_db(db_path: Optional[str] = None) -> None:
        """Initialize the database by creating the file and executing schema.
        
        This method is idempotent and can be called multiple times safely.
        Creates the database directory if it doesn't exist and executes the
        schema.sql file to set up tables.
        
        Args:
            db_path: Path to the database file. Defaults to data/decisions.db
            
        Raises:
            FileNotFoundError: If schema.sql file is not found
            PermissionError: If unable to create database directory or file
            sqlite3.Error: If database initialization fails
        """
        if db_path is None:
            db_path = DatabaseManager.DEFAULT_DB_PATH
            
        try:
            # Create database directory if it doesn't exist
            db_dir = Path(db_path).parent
            db_dir.mkdir(parents=True, exist_ok=True)
            
            # Get the path to schema.sql (in same directory as this file)
            schema_path = Path(__file__).parent / "schema.sql"
            
            if not schema_path.exists():
                raise FileNotFoundError(
                    f"Schema file not found at {schema_path}. "
                    "Please ensure schema.sql exists in the decisions directory."
                )
            
            # Read schema file
            with open(schema_path, 'r') as f:
                schema_sql = f.read()
            
            # Create/open database and execute schema
            conn = sqlite3.connect(db_path)
            try:
                # Enable foreign keys
                conn.execute("PRAGMA foreign_keys = ON")
                
                # Execute schema (will be idempotent if schema uses IF NOT EXISTS)
                conn.executescript(schema_sql)
                conn.commit()
            finally:
                conn.close()
                
        except PermissionError as e:
            raise PermissionError(
                f"Permission denied when creating database at {db_path}: {e}"
            )
        except sqlite3.Error as e:
            raise sqlite3.Error(
                f"Database initialization failed for {db_path}: {e}"
            )
        except OSError as e:
            raise OSError(
                f"File system error when initializing database at {db_path}: {e}"
            )
    
    @staticmethod
    def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
        """Get a connection to the database with foreign keys enabled.
        
        Args:
            db_path: Path to the database file. Defaults to data/decisions.db
            
        Returns:
            sqlite3.Connection: A connection object with foreign keys enabled
            
        Raises:
            FileNotFoundError: If database file doesn't exist
            PermissionError: If unable to access database file
            sqlite3.Error: If connection fails
        """
        if db_path is None:
            db_path = DatabaseManager.DEFAULT_DB_PATH
            
        try:
            # Check if database file exists
            if not Path(db_path).exists():
                raise FileNotFoundError(
                    f"Database file not found at {db_path}. "
                    "Please run initialize_db() first."
                )
            
            # Create connection
            conn = sqlite3.connect(db_path)
            
            # Enable foreign keys
            conn.execute("PRAGMA foreign_keys = ON")
            
            return conn
            
        except PermissionError as e:
            raise PermissionError(
                f"Permission denied when accessing database at {db_path}: {e}"
            )
        except sqlite3.Error as e:
            raise sqlite3.Error(
                f"Failed to connect to database at {db_path}: {e}"
            )
    
    @staticmethod
    def close_connection(conn: sqlite3.Connection) -> None:
        """Safely close a database connection.
        
        This method will not raise exceptions even if the connection is
        already closed or invalid.
        
        Args:
            conn: The connection to close
        """
        if conn is None:
            return
            
        try:
            conn.close()
        except Exception:
            # Silently ignore any errors during close
            pass
