FROM python:3.9-slim-buster
WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
    apt-get install -y gcc build-essential libssl-dev libffi-dev python-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install poetry==1.1.6 gunicorn==20.1.0

# copy requirements first for caching
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
 && poetry install --no-dev --no-interaction --no-ansi

COPY . /app/backend
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=5", "backend.wsgi:app"]
