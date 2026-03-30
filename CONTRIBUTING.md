# Contributing to LLM Benchmark

Thank you for your interest in contributing to the LLM Benchmark project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors and maintainers. We're committed to providing a welcoming and inclusive environment for all contributors.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. **Check existing issues** - Search the issue tracker to see if the issue has already been reported
2. **Create a detailed issue** - Include:
   - A clear, descriptive title
   - A detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected and actual behavior
   - Your environment (Python version, OS, etc.)
   - Any relevant code samples or error messages

### Submitting Changes

1. **Fork the repository** - Create your own fork of the project
2. **Create a feature branch** - Use a descriptive branch name:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes** - Implement your contribution:
   - Keep changes focused and manageable
   - Write clear, descriptive commit messages
   - Follow the project's code style (see below)
   - Add or update tests as needed

4. **Run tests and linting** - Ensure your changes pass all checks:
   ```bash
   poetry run pytest
   poetry run black src/ tests/ main.py
   poetry run isort src/ tests/ main.py
   ```

5. **Commit your changes** - Use clear commit messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   git commit -m "Fix: description of what you fixed"
   ```

6. **Push to your fork** - Push your changes to your forked repository
7. **Create a pull request** - Submit a PR against the main branch:
   - Use a clear title describing the change
   - Reference any related issues
   - Describe what changes you made and why
   - Ensure the PR description is clear and concise

## Code Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) conventions with enforcement through Black and isort.

#### Formatting

**Black** is used for automatic code formatting:
```bash
poetry run black src/ tests/ main.py
```

**isort** is used for consistent import ordering:
```bash
poetry run isort src/ tests/ main.py
```

#### Code Style Rules

1. **Type Hints** - Use type hints for function parameters and return values:
   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

2. **Docstrings** - Use docstrings for all public functions and classes:
   ```python
   def calculate_sum(numbers: List[int]) -> int:
       """Calculate the sum of a list of numbers.
       
       Args:
           numbers (List[int]): List of integers to sum
       
       Returns:
           int: The sum of all numbers
       """
       return sum(numbers)
   ```

3. **Class Organization** - Organize class methods logically:
   - Use `@staticmethod` for utility methods (as in this project)
   - Group related methods together
   - Document each public method

4. **Naming Conventions**:
   - Use `snake_case` for functions and variables
   - Use `PascalCase` for classes
   - Use `UPPER_CASE` for constants

5. **Line Length** - Keep lines to a reasonable length (Black defaults to 88 characters)

### Example Function Structure

```python
from typing import List, Optional

class MyAlgorithm:
    @staticmethod
    def process_data(data: List[int], threshold: Optional[int] = None) -> List[int]:
        """Process data with optional threshold filtering.
        
        This is a longer description explaining the algorithm's behavior,
        edge cases, and any important notes.
        
        Args:
            data (List[int]): Input data to process
            threshold (Optional[int]): Optional threshold value. Defaults to None.
        
        Returns:
            List[int]: Processed data
        """
        result = []
        for item in data:
            if threshold is None or item > threshold:
                result.append(item)
        return result
```

## Testing

All contributions should include appropriate tests. We use pytest for testing.

### Writing Tests

1. **Test Location** - Place tests in the `tests/` directory, mirroring the source structure:
   - Source: `src/llm_benchmark/algorithms/primes.py`
   - Tests: `tests/llm_benchmark/algorithms/test_primes.py`

2. **Test Structure**:
   ```python
   import pytest
   from llm_benchmark.algorithms.primes import Primes

   class TestPrimes:
       def test_is_prime_returns_true_for_primes(self):
           assert Primes.is_prime(2) is True
           assert Primes.is_prime(17) is True
       
       def test_is_prime_returns_false_for_non_primes(self):
           assert Primes.is_prime(1) is False
           assert Primes.is_prime(4) is False
       
       def test_edge_cases(self):
           assert Primes.is_prime(-5) is False
           assert Primes.is_prime(0) is False
   ```

3. **Test Coverage** - Aim for good coverage:
   - Normal cases
   - Edge cases
   - Error conditions
   - Boundary values

4. **Running Tests**:
   ```bash
   # Run all tests
   poetry run pytest
   
   # Run with verbose output
   poetry run pytest -v
   
   # Run a specific test file
   poetry run pytest tests/llm_benchmark/algorithms/test_primes.py
   
   # Run tests with coverage
   poetry run pytest --cov=src
   ```

## Development Workflow

### Setting Up Your Environment

```bash
# Clone your fork
git clone https://github.com/your-username/llm_benchmark.git
cd llm_benchmark

# Install dependencies
poetry install

# Create a feature branch
git checkout -b feature/your-feature
```

### During Development

```bash
# Run tests frequently
poetry run pytest

# Check code style
poetry run black --check src/ tests/
poetry run isort --check-only src/ tests/

# Format code before committing
poetry run black src/ tests/ main.py
poetry run isort src/ tests/ main.py
```

### Before Submitting PR

```bash
# Run full test suite
poetry run pytest -v

# Format all code
poetry run black src/ tests/ main.py
poetry run isort src/ tests/ main.py

# Do a final check
poetry run pytest
```

## Commit Message Guidelines

Write clear, descriptive commit messages:

**Good commit messages:**
```
Add is_prime optimization using sqrt approach
Fix count_duplicates to compare positions not unique values
Update documentation for sort module
Refactor GenList to improve random generation
```

**Avoid:**
```
fixed stuff
update
wip
asdf
```

**Format:**
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and PRs when relevant: "Fix #123"

## PR Review Process

1. **Automated Checks** - Your PR must pass:
   - All tests pass
   - Code style checks pass
   - No breaking changes

2. **Code Review** - At least one maintainer will review your PR:
   - They may request changes
   - Be responsive to feedback
   - Update your PR as needed

3. **Approval and Merge** - Once approved:
   - Your PR will be merged into the main branch
   - Thank you for your contribution!

## Documentation

When adding new features:

1. **Update docstrings** - Add comprehensive docstrings to new functions
2. **Update README.md** - Add your feature to the module overview if applicable
3. **Update architecture diagram** - If adding a new module, update the Mermaid diagram in README.md
4. **Add examples** - Include usage examples in docstrings or README

## Project Structure

```
llm_benchmark/
├── src/llm_benchmark/          # Source code
│   ├── algorithms/             # Algorithm implementations
│   ├── control/                # Control flow patterns
│   ├── datastructures/         # Data structure operations
│   ├── generator/              # Test data generation
│   ├── sql/                    # SQL operations
│   └── strings/                # String operations
├── tests/llm_benchmark/        # Test files (mirror src structure)
├── main.py                     # Entry point demonstrating all modules
├── pyproject.toml              # Project configuration
└── README.md                   # Project documentation
```

## Areas for Contribution

- **New algorithms** - Add interesting algorithm implementations to appropriate modules
- **Performance improvements** - Optimize existing implementations
- **Tests** - Add more test coverage, especially edge cases
- **Documentation** - Improve docstrings, examples, and guides
- **Bug fixes** - Fix identified issues
- **Code cleanup** - Refactor and improve code quality

## Questions or Need Help?

- Check existing documentation and issues
- Review the code and comments
- Ask in an issue or PR discussion
- Reach out to the maintainers

## Recognition

Contributors will be recognized in the project. Thank you for helping make this project better!

---

Thank you for contributing to LLM Benchmark! 🎉
