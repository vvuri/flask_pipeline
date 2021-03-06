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
  - Show SQL command:
  - ```$ python manage.py sqlmigrate news 0003``` -> "CREATE TABLE news_news ..." 
- Run migration:
  - ```$ python .\manage.py migrate```
- For debug SQL:
  - ```$ python manage.py shell```
  - ```>>> from news.models import Movies```
  - ```>>> a = Movies(name="Film1", rating = 10)```
  - ```>>> a.save()``` save to DB or update
  - ```>>> a.delete()``` return record 
  - ```>>> Movies.object.create(name="Film1", rating = 10) ``` alternative method with save
  - ```>>> Movies.objects.all()``` -> use \_\_str__ method
  - ```>>> Movies.objects.all()[1].name``` select from table to collection
  - ```>>> Movies.objects.get(id=1).name``` select by id
  - ```>>> from django.db import connection```
  - ```>>> connection.queries``` show SQL query
  - ```>>> Movies.objects.filter(name='Film')``` -> LIKE
  - object.order_by('field') or '-field'
  - exclude(name='5') - without this
- Plugin for show SQL
  - ```$ pip install django-extensions```
  - ```$ python manage.py shell_plus --print-sql``` Not work for me
- Add Admin panel - for control DB data
  - ```$ python manage.py createsuperuser```
  - user: admin, password: admin
  - http://127.0.0.1:8000/admin/
  - add support DB Movies: ```admin.site.register(Movies)``` in admin.py
- Add templates for news
  - http://127.0.0.1:8000/movies/
- for file upload:
  - ```$ pip install pillow``` 
- Add React frontend
  - Update nodejs https://nodejs.org/en/download/ -> v16.13.2
  - ```$ cd .\app\django_first\``` 
  - ```$ npx create-react-app frontend```
  - Run app: ```$ npm start``` -> http://localhost:3000/
  - Add Bootstrap 4
- Add CORS
  - ```pip install djangorestframework django-cors-headers```
  - configure settings.py
- Work with admin
  - Add Meta class
  - method for rename fields in admin
  - add migration
  - admin.py, apps.py, models.py
- ```$  flake8 app/django_first --exclude app/django_first/frontend```
- Run test - unittest 
  - ```$ python .\manage.py test .``` 
- Coverage
  - ```$ pip install coverage```
  - ```$ coverage run --source='.' ./manage.py test .```
  - ```$ coverage report``` - in cli
  - ```$ coverage html``` - as web page with show tested function
- [Lorem Ipsum](https://ru.lipsum.com/) - is simply dummy text 
- Lorem [photo](https://picsum.photos/)
- [Bootstrap](https://getbootstrap.com/docs/5.1/components/navbar/) Navbar, Card
- Debug tool ```$ pip install django-debug-toolbar``` 
- [Debug documentation Install](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- Color schema from https://materializecss.com/color.html - brown for admin 

### Developer env
- ```python .\manage.py runserver```
- ```cd .\app\django_first\```  
- ```npm start```

### GitHub Actions
- create dir .github/workflow
- add test.yml with scenario linting
- run only when code changed

### Deploy on VDS
- SSH connect 
- ```git clone ...```
- ```sudo apt update```
- ```sudo apt install ... ```
- ...
- ```python manage.py collectstatic``` for create static from templates

### SSL
- self-signed certificate
- OpenSSL 1.1.1f for create
- ```$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt```
- ```$ vim /etc/nginx/sites-available/default```
  - listen 80; 
  - server_name 195.234.208.54;  
  - charset utf-8;
  - listen 443 ssl http2; 
  - listen [::]:443 ssl http2;
  - ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
  - ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
- ```$ service nginx restart```

### ToDo
1. Django - all course I part
   1. 16 + 
   2. part II
   3. Bootstrap
2. PostgreSQL - install + connect
   1. dumpdate + loaddata for move data to server
   2. add backup to crontab
3. Add Grafana and Prometheus to admin
   1. metrics
   2. UI add to admin
4. Auth - some variant
5. Add test - Unit, API, Selenium + add in GitHub CI
6. Add React Frontend
7. Terraform deployment 
8. SSL by soft + vvuri.ru redirect
9. Add telegram bot for connection
10. Slides to UI module
11. Add FastAPI module and nginx 
12. CI/CD - [Run Django Tests with DB](https://blog.healthchecks.io/2020/11/using-github-actions-to-run-django-tests/)
13. GraphQL - [example](https://proglib.io/p/polnyy-fullstek-pishem-sayt-na-django-vue-i-graphql-2021-07-22)
14. 