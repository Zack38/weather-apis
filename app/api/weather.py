from fastapi import APIRouter, Query
import pandas as pd
import json

router = APIRouter()

# This is a get for testing apis
@router.get("/")
async def read_root_v1():
    return {"message": "Hello from API version 1 223423!"}

# api that gets all weather data
@router.get("/weather")
async def get_weather():
    
    weatherData = pd.read_csv('seattle-weather.csv', sep=',')
    

    jsonOutput = weatherData.to_json(orient='records', date_format='epoch')
    return json.loads(jsonOutput)

# api that gets all weather by limits the results
@router.get("/weather-limit")
async def get_weather(limit: int = Query(default=10, description="Limit the number of results", ge=1)):
    
    weatherData = pd.read_csv('seattle-weather.csv', sep=',')
    

    jsonOutput = weatherData.to_json(orient='records', date_format='epoch')
    if(limit == 0):
        limit = len(jsonOutput)

    jsonOutput = json.loads(jsonOutput)
    jsonOutput = jsonOutput[:limit]
    
    return jsonOutput

# api that gets all weather by a certain date
@router.get("/weather-by-date")
async def get_weather(date: str = Query(None, description="Filter by date in yyyy-mm-dd format")):
    
    weatherData = pd.read_csv('seattle-weather.csv', sep=',')
    
    jsonOutput = weatherData.to_json(orient='records', date_format='epoch')
    jsonOutput = json.loads(jsonOutput)

    if date:
        jsonOutput = [item for item in jsonOutput if item["date"] == date]

    return jsonOutput

# api that gets all weather by a certain type (e.g = rain)
@router.get("/weather-by-type")
async def get_weather(weather: str = Query(None, description="Filter by weather type")):
    
    weatherData = pd.read_csv('seattle-weather.csv', sep=',')

    jsonOutput = weatherData.to_json(orient='records', date_format='epoch')
    jsonOutput = json.loads(jsonOutput)

    if weather:
        jsonOutput = [item for item in jsonOutput if item["weather"] == weather]

    return jsonOutput

# api that gets all weather but can limit results by a certain number, type & date
@router.get("/weather-multi")
async def get_weather(
    limit: int = Query(default=0, description="Limit the number of results", ge=1),
    date: str = Query(None, description="Filter by date in yyyy-mm-dd format"),
    weather: str = Query(None, description="Filter by weather type")):
    
    weatherData = pd.read_csv('seattle-weather.csv', sep=',')
    
    jsonOutput = weatherData.to_json(orient='records', date_format='epoch')
    jsonOutput = json.loads(jsonOutput)

    if(limit == 0):
        limit = len(jsonOutput)

    if weather:
        jsonOutput = [item for item in jsonOutput if item["weather"] == weather]

    if date:
        jsonOutput = [item for item in jsonOutput if item["date"] == date]

    
    jsonOutput = jsonOutput[:limit]

    return jsonOutput


