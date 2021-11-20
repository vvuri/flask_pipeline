import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from typing import Optional

app = FastAPI(title="Random phrase")


@app.get("/")
def read_root():
    return {"Hello": "World"}


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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)