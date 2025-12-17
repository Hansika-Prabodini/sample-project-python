# Data Directory

This directory contains the database files used by the `llm_benchmark` project for SQL query benchmarking.

## Chinook Database

### Overview

The **Chinook database** (`chinook.db`) is a sample SQLite database that represents a digital media store. It's widely used for learning and testing SQL queries.

### Database Contents

The Chinook database contains 11 tables representing different aspects of a music store:

#### Core Tables

- **Album** - Music albums
  - AlbumId (PK)
  - Title
  - ArtistId (FK → Artist)

- **Artist** - Music artists
  - ArtistId (PK)
  - Name

- **Track** - Individual songs/tracks
  - TrackId (PK)
  - Name
  - AlbumId (FK → Album)
  - MediaTypeId (FK → MediaType)
  - GenreId (FK → Genre)
  - Composer
  - Milliseconds
  - Bytes
  - UnitPrice

- **MediaType** - Format of tracks (MP3, AAC, etc.)
  - MediaTypeId (PK)
  - Name

- **Genre** - Music genres
  - GenreId (PK)
  - Name

#### Sales & Customer Tables

- **Customer** - Store customers
  - CustomerId (PK)
  - FirstName, LastName
  - Company, Address, City, State, Country, PostalCode
  - Phone, Fax, Email
  - SupportRepId (FK → Employee)

- **Employee** - Store employees
  - EmployeeId (PK)
  - FirstName, LastName, Title
  - ReportsTo (FK → Employee)
  - BirthDate, HireDate
  - Address, City, State, Country, PostalCode
  - Phone, Fax, Email

- **Invoice** - Customer purchases
  - InvoiceId (PK)
  - CustomerId (FK → Customer)
  - InvoiceDate
  - BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode
  - Total

- **InvoiceLine** - Items in each invoice
  - InvoiceLineId (PK)
  - InvoiceId (FK → Invoice)
  - TrackId (FK → Track)
  - UnitPrice
  - Quantity

#### Playlist Tables

- **Playlist** - Named collections of tracks
  - PlaylistId (PK)
  - Name

- **PlaylistTrack** - Junction table linking playlists and tracks
  - PlaylistId (FK → Playlist)
  - TrackId (FK → Track)

### Usage in llm_benchmark

The SQL module (`llm_benchmark.sql.query`) uses this database to benchmark SQL query generation and execution:

- **Album queries** - Search for specific albums
- **Table joins** - Complex queries joining Album, Artist, and Track tables
- **Aggregations** - Finding top invoices by total amount

### Database Schema Diagram

```
Artist ────┐
           │
           ├─→ Album ───→ Track ──┬─→ InvoiceLine ───→ Invoice ───→ Customer ───→ Employee
           │                      │                                                    ↓
           │                      └─→ PlaylistTrack ──→ Playlist              (Manager/Reports)
           │                      │
           │                      ├─→ MediaType
           │                      └─→ Genre
```

### Sample Data

The database contains:
- 347 Artists
- 275 Albums  
- 3,503 Tracks
- 59 Customers
- 412 Invoices
- 8 Employees
- 18 Playlists

### File Information

- **Filename**: `chinook.db`
- **Format**: SQLite 3
- **Size**: ~1.3 MB
- **License**: Public domain sample database

### References

The Chinook database is maintained by Luis Rocha and is available at:
- GitHub: [lerocha/chinook-database](https://github.com/lerocha/chinook-database)

### Exploring the Database

You can explore the database using any SQLite client:

```bash
# Using sqlite3 command-line tool
sqlite3 data/chinook.db

# List all tables
.tables

# View schema of a specific table
.schema Album

# Run a sample query
SELECT * FROM Artist LIMIT 5;
```

Or use GUI tools like:
- DB Browser for SQLite
- DBeaver
- DataGrip
