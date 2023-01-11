#!/usr/bin/env python3
"""Author: Sergio Garcia"""

import requests
import datetime
import reverse_geocoder as rg


API_URL = "http://api.open-notify.org/iss-now.json"

def main():
    """Displays information about the ISS"""
    # Get data from API
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("Something went wrong")
        exit(1)

    data = response.json()
    if data["message"] != "success":
        print("Successful response, but no data")
        exit(1)

    # Successful response with meaning ful data; extract and transform.
    reading_date = datetime.datetime.fromtimestamp(data["timestamp"])
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    coordinates = (latitude, longitude)
    location = rg.search(coordinates, verbose=False)[0]

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {reading_date}")
    print(f"Lon: {longitude}\nLan: {latitude}")
    print(f"City/Country: {location['name']}, {location['cc']}")

if __name__ == '__main__':
    main()
