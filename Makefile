.PHONY: run-server postgres app migrate


run-server:
	@echo "Starting server..."
	@poetry run python3 run.py

postgres:
	docker-compose -f bd.yaml up -d
	alembic upgrade head

migrate:
	alembic upgrade head

