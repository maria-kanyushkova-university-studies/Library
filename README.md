# Library
[![PyPI](https://img.shields.io/pypi/pyversions/Django)](https://pypi.org/project/Django/)
[![PyPI](https://img.shields.io/badge/django-v3.0-blue)](https://pypi.org/project/django-flexible-subscriptions/)

## Overview

Library is an ordered system of heterogeneous electronic documents equipped with navigation and search tools.

**Features:**
* Fast search library data
* Display in REST-API form 

**Technologies used:**
* Python + Django
* PostgreSQL
* ElasticSearch

**Dependencies**
* [Django ElasticSearch](https://pypi.org/project/django-elasticsearch/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Postgresql Psycopg2](https://pypi.org/project/psycopg2/)
 

## Getting started

### Install the App
Clone the repository:

```sh
$ https://github.com/maria-kanyushkova/Library.git
$ cd Library
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

### Setting up PostgreSQL
Now you need to setup `PostgreSQL`. Download and install it from [official download page](https://www.postgresql.org/download/).

Database already defined in `library/settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Setup database by following command (make sure you are at the same level as `manage.py`):
```sh
$ python manage.py migrate
```


### Run Library backend server
Run server by following command:
```sh
$ python manage.py runserver
```
And main link = `http://127.0.0.1:8080/`.