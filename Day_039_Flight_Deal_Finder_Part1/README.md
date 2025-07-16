# Day_039_Flight_Deal_Finder_Part1

This project is part of my 100 Days of Code journey.

## Project Description

On Day 39, I began building the **Flight Deal Finder Capstone Project**, with this first part focusing on **data management and preparation** for finding cheap flights. The primary goals were to:

1. **Google Sheets Integration (via Sheety API):** Set up a Google Sheet to store flight deal data (e.g., cities, IATA codes, target prices). This project leverages Sheety to interact with this sheet.
    
2. **Sheety API Interaction:** Learn to read data from and potentially update data in a Google Sheet using Sheety's RESTful API.
    
3. **Data Manager Class:** Implement a `DataManager` class to encapsulate all interactions with the Google Sheet, promoting clean and modular code.
    
4. **IATA Code Lookup (Conceptual):** Prepare for integrating with a flight search API (like Tequila) to look up IATA codes for cities if they are missing in the Google Sheet. (The actual Tequila API integration for searching flights comes in Part 2).
    
5. **API Authentication:** Understand how to use basic authentication with Sheety.
    

This initial phase establishes the central data source for the flight deals and sets up the programmatic way to interact with it, laying the groundwork for the flight searching and notification system.

## How to Run

This project requires a Sheety endpoint linked to your Google Sheet.

1. **Set up Google Sheet and Sheety:**
    
    - Create a new Google Sheet (e.g., named "Flight Deals") with columns like `City`, `IATA Code`, `Lowest Price`.
        
    - Go to [Sheety](https://sheety.co/ "null") and create a new project. Link it to your Google Sheet. Sheety will provide you with a unique endpoint URL for your sheet. You'll also set up Basic Authentication for this endpoint (username and password).
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_039_Flight_Deal_Finder_Part1
    ```

4. **Install Required Libraries:**
    
    ```
    pip install requests
    ```
    
5. **Configure Credentials:** Open the `main.py` (or `data_manager.py` and `main.py` if split) file and replace the placeholder values for `SHEETY_ENDPOINT`, `SHEETY_USERNAME`, and `SHEETY_PASSWORD` with your actual credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will fetch data from your Google Sheet via Sheety. It will print the fetched data to the console. If any city in your sheet is missing its IATA code, the script might conceptually prepare to look it up (though the actual lookup and update logic for Tequila API integration will be in Day 40).

```
Fetching data from Google Sheet...
Successfully fetched data:
[{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 196, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 260, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 200, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
```

## Concepts Learned

- **Google Sheets as a Database:** Using spreadsheets as a simple, human-readable data store.
    
- **Sheety API:** A practical tool for bridging Python applications with Google Sheets.
    
- **Data Management in OOP:** Designing a class (`DataManager`) to handle data interactions.
    
- **API Read Operations:** Performing `GET` requests to retrieve data.
    
- **API Write/Update Operations (Conceptual):** Preparing for `PUT` requests to update data.
    
- **Modular Project Structure:** Breaking down a larger project into logical components.

## Author

[Musn0o](https://github.com/Musn0o)