# SQL Module

This module contains SQL query operations using the Chinook database for benchmarking purposes.

## Database

The module uses the **Chinook SQLite database** (`data/chinook.db`), which contains:
- Album, Artist, and Track information
- Customer and Invoice data
- Various music store related tables

## Modules

### SqlQuery (`query.py`)

SQL query operations for database interactions.

#### Methods

- **`query_album(name: str) -> bool`**
  - Check if an album with the given name exists in the database
  - Args: `name` - Album title to search for
  - Returns: `True` if the album exists, `False` otherwise
  - Example:
    ```python
    from llm_benchmark.sql.query import SqlQuery
    SqlQuery.query_album("Presence")    # Returns: True (if exists)
    SqlQuery.query_album("NonExistent") # Returns: False
    ```

- **`join_albums() -> list`**
  - Join the Album, Artist, and Track tables to get comprehensive track information
  - Returns: List of tuples containing (TrackName, AlbumName, ArtistName)
  - Uses subqueries to fetch related album and artist information for each track
  - Example:
    ```python
    results = SqlQuery.join_albums()
    for track_name, album_name, artist_name in results[:5]:
        print(f"{track_name} - {album_name} by {artist_name}")
    ```

- **`top_invoices() -> list`**
  - Get the top 10 invoices ordered by total amount
  - Returns: List of tuples containing (InvoiceId, CustomerId, Total)
  - Ordered by Total in descending order
  - Example:
    ```python
    top_10 = SqlQuery.top_invoices()
    for invoice_id, customer_id, total in top_10:
        print(f"Invoice {invoice_id}: Customer {customer_id} - ${total}")
    ```

## Usage Example

```python
from llm_benchmark.sql.query import SqlQuery

# Check if albums exist
albums_to_check = ["Abbey Road", "Dark Side of the Moon", "Unknown Album"]
for album in albums_to_check:
    exists = SqlQuery.query_album(album)
    print(f"{album}: {'Found' if exists else 'Not Found'}")

# Get joined album/artist/track information
print("\nSample tracks with album and artist info:")
results = SqlQuery.join_albums()
for track_name, album_name, artist_name in results[:10]:
    print(f"  {track_name} - {album_name} by {artist_name}")

# Get top invoices
print("\nTop 10 Invoices:")
top_invoices = SqlQuery.top_invoices()
for invoice_id, customer_id, total in top_invoices:
    print(f"  Invoice #{invoice_id}: Customer {customer_id} - ${total:.2f}")
```

## Database Schema (Relevant Tables)

### Album
- AlbumId (Primary Key)
- Title
- ArtistId (Foreign Key)

### Artist
- ArtistId (Primary Key)
- Name

### Track
- TrackId (Primary Key)
- Name
- AlbumId (Foreign Key)
- MediaTypeId
- GenreId
- Composer
- Milliseconds
- Bytes
- UnitPrice

### Invoice
- InvoiceId (Primary Key)
- CustomerId (Foreign Key)
- InvoiceDate
- BillingAddress
- BillingCity
- BillingState
- BillingCountry
- BillingPostalCode
- Total

## Performance Notes

- All queries use proper parameterization to prevent SQL injection
- The `join_albums()` method uses subqueries rather than JOINs for demonstration
- Database connections are properly managed with context managers
- Designed to benchmark LLM code generation for SQL query construction

## Requirements

- SQLite3 (included with Python standard library)
- Chinook database file at `data/chinook.db`
