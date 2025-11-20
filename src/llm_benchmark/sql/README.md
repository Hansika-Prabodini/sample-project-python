# SQL

This module provides SQL query operations for benchmarking database access patterns.

## Modules

### query.py

SQL query operations using the Chinook database:
- `SqlQuery.query_album(name)` - Check if an album with a given name exists
- `SqlQuery.join_albums()` - Join Album, Artist, and Track tables to retrieve complete track information
- `SqlQuery.top_invoices()` - Get the top 10 invoices by total amount

These operations benchmark different SQL query patterns including simple selects, joins, and aggregations.

### query.md

Documentation for SQL queries used in benchmarking.

## Database

Uses the Chinook sample database located in `data/chinook.db`. This database contains real-world-like data structures for music industry operations.
