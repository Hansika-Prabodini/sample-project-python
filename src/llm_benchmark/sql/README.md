# SQL Module

This module contains functions for benchmarking SQL query generation and execution using SQLite database operations.

## Database

The module uses the Chinook sample database (`data/chinook.db`), which contains:
- **Album**: Music albums with titles and artist relationships
- **Artist**: Music artists
- **Track**: Individual songs/tracks
- **Invoice**: Sales invoices
- **Customer**: Customer information

## Files

### query.py

SQL query operations for testing database interaction and query generation.

**Class: `SqlQuery`**

#### Methods

##### `query_album(name: str) -> bool`
Checks if an album exists in the database by title.

- **Args**: `name` - Album title to search for
- **Returns**: `True` if album exists, `False` otherwise
- **Query Type**: Simple SELECT with WHERE clause

```python
from llm_benchmark.sql.query import SqlQuery

SqlQuery.query_album('Presence')     # True (Led Zeppelin album)
SqlQuery.query_album('Nonexistent')  # False
```

**SQL Query:**
```sql
SELECT * FROM Album WHERE Title = '{name}'
```

##### `join_albums() -> list`
Performs a complex join across Album, Artist, and Track tables using subqueries.

- **Args**: None
- **Returns**: List of tuples containing (TrackName, AlbumName, ArtistName)
- **Query Type**: Complex SELECT with correlated subqueries

```python
results = SqlQuery.join_albums()
print(results[0])  # ('For Those About To Rock', 'For Those About To Rock We Salute You', 'AC/DC')
```

**SQL Query:**
```sql
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
```

**Note**: This query uses subqueries instead of JOINs, which can be less efficient but tests different SQL patterns.

##### `top_invoices() -> list`
Retrieves the top 10 invoices by total amount with customer information.

- **Args**: None
- **Returns**: List of tuples containing (InvoiceId, CustomerName, Total)
- **Query Type**: JOIN with ORDER BY and aggregation

```python
top_10 = SqlQuery.top_invoices()
for invoice_id, customer_name, total in top_10:
    print(f"Invoice {invoice_id}: {customer_name} - ${total}")
```

**SQL Query:**
```sql
SELECT 
    i.InvoiceId, 
    c.FirstName || ' ' || c.LastName AS CustomerName, 
    i.Total
FROM 
    Invoice i
JOIN Customer c ON c.CustomerId = i.CustomerId
ORDER BY i.Total DESC
```

**Returns**: First 10 results (sliced with Python: `[:10]`)

## Usage Examples

### Basic Album Query

```python
from llm_benchmark.sql.query import SqlQuery

# Check for specific albums
albums_to_check = ['Abbey Road', 'Dark Side of the Moon', 'Thriller']
for album in albums_to_check:
    exists = SqlQuery.query_album(album)
    print(f"{album}: {'Found' if exists else 'Not found'}")
```

### Browsing Music Catalog

```python
# Get all track-album-artist combinations
catalog = SqlQuery.join_albums()

# Display first 5 entries
for track, album, artist in catalog[:5]:
    print(f"{artist} - {album}: {track}")
```

### Invoice Analysis

```python
# Get top customers by invoice total
top_invoices = SqlQuery.top_invoices()

print("Top 10 Invoices:")
for inv_id, customer, total in top_invoices:
    print(f"  {inv_id:4d} | {customer:30s} | ${total:6.2f}")
```

## Database Schema

### Relevant Tables

**Album**
- `AlbumId` (INTEGER PRIMARY KEY)
- `Title` (TEXT)
- `ArtistId` (INTEGER FOREIGN KEY)

**Artist**
- `ArtistId` (INTEGER PRIMARY KEY)
- `Name` (TEXT)

**Track**
- `TrackId` (INTEGER PRIMARY KEY)
- `Name` (TEXT)
- `AlbumId` (INTEGER FOREIGN KEY)

**Invoice**
- `InvoiceId` (INTEGER PRIMARY KEY)
- `CustomerId` (INTEGER FOREIGN KEY)
- `Total` (REAL)

**Customer**
- `CustomerId` (INTEGER PRIMARY KEY)
- `FirstName` (TEXT)
- `LastName` (TEXT)

## Benchmarking Purpose

This module tests:
- **SQL syntax generation**: Correct query structure
- **JOIN operations**: Multiple table relationships
- **Aggregation**: String concatenation, ordering
- **Subqueries**: Correlated and nested queries
- **Database I/O**: Connection and cursor management

## Implementation Notes

- Uses SQLite3 (built-in Python module)
- Database file path: `data/chinook.db` (relative to project root)
- No connection pooling (creates new connection per query)
- No parameterized queries in `query_album` (uses string formatting for simplicity)

## Running Benchmarks

```bash
# Run all SQL benchmarks
poetry run pytest --benchmark-only tests/llm_benchmark/sql/

# Run unit tests
poetry run pytest tests/llm_benchmark/sql/
```

## Security Note

The `query_album` method uses string formatting for SQL queries, which is generally not recommended for production code due to SQL injection risks. This is acceptable in a benchmarking context with controlled inputs.

For production code, use parameterized queries:
```python
cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
```
