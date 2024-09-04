.PHONY: run-server postgres app


app:
	pip install poetry
	poetry install

run-server:
	@echo "Starting server..."
	@poetry run python3 run.py

postgres:
	docker-compose -f bd.yaml up -d
	alembic upgrade head

app:
	docker-compose up -d

