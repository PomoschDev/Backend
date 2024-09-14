FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip3 install poetry

ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml /app/
RUN poetry install --no-interaction --no-cache --no-root || poetry install

COPY start.sh /app/start.sh
COPY . /app/
COPY .env /app/

EXPOSE 8080

CMD ["python", "run.py"]

