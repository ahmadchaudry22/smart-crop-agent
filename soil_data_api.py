import requests

def get_soil_data(lat, lon):
    url = f"https://rest.soilgrids.org/query?lon={lon}&lat={lat}"
    res = requests.get(url).json()
    return {
        "ph": res["properties"]["phh2o"]["mean"],
        "organic_carbon": res["properties"]["ocd"]["mean"],
        "texture": res["properties"]["texture"]["mean"]
    }
