from typing import Union
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alex = 'alex'

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
