# Todos os import, incluso parte de classes comentadas
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

"""
# Codigo do primeiro tutorial
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {'Hello': 'World '}


@app.get("/items'/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
"""

# Codigos do Guia 'Primeiros Passos'

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Wold"}


@app.get("/items/{item_id}")
# async def read_tem(item_id):      # Pode ser usado qualquer valor, int, float strings
async def read_item(item_id: int):   # Somente tipos int "Validação de dados"
    return {"item_id": item_id}


@app.get("/users/me")                       # Ver usuario atual
async def read_user_me():
    return {"usuer_id:" "the current user"}


@app.get("/user/{user_id}")
async def read_user(user_id: str): # Permitir entrar com um usuario
    return {"user_id": user_id}

# Usa Enum para criar classes que herdam str de Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Enum é biblioteca padrão python > 3.5
@app.get("/models/{model_name}") # Cria classes que herdam str de Enum
async def get_model(model_name: ModelName): # Paramentro de caminho
    if model_name == ModelName.alexnet: # Compara membros de enumeração
        return {"model_name" : model_name, "message" : "Deep Learning FTW"} # Retorna menbros de Enum
    
    if model_name.value == "lenet": # Obtem o valor de Enum
        return {"model_name": model_name, "message": "LeCNN all the images"} # Retorna menbros de Enum
    
    return {"model_name": model_name, "message": "Have some residuals"} # Retorna menbros de Enum

# Usando conversor de caminhos em 'PATH'
# Usa função direta do starlette
@app.get("/files/{file_path:path}") 
async def read_file(file_path: str):
    return {"file_path": file_path}




