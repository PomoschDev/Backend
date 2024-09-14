#!/bin/sh

# Запуск миграций
alembic upgrade head

# Запуск сервера
exec python run.py
