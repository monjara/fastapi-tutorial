from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alex = 'alex'

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

@app.get('/model/{model_name}')
async def read_model(model_name: ModelName):
    if model_name == ModelName.alex:
        return {'model_name': model_name}

@app.get('/file/{file_path:path}')
async def read_fiel(file_path: str):
    return {'file_path': file_path}

