import requests
# The Twilio library is used to send SMS messages.
# Install it using: pip install twilio
from twilio.rest import Client

# --- Configuration ---
# Your OpenWeatherMap API Key.
# Get this from https://openweathermap.org/api
OWM_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Coordinates for the location you want to check (e.g., London)
# You can find coordinates using online tools or other APIs.
MY_LAT = 51.507351 # Latitude
MY_LON = -0.127758 # Longitude

# Twilio Account SID and Auth Token.
# Get these from your Twilio console: https://www.twilio.com/console
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Replace with your Account SID
TWILIO_AUTH_TOKEN = "your_auth_token_here" # Replace with your Auth Token

# Your Twilio phone number (the one you got from Twilio).
TWILIO_PHONE_NUMBER = "+1234567890" # Replace with your Twilio phone number

# Your personal phone number to receive the SMS alerts.
MY_PHONE_NUMBER = "+19876543210" # Replace with your actual phone number

# OpenWeatherMap One Call API endpoint
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

# Parameters for the API request
# 'lat' and 'lon' are for coordinates.
# 'exclude' is to exclude parts of the response we don't need (current, minutely, daily alerts).
# 'appid' is your API key.
params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": OWM_API_KEY,
}

# --- Fetch Weather Data ---
print("Checking weather for rain...")
try:
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(OWM_ENDPOINT, params=params)
    # Raise an exception for bad status codes (e.g., 401, 404, 500)
    response.raise_for_status()
    # Parse the JSON response
    weather_data = response.json()

    # --- Check for Rain in Next 12 Hours ---
    # The 'hourly' data provides a forecast for the next 48 hours.
    # We only need the first 12 hours (indices 0 to 11).
    will_rain = False
    # Iterate through the weather data for the next 12 hours
    for hour_data in weather_data["hourly"][:12]:
        # 'weather' is a list of weather conditions. We take the first one.
        # 'id' is the weather condition ID. IDs below 700 typically indicate rain/snow/thunderstorm.
        condition_code = hour_data["weather"][0]["id"]
        if condition_code < 700: # OpenWeatherMap weather codes for rain, snow, thunderstorms etc.
            will_rain = True
            break # No need to check further if rain is found

    # --- Send SMS Alert (if rain is predicted) ---
    if will_rain:
        message_body = "It's going to rain today. Remember to bring an umbrella! ☔️"
        print(message_body) # Print to console
        try:
            # Initialize Twilio client
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            # Create and send the SMS message
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER, # Your Twilio phone number
                to=MY_PHONE_NUMBER         # Your personal phone number
            )
            print(f"SMS sent successfully. Message SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS. Check Twilio credentials or network. Error: {e}")
    else:
        print("No rain expected in the next 12 hours.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    print("Please check your API key, network connection, or coordinates.")
except KeyError as e:
    print(f"Error parsing weather data. Missing key: {e}")
    print("API response structure might have changed or unexpected data received.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

