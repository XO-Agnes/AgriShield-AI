def get_irrigation_advice(data):
    if data.soil_moisture < 40 and data.rain_probability < 50:
        return {
            "recommendation": "Irrigate the field today",
            "confidence": 91,
            "reason": "Soil moisture is low and rainfall probability is low."
        }

    if data.soil_moisture >= 60 and data.rain_probability >= 70:
        return {
            "recommendation": "Delay irrigation",
            "confidence": 91,
            "reason": "Soil moisture is sufficient and rainfall probability is high."
        }

    return {
        "recommendation": "Monitor soil moisture before irrigating",
        "confidence": 78,
        "reason": "Current soil and weather conditions are moderate."
    }