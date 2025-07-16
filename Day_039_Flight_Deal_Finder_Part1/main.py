# --- main.py ---
# This is the main script for Day 39 of the Flight Deal Finder Capstone Project.
# It demonstrates fetching data from Google Sheets via Sheety.

from data_manager import DataManager

# Create an instance of the DataManager
data_manager = DataManager()

# Get the destination data from Google Sheet
sheet_data = data_manager.get_destination_data()

print("Fetching data from Google Sheet...")
print("Successfully fetched data:")
print(sheet_data)

# In Day 39, the primary goal is to fetch the data.
# In Day 40, you would typically add logic here to:
# 1. Check if IATA codes are missing for any city.
# 2. Use a flight search API (like Tequila) to get the IATA codes.
# 3. Update the Google Sheet with the missing IATA codes using data_manager.update_destination_codes().

# Example of how you might check for missing IATA codes (for Day 40 preparation):
# if sheet_data[0]["iataCode"] == "": # Check if the first city has an empty IATA code
#     from flight_search import FlightSearch # Assuming FlightSearch class exists in Day 40
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         # In a real scenario, you'd call a method to get IATA code for row["city"]
#         # For now, just print a placeholder
#         print(f"IATA code for {row['city']} is missing. Would look it up.")
#         # Example: row["iataCode"] = flight_search.get_iata_code(row["city"])
#         # data_manager.update_destination_codes(row["id"], row["iataCode"])


