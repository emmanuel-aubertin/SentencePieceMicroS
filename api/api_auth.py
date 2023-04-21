from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer
import glob
import os
from pydantic import BaseModel
from typing import List
from main import model

app = FastAPI()
token_auth_scheme = HTTPBearer()
model = None

def set_model(in_model):
    global model
    model = in_model

def load_auth(type):
    if type == 'auth0':
        from auth0.auth0 import tokenValidator
        return True
    return False

class Text(BaseModel):
    message: str

class EncodeText(BaseModel):
    message: List[int]

# Encoding Hello World
@app.get("/")
async def root():
    global model
    return {"message": model.encode("Welcome at SentencePieceMicroS")}

# Encoding with arg
@app.post("/encode")
async def encode_api(text: Text, response: Response, token: str = Depends(token_auth_scheme)):
    global model
    return {"message": model.encode(text.message)}

# Encoding with arg
@app.post("/decode")
async def decode_api(encode_text: EncodeText, response: Response, token: str = Depends(token_auth_scheme)):
    global model
    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return {"message": model.decode(encode_text.message)}
