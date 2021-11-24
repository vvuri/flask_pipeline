from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Python WiKi blog")

templates = Jinja2Templates(directory="templates")
