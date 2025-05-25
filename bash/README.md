# Bash Snippets

Placed in your `~/.bashrc` or `~/.bash_profile` this bash function opens the git repository website of your current project (you must be inside a folder that is managed by git).

```bash
open_git_remote() {
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