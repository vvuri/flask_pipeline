from fastapi import Request
from app import app, templates
from fastapi.responses import PlainTextResponse, HTMLResponse


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    date = "12:10"
    return templates.TemplateResponse("index.html", {"request": request, "date": date})
