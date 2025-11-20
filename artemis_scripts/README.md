# Artemis Scripts

This directory contains shell scripts for building, testing, and benchmarking the LLM Benchmark project.

## Scripts

### build.sh
Builds the project using poetry and installs dependencies.

### test.sh
Runs unit tests for the project, skipping benchmark tests.

### benchmark.sh
Runs benchmark tests to measure performance of implemented functions.

### clean.sh
Cleans up temporary files and build artifacts from the project.

### variables.sh
Contains shared environment variables and utility functions used by other scripts.

## Usage

Run any script directly from the `artemis_scripts` directory or from the project root:

```bash
./artemis_scripts/build.sh
./artemis_scripts/test.sh
./artemis_scripts/benchmark.sh
./artemis_scripts/clean.sh
```
