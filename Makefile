.PHONY: run-server postgres

run-server:
	@echo "Starting server..."
	@poetry run python3 run.py

postgres:
	docker-compose up -d