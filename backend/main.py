from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AgriShield AI")

class FarmData(BaseModel):
    crop: str
    soil_moisture: float
    temperature: float
    rain_probability: float

@app.get("/")
def home():
    return {"message": "AgriShield AI Backend is running"}

@app.post("/api/advisory")
def get_advisory(data: FarmData):
    if data.soil_moisture < 40 and data.rain_probability < 50:
        recommendation = "Irrigate the field today"
        reason = "Soil moisture is low and rainfall probability is low."
    elif data.soil_moisture >= 60 and data.rain_probability >= 70:
        recommendation = "Delay irrigation"
        reason = "Soil moisture is sufficient and rainfall probability is high."
    else:
        recommendation = "Monitor soil moisture before irrigating"
        reason = "Current soil and weather conditions are moderate."

    return {
        "crop": data.crop,
        "recommendation": recommendation,
        "confidence": 91,
        "reason": reason
    }