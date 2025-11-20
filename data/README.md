# Data Directory

This directory contains data files used by the LLM Benchmark project.

## Files

### chinook.db
SQLite database file containing the Chinook sample database. This database is used for SQL query benchmarking and testing.

The Chinook database includes tables for:
- Artists
- Albums
- Tracks
- Customers
- Invoices
- And other music-related data

## Usage

The SQL query functions in the `src/llm_benchmark/sql` module use this database to perform various queries and benchmark SQL operations.
