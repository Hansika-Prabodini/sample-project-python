# SQL Module

This module contains SQL query implementations for benchmarking database operations.

## Classes

### SqlQuery
Provides methods for performing SQL queries against the Chinook sample database:
- `query_album(name)`: Check if an album exists by title
- `join_albums()`: Join Album, Artist, and Track tables to retrieve track information
- `top_invoices()`: Get the top 10 invoices by total amount

## Database

All queries operate on the `data/chinook.db` SQLite database, which contains sample music industry data including artists, albums, tracks, customers, and invoices.

## Performance Notes

These implementations include both efficient and potentially inefficient query patterns for benchmarking purposes:
- `query_album()` demonstrates SELECT with WHERE clause optimization
- `join_albums()` shows different JOIN patterns and their performance implications
- `top_invoices()` demonstrates ordering and limiting result sets

## Usage

```python
from llm_benchmark.sql import SqlQuery

# Check if an album exists
exists = SqlQuery.query_album("Dark Side of the Moon")

# Get joined album information
albums = SqlQuery.join_albums()

# Get top invoices
top_invoices = SqlQuery.top_invoices()
```
