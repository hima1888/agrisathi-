from fastapi import FastAPI

from routes.prediction import router as prediction_router
from routes.environment import router as environment_router
from routes.recommendation import router as recommendation_router


app = FastAPI(
    title="Smart Farming Backend",
    description="Backend API for Agriculture and Smart Farming",
    version="1.0"
)


app.include_router(
    prediction_router,
    prefix="/api"
)

app.include_router(
    environment_router,
    prefix="/api"
)

app.include_router(
    recommendation_router,
    prefix="/api"
)


@app.get("/")
def home():
    return {
        "message": "Smart Farming Backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
