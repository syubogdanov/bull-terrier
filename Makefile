VENV = poetry run

# Linters
lint: mypy ruff

mypy:
	$(VENV) mypy .

ruff:
	$(VENV) ruff check --no-cache .

# Tests
test: docstring-tests

docstring-tests:
	$(VENV) python -B -m tests.docstring
