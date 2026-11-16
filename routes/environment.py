from fastapi import APIRouter

router = APIRouter()


@router.post("/environment")
def receive_environment_data(
    temperature: float,
    humidity: float,
    soil_moisture: float
):
    irrigation_required = soil_moisture < 30

    return {
        "success": True,
        "environment": {
            "temperature": temperature,
            "humidity": humidity,
            "soil_moisture": soil_moisture
        },
        "irrigation_required": irrigation_required
    }