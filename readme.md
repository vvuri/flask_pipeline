## Python pipeline

Simple APi project

#### Steps
1. PyCharm - new project
2. Shift+F10 for Run
3. ```pip install flask```
4. Simple Flask server
``` set FLASK_APP=hello | flask run ```
5. ```python.exe -m pip install --upgrade pip```
6. venv activate Windows
``` .\venv\Scripts\activate.bat```
7. add pytest
```pip install pytest```
8. create requirements.txt
```pip freeze > requirements.txt```
9. Run pytest with param: --no-header --no-summary -q
10. Add code analyse 
```
pip install flake8
flake8 --help
flake8 .\app\hello.py
```
11. Add DB connector SQL Alchemy ``` pip install flask-sqlalchemy ```
12. Add module for SQL Alchemy ``` pip install psycopg2-binary ```
13. psycopg2 didn't work on Python 3.10 -> go to 3.8
14. In new Env ``` pip install -r requirements.txt ```
15. ``` pip install flask-login```
16. Swagger ``` pip install flask-restful-swagger ``` - don't work for me
17. Swagger ```pip install flask-swagger``` - only json
18. CORS ``` pip install -U flask-cors ``` + CORS(app) - it's all
19. Swagger 
``` 
pip install flask-marshmallow 
pip install flask-restplus
pip install marshmallow-sqlalchemy
```
needed fix for 'werkzeug' 
20. Add google sheets support 
```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
21. Go to 'https://console.cloud.google.com/' -> API and services -> Credentials -> Create Credentials 
22. 'Google Sheets API' -> Enable ->  
23. Alternative - FastAPI 
```
pip install fastapi
pip install "uvicorn[standard]"
```
24. Run server ```$ uvicorn main:app``` - ASGI (Asynchronous Server Gateway Interface)
25. Swagger: http://127.0.0.1:8000/docs
26. ReDoc: http://127.0.0.1:8000/redoc

### Links
- [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/templates/|Jinja2)
- [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
- [DB connector SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
- [Flask login](https://flask-login.readthedocs.io/en/latest/)
- [CORS](https://flask-cors.readthedocs.io/en/latest/)
- [Swagger]() 
- [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)