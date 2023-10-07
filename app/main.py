from fastapi import FastAPI
from api.weather import router as v1_router


app = FastAPI()

# Include API routes from different versions
app.include_router(v1_router, prefix="/v1")
