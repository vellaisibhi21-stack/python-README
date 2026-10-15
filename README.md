# LaneSync Starter (Python)

A minimal Python project scaffolded by LaneSync with a working CI pipeline.

## Getting started

```bash
python -m pip install -e .
pip install pytest pytest-html pytest-cov
pytest          # runs tests with HTML + coverage reports
```

CI runs automatically on every PR and push via `.github/workflows` (managed by LaneSync).
Replace the sample code in `src/app/` and tests in `tests/` with your own.

## Usage

```python
from app.main import greet

greet("Ana")  # "Hello, Ana!"
greet()       # "Hello, world!"
```

```python
from app.main import shout

shout("Ana")  # "HELLO, ANA!"
```

## cheer()

```python
from app.main import cheer

cheer("Ana")  # "Hello, Ana! 🎉"
```

`farewell(None)` and `greet(None)` treat a missing name as no name.
