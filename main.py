from agents.crop_advisor_agent import crop_advisor_agent

if __name__ == "__main__":
    lat = float(input("Enter Latitude: "))
    lon = float(input("Enter Longitude: "))
    crop_advisor_agent(lat, lon)
