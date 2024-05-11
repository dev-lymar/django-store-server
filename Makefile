code-style:
	flake8 .
	ruff check .
	ruff format .
	ruff check --select I --fix .