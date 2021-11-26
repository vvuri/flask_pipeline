from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory=["posts/templates", "templates"])


@router.get('/posts', response_class=HTMLResponse)
def list_post(request: Request):
    return templates.TemplateResponse("posts.html", {"request": request})
