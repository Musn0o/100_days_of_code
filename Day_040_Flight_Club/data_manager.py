# --- data_manager.py ---
# This file defines the DataManager class for interacting with Google Sheets via Sheety.

import requests
import os # Used for environment variables, though direct assignment is used here for simplicity
import base64

# Sheety API Endpoint for your Google Sheet
# Create a Google Sheet, then go to https://sheety.co/ to get your endpoint.
# Example: "https://api.sheety.co/YOUR_USERNAME/flightDeals/prices"
SHEETY_PRICES_ENDPOINT = "YOUR_SHEETY_PRICES_ENDPOINT_URL"

# Sheety Basic Authentication (Optional, but recommended for security)
# Set these in Sheety when you create your endpoint.
SHEETY_USERNAME = "YOUR_SHEETY_USERNAME"
SHEETY_PASSWORD = "YOUR_SHEETY_PASSWORD"

class DataManager:
    def __init__(self):
        # Headers for Sheety API requests, including Basic Authentication
        # If your Sheety endpoint does not require authentication, you can remove this.
        credentials = f"{SHEETY_USERNAME}:{SHEETY_PASSWORD}".encode("utf-8")
        b64_credentials = base64.b64encode(credentials).decode("utf-8")
        self.headers = {
            "Authorization": f"Basic {b64_credentials}"
        }
        self.destination_data = {} # To store data fetched from the sheet

    def get_destination_data(self):
        """Fetches all destination data from the Google Sheet via Sheety."""
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
            response.raise_for_status() # Raise an exception for bad status codes
            # The key 'prices' depends on your sheet name in Sheety.
            # If your sheet is named 'prices', the key will be 'prices'.
            # If your sheet is named 'Sheet1', it might be 'sheet1'.
            # Adjust this key based on your Sheety setup.
            self.destination_data = response.json()["prices"] # Assuming your sheet is named 'prices'
            return self.destination_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Sheety: {e}")
            print("Please check your SHEETY_PRICES_ENDPOINT, username, and password.")
            return None
        except KeyError:
            print("Error: 'prices' key not found in Sheety response. Check your sheet name in Sheety.")
            return None

    def update_destination_codes(self, object_id, iata_code):
        """
        Updates the IATA Code for a specific row in the Google Sheet.
        """
        update_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{object_id}"
        new_data = {
            "price": { # 'price' matches the singular form of your sheet name in Sheety
                "iataCode": iata_code
            }
        }
        print(f"Updating row {object_id} with IATA code {iata_code}...")
        try:
            response = requests.put(url=update_endpoint, json=new_data, headers=self.headers)
            response.raise_for_status()
            print(response.text)
            print("Successfully updated IATA code in Google Sheet.")
        except requests.exceptions.RequestException as e:
            print(f"Error updating IATA code in Sheety: {e}")
