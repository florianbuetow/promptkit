# Bash Snippets

The bash function opens the git repository website of your current project. Place it in your `~/.bashrc` or `~/.bash_profile` or `~/.zshrc` depending on which shell you use. Open a new terminal and run `opengit` inside a git repository path.

```bash
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
```

A