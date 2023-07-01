# mess-with-python

Assuming macOS 12 or so.

## Prerequisites

- Install Xcode or Command Line Tools
- Install Homebrew
- Install VS Code
  - Python extension
  - Jupyter extension

## Python

### One version

- brew install python
- python3

### Many versions

- brew install python@3.11
- brew install python@3.10
- brew install pypy3.9
- python3.11
- python3.10
- pypy3.9

Then in VS Code:

- `>Python: Select Interpreter`
  - Refresh, then add if not found

### Pyenv

- brew install pyenv

In your shell profile:

```
if [ -x "$(which pyenv)" ]; then
  eval "$(pyenv init --path --no-rehash zsh)")"
fi
```

- pyenv install --list
- pyenv install 3.11.4
- pyenv local 3.11.4
- pyenv rehash
- pip3
- python3

## Virtual environments

### venv

- python3.10 -m venv myvenv
- source myvenv/bin/activate
- which python3
- python3 --version
- deactivate
- rm -rf myvenv

Or in VS Code:
- `>Python: Create Environment…`

### poetry

- brew install poetry
- poetry new foo

