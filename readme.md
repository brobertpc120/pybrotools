<!-- Copyright 2024 PYBROTOOLS authors. -->
<!-- See license.md file for details. -->

# Python project `pybrotools`

*pybrotools* is a Python package gathering tools for clinical science
activities. Beyond gathering different tools, the objective of this module is
to provide different method or classes to simplify development of new tools and
accelerate development of these tools.

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [Installation](#installation)
  - [Development version](#development-version)
- [Contributing](#contributing)

<!-- /code_chunk_output -->

## Installation

### Development version

#### Prepare your environment

*pybrotools* has been developed using [Python](https://www.python.org/). All
requirements in terms of python version and libraries are listed in the file
`pyproject.toml` which is located at the root of the project.

To simplify development and use of this package, [poetry](https://python-poetry.org/)
is strongly recommended as it is a tool for dependency management and packaging
in Python.

#### Install the development version from github

The different branches of *pybrotools* are under active development. All
branches might not be properly documented. While `main` branch is usually
stable, it may have undocumented changes or bugs.

If you want to keep up-to-date with the latest code, make sure you have
[Git](https://git-scm.com) installed, and then clone the `main` branch (this
will create a *pybrotools* directory in your current directory). You can
download repository from [github](https://github.com/brobertpc120/pybrotools.git).

#### Post installation

After your first installation of the development version, you should initialize
a Poetry virtual environment with command:

```bash
poetry env use python_version
```

where `python_version` is the name of the Python version you want to use.
Open file `pyproject.toml` to control the minimum version required by the
project.

To use this virtual environment, you should type in the terminal:

```bash
poetry shell
```

Whenever you need to add a required library to this project, you should add it
with Poetry"

```bash
poetry add package
```

The package is installed in the virtual environment and it is added to the
package requirement in the `pyproject.toml` file.

#### Use of makefile

A `makefile` offers different possibilities to work with the package:

- `install`   installs packages and prepare environment using poetry
- `clean`     removes all temp files and dev package
- `format`    runs [ruff](https://docs.astral.sh/ruff/) linter on source code
- `test`      runs all the tests using [pytest](https://docs.pytest.org/en/8.2.x/)

## Contributing

All contributors of *pybrotools* do not have dedicated time to develop and
support this package. As our resources are limited, we very much value your
contributions, be it bug fixes, new core features, or documentation
improvements. For more information, please read our
[contribution guide](contributing.md).
