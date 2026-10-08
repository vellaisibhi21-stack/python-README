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
