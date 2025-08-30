
# Contributing

1. Create a topic branch.
2. Run ruff and black.
3. Add or update tests.
4. Open a pull request.

## Dev setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
ruff check .
black --check .
pytest -q
```
