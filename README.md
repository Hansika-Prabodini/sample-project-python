# LLM Benchmark

A comprehensive Python library for benchmarking common algorithms and data structures tested in LLM coding challenges. This project provides efficient, well-tested implementations of classic algorithms including prime number operations, sorting, control flow patterns, and more.

## Overview

The **llm_benchmark** library is designed to help developers:
- Learn and understand algorithms commonly tested in LLM-based coding challenges
- Benchmark algorithm performance across different problem sizes
- Serve as a reference for optimal implementations
- Practice with comprehensive test suites and benchmarking tools

## Features

- **Algorithm Implementations**: Prime numbers, sorting algorithms, and factorization
- **Control Flow**: Single and double loop patterns with various operations
- **Data Structures**: List operations including search, sort, merge, and rotation
- **SQL Operations**: Query examples and join operations
- **String Operations**: String manipulation including palindrome checks
- **Performance Benchmarking**: Integrated pytest-benchmark for detailed performance analysis
- **Comprehensive Testing**: Unit tests covering all algorithms with parametrized test cases

## Project Structure

```
llm_benchmark/
├── algorithms/           # Prime numbers and sorting algorithms
├── control/              # Single and double loop patterns
├── datastructures/       # List and data structure operations
├── generator/            # Random data generators for testing
├── sql/                  # SQL query examples
└── strings/              # String manipulation operations
```

For a detailed architecture overview, see [ARCHITECTURE.md](./ARCHITECTURE.md).

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)

### Installation

1. **Clone the repository** (if applicable):
```bash
git clone <repository-url>
cd llm_benchmark
```

2. **Install dependencies** using Poetry:
```bash
poetry install
```

This will install the project and all development dependencies including pytest, pytest-benchmark, black, and isort.

### Building

To build and install the package:

```bash
# Using the provided build script
./artemis_scripts/build.sh

# Or manually
poetry install
```

### Running

#### Run the Main Demonstration

Execute the main demonstration script which showcases all modules:

```bash
# Using the installed command
poetry run main

# Or directly with Python
python main.py
```

This will output demonstrations of:
- Single loop algorithms (sum, max, modulus)
- Double loop algorithms (matrix operations, pair counting)
- SQL queries (album and invoice queries)
- Prime number operations
- Sorting algorithms
- Data structure operations
- String operations

#### Run Tests

Run all unit tests:

```bash
# Using the test script
./artemis_scripts/test.sh

# Or manually
poetry run pytest tests/
```

Run tests with verbose output:

```bash
poetry run pytest tests/ -v
```

Run a specific test file:

```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py -v
```

Run a specific test:

```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py::test_is_prime -v
```

#### Run Benchmarks

Run performance benchmarks (requires pytest-benchmark):

```bash
# Using the benchmark script
./artemis_scripts/benchmark.sh

# Or manually - run only benchmarks
poetry run pytest --benchmark-only tests/

# Skip benchmarks (run only tests)
poetry run pytest --benchmark-skip tests/
```

View benchmark results:
- Benchmarks are saved to `.benchmarks/` directory
- Results include timing statistics (min, max, median, stddev)
- Compare against previous benchmark runs

### Clean Build Artifacts

Remove build artifacts and cache files:

```bash
./artemis_scripts/clean.sh
```

## Usage Examples

### Prime Number Operations

```python
from llm_benchmark.algorithms.primes import Primes

# Check if a number is prime
is_prime = Primes.is_prime(17)  # True

# Sum all primes up to n
sum_of_primes = Primes.sum_primes(100)  # 1060

# Get prime factors
factors = Primes.prime_factors(84)  # [2, 2, 3, 7]
```

### Sorting Algorithms

```python
from llm_benchmark.algorithms.sort import Sort

# Sort a list in-place
numbers = [5, 3, 2, 1, 4]
Sort.sort_list(numbers)  # [1, 2, 3, 4, 5]

# Dutch flag partition (3-way partition)
data = [5, 3, 2, 1, 4]
Sort.dutch_flag_partition(data, 3)

# Find N largest elements
top_3 = Sort.max_n([5, 3, 2, 1, 4], 3)  # [5, 4, 3]
```

### Control Flow - Single Loop

```python
from llm_benchmark.control.single import SingleForLoop

# Sum numbers in a range
result = SingleForLoop.sum_range(10)  # 0 + 1 + ... + 9 = 45

# Find maximum in list
maximum = SingleForLoop.max_list([1, 2, 3])  # 3

# Sum with modulus condition
result = SingleForLoop.sum_modulus(100, 3)
```

### Control Flow - Double Loop

```python
from llm_benchmark.control.double import DoubleForLoop

# Sum of square numbers
sum_sq = DoubleForLoop.sum_square(10)  # 1² + 2² + ... + 10²

# Sum triangle numbers
sum_tri = DoubleForLoop.sum_triangle(10)  # 1 + (1+2) + (1+2+3) + ...

# Count pairs with specific property
pairs = DoubleForLoop.count_pairs([1, 2, 3, 4])
```

### Data Structure Operations

```python
from llm_benchmark.datastructures.dslist import DsList

test_list = [1, 2, 3, 4, 5]

# Reverse a list
reversed_list = DsList.reverse_list(test_list)  # [5, 4, 3, 2, 1]

# Rotate list
rotated = DsList.rotate_list(test_list, 2)  # [4, 5, 1, 2, 3]

# Merge lists
merged = DsList.merge_lists([1, 2], [3, 4])  # [1, 2, 3, 4]
```

### String Operations

```python
from llm_benchmark.strings.strops import StrOps

# Reverse a string
reversed_str = StrOps.str_reverse("hello")  # "olleh"

# Check if palindrome
is_pal = StrOps.palindrome("racecar")  # True
```

## Development Workflow

### Code Formatting

This project uses Black and isort for code formatting. Format your code before committing:

```bash
# Format with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/
```

### Testing Best Practices

- Write tests for all new functions using pytest
- Use parametrized tests for multiple test cases
- Include docstrings explaining test purpose
- Benchmark performance-critical functions

For contribution guidelines, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Dependencies

### Runtime Dependencies
- **Python**: ^3.8

### Development Dependencies
- **pytest**: ^7.4.3 - Testing framework
- **pytest-benchmark**: ^4.0.0 - Benchmarking utilities
- **black**: ^23.12.0 - Code formatter
- **isort**: ^5.13.1 - Import sorter

## Project Configuration

The project is configured using Poetry. Key configuration files:

- **pyproject.toml**: Project metadata, dependencies, and tool configuration
- **artemis_scripts/**: Build, test, and benchmark automation scripts
- **tests/**: Unit and benchmark tests

## Architecture

The project follows a modular architecture with clear separation of concerns:

```
Input Data → Algorithm Module → Output Result
    ↓             ↓                ↓
  Lists      Primes, Sort,    Integers,
  Numbers    Strings, etc.    Booleans,
  Strings                     Lists
```

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed architecture diagram and module descriptions.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on:
- Code style and formatting
- Testing requirements
- Submitting pull requests
- Reporting issues

## License

This project is provided as-is for educational and benchmarking purposes.

## Author

Matthew Truscott <matthew.truscott@turintech.ai>

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-benchmark Guide](https://pytest-benchmark.readthedocs.io/)
- [Python Algorithm Patterns](https://en.wikipedia.org/wiki/Algorithm)
- [Big O Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
