from utils import deg_to_arrow, phase_to_emoji

def parse_current(results: dict, metric: bool):
    # TODO move parsing directly to 'return' section
    current = results["current_condition"][0]
    area = results["nearest_area"][0]["areaName"][0]["value"]
    region = results["nearest_area"][0]["region"][0]["value"]
    if not region: 
        region = results["nearest_area"][0]["country"][0]["value"]
    country = results["nearest_area"][0]["country"][0]["value"]
    description = current["weatherDesc"][0]["value"]
    windpoint = current["winddir16Point"]
    winddeg = deg_to_arrow(int(current["winddirDegree"]))
    humidity = current["humidity"]


    if metric:
        temperature = current["temp_C"]
        windspeed = round(float(current["windspeedKmph"])*0.5399)
        percipitation = current["precipMM"]
        visibility = current["visibility"]
    else:
        temperature = current["temp_F"]
        windspeed = current["windspeedMiles"]
        percipitation = current["precipInches"]
        visibility = current["visibilityMiles"]


    return {
            "area": area, 
            "region": region,
            "country": country,
            "description": description, 
            "temperature": temperature, 
            "winddeg": winddeg, 
            "windpoint": windpoint, 
            "windspeed": windspeed, 
            "precipitation": percipitation, 
            "humidity": humidity, 
            "visibility": visibility
           }


def parse_astronomy(results: dict):
    astronomy = results["weather"][0]["astronomy"][0]
    area = results["nearest_area"][0]["areaName"][0]["value"]
    region = results["nearest_area"][0]["region"][0]["value"]
    illumination = astronomy["moon_illumination"]
    phase = astronomy["moon_phase"]
    phase_emoji = phase_to_emoji(phase)
    moonrise = astronomy["moonrise"]
    moonset = astronomy["moonset"]
    sunrise = astronomy["sunrise"]
    sunset = astronomy["sunset"]
    date = results["weather"][0]["date"]

    return {
            "area": area,
            "region": region,
            "illumination": illumination,
            "phase": phase,
            "phase_emoji": phase_emoji,
            "moonrise": moonrise,
            "moonset": moonset,
            "sunrise": sunrise,
            "sunset": sunset,
            "date": date
    }
