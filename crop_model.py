# Dummy ML model logic
def recommend_crop(soil_data, weather_data):
    if soil_data["ph"] > 6.5 and weather_data[0]['main']['temp'] > 20:
        return "Soybean"
    else:
        return "Maize"
