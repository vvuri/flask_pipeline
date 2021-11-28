from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from posts import post

app = FastAPI(title="Python WiKi blog")

templates = Jinja2Templates(directory="templates")

app.include_router(post.router)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# db = SQLAlchemy(app)
