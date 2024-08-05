# mess-with-python

## Study path

- [ChatGPT Explained Completely.](https://www.youtube.com/watch?v=-4Oso9-9KTQ) (2023)
- [The Hitchhiker's Guide to Python!](https://docs.python-guide.org)
- Interpreter versions
  - [How can I install multiple versions of Python on latest OS X and use them in parallel?](https://stackoverflow.com/a/65094122/10906) (2020)
  - [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
- [Using Python Environments in Visual Studio Code](https://code.visualstudio.com/docs/python/environments)
  - [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
    - [If this project is dead, just tell us](https://github.com/pypa/pipenv/issues/4058) (2019)
    - [poetry](https://github.com/python-poetry/poetry)
  - [Conda](https://docs.conda.io/en/latest/index.html)
    - [Anaconda or Miniconda?](https://docs.conda.io/projects/conda/en/stable/user-guide/install/download.html#anaconda-or-miniconda)
    - [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [The Long Story of How Neural Nets Got to Where They Are: A Conversation with Terry Sejnowski](https://www.youtube.com/watch?v=XKC-4Tosdd8) (2023)
  - [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
  - [Hopfield network](https://en.wikipedia.org/wiki/Hopfield_network)
  - [Boltzmann machine](https://en.wikipedia.org/wiki/Boltzmann_machine)
  - [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
  - [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
  - [Control theory](https://en.wikipedia.org/wiki/Control_theory)
  - [Knowledge distillation](https://en.wikipedia.org/wiki/Knowledge_distillation)
- [PyPI · The Python Package Index](https://pypi.org/)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
  - Interpreters
    - [CPython](https://en.wikipedia.org/wiki/CPython)
      - [GlobalInterpreterLock](https://wiki.python.org/moin/GlobalInterpreterLock)
    - [PyPy](https://en.wikipedia.org/wiki/PyPy)
      - [Tracing just-in-time compilation](https://en.wikipedia.org/wiki/Tracing_just-in-time_compilation)
    - [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
      - [Microthread](https://en.wikipedia.org/wiki/Microthread)
    - [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
    - [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
    - [IronPython](https://en.wikipedia.org/wiki/IronPython)
      - [Dynamic Language Runtime](https://en.wikipedia.org/wiki/Dynamic_Language_Runtime)
    - [Jython](https://en.wikipedia.org/wiki/Jython)
  - Dialects
    - [Cython](https://en.wikipedia.org/wiki/Cython)
      - [Using in IPython/Jupyter notebook](https://en.wikipedia.org/wiki/Cython#Using_in_IPython/Jupyter_notebook)
    - [RPython](https://en.wikipedia.org/wiki/PyPy#RPython)
    - [Mojo](https://en.wikipedia.org/wiki/Mojo_(programming_language))
      - [Why Mojo🔥](https://docs.modular.com/mojo/why-mojo.html)
- [Project Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter)
  - [IPython](https://en.wikipedia.org/wiki/IPython)
  - [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
  - [NumPy](https://en.wikipedia.org/wiki/NumPy)
    - [Numba](https://en.wikipedia.org/wiki/Numba)
  - [pandas](https://en.wikipedia.org/wiki/Pandas_(software))
  - [The Scientific Paper Is Obsolete. Here's What's Next. - The Atlantic](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/) (2018) ([archive](https://archive.is/4l509))
    - [Jupyter, Mathematica, and the Future of the Research Paper](https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/) (2018)
  - [mwouts/jupytext](https://github.com/mwouts/jupytext)
- [Doing Data Science in Visual Studio Code](https://code.visualstudio.com/docs/datascience/overview)
- [What's New in Python](https://docs.python.org/3/whatsnew/index.html)

## Prerequisites

- macOS 12 or so
- Install Xcode or Command Line Tools
- Install Homebrew
- Install VS Code
  - Python extension
  - Jupyter extension

## Interpreters

### One interpreter

- brew install python
- python3

### Many interpreters

- brew install python@3.11
- brew install python@3.10
- brew install pypy3.9
- python3.11
- python3.10
- pypy3.9

Then in VS Code:

- ⇧⌘P `>Python: Select Interpreter`
  - Refresh, then add if not found

### Alternative: Pyenv

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
- rm -r myvenv

Or in VS Code:

- ⇧⌘P `>Python: Create Environment…`

Don't commit a virtual environment.

### Alternative: poetry

- brew install poetry
- poetry new foo

## Packages

- pip install beep-boop-test
- pip freeze > requirements.txt

To recall them later:

- pip install -r requirements.txt

To upgrade:

- pip list --outdated
- pip install --upgrade beep-boop-test
- (Freeze again)

## Jupyter

- pip install jupyter
- jupyter notebook
- ipython
- pip install jupyterlab
- jupyter lab

## VS Code

- Open the project folder
- Open a .py file
- ⇧⌘P `>Python: Select Interpreter` or `>Python: Create Environment…`
- ⇧↩︎ = ⇧⌘P `Python: Run Selection/Line in Python Terminal`
  - REPL-driven development?
- Python › Analysis settings
  - Enable Auto Import Completions
  - Set Type Checking Mode to basic
- Make a debug launcher
- Open an .ipynb file
  - `>Notebook: …`
- ⇧⌘P `>Jupyter: Create Interactive Window`

## Conda

Install:

- brew install conda
- brew install conda-zsh-completion
- conda init zsh # or whatever shell
- Start a new tab

Use it:

- ⇧⌘P `>Python: Create Environment…`
- conda activate \`pwd\`/.conda
- conda install jupyter
- which jupyter
- conda env export > environment.yml
- conda deactivate
- rm -r .conda
- ⇧⌘P `>Python: Create Environment…`
- conda activate example
- which jupyter

To remove Conda:

- conda init --reverse zsh
- brew uninstall conda conda-zsh-completion
