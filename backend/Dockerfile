FROM python:3.9-slim-buster
WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6 \
  GUNICORN_VERSION=20.1.0

RUN pip install poetry==$POETRY_VERSION gunicorn==$GUNICORN_VERSION

# copy requirements first for caching
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
 && poetry install --no-dev --no-interaction --no-ansi

COPY . /app/backend
CMD ["gunicorn", "--bind=0.0.0.0:5000", "backend.wsgi:app"]
