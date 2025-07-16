# Day_038_Workout_Tracking_Using_Google_Sheets

This project is part of my 100 Days of Code journey.

## Project Description

On Day 38, the focus was on building an automated **Workout Tracking** system that logs exercise data directly into a **Google Sheet**. This project involved integrating with multiple external APIs and covered:

1. **Nutritionix Natural Language for Exercise API:** Using this API to parse natural language exercise descriptions (e.g., "ran 3 miles") into structured data (exercise type, duration, calories burned).
    
2. **Google Sheets Integration (via Sheety API):** Leveraging Sheety as an intermediary to interact with a Google Sheet. Sheety provides simple RESTful endpoints for reading, writing, and updating data in Google Sheets.
    
3. **API Authentication:** Implementing API key authentication for Nutritionix and basic authentication for Sheety.
    
4. **HTTP Methods:** Making `POST` requests to Nutritionix and `POST` requests to Sheety.
    
5. **Date and Time Manipulation:** Using Python's `datetime` module to record the exact time and date of the workout.
    
6. **Data Flow:** Understanding how data flows from user input -> Nutritionix API -> Python script -> Sheety API -> Google Sheet.
    

The application prompts the user for their workout activities in natural language. It then uses the Nutritionix API to interpret this input and get detailed exercise metrics. Finally, it logs this structured workout data (date, time, exercise, duration, calories) into a designated Google Sheet.

## How to Run

This project requires API keys from Nutritionix and a Sheety endpoint linked to your Google Sheet.

1. **Obtain API Keys and Setup Sheety:**
    
    - **Nutritionix:** Sign up at [Nutritionix API](https://www.nutritionix.com/business/api "null") to get your Application ID (`X-APP-ID`) and API Key (`X-APP-KEY`).
        
    - **Google Sheet:** Create a new Google Sheet (e.g., named "Workout Tracker") with columns like `Date`, `Time`, `Exercise`, `Duration`, `Calories`.
        
    - **Sheety:** Go to [Sheety](https://sheety.co/ "null") and create a new project. Link it to your Google Sheet. Sheety will provide you with a unique endpoint URL for your sheet. You'll also set up Basic Authentication for this endpoint (username and password).
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_038_Workout_Tracking_Using_Google_Sheets
    ```

4. **Install Required Libraries:**
    
    ```
    pip install requests
    ```
    
5. **Configure Credentials:** Open the `main.py` file and replace the placeholder values for `NUTRITIONIX_APP_ID`, `NUTRITIONIX_API_KEY`, `SHEETY_ENDPOINT`, `SHEETY_USERNAME`, and `SHEETY_PASSWORD` with your actual credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will prompt you for your workout. After you enter it, it will process the data and print the API responses to the console. If successful, you will see the workout details appear in your linked Google Sheet.

```
Tell me which exercises you did:
I ran 3 miles and cycled for 30 minutes.
# (Nutritionix API response for parsed exercises will be printed)
# (Sheety API response for successful row addition will be printed)
Successfully logged workout to Google Sheet.
```

## Concepts Learned

- **Multi-API Workflow:** Chaining API calls where the output of one API (Nutritionix) serves as input for another (Sheety).
    
- **Natural Language Processing (Basic):** Leveraging an API to interpret human-like input.
    
- **Automated Data Logging:** Programmatically adding data to a spreadsheet.
    
- **API Authentication Best Practices:** Using headers and basic auth for secure API access.
    
- **JSON Data Handling:** Constructing and parsing complex JSON payloads.
    
- **Real-World Application:** Building a practical tool for personal data tracking.

## Author

[Musn0o](https://github.com/Musn0o)