import asyncio
import os
from typing import Optional, Dict

from dotenv import load_dotenv
import httpx

load_dotenv()
api_key = os.getenv("API_KEY")
subdomain = os.getenv("YOUR_SUBDOMAIN")
version = os.getenv("VERSION")

base_url = base_url = f"https://{subdomain}.retailcrm.ru/api/{version}/"


async def get_customers(client, url, params):
    response = await client.get(url, params=params)
    return response.json()


async def get_customers_service(query_params: Optional[Dict[str, str]] = None):
    async with httpx.AsyncClient() as client:
        tasks = []
        endpoint = "customers"
        url = f"{base_url}{endpoint}"
        params = {
            "apiKey": api_key
        }
        if query_params:
            query_params.update(params)
        else:
            query_params = params
        tasks.append(asyncio.create_task(get_customers(client, url, query_params)))
        responses = await asyncio.gather(*tasks)
        return responses


async def post_customers(client, url, params, json):
    response = await client.post(url, params=params, json=json)
    return response.json()


async def post_customers_service(json):
    async with httpx.AsyncClient() as client:
        tasks = []
        endpoint = "customers/create"
        url = f"{base_url}{endpoint}"
        params = {
            "apiKey": api_key
        }
        tasks.append(asyncio.create_task(post_customers(client, url, params, json)))
        responses = await asyncio.gather(*tasks)
        return responses


async def get_orders(client, url, params):
    response = await client.get(url, params=params)
    return response.json()


async def get_orders_service(id):
    async with httpx.AsyncClient() as client:
        tasks = []
        endpoint = "orders"
        url = f"{base_url}{endpoint}"
        params = {
            "apiKey": api_key,
            "filter[customerId]": id
        }
        tasks.append(asyncio.create_task(get_orders(client, url, params, )))
        responses = await asyncio.gather(*tasks)
        return responses


async def post_orders(client, url, params, json):
    response = await client.get(url, params=params, json=json)
    return response.json()


async def post_orders_service(json):
    async with httpx.AsyncClient() as client:
        tasks = []
        endpoint = "orders/create"
        url = f"{base_url}{endpoint}"
        params = {
            "apiKey": api_key
        }
        tasks.append(asyncio.create_task(post_orders(client, url, params, json)))
        responses = await asyncio.gather(*tasks)
        return responses
