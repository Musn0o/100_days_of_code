import requests
from datetime import datetime

# --- Configuration ---

# Nutritionix API Credentials
# Get your App ID and API Key from https://www.nutritionix.com/business/api
NUTRITIONIX_APP_ID = "YOUR_NUTRITIONIX_APP_ID"
NUTRITIONIX_API_KEY = "YOUR_NUTRITIONIX_API_KEY"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API Endpoint for your Google Sheet
# Create a Google Sheet, then go to https://sheety.co/ to get your endpoint.
# Make sure your sheet has columns like 'date', 'time', 'exercise', 'duration', 'calories'.
SHEETY_ENDPOINT = "YOUR_SHEETY_ENDPOINT_URL" # e.g., "https://api.sheety.co/YOUR_USERNAME/YOUR_PROJECT_NAME/workouts"

# Sheety Basic Authentication (Optional, but recommended for security)
# Set these in Sheety when you create your endpoint.
SHEETY_USERNAME = "YOUR_SHEETY_USERNAME"
SHEETY_PASSWORD = "YOUR_SHEETY_PASSWORD"


# --- Nutritionix API Request ---

# Get exercise input from the user
exercise_text = input("Tell me which exercises you did: ")

# Headers for Nutritionix API request
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json" # Specify content type for POST request
}

# Request body for Nutritionix API
nutritionix_body = {
    "query": exercise_text,
    "gender": "male", # Customize as needed
    "weight_kg": 70, # Customize as needed
    "height_cm": 175, # Customize as needed
    "age": 30 # Customize as needed
}

print("Sending exercise data to Nutritionix...")
try:
    nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_body, headers=nutritionix_headers)
    nutritionix_response.raise_for_status() # Raise an exception for bad status codes
    exercise_data = nutritionix_response.json()
    print("Nutritionix API Response:")
    print(exercise_data) # Print the raw response for debugging/confirmation
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Nutritionix API: {e}")
    exit() # Exit if API call fails

# --- Sheety API Request ---

# Get current date and time
today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%H:%M:%S")

# Prepare data to be sent to Google Sheet via Sheety
# Iterate through each exercise parsed by Nutritionix
for exercise in exercise_data["exercises"]:
    sheety_body = {
        "workout": { # 'workout' matches the sheet name (or singular form of endpoint name)
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(), # Capitalize first letter
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Headers for Sheety API request (for basic authentication)
    # If your Sheety endpoint does not require authentication, you can remove this.
    sheety_headers = {
        "Authorization": f"Basic {requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD).encode().decode()}"
    }

    print(f"\nLogging '{exercise['name'].title()}' to Google Sheet...")
    try:
        # Send POST request to Sheety endpoint
        sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_headers)
        sheety_response.raise_for_status()
        print("Sheety API Response:")
        print(sheety_response.text) # Print Sheety's response
        print("Successfully logged workout to Google Sheet.")
    except requests.exceptions.RequestException as e:
        print(f"Error logging workout to Google Sheet via Sheety: {e}")
        print("Please check your Sheety endpoint URL, authentication, and Google Sheet column names.")

