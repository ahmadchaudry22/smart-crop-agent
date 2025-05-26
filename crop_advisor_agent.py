from tools.weather_api import get_weather_forecast
from tools.soil_data_api import get_soil_data
from tools.crop_model import recommend_crop

def crop_advisor_agent(lat, lon):
    print("📡 Fetching weather forecast...")
    weather_data = get_weather_forecast(lat, lon)

    print("🌱 Getting soil data...")
    soil_data = get_soil_data(lat, lon)

    print("🧠 Running crop recommendation model...")
    crop = recommend_crop(soil_data, weather_data)

    print("\n✅ Recommended Crop: ", crop)
    print("📊 Reason: Suitable temp & soil pH")
    return crop
