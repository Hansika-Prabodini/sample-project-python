#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Run the build command
echo "Running build command: poetry install"
poetry install
