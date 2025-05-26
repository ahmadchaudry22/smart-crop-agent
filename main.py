from agents.crop_advisor_agent import crop_advisor_agent

def main():
    print("🌾 Welcome to the Smart Crop Advisor Agent 🌾")
    print("This tool helps Pakistani farmers choose the best crop using real-time weather and soil data.\n")

    try:
        lat = float(input("📍 Enter your farm's Latitude (e.g., 30.1575): "))
        lon = float(input("📍 Enter your farm's Longitude (e.g., 71.5249): "))
    except ValueError:
        print("❌ Invalid input. Please enter valid numeric coordinates.")
        return

    print("\n🔍 Analyzing your location...\n")
    recommended_crop = crop_advisor_agent(lat, lon)

    print("\n🌱 Final Recommendation:")
    print(f"✅ You should consider planting **{recommended_crop}** based on your soil and upcoming weather.\n")

if __name__ == "__main__":
    main()
