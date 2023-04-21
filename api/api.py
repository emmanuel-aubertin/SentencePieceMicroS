from fastapi import FastAPI
import glob
import os
from pydantic import BaseModel
from typing import List
from main import model
app = FastAPI()


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
async def encode_api(text: Text):
    global model
    return {"message": model.encode(text.message)}

# Encoding with arg
@app.post("/decode")
async def decode_api(encode_text: EncodeText):
    global model
    return {"message": model.decode(encode_text.message)}
