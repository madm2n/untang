# Agent Instructions

## Project

- This is a Python 3.11+ package for entity resolution.
- Preserve sklearn estimator compatibility when changing public APIs.
- Keep runtime and development dependencies in `pyproject.toml`.

## Verification

Before completing changes, run:

```bash
python -m pytest
python -m basedpyright
python -m ruff check .
```

Report any failures rather than ignoring them.
