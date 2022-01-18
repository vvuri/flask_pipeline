## Django simple project

### Steps
- Install Django 
  - ```$ pip install django```
  - ```$ django-admin version``` -> 4.0.1
- Create project:
  - ```$ django-admin startproject django_first```
  - ```$ cd django_first```
- Add application in project
  - ```$ python .\manage.py startapp horoscope```
- Run dev server: 
  - ```$ python .\manage.py runserver```
  - Starting development server at http://127.0.0.1:8000/
- [Django documentation](https://docs.djangoproject.com/en/4.0/)
- [Doc Rus](https://django.fun/docs/django/ru/4.0/)
- ConEmu good console with multitab
- Add templates folder in horoscope
- Add app to settings.py INSTALLED_APP
- Add second application in project
  - ```$ python .\manage.py startapp news```
  - Add app to settings.py INSTALLED_APP
- Create migration script:
  - ```$ python .\manage.py makemigrations```
  - ```news\migrations\0001_initial.py```
- Run migration:
  - ```$ python .\manage.py migrate```