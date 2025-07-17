import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Configuration ---
# URL of the property listing website to scrape (e.g., Zillow)
# You will need to find a suitable URL for your scraping target.
# This is an EXAMPLE URL and might not work or might require different selectors.
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQuery=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.691585%2C%22east%22%3A-122.304415%2C%22south%22%3A37.703385%2C%22north%22%3A37.848574%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A97577%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isRentWithRetail%22%3Afalse%2C%22isRentByOwner%22%3Afalse%2C%22isNewConstruction%22%3Afalse%2C%22isComingSoon%22%3Afalse%2C%22isAuction%22%3Afalse%2C%22isForeclosure%22%3Afalse%2C%22isPreMarketForeclosure%22%3Afalse%2C%22isPreMarketBankOwned%22%3Afalse%2C%22isBankOwned%22%3Afalse%7D"

# URL of your Google Form for data entry
# Create your own Google Form with fields for "Address", "Price", "Link".
# Get the "pre-filled link" for your form to easily identify input field names.
GOOGLE_FORM_URL = "YOUR_GOOGLE_FORM_URL_HERE" # Example: "https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform"

# Headers for HTTP request to mimic a browser
# User-Agent is crucial to avoid being blocked.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# --- Step 1: Web Scraping ---
print("--- Step 1: Scraping Property Data ---")
response = requests.get(ZILLOW_URL, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Find all property listings. These selectors are highly dependent on the website.
# You MUST inspect the HTML of your target website to find the correct selectors.
# Example selectors for Zillow (these are prone to change):
# Addresses:
addresses = [address.get_text().strip() for address in soup.select(".list-card-addr")]
# Prices:
prices = [price.get_text().split("+")[0].strip() for price in soup.select(".list-card-price")]
# Links:
links = [link.get("href") for link in soup.select(".list-card-info a")]

# Combine the scraped data into a list of dictionaries
property_data = []
# Ensure all lists have the same length to avoid errors
min_len = min(len(addresses), len(prices), len(links))

for i in range(min_len):
    property_data.append({
        "address": addresses[i],
        "price": prices[i],
        "link": links[i]
    })

print(f"Scraped {len(property_data)} properties:")
for prop in property_data:
    print(f"  Address: {prop['address']}, Price: {prop['price']}, Link: {prop['link']}")

# --- Step 2: Automate Data Entry into Google Form ---
print("\n--- Step 2: Automating Data Entry into Google Form ---")

# WebDriver Setup
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

for entry in property_data:
    print(f"Entering data for: {entry['address']}...")
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2) # Wait for the form to load

    try:
        # Locate form fields by their XPath or CSS selector.
        # To find these, open your Google Form, right-click on an input field,
        # and select "Inspect". Look for the 'name' attribute or a unique ID.
        # Google Forms often use XPaths like '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        # or input elements with specific 'data-idx' attributes.

        # Example selectors (YOU MUST REPLACE THESE WITH YOUR FORM'S ACTUAL SELECTORS):
        address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


        # Fill the form fields
        address_input.send_keys(entry["address"])
        price_input.send_keys(entry["price"])
        link_input.send_keys(entry["link"])

        # Submit the form
        submit_button.click()
        print("Form submitted successfully.")
        time.sleep(2) # Wait for submission confirmation or next form load

    except Exception as e:
        print(f"Error filling or submitting form for {entry['address']}: {e}")
        print("Please check your Google Form selectors.")
        # Continue to the next property even if one fails

    finally:
        print("\nData entry automation complete. Closing browser.")
        driver.quit()

