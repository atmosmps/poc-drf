# Deploy Django App at Heroku

## Minimal configuration to host a Django project at Heroku.

If you use a Django app with the poetry dependence manager.
You need install a [Python Poetry Buildpack](https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack)
for [deploy in Heroku](https://github.com/moneymeets/python-poetry-buildpack).
After having installed follow the steps below.

If you are trying to configure a project that has already been deployed on Heroku with pip,
and are now switching to Poetry, you will need to remove the app from Heroku and deploy again.

**Don't forget, in the following steps, to adapt the commands to use `poetry` instead of `pip`.**

## Create the project directory

- `mkdir directory_name`
- `cd directory_name`

## Create and activate your virtuanenv

- `virtualenv -p python3 .venv`
- `. .vEnv/bin/activate`

## Install Django

- `pip install django`

## Create the Django Project

- `django-admin startproject myproject`

## Initialize the Git repository

- `git init`
- add the `.gitignore` file

## Hidding instance configuration

- `pip install python-decouple`
- create an `.env` file at the root path and insert the following variables
- `SECRET_KEY=Your$eCretKeyHere (Get this secrety key from the settings.py)`
- `DEBUG=True`

### Settings.py

```
from decouple import config
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

## Configuring the Data Base (You don't need that if you already had an database)

- `pip install dj-database-url`

### Settings.py

```
from dj_database_url import parse as dburl

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}
```

## Static Files

- `pip install dj-static`

### WSGI

```
from dj_static import Cling
application = Cling(get_wsgi_application())
```

- Also don't forget to check "DJANGO_SETTINGS_MODULE". It is prone to frequent mistakes.

### Settings.py

- `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`

## Create a requirements-dev.txt

**If you use the Python Poetry Buildpack this step is non necessery.**

- `pip freeze > requirements-dev.txt`

## Create a file requirements.txt file and include reference to previows file and add two more requirements

**If you use the Python Poetry Buildpack this step is non necessery.**

- `-r requirements-dev.txt`

### Install production dependences

**If you use the Python Poetry Buildpack this step is non necessery.**

With Poetry use `poetry install` command.

```
pip install gunicorn
pip install  psycopg2
```

## Create a file Procfile and add the following code

`web: gunicorn <you-apppath-here>.wsgi`

You can check in django website or heroku website for more information:

- https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/gunicorn/
- https://devcenter.heroku.com/articles/django-app-configuration

## Create a file `runtime.txt` and add the following core

**If you use the Python Poetry Buildpack this step is non necessery.**

**For use the Poetry the `runtime.txt` file is do not necessary.**

- python-3.7.8 (add your python version here)

## Creating the app at Heroku

You should install heroku CLI tools in your computer previously (See http://bit.ly/2jCgJYW)

`heroku apps:create app-name`

You can also login in heroku by: `heroku login`. Remember to grab the address of the app in this point;

## Setting the allowed hosts

Include your address at the `ALLOWED_HOSTS` directives in `settings.py` - Just the domain, make sure that you will take the protocol and slashes from the string.

## Heroku install config plugin

`heroku plugins:install heroku-config`

### Sending configs from `.env` to Heroku (you have to be inside tha folther where `.env` files is)

```
heroku plugins:install heroku-config

heroku config:push -a
```

### To show heroku configs do

`heroku config `

(check this, if you fail changing by code, try changing by heroku dashboard)

## Publishing the app

```
git add .
git commit -m 'Configuring the app'
git push heroku main
```

## Creating the data base (if you are using your own data base you don't need it, if was migrated there)

`heroku run python3 manage.py migrate`

## Creating the Django Admin user

`heroku run python3 manage.py createsuperuser (the same as above)`

## EXTRAS

### You may need to disable the collectstatic

`heroku config:set DISABLE_COLLECTSTATIC=1`

### Also recommend set this configuration to your heroku settings

`WEB_CONCURRENCY=3`

### Changing a specific configuration

`heroku config:set DEBUG=True`
