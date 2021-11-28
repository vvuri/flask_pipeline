from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from posts import post

import models
from database import SessionLocal, engine

app = FastAPI(title="Python WiKi blog")

templates = Jinja2Templates(directory="templates")

app.include_router(post.router)

models.Base.metadata.create_all(bind=engine)
