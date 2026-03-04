"""
Configuration module for LLM Benchmark.

This module provides environment variable-based configuration with sensible defaults.
It reads configuration from environment variables and falls back to defaults when
environment variables are not set, ensuring backward compatibility with existing code.

Environment Variables:
    DB_PATH: Path to the SQLite database file (default: "data/chinook.db")

Example:
    >>> from llm_benchmark.config import get_db_path
    >>> db_path = get_db_path()
    >>> print(db_path)
    data/chinook.db
"""

import os
from pathlib import Path
from typing import Optional


class Config:
    """Configuration class for LLM Benchmark application.
    
    Provides methods to retrieve configuration values from environment variables
    with sensible defaults. Includes path validation to ensure database files
    are accessible.
    """

    # Default configuration values
    DEFAULT_DB_PATH = "data/chinook.db"

    @classmethod
    def get_db_path(cls, validate: bool = False) -> str:
        """Get the database path from environment variable or default.

        Reads the DB_PATH environment variable. If not set, returns the default
        path. When validate=True, checks that the file exists and is readable.

        Args:
            validate (bool, optional): If True, validates that the database file
                exists and is accessible. Defaults to False.

        Returns:
            str: Path to the database file.

        Raises:
            FileNotFoundError: If validate=True and the database file does not exist
                or is not accessible.
            PermissionError: If validate=True and the database file exists but is
                not readable due to permission issues.

        Example:
            >>> db_path = Config.get_db_path()
            >>> db_path = Config.get_db_path(validate=True)  # Raises if file missing
        """
        db_path = os.getenv("DB_PATH", cls.DEFAULT_DB_PATH)

        if validate:
            cls._validate_path(db_path, "database")

        return db_path

    @classmethod
    def _validate_path(cls, path: str, path_type: str = "file") -> None:
        """Validate that a path exists and is accessible.

        Args:
            path (str): The path to validate.
            path_type (str, optional): Description of the path type for error messages.
                Defaults to "file".

        Raises:
            FileNotFoundError: If the path does not exist.
            PermissionError: If the path exists but is not readable.
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileNotFoundError(
                f"The {path_type} at '{path}' does not exist. "
                f"Please ensure the file is present or set the correct path "
                f"via the DB_PATH environment variable."
            )

        if not os.access(path, os.R_OK):
            raise PermissionError(
                f"The {path_type} at '{path}' is not readable. "
                f"Please check file permissions."
            )

    @classmethod
    def get_all_config(cls) -> dict:
        """Get all configuration values as a dictionary.

        Returns:
            dict: Dictionary containing all configuration values.

        Example:
            >>> config = Config.get_all_config()
            >>> print(config['db_path'])
        """
        return {
            "db_path": cls.get_db_path(),
        }


# Module-level convenience function for easy access
def get_db_path(validate: bool = False) -> str:
    """Get the database path from environment variable or default.

    This is a convenience function that calls Config.get_db_path().
    Reads the DB_PATH environment variable. If not set, returns the default
    path "data/chinook.db".

    Args:
        validate (bool, optional): If True, validates that the database file
            exists and is accessible. Defaults to False.

    Returns:
        str: Path to the database file.

    Raises:
        FileNotFoundError: If validate=True and the database file does not exist.
        PermissionError: If validate=True and the database file is not readable.

    Example:
        >>> from llm_benchmark.config import get_db_path
        >>> db_path = get_db_path()
        >>> db_path = get_db_path(validate=True)
    """
    return Config.get_db_path(validate=validate)
