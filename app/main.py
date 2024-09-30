import json
from typing import Dict, Optional

from fastapi import FastAPI, Request

from .services import get_customers_service, post_customers_service, get_orders_service, post_orders_service
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World  "}


@app.get("/customers")
async def get_customers(request: Request):
    query_params = dict(request.query_params)
    response = await get_customers_service(query_params)
    return response

@app.post("/customers")
async def create_customer(data: Dict):
    json_data = json.dumps(data)
    response = await post_customers_service(json_data)
    return response

@app.get("/orders/{id}")
async def get_orders(id:str):
    response = await get_orders_service(id)
    return response

@app.post("/orders")
async def create_order(data: Dict):
    json_data = json.dumps(data)
    response = await post_orders_service(json_data)
    return response