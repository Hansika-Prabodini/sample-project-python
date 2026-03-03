# Contributing to LLM Benchmark

Thank you for your interest in contributing to **llm_benchmark**! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to maintain a welcoming community for all contributors.

## Getting Started

### Prerequisites

Before you start contributing, ensure you have:
- Python 3.8 or higher
- Poetry installed
- Basic knowledge of Git and GitHub workflow

### Setting Up Your Development Environment

1. **Fork and Clone** the repository:
```bash
git clone https://github.com/your-username/llm_benchmark.git
cd llm_benchmark
```

2. **Install dependencies**:
```bash
poetry install
```

3. **Verify setup** by running tests:
```bash
poetry run pytest tests/
```

## Development Workflow

### Creating a Feature Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b bugfix/your-bug-name
```

Use descriptive branch names that indicate the type and nature of your changes.

### Code Style and Standards

This project follows strict code style guidelines:

#### Black Code Formatting

All Python code must be formatted with Black:

```bash
# Format entire codebase
black src/ tests/

# Format specific file
black src/llm_benchmark/your_module.py
```

**Black Configuration**: Uses default settings with line length of 88 characters.

#### Import Sorting with isort

All imports must be sorted and organized with isort:

```bash
# Sort imports in entire codebase
isort src/ tests/

# Sort imports in specific file
isort src/llm_benchmark/your_module.py
```

#### Pre-commit Checklist

Before committing, ensure:
- [ ] Code is formatted with Black
- [ ] Imports are sorted with isort
- [ ] All tests pass
- [ ] No new warnings introduced

### Committing Changes

Write clear and concise commit messages:

```bash
git add .
git commit -m "feat: add new algorithm" 
# or
git commit -m "fix: correct edge case in prime check"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation updates
- `refactor:` for code refactoring
- `test:` for test additions or updates
- `chore:` for maintenance tasks

## Testing Requirements

### Writing Tests

All new code **must** include corresponding tests. Follow these guidelines:

#### Test File Structure

```python
"""Module docstring describing what is tested."""

import pytest
from llm_benchmark.module import YourClass


@pytest.mark.parametrize(
    "input_param, expected_output",
    [
        (value1, result1),
        (value2, result2),
    ],
)
def test_your_function(input_param, expected_output):
    """Test docstring explaining what is tested."""
    assert YourClass.your_function(input_param) == expected_output


def test_benchmark_your_function(benchmark):
    """Benchmark test for performance-critical functions."""
    benchmark(YourClass.your_function, input_value)
```

#### Test Best Practices

1. **Use descriptive test names**: Test names should clearly indicate what they test
   - ✓ `test_is_prime_returns_true_for_prime_numbers`
   - ✗ `test_prime`

2. **Use parametrized tests**: Use `@pytest.mark.parametrize` for multiple test cases
   ```python
   @pytest.mark.parametrize("n, expected", [(2, True), (4, False)])
   def test_is_prime(n, expected):
       assert Primes.is_prime(n) == expected
   ```

3. **Include docstrings**: Explain the purpose and expected behavior
   ```python
   def test_sum_primes():
       """Test that sum_primes correctly adds all primes below n."""
       assert Primes.sum_primes(10) == 17
   ```

4. **Test edge cases**: Include boundary conditions and special cases
   ```python
   # Test edge cases: empty, single element, etc.
   @pytest.mark.parametrize("input, expected", [
       ([], None),           # empty
       ([1], 1),             # single element
       ([1, 2, 3], 3),       # normal case
   ])
   ```

5. **Benchmark performance-critical functions**: Use `benchmark` fixture for algorithms with significant runtime
   ```python
   def test_benchmark_is_prime(benchmark):
       benchmark(Primes.is_prime, 17)
   ```

### Running Tests

Run all tests:
```bash
poetry run pytest tests/ -v
```

Run tests in a specific file:
```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py -v
```

Run tests matching a pattern:
```bash
poetry run pytest tests/ -k "prime" -v
```

