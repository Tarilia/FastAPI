dev:
	poetry run uvicorn app:app --reload
lint:
	poetry run flake8
install:
	poetry install
