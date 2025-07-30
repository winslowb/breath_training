# CRUSH.md

This file provides build, lint, test commands and coding style guidelines for agentic coding in this repository.

## Build Commands
- Build/Run: `python breath.py`

## Lint Commands
- Lint (Python): `flake8 .`
- Format: `black .`

## Test Commands
- Run all tests: `pytest`
- Run a single test: `pytest -q path/to/test_file.py::test_function`

## Code Style Guidelines
- Imports: Group into standard library, third-party, and local packages (in that order).
- Formatting: Follow PEP8 style conventions; use Black for automated formatting.
- Types: Use type annotations where practical.
- Naming Conventions: Use snake_case for variables and functions, PascalCase for classes.
- Error Handling: Use exceptions for error cases; avoid broad exception catches.

## Additional Guidelines
- Use pre-commit hooks if configured.
- Provide minimal inline comments where necessary.
- Prefer pure functions and modular design.

## Cursor & Copilot
- Refer to any existing rules in .cursor/rules/ or in .github/copilot-instructions.md for additional guidelines.

Happy coding!
