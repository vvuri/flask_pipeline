## Best practice 
~/projects/project_name/ 
```
docs/               # documentation
scripts/
  manage.py         # installed to PATH via setup.py
project_name/       # project dir (the one which django-admin.py creates)
  apps/             # project-specific applications
    accounts/       # most frequent app, with custom user model
    __init__.py
    ...
  settings/         # settings for different environments, see below
    __init__.py
    production.py
    development.py
    ...

  __init__.py       # contains project version
  urls.py
  wsgi.py
static/             # site-specific static files
templates/          # site-specific templates
tests/              # site-specific tests (mostly in-browser ones)
tmp/                # excluded from git
setup.py
requirements.txt
requirements_dev.txt
pytest.ini
```

with virtualenv:
```
~/.venvs
```

deploy
```
source $VENV/bin/activate
export DJANGO_SETTINGS_MODULE=project_name.settings.production
git pull
pip install -r requirements.txt

# Update database, static files, locales
manage.py syncdb  --noinput
manage.py migrate
manage.py collectstatic --noinput
manage.py makemessages -a
manage.py compilemessages

# restart wsgi
touch project_name/wsgi.py
```