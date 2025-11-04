#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate CLEAN with the clean command
CLEAN=""

if [[ -z "${CLEAN:-}" ]]; then
  echo "No clean command specified; skipping."
  exit 0
fi

# Split CLEAN into an array to avoid eval and prevent injection
read -r -a CLEAN_ARR <<< "$CLEAN"
printf 'Running clean command: '
printf '%q ' "${CLEAN_ARR[@]}"
printf '\n'
"${CLEAN_ARR[@]}"
