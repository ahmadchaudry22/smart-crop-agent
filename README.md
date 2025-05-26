# 🌾 Smart Crop Advisory Agent

An AI-powered agent built with Agent Pro that suggests the best crop based on weather forecasts and soil data.

## Features
- Fetches 5-day weather forecast using OpenWeather API
- Pulls soil data from SoilGrids (ISRIC)
- Applies ML model to suggest optimal crop
- Ready to deploy for real farmers

## Setup
```bash
git clone https://github.com/ahmadchaudry22/smart-crop-agent
cd smart-crop-agent
pip install -r requirements.txt
python main.py
```

## Example Output
```
✅ Recommended Crop: Soybean
📊 Reason: Suitable pH and good rainfall expected
```
