from fastapi import FastAPI
from .models import FarmData
from .ai_service import get_irrigation_advice

app = FastAPI(title="AgriShield AI")

@app.get("/")
def home():
    return {"message": "AgriShield AI Backend is running"}

@app.post("/api/advisory")
def get_advisory(data: FarmData):
    result = get_irrigation_advice(data)

    return {
        "crop": data.crop,
        **result
    }