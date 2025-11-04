# Security Policy

We take the security of this project seriously. This document explains how to report vulnerabilities, our supported versions, and our ongoing security improvements and next steps.

- Project: llm_benchmark
- Maintainers: see Git history/authors

## Reporting a Vulnerability

- Please email security reports to: security@invalid.example (replace with a monitored address in your fork/org).
- Provide a minimal reproducer, affected versions/commits, and impact assessment if known.
- We aim to acknowledge reports within 3 business days and provide a remediation plan within 14 days.
- Do not create public issues for sensitive reports. We will open a public advisory after a fix is available.

## Supported Versions and Upgrade Plan

This project currently targets Python 3.8 per pyproject.toml. Python 3.8 is End-of-Life. We will maintain only critical security patches on 3.8 while we migrate to supported versions.

Planned support window:
- Current stable (planned): Python 3.11 and 3.12
- Transition period: test against 3.8, 3.10, 3.11, 3.12 in CI

Upgrade path:
- Short term: keep code compatible with 3.8 while adding CI for newer versions.
- Next minor release: bump `python` in `pyproject.toml` to ">=3.10,<3.13" and drop 3.8 from CI.
- Follow-up: update docs, cut a deprecation notice for 3.8, and remove shims if any were added.

## Secure Development Practices

- Dependencies are managed via Poetry. We audit dependencies in CI using `pip-audit` (or `safety`).
- Static analysis with `bandit` runs on every PR.
- `pre-commit` enforces basic hygiene: `black`, `isort`, `bandit`, and dependency audit.
- SQLite usage is read-only and parameterized to prevent SQL injection.

## Known Risks and Mitigations

- SQL Injection: Fixed by parameterized queries and read-only DB connections.
- Resource Handling: All DB operations use context managers.
- Supply Chain: Run `pip-audit` (or `safety`) in CI and locally via pre-commit.

## Hardening and Next Steps

- Add type checking (`mypy`) and enable strict settings over time.
- Consider security-focused fuzz tests (e.g., `hypothesis`) for parsing and SQL boundaries.
- Enable SAST in your hosting platform (e.g., GitHub Code Scanning with CodeQL).
- If shipping as a package, sign releases (e.g., Sigstore) and publish SBOM.

## Coordinated Disclosure

We follow responsible disclosure. We will credit reporters unless anonymity is requested.
