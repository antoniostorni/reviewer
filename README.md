# Reviewer

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A simple API that allows users to post and retrieve their reviews.

Check out the API documentation in

http://localhost:8000/docs/

# Prerequisites

- Docker

or
 
- Python 3 (recommended with virtualenv)
  
# Local Development with Docker

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```


# Local Development with virtualenv


Install dependencies
```bash
pip install -r requirements.txt
```


Create DB

```bash
python manage.py migrate
```

Create super user to use the admin interface in http://localhost:8000/admin/

```bash
python manage.py createsuperuser
```


Run development server
```bash
python manage.py runserver
```

Run tests
```bash
python manage.py test
```