# Day_036_Stock_News

This project is part of my 100 Days of Code journey.

## Project Description

On Day 36, the focus was on building a **Stock News Alert System**. This project involved integrating with multiple external APIs to monitor stock price fluctuations and deliver relevant news updates via SMS. Key areas covered include:

1. **Stock Market Data API (Alpha Vantage):** Fetching daily stock price data to determine significant changes.
    
2. **News API:** Retrieving top news articles related to a specific company if its stock price experiences a notable change.
    
3. **Twilio API for SMS:** Sending automated SMS messages to alert the user about stock movements and associated news headlines.
    
4. **Conditional Logic:** Implementing thresholds to trigger alerts only when stock prices change by a certain percentage.
    
5. **Data Parsing:** Extracting specific information (closing prices, headlines, descriptions) from JSON API responses.
    

The application automatically checks a chosen stock's performance. If the price changes significantly (e.g., by 5% or more), it fetches relevant news articles and sends an SMS alert summarizing the change and providing key headlines.

## How to Run

This project requires API keys from Alpha Vantage, News API, and Twilio. You will need to sign up for accounts on these platforms to get your keys and account details.

1. **Obtain API Keys:**
    
    - **Alpha Vantage:** Sign up at [Alpha Vantage](https://www.alphavantage.co/documentation/ "null") to get your API Key.
        
    - **News API:** Sign up at [News API](https://newsapi.org/ "null") to get your API Key.
        
    - **Twilio:** Sign up at [Twilio](https://www.twilio.com/ "null") to get your Account SID, Auth Token, and a Twilio Phone Number.
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_036_Stock_News
    ```

   4. **Install Required Libraries:**

    ```
    pip install requests twilio
    ```

5. **Configure API Keys:** Open the `main.py` file and replace the placeholder values for `ALPHA_VANTAGE_API_KEY`, `NEWS_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `MY_PHONE_NUMBER` with your actual credentials.

6. **Run the Python Script:**

    ```
    python main.py
    ```

## Demo

When you run the script, it will fetch stock data and then news data if the stock change threshold is met. If an alert is triggered, it will print messages to the console and, if configured correctly, send an SMS.

```
Checking stock price for TSLA...
TSLA: 🔺5.2%
Headline 1: Tesla's new Gigafactory production ramps up.
Brief: New factory expected to boost production by 20%.
Headline 2: Analyst upgrades Tesla stock rating.
Brief: Positive outlook on future growth.
(SMS sent via Twilio - if configured correctly)
```

OR

```
Checking stock price for TSLA...
TSLA price change is within threshold. No alert sent.
```

## Concepts Learned

- **Multi-API Integration:** Combining data from different web services.
    
- **API Authentication:** Securely accessing external APIs.
    
- **Data Extraction and Transformation:** Parsing complex JSON responses and extracting specific data points.
    
- **Conditional Alerting:** Implementing logic to trigger actions based on data conditions.
    
- **Real-world Application:** Building a practical tool that leverages real-time data.
    
- **Automated Notifications:** Sending programmatic messages via SMS.

## Author

[Musn0o](https://github.com/Musn0o)