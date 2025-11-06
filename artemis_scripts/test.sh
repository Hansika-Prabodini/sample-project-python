#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate TEST with the test command as an array to avoid eval and word-splitting
TEST=(poetry run pytest --benchmark-skip tests/)
# Show the command being run (quoted)
printf 'Running test command:'
printf ' %q' "${TEST[@]}"
printf '\n'
# Execute safely
"${TEST[@]}"
