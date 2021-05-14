# Backend service

## Setup dev environment
Requirements:
 - Python > 3.8 is installed
 - Poetry is installed (https://python-poetry.org/docs/)

```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
poetry install
```

## Startup in development

```
source venv/bin/activate
export FLASK_ENV=development
flask run
```
