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
- Linter: flake8
- PyTest

#### Steps
1. FastAPI ```pip install fastapi```
2. Uvicorn ```pip install "uvicorn[standard]"```
3. Debug mode ```uvicorn app.pywiki.app:app --host 0.0.0.0 --reload --port 80 --debug```
4. Templates ```pip install jinja2```
5. Swagger ```http://127.0.0.1/docs```
6. Linter ```flake8 .\app\pywiki\```
7. Color schema from [Color Hunt](https://colorhunt.co/palette/009dae71dfe7c2fff9ffe652)
8. Color: #009DAE #71DFE7 #C2FFF9 #FFE652
9. Img [Logo](https://www.designevo.com/apps/logo/?name=abstract-human-face-and-vr-glasses)
10. Download SQLite3 [bin Windows](https://www.sqlite.org/) unpack and add Path
11. Download [SQLiteStudio](https://sqlitestudio.pl/)
12. Add Alembic DB Migration ```pip install alembic```
13. Init Alembic ```app\pywiki> alembic init alembic```
14. Configure alembic.ini -> sqlalchemy.url
15. Configure alembic/env.py -> target_metadata
16. Create first migration ```alembic revision --message="Initial" --autogenerate```
17. Create SQL script ```alembic upgrade 995153f9b9f3 --sql```
18. Run migration ```alembic upgrade head``` -> Running upgrade  -> 995153f9b9f3, Initial
19. New migration ```alembic revision --message="Slugify" --autogenerate```
20. Run new migration ```alembic upgrade cc92188f32a1``` - slugify 
21. Hook for SQLite only in env.py  ```render_as_batch=True``` but no work for me  
22. History migration ```alembic history ```
23. Rollback to base DB ```alembic downgrade base```


#### ToDo
- favicon
- static images
- markdown
- about text
- menu - change active