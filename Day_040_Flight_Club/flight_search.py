# --- flight_search.py ---
# This file defines the FlightSearch class for interacting with the Tequila API.

import requests
from datetime import datetime, timedelta

# Tequila API Configuration
TEQUILA_API_KEY = "YOUR_TEQUILA_API_KEY"
TEQUILA_API_ENDPOINT = "https://api.tequila.kiwi.com"

# Class to hold flight data
class FlightData:
    def __init__(self, price, origin_city, origin_airport_code, destination_city, destination_airport_code, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport_code = origin_airport_code
        self.destination_city = destination_city
        self.destination_airport_code = destination_airport_code
        self.out_date = out_date
        self.return_date = return_date

class FlightSearch:
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_API_KEY
        }

    def get_iata_code(self, city_name):
        """
        Gets the IATA code for a given city name using Tequila's location search.
        """
        location_endpoint = f"{TEQUILA_API_ENDPOINT}/locations/query"
        query_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1
        }
        print(f"Looking up IATA code for {city_name}...")
        try:
            response = requests.get(url=location_endpoint, headers=self.headers, params=query_params)
            response.raise_for_status()
            data = response.json()["locations"]
            if data:
                return data[0]["code"]
            else:
                print(f"No IATA code found for {city_name}.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching IATA code for {city_name}: {e}")
            return None
        except KeyError:
            print(f"Error parsing IATA code response for {city_name}.")
            return None

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Searches for the cheapest flights between two cities within a date range.
        """
        search_endpoint = f"{TEQUILA_API_ENDPOINT}/v2/search"
        query_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7, # Minimum nights at destination
            "nights_in_dst_to": 28,  # Maximum nights at destination
            "flight_type": "round",
            "one_for_city": 1, # Only one flight per city
            "max_stopovers": 0, # Direct flights only
            "curr": "USD", # Currency
            "limit": 1 # Only get the cheapest flight
        }
        try:
            response = requests.get(url=search_endpoint, headers=self.headers, params=query_params)
            response.raise_for_status()
            data = response.json()["data"]

            if not data:
                # print(f"No direct flights found for {destination_city_code}.")
                return None

            # Get the first (cheapest) flight found
            flight_details = data[0]

            # Parse relevant flight data
            flight_data = FlightData(
                price=flight_details["price"],
                origin_city=flight_details["cityFrom"],
                origin_airport_code=flight_details["flyFrom"],
                destination_city=flight_details["cityTo"],
                destination_airport_code=flight_details["flyTo"],
                out_date=datetime.fromtimestamp(flight_details["route"][0]["dTime"]).strftime("%Y-%m-%d"),
                return_date=datetime.fromtimestamp(flight_details["route"][1]["aTime"]).strftime("%Y-%m-%d")
            )
            return flight_data
        except requests.exceptions.RequestException as e:
            print(f"Error searching flights for {destination_city_code}: {e}")
            return None
        except KeyError:
            # print(f"No flights found for {destination_city_code} in the specified range.")
            return None
