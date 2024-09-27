from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World  "+API_KEY}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
