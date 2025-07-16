# --- main.py ---
# This is the main script for Day 40 of the Flight Club Capstone Project.
# It orchestrates fetching data, searching for flights, and sending notifications.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# --- Configuration ---
# Your departure city IATA code (e.g., London's LON)
ORIGIN_CITY_IATA = "LON" # Assuming London as the departure city

# --- Initialize Managers ---
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# --- Step 1: Get Destination Data from Google Sheet ---
print("Fetching destination data from Google Sheet...")
sheet_data = data_manager.get_destination_data()

# --- Step 2: Update Missing IATA Codes in Google Sheet ---
# If any IATA codes are missing in the sheet, look them up using Tequila API
if sheet_data and sheet_data[0]["iataCode"] == "": # Check if the first entry has an empty IATA code
    print("IATA codes are missing for some destinations. Looking up...")
    for row in sheet_data:
        # Use FlightSearch to get the IATA code for the city name
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        # Update the Google Sheet with the newly found IATA code
        data_manager.update_destination_codes(row["id"], row["iataCode"])
    # Re-fetch the data to ensure we have the updated IATA codes
    sheet_data = data_manager.get_destination_data()
    print("All IATA codes updated in Google Sheet.")

# --- Step 3: Search for Flights ---
# Define the date range for flight search (e.g., from tomorrow to 6 months from now)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30)) # Approx 6 months

print("\nSearching for flights...")
for destination in sheet_data:
    print(f"Searching for flights to {destination['city']}...")
    # Search for flights using the FlightSearch class
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_now
    )

    # If a flight is found and its price is lower than the lowest price in the sheet
    if flight and flight.price < destination["lowestPrice"]:
        print(f"Low price found to {destination['city']}!")
        # Construct the message for SMS notification
        message = (
            f"Low price alert! Only ${flight.price} to {flight.destination_city}-"
            f"{flight.destination_airport_code} from {flight.origin_city}-"
            f"{flight.origin_airport_code}, from {flight.out_date} to {flight.return_date}."
        )
        # Send the SMS notification
        notification_manager.send_sms(message)
    else:
        print(f"No flight deal found for {destination['city']}.")