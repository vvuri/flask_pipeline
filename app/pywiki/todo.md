##PyWiki 

Простое приложение полного цикла.
- серия статей по Python
- админка для добавления и редактирования статей
- основная форма для отображения текущих материалов
- поисковый движок
- markdown разметка для статей
- тесты API
- тесты UI
- CI run test в gitlab

#### Технологии:
- FastAPI + Swagger documentation
- PostgreSQL + Migration
- SQLAlchemy
- Terraform for deployment
- [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) 
- Linter: 
- PyTest

#### Steps
1. FastAPI ```pip install fastapi```
2. Uvicorn ```pip install "uvicorn[standard]"```
3. Debug mode ```uvicorn app.pywiki.app:app --host 0.0.0.0 --reload --port 80 --debug```
4. Templates ```pip install jinja2```
5. Swagger ```http://127.0.0.1/docs```
6. 
