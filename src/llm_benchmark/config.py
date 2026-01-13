"""Configuration module for llm-benchmark.

This module provides configurable constants for the benchmark suite,
including database path configuration with environment variable support.

Configuration Options:
    DB_PATH: Path to the SQLite database file used for SQL benchmarks.
             Default: "data/chinook.db"
             Environment Variable: LLM_BENCHMARK_DB_PATH

Usage:
    To override the default database path, set the environment variable:
    
    Linux/Mac:
        export LLM_BENCHMARK_DB_PATH="/path/to/custom/database.db"
    
    Windows:
        set LLM_BENCHMARK_DB_PATH=C:\\path\\to\\custom\\database.db
    
    Or in Python:
        import os
        os.environ['LLM_BENCHMARK_DB_PATH'] = '/path/to/custom/database.db'
"""

import os

# Database configuration
# Override by setting LLM_BENCHMARK_DB_PATH environment variable
DB_PATH = os.environ.get("LLM_BENCHMARK_DB_PATH", "data/chinook.db")
