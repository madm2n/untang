# untang

`untang` is a Python package under active development.

## Status

Early development. The package currently contains its initial project structure and tooling configuration.

## Requirements

- Python 3.11 or newer

## Installation

From a checkout of this repository, install the package in editable mode:

```bash
python -m pip install -e .
```

For development, install the package with its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Development

Run the test suite and development checks with:

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m basedpyright
```

Runtime and development dependencies are declared in `pyproject.toml`. A separate `requirements.txt` is not used.

## Contributing

Contributions are welcome. Please add tests for new behavior and ensure the development checks pass before opening a pull request.
