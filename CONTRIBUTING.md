# Contributing to llm-benchmarking-py

Thank you for your interest in contributing to llm-benchmarking-py! We welcome contributions from all team members and the community.

## Table of Contents

- [Getting Started](#getting-started)
- [Requesting Repository Access](#requesting-repository-access)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Review Process](#code-review-process)

## Getting Started

Before you begin contributing, please:

1. Read through this contributing guide
2. Familiarize yourself with the project structure and codebase
3. Review the [README.md](README.md) for project overview
4. Check the [TEAM_ACCESS.md](TEAM_ACCESS.md) file for access procedures

## Requesting Repository Access

### For New Team Members

If you're a new team member needing repository access:

1. **Contact the Repository Maintainers:**
   - Primary maintainer: Matthew Truscott (matthew.truscott@turintech.ai)
   - See [CODEOWNERS](CODEOWNERS) for the full list of code owners

2. **Provide the Following Information:**
   - Your full name
   - Your company email address
   - Your GitHub/GitLab username
   - Your team/department
   - Reason for access (development, testing, documentation, etc.)
   - Required permission level (read, write, admin)

3. **Access Levels:**
   - **Read**: View code, clone repository, create issues
   - **Write**: All read permissions + push code, create branches, manage issues and PRs
   - **Maintain**: All write permissions + manage settings (without destructive actions)
   - **Admin**: All permissions including repository settings and team management

4. **Onboarding Steps:**
   - Once access is granted, you'll receive an invitation via email
   - Accept the invitation to gain access to the repository
   - Clone the repository and follow the development setup below
   - Review any team-specific documentation or guidelines

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)
- Git

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd llm-benchmarking-py
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Verify installation:**
   ```bash
   poetry run main
   poetry run pytest --benchmark-skip tests/
   ```

## Contributing Guidelines

### Types of Contributions

We welcome the following types of contributions:

- **Bug Fixes**: Fix issues in existing code
- **New Features**: Add new benchmark functions or modules
- **Documentation**: Improve README, docstrings, or guides
- **Tests**: Add or improve test coverage
- **Performance**: Optimize existing implementations
- **Refactoring**: Improve code quality without changing functionality

### Before You Start

1. Check existing issues to avoid duplicate work
2. For major changes, open an issue first to discuss the approach
3. Create a feature branch for your work
4. Keep changes focused and atomic

## Code Standards

### Python Style Guide

We follow PEP 8 style guidelines with some modifications:

- **Formatting**: Use `black` for code formatting
- **Import Sorting**: Use `isort` for organizing imports
- **Line Length**: Maximum 88 characters (black default)
- **Type Hints**: Use type hints where appropriate
- **Docstrings**: Use Google-style docstrings for all public functions

### Code Formatting

Before committing, format your code:

```bash
poetry run black src/ tests/
poetry run isort src/ tests/
```

### Naming Conventions

- **Classes**: PascalCase (e.g., `Primes`, `SqlQuery`)
- **Functions**: snake_case (e.g., `sum_range`, `is_prime`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_VALUE`)
- **Private Functions**: prefix with underscore (e.g., `_helper_function`)

## Testing

### Running Tests

All contributions must include appropriate tests:

```bash
# Run unit tests
poetry run pytest --benchmark-skip tests/

# Run benchmarks
poetry run pytest --benchmark-only tests/

# Run all tests
poetry run pytest tests/
```

### Writing Tests

- Place tests in the `tests/` directory mirroring the `src/` structure
- Use `pytest` framework
- Include both functional tests and performance benchmarks
- Aim for high code coverage

### Test Requirements

- All new functions must have corresponding tests
- Tests should cover edge cases and error conditions
- Performance-critical code should include benchmarks

## Submitting Changes

### Branch Naming

Use descriptive branch names following this pattern:

- `feature/description` - for new features
- `bugfix/description` - for bug fixes
- `docs/description` - for documentation changes
- `refactor/description` - for refactoring
- `test/description` - for test additions/improvements

Examples:
- `feature/add-fibonacci-benchmark`
- `bugfix/fix-prime-edge-case`
- `docs/update-contributing-guide`

### Commit Messages

Write clear, descriptive commit messages:

```
<type>: <short summary> (max 50 chars)

<detailed description if needed>
<why the change was made>
<what impact it has>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: add Fibonacci sequence benchmark function

Implements iterative and recursive Fibonacci calculations
for LLM benchmarking. Includes tests and performance comparisons.
```

### Pull Request Process

1. **Create a Pull Request:**
   - Use the PR template (it will auto-populate)
   - Fill in all required sections
   - Link related issues using keywords (e.g., "Fixes #123")

2. **PR Checklist:**
   - [ ] Code follows project style guidelines
   - [ ] Code has been formatted with `black` and `isort`
   - [ ] All tests pass
   - [ ] New tests added for new functionality
   - [ ] Documentation updated (if applicable)
   - [ ] No breaking changes (or clearly documented)

3. **PR Title Format:**
   - Use the same format as commit messages
   - Be clear and descriptive
   - Example: `feat: add matrix multiplication benchmark`

## Code Review Process

### Review Timeline

- Initial review typically within 2-3 business days
- Follow-up reviews within 1 business day
- Urgent fixes reviewed within 24 hours

### Review Guidelines

**For Authors:**
- Respond to feedback promptly
- Be open to suggestions and changes
- Ask questions if feedback is unclear
- Update PR based on review comments

**For Reviewers:**
- Be constructive and respectful
- Explain the reasoning behind suggestions
- Approve when requirements are met
- Focus on code quality, correctness, and maintainability

### Approval Requirements

- At least one approval from a code owner required
- All automated checks must pass
- No unresolved conversations
- Branch must be up to date with main/master

### Merging

- Squash and merge is preferred for feature branches
- Merge commit for release branches
- Delete branch after merging

## Questions or Issues?

If you have questions or run into issues:

1. Check existing documentation and issues
2. Ask in team communication channels
3. Contact the maintainers directly
4. Open an issue for bugs or feature requests

## License and Contributor Agreement

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing to llm-benchmarking-py!
