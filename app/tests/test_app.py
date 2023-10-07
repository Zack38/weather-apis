import json
import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client for your FastAPI app
client = TestClient(app)

print(client)
# Define the hostname of the linked API container
api_container_hostname = "weather-apis"

def test_read_root_v1():
    response = client.get(f"http://{api_container_hostname}:8000/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from API version 1 223423!"}

def test_get_weather():
    response = client.get(f"http://{api_container_hostname}:8000/v1/weather")
    assert response.status_code == 200
    # Add more specific assertions based on your expected data format

def test_get_weather_limit():
    response = client.get(f"http://{api_container_hostname}:8000/v1/weather-limit?limit=5")
    assert response.status_code == 200
    # Add more specific assertions based on your expected data format

def test_get_weather_by_date():
    response = client.get(f"http://{api_container_hostname}:8000/v1/weather-by-date?date=2022-06-04")
    assert response.status_code == 200
    # Add more specific assertions based on your expected data format

def test_get_weather_by_type():
    response = client.get(f"http://{api_container_hostname}:8000/v1/weather-by-type?weather=rain")
    assert response.status_code == 200
    # Add more specific assertions based on your expected data format

def test_get_weather_multi():
    response = client.get(f"http://{api_container_hostname}:8000/v1/weather-multi?limit=5&date=2022-06-04&weather=rain")
    assert response.status_code == 200
    # Add more specific assertions based on your expected data format
