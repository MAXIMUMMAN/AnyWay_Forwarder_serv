import json
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_cities():
    with open('data.json') as cities:
        response = json.load(cities)
        return response[0:len(response)]


@app.get('/{num}')
async def get_city(num: int):
    with open('data.json') as cities:
        response = json.load(cities)
        return response[num]


@app.get('/{filt}/{f}')
async def get_city_filtered(sea_filt : int, moun_filt : int):
    with open('data.json') as cities:
        res = json.load(cities)
        res2 = list(filter(lambda x: (x["sea"] >= sea_filt) and (x["mountains"] >= moun_filt), res))
        return res2[0:len(res2)]
