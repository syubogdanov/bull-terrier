VENV = poetry run

# Linters
lint: mypy ruff

mypy:
	$(VENV) mypy .

ruff:
	$(VENV) ruff check --no-cache .
