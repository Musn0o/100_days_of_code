import requests
from twilio.rest import Client

# --- Configuration ---

# Stock Market Data (Alpha Vantage)
STOCK_NAME = "TSLA"  # Tesla stock symbol
COMPANY_NAME = "Tesla Inc"
# Get your API Key from https://www.alphavantage.co/documentation/
ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

# News API
# Get your API Key from https://newsapi.org/
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

# Twilio SMS Service
# Get your Account SID and Auth Token from https://www.twilio.com/console
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Replace with your Account SID
TWILIO_AUTH_TOKEN = "your_auth_token_here" # Replace with your Auth Token
# Your Twilio phone number (the one you got from Twilio)
TWILIO_PHONE_NUMBER = "+1234567890" # Replace with your Twilio phone number
# Your personal phone number to receive the SMS alerts
MY_PHONE_NUMBER = "+19876543210" # Replace with your actual phone number

# Threshold for stock price change (e.g., 5% increase or decrease)
STOCK_CHANGE_THRESHOLD_PERCENT = 5

# --- Step 1: Get Stock Price Data ---
print(f"Checking stock price for {STOCK_NAME}...")
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,
}

stock_response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=stock_params)
stock_response.raise_for_status() # Raise an exception for bad status codes
stock_data = stock_response.json()["Time Series (Daily)"]

# Convert daily data to a list of (date, values) tuples and get the most recent two days
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

# Get closing prices
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Calculate the percentage difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
percentage_diff = round((difference / yesterday_closing_price) * 100, 2)

# Determine the emoji for price change
up_down = None
if percentage_diff > 0:
    up_down = "🔺"
elif percentage_diff < 0:
    up_down = "🔻"

# --- Step 2: Get News Articles if Significant Change ---
if abs(percentage_diff) > STOCK_CHANGE_THRESHOLD_PERCENT:
    print(f"{STOCK_NAME}: {up_down}{abs(percentage_diff)}%")

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME, # Search for company name in article titles
        "language": "en",
        "sortBy": "relevancy", # Get most relevant articles
    }

    news_response = requests.get(NEWS_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles_data = news_response.json()["articles"]

    # Get the first 3 relevant articles
    # Use list slicing to get the top 3, or fewer if not enough articles.
    three_articles = articles_data[:3]

    # Format the articles into a list of strings for the SMS message
    formatted_articles = [
        f"Headline {i+1}: {article['title']}.\nBrief: {article['description']}"
        for i, article in enumerate(three_articles)
    ]

    # --- Step 3: Send SMS via Twilio ---
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # Construct the main SMS message
        message_body = f"{STOCK_NAME}: {up_down}{abs(percentage_diff)}%\n" + "\n".join(formatted_articles)

        # Twilio messages have a character limit, so we might need to send multiple messages
        # if the content is too long. For simplicity, we'll send one message here.
        # In a real app, you might split the message or truncate it.
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(f"SMS sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS. Check Twilio credentials or network. Error: {e}")
else:
    print(f"{STOCK_NAME} price change is within threshold. No alert sent.")

