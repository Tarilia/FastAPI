dev:
	poetry run uvicorn fast_api:app --reload
lint:
	poetry run flake8
install:
	poetry install
