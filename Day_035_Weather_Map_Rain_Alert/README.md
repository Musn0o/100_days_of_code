# Day_035_Weather_Map_Rain_Alert

This project is part of my 100 Days of Code journey.

## Project Description

On Day 35, the focus was on integrating **External APIs** into a Python application to create a practical weather alert system. This day covered a range of advanced topics:

1. **API Authentication:** Understanding why and how to authenticate with APIs using API Keys.
    
2. **OpenWeatherMap API:** Utilizing the OpenWeatherMap One Call API to fetch detailed weather data, including hourly forecasts.
    
3. **Checking for Rain:** Implementing logic to parse hourly weather data and determine if it will rain within the next 12 hours.
    
4. **Twilio API for SMS:** Using the Twilio API to send an SMS message to a phone number if rain is predicted.
    
5. **Automation with PythonAnywhere (Conceptual):** Discussing how such a script could be deployed and automated on a cloud platform like PythonAnywhere to run periodically without manual intervention.
    

The application fetches weather data for a specific location, checks for rain in the near future, and conceptually sends an SMS alert if rain is expected.

## How to Run

This project requires API keys from OpenWeatherMap and Twilio. You will need to sign up for accounts on both platforms to get your keys and account details.

1. **Obtain API Keys:**
    
    - **OpenWeatherMap:** Sign up at [OpenWeatherMap](https://openweathermap.org/api "null") to get your API Key.
        
    - **Twilio:** Sign up at [Twilio](https://www.twilio.com/ "null") to get your Account SID, Auth Token, and a Twilio Phone Number.
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_035_Weather_Map_Rain_Alert
    ```

4. **Install Required Libraries:**
    
    ```
    pip install requests twilio
    ```
    
5. **Configure API Keys:** Open the `main.py` file and replace the placeholder values for `OWM_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `MY_PHONE_NUMBER` with your actual credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will connect to the OpenWeatherMap API. If rain is detected within the next 12 hours, it will print a message indicating rain and, if configured with valid Twilio credentials, attempt to send an SMS. Otherwise, it will indicate no rain is expected.

```
Checking weather for rain...
It's going to rain today. Remember to bring an umbrella!
(SMS sent via Twilio - if configured correctly)
```

OR

```
Checking weather for rain...
No rain expected in the next 12 hours.
```

## Concepts Learned

- **API Integration:** Making HTTP requests to external web services.
    
- **JSON Parsing:** Working with JSON data returned by APIs.
    
- **API Security:** Understanding the role of API keys in authentication.
    
- **Third-Party Libraries:** Using `requests` for HTTP and `twilio` for SMS.
    
- **Conditional Logic for Data Analysis:** Analyzing API responses to make decisions.
    
- **Automation Principles:** Conceptual understanding of scheduling scripts (e.g., cron jobs on PythonAnywhere).

## Author

[Musn0o](https://github.com/Musn0o)