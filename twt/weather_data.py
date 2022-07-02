import requests
import json

def weather(location: str=None):
    url = "https://wttr.in/{}?format=j1".format(location)
    response = requests.get(url, timeout=10)

    try:
        data = response.json() 
    except ValueError:
        data = {}

    return data

