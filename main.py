from fastapi import FastAPI
import sentencepiece as tokenizer
import glob
import os
from pydantic import BaseModel
from typing import List

model = None
app = FastAPI()



class Text(BaseModel):
    message: str

class EncodeText(BaseModel):
    message: List[int]

# Encoding Hello World
@app.get("/")
async def root():
    global model
    hello_world = model.encode("Hello World")
    return {"message": hello_world}

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

if __name__ == "__main__":
    # Check if there is file with .model or .srl extension  in ./models/
    print("##### Checking for model #####")
    if not os.path.exists("./models/tokenizer.model"):
        print("There is no model in folder./models/\nPlease you have to train the model or download a model")
        print("😩 \033[1;31mNo model in folder ./models/\033[0m 😩")
        exit(1)
    print("🤗 \033[1;32mModel found\033[0m 🤗")

    # Loading the model
    print("##### Loading model #####")
    model = tokenizer.SentencePieceProcessor(model_file='models/tokenizer.model')
    print("✅ \033[1;32mModel loaded\033[0m ✅")


    # Strating the FastAPI
    print("##### Strating FastAPI #####")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)









