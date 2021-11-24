from random import random

import uvicorn
from fastapi import FastAPI, Body
from fastapi import HTTPException
from typing import Optional

from flask import jsonify
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse


app = FastAPI(title="Random phrase")

# опционально; требуется при обслуживании статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# опционально; требуется при обслуживании страницы через шаблонизатор
templates = Jinja2Templates(directory="templates")


# зависит от варианта использования
class Item(BaseModel):
    language = 'english'


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
@app.get("/", response_class=PlainTextResponse)  # По умолчанию возвращается ответ в формате JSON, тут меняем
async def hello():         # async не обязателен но лучше сразу так
    return "Hello World!"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q}


@app.get(
    "/get",
    response_description="Random phrase",
    description="Get random phrase from database"
)
async def get():
    try:
        phrase = "Simple response"
    except IndexError:
        raise HTTPException(404, "Phrase list is empty")
    return phrase


@app.get('/random-number', response_class=PlainTextResponse)
async def random_number():
    return str(random.randrange(100))


@app.get('/alpha')
async def alpha(text: str):
    result = {'text': text, 'is_alpha': text.isalpha()}
    return result


@app.route('/create-user', methods=['POST'])
def create_user():
    id = request.form.get('id', '0001')
    name = request.form.get('name', 'Anonymous')
    # код для аутентификации, валидации, обновления базы данных
    data = {'id': id, 'name': name}
    result = {'status_code': '0', 'status_message': 'Success', 'data': data}
    return jsonify(result)


# Обновление языка
@app.put('/update-language', response_class=PlainTextResponse)
async def update_language(item: Item):
    language = item.language
    return "Successfully updated language to %s" % (language)


class Number(BaseModel):
    value: int


class Response(BaseModel):
    code: int
    message: str
    result: bool


odd_examples = {
    "odd": {
        "summary": "Odd number",
        "value": {
            "value": 1111
        }
    },
    "even": {
        "summary": "Even number",
        "value": {
            "value": 322
        }
    },
    "alphabet": {
        "summary": "Example using alphabet",
        "description": "Using invalid, non-number input. Will raise `Error: Unprocessable Entity` message.",
        "value": {
            "value": "abc"
        }
    },
}

odd_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "odd": {
                        "summary": "Odd Number",
                        "value": {"code": 0, "message": "Success", "result": True}
                    },
                    "even": {
                        "summary": "Even Number",
                        "value": {"code": 0, "message": "Success", "result": False}
                    },
                }
            }
        }
    },
}


@app.post("/odd", response_model=Response, responses=odd_responses)
def odd(number: Number = Body(..., examples=odd_examples)):
    return Response(code=200, message="Success", result=number.value % 2)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)