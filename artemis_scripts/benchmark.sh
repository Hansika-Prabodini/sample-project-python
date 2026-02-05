#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Run benchmark tests directly (no eval for security)
echo "Running benchmark command: poetry run pytest --benchmark-only tests/"
poetry run pytest --benchmark-only tests/
