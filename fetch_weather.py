import urllib.request
import json

def fetch_weather():
    try:
        # IP-based weather request format=j1
        url = "https://wttr.in/?format=j1"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            current = data["current_condition"][0]
            temp = current["temp_C"]
            desc = current["weatherDesc"][0]["value"]
            precip = current["precipMM"]
            
            # Extract detected location name if available
            try:
                area = data["nearest_area"][0]
                city = area["areaName"][0]["value"]
                country = area["country"][0]["value"]
                location_name = f"{city}, {country}"
            except:
                location_name = "Detected Location"

            weather_summary = {
                "temp": temp,
                "desc": desc,
                "precip": precip,
                "location": location_name,
                "fetched_at": current["observation_time"]
            }
            with open("/dashboard-yannis/weather.json", "w") as f:
                json.dump(weather_summary, f, indent=2)
            print(f"Successfully updated weather.json for detected location: {location_name}")
    except Exception as e:
        print(f"Error fetching IP-based weather: {e}")
        # Default fallback
        fallback = {
            "temp": "22",
            "desc": "Fair",
            "precip": "0.0",
            "location": "IP-Detected Location",
            "fetched_at": "12:00 PM"
        }
        with open("/dashboard-yannis/weather.json", "w") as f:
            json.dump(fallback, f, indent=2)

if __name__ == "__main__":
    fetch_weather()
