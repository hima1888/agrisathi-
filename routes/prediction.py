
from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
import io

router = APIRouter()


@router.post("/predict-disease")
async def predict_disease(
    image: UploadFile = File(...),
    temperature: float = Form(...),
    humidity: float = Form(...),
    soil_moisture: float = Form(...)
):

    image_data = await image.read()

    try:
        img = Image.open(io.BytesIO(image_data))
        img.verify()
    except Exception:
        return {
            "success": False,
            "message": "Invalid image file"
        }

    # Temporary prediction
    # We will connect your trained AI model here later.

    disease = "Healthy"
    confidence = 0.95

    return {
        "success": True,
        "prediction": {
            "disease": disease,
            "confidence": confidence
        },
        "environment": {
            "temperature": temperature,
            "humidity": humidity,
            "soil_moisture": soil_moisture
        }
    }