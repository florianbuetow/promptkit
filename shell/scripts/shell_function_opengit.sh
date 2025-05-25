#!/bin/bash

# Git Repository Opener
# Opens the git repository website of your current project
# Usage: ./opengit.sh (run from within a git repository)

opengit() {
  local url
  url=$(git config --get remote.origin.url | \
    uniq | \
    cut -d'@' -f2 | \
    sed 's/:/\//g' | \
    rev | \
    cut -d'.' -f2,3,4 | \
    rev | \
    xargs -I {} echo "https://{}")

  if [[ "$OSTYPE" == "darwin"* ]] || [[ "$(uname)" == "Darwin" ]]; then
    open "$url"
  elif [[ "$OSTYPE" == "linux"* ]] || [[ "$(uname)" == "Linux" ]]; then
    xdg-open "$url"
  else
    echo "Unsupported OS. Please open this URL manually:"
    echo "$url"
  fi
}

# Call the function
opengit 