Run with coverage:
```bash
poetry run pytest tests/ --cov=src/llm_benchmark
```

Run benchmarks:
```bash
poetry run pytest --benchmark-only tests/
```

Skip benchmarks:
```bash
poetry run pytest --benchmark-skip tests/
```

### Test Coverage

Aim for high test coverage. New code should:
- Have unit tests covering normal cases
- Have tests for edge cases and error conditions
- Include docstrings explaining test purpose
- Pass all existing tests

## Algorithm Implementation Guidelines

### Code Quality Standards

1. **Type Hints**: All functions must include type hints
   ```python
   def is_prime(n: int) -> bool:
       """Check if a number is prime."""
   ```

2. **Docstrings**: All public functions must have docstrings
   ```python
   def is_prime(n: int) -> bool:
       """Check if a number is prime.
       
       Args:
           n: The number to check
           
       Returns:
           True if n is prime, False otherwise
       """
   ```

3. **Comments**: Add comments for complex logic
   ```python
   # Only check odd divisors up to sqrt(n)
   i = 3
   while i * i <= n:
       if n % i == 0:
           return False
       i += 2
   ```

4. **Efficiency**: Consider algorithmic complexity
   - Prefer O(sqrt(n)) over O(n) when possible
   - Document any known performance characteristics
   - Include optimization comments

5. **Static Methods**: Use `@staticmethod` for algorithm classes without state
   ```python
   class Primes:
       @staticmethod
       def is_prime(n: int) -> bool:
           ...
   ```

### Adding a New Algorithm

1. Create a new module in the appropriate directory:
   ```bash
   touch src/llm_benchmark/algorithms/new_algo.py
   ```

2. Implement the algorithm with type hints and docstrings:
   ```python
   class NewAlgorithm:
       @staticmethod
       def solve(param: int) -> int:
           """Solve the problem.
           
           Args:
               param: Input parameter
               
           Returns:
               Result of computation
           """
           # Implementation
           pass
   ```

3. Create comprehensive tests:
   ```bash
   touch tests/llm_benchmark/algorithms/test_new_algo.py
   ```

4. Update the main.py to include your algorithm in the demonstration
5. Update README.md with usage examples
6. Format code and run tests

## Submitting Changes

### Before Submitting

1. **Format your code**:
```bash
black src/ tests/
isort src/ tests/
```

2. **Run all tests**:
```bash
poetry run pytest tests/ -v
```

3. **Run benchmarks** (if applicable):
```bash
poetry run pytest --benchmark-only tests/
```

4. **Verify no warnings** or style issues

### Creating a Pull Request

1. Push your branch to your fork:
```bash
git push origin feature/your-feature-name
```

2. Open a pull request on GitHub with:
   - Clear description of changes
   - Reference to any related issues
   - List of test cases added
   - Benchmark results (if applicable)

3. Respond to review feedback promptly

### PR Review Process

- At least one review required before merge
- All tests must pass
- Code style requirements must be met
- Documentation must be updated

## Reporting Issues

When reporting bugs or suggesting features:

1. **Use clear titles**: "Bug: is_prime fails for negative numbers"
2. **Include details**:
   - Expected behavior
   - Actual behavior
   - Steps to reproduce
   - Python version and OS
3. **Provide examples**:
   ```python
   # This should return False but returns True
   Primes.is_prime(-5)
   ```

## Documentation

### Updating Documentation

1. **README.md**: Update if adding new features or modules
2. **ARCHITECTURE.md**: Update if changing module structure
3. **Code Comments**: Keep inline comments current
4. **Docstrings**: Update if function behavior changes

### Documentation Standards

- Use clear, concise language
- Include code examples
- Explain the "why" not just the "what"
- Keep examples up-to-date

## Questions or Need Help?

- Check existing issues and discussions
- Review the README.md and ARCHITECTURE.md
- Look at existing code for patterns and examples

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing to LLM Benchmark! 🚀
