FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

COPY . /app/backend
CMD ["gunicorn", "--bind=0.0.0.0:5000", "backend.wsgi:app"]
