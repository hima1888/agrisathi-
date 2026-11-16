from fastapi import APIRouter

router = APIRouter()


@router.post("/recommendation")
def get_recommendation(
    temperature: float,
    humidity: float,
    soil_moisture: float
):
    recommendations = []

    if soil_moisture < 30:
        recommendations.append(
            "Soil moisture is low. Irrigation is recommended."
        )
    else:
        recommendations.append(
            "Soil moisture is sufficient. Irrigation is not required."
        )

    if temperature > 35:
        recommendations.append(
            "Temperature is high. Provide suitable crop protection."
        )

    if humidity > 80:
        recommendations.append(
            "Humidity is high. Monitor the crop for possible fungal problems."
        )

    if not recommendations:
        recommendations.append(
            "Environmental conditions are within the normal range."
        )

    return {
        "success": True,
        "environment": {
            "temperature": temperature,
            "humidity": humidity,
            "soil_moisture": soil_moisture
        },
        "recommendations": recommendations
    }