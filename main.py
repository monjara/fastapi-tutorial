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
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

