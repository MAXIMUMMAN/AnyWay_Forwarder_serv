import json
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_cities():
    with open('data.json') as cities:
        response = json.load(cities)
        return {"data": response[0:len(response)]}


@app.get('/id')
async def get_city(num: int):
    with open('data.json') as cities:
        response = json.load(cities)
        return {"data": response[num]}


@app.get('/filters')
async def get_city_filtered(filters):
    with open('data.json') as cities:
        res = json.load(cities)
        fil = json.loads(filters)
        res2 = list(filter(lambda x: filter_func(x, fil), res))
        return {"data": res2[0:len(res2)]}


def filter_func(x, filters):
    for i in filters.keys():
        if x["filters"][i] < filters[i]:
            return False
    return True
