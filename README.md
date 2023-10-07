# My FastAPI Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)

Description of your project goes here.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Installation
Describe how to set up and install your project locally. Include any dependencies and environment setup steps.

```bash

# make sure you have docker and git installed on your computer

# Clone the repository
git clone https://github.com/Zack38/weather-apis.git

# Change into the project directory
cd weather-apis

# Once docker in running run the docker compose command
docker compose up --build

# This will build the project and run the tests. Go to localhost to test apis in browser

http://127.0.0.1:8000/docs 
```

# Project Structure
```
weather-apis/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── conftest.py
│   ├── requirements.txt
│   ├── seattle-weather.csv
│   ├── api/
│   │   ├── __init__.py
│   │   ├── weather.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── pytest.ini
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── README.md
├── .dockerignore
├── .gitignore
```

