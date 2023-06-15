FROM python:3.11-slim-buster
WORKDIR /fastapi_template
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install poetry==1.4.2
COPY poetry.lock pyproject.toml /fastapi_template/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi --no-root
COPY ./ /fastapi_template
