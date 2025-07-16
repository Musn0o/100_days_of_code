# Day_040_Flight_Club

This project is part of my 100 Days of Code journey.

## Project Description

On Day 40, I completed the **Flight Deal Finder Capstone Project**, transforming it into a "Flight Club" that not only finds cheap flights but also **notifies users via SMS**. This part integrated and expanded upon the concepts from Day 39, specifically focusing on:

1. **Flight Search API (Tequila by Kiwi.com):** Integrated with the Tequila API to search for actual flight deals based on specified criteria (origin, destination, dates, price).
    
2. **IATA Code Auto-Population:** Enhanced the `DataManager` to automatically look up and update missing IATA codes in the Google Sheet using the Tequila API's location search endpoint.
    
3. **Deal Comparison:** Compared the found flight prices with the target `Lowest Price` stored in the Google Sheet.
    
4. **SMS Notification with Twilio:** Utilized the Twilio API to send detailed SMS alerts to the user when a flight deal below the target price is found.
    
5. **Date Range for Search:** Implemented logic to search for flights within a specific future date range (e.g., next 6 months).
    
6. **User Management (Conceptual):** While the core focus is on flight deals, the "Flight Club" concept implies managing users. This could involve a separate Google Sheet for user emails/phone numbers to send mass notifications (not fully implemented here but mentioned for context).
    

The application now automates the process of finding cheap flights to desired destinations and proactively notifies the user about potential savings.

## How to Run

This project requires API keys from Tequila by Kiwi.com, Twilio, and a Sheety endpoint linked to your Google Sheet.

1. **Obtain API Keys and Setup Sheety:**
    
    - **Tequila API:** Sign up at [Tequila by Kiwi.com](https://tequila.kiwi.com/ "null") to get your API Key.
        
    - **Twilio:** Sign up at [Twilio](https://www.twilio.com/ "null") to get your Account SID, Auth Token, and a Twilio Phone Number.
        
    - **Google Sheet:** Continue using the Google Sheet from Day 39 (e.g., "Flight Deals") with columns like `City`, `IATA Code`, `Lowest Price`.
        
    - **Sheety:** Continue using your Sheety project from Day 39. Ensure you have the endpoint URL and Basic Authentication credentials.
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_040_Flight_Club
    ```

4. **Install Required Libraries:**
    
    ```
    pip install requests twilio
    ```
    
5. **Configure Credentials:** Open the `main.py` file and replace the placeholder values for `SHEETY_ENDPOINT`, `SHEETY_USERNAME`, `SHEETY_PASSWORD`, `TEQUILA_API_KEY`, `TEQUILA_API_ENDPOINT`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `MY_PHONE_NUMBER` with your actual credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will first check your Google Sheet for missing IATA codes and update them if necessary. Then, it will search for flights to each destination. If a deal is found below your target price, it will print details to the console and send an SMS (if Twilio is configured).

```
Fetching destination data from Google Sheet...
IATA code for Paris is missing. Looking up...
Updating IATA code for Paris (row 2) to PAR...
Successfully updated IATA code in Google Sheet.
Searching for flights to Paris...
Low price found to Paris!
Only $50 to Paris from London-LON, from 2024-07-20 to 2025-01-20.
SMS sent successfully. Message SID: SMxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Searching for flights to Berlin...
No flight deal found for Berlin.
... (continues for other destinations)
```

## Concepts Learned

- **Full API Workflow:** Orchestrating multiple API calls (Sheety, Tequila, Twilio) in a single application.
    
- **Dynamic Data Updates:** Programmatically updating a spreadsheet based on API lookups.
    
- **Complex Querying:** Constructing detailed API requests for flight searches (dates, prices, origins/destinations).
    
- **Real-time Notifications:** Delivering timely information to users via SMS.
    
- **Capstone Project Integration:** Combining all previously learned concepts (OOP, APIs, data handling, conditional logic) into a substantial application.
    
- **Date and Time Handling:** Working with `datetime` and `timedelta` for flight search date ranges.

## Author

[Musn0o](https://github.com/Musn0o)