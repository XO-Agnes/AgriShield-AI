from pydantic import BaseModel

class FarmData(BaseModel):
    crop: str
    soil_moisture: float
    temperature: float
    rain_probability: float