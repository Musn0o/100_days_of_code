import requests
from bs4 import BeautifulSoup
import smtplib # For sending emails

# --- Configuration ---

# Amazon Product URL to track
PRODUCT_URL = "YOUR_AMAZON_PRODUCT_URL_HERE"
# Example: "https://www.amazon.com/Dyson-V11-Torque-Drive-Cordless/dp/B07R9L7L4Y/"

# Your desired target price (e.g., send alert if price drops below this)
TARGET_PRICE = 100.00 # Set your target price here

# Your email credentials for sending the alert
# If using Gmail, you might need an "App password" instead of your regular password.
# Search "Gmail app password" for instructions.
MY_EMAIL = "YOUR_EMAIL@gmail.com"
MY_PASSWORD = "YOUR_EMAIL_APP_PASSWORD" # Use an app password if 2FA is on

# Recipient email address for the alert
RECIPIENT_EMAIL = "RECIPIENT_EMAIL@example.com"

# --- HTTP Headers for Web Scraping ---
# Amazon often blocks requests without a proper User-Agent.
# You can find your User-Agent by searching "my user agent" in Google.
# The Accept-Language header helps get content in English.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", # Replace with your User-Agent
    "Accept-Language": "en-US,en;q=0.9",
}

# --- Step 1: Fetch Product Page HTML ---
print(f"Checking price for {PRODUCT_URL}...")
try:
    response = requests.get(url=PRODUCT_URL, headers=HEADERS)
    response.raise_for_status() # Raise an exception for bad status codes
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching Amazon page: {e}")
    print("Please check the URL, your internet connection, or your User-Agent header.")
    exit()

# --- Step 2: Parse HTML and Extract Price ---
soup = BeautifulSoup(html_content, "lxml") # Using 'lxml' parser for speed

# The CSS selector for the price might vary. Inspect Amazon's page HTML to find the correct one.
# Common selectors include:
# span.a-price-whole (for whole part) and span.a-price-fraction (for fractional part)
# span.a-offscreen (often contains the full price text, but might be hidden)
# #priceblock_ourprice or #priceblock_dealprice
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")

# Fallback if specific price parts are not found, try to get the full price string
price_element = soup.find(name="span", class_="a-offscreen")

current_price = None
if price_whole and price_fraction:
    price_text = f"{price_whole.getText()}{price_fraction.getText()}"
    # Remove currency symbols and commas, then convert to float
    current_price = float(price_text.replace(",", "").replace("$", ""))
elif price_element:
    price_text = price_element.getText()
    current_price = float(price_text.replace(",", "").replace("$", ""))

if current_price is None:
    print("Could not find the price element. The HTML structure might have changed.")
    exit()

# Get product title for the email
product_title_element = soup.find(id="productTitle")
product_title = product_title_element.getText().strip() if product_title_element else "Product"

print(f"Current price: ${current_price:.2f}")
print(f"Target price: ${TARGET_PRICE:.2f}")

# --- Step 3: Compare Price and Send Email Alert ---
if current_price <= TARGET_PRICE:
    message = f"{product_title} is now ${current_price:.2f}!\n\nBuy now: {PRODUCT_URL}"
    print("Price has dropped! Sending email notification...")

    try:
        # Connect to your email's SMTP server
        # For Gmail, it's smtp.gmail.com on port 587 (TLS)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # Start TLS encryption
            connection.login(user=MY_EMAIL, password=MY_PASSWORD) # Log in to your email account
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject:Amazon Price Alert! - {product_title}\n\n{message}".encode('utf-8') # Encode for non-ASCII chars
            )
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Email sending failed: SMTP Authentication Error.")
        print("Check your email address and password (or app password for Gmail).")
    except smtplib.SMTPException as e:
        print(f"Email sending failed: SMTP Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during email sending: {e}")
else:
    print("Price is still too high. No email sent.")

