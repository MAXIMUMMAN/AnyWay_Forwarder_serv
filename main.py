import json
from fastapi import FastAPI

app = FastAPI()


@app.get(
    '/',
)
async def get_cities():
    with open('data.json') as cities:
        response = json.load(cities)
        return response[0:len(response)]
