from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import FarmData
from .ai_service import get_irrigation_advice

app = FastAPI(title="AgriShield AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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