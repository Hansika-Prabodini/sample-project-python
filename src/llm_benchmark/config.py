"""Configuration module for llm-benchmark.

This module provides configurable constants for the benchmark suite.

Environment Variables:
    LLM_BENCHMARK_DB_PATH: Path to the SQLite database file.
                          Defaults to "data/chinook.db" if not set.

Example Usage:
    # Use default path
    from llm_benchmark.config import DB_PATH
    
    # Override via environment variable (before importing)
    import os
    os.environ['LLM_BENCHMARK_DB_PATH'] = '/custom/path/to/database.db'
    from llm_benchmark.config import DB_PATH
    
    # Or set in shell
    export LLM_BENCHMARK_DB_PATH=/custom/path/to/database.db
    poetry run pytest tests/
"""

import os

# Database configuration
DB_PATH = os.environ.get("LLM_BENCHMARK_DB_PATH", "data/chinook.db")
"""Path to the SQLite database file. 

Can be overridden by setting the LLM_BENCHMARK_DB_PATH environment variable.
Default: "data/chinook.db"
"""
