from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # Optional: for automatic driver management
import time

# --- Configuration ---
# URL of the Cookie Clicker game
COOKIE_CLICKER_URL = "http://orteil.dashnet.org/cookieclicker/"

# Time intervals for checking upgrades (in seconds)
# The bot will click the cookie continuously, but check for upgrades every 5 seconds.
CHECK_UPGRADES_INTERVAL = 5

# Duration for the bot to run (in seconds)
# After this time, the bot will stop and print the final cookie count.
GAME_DURATION_SECONDS = 300 # 5 minutes

# --- WebDriver Setup ---
# Option 1: Manual WebDriver path (uncomment and set if not using webdriver_manager)
# CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe" # Replace with your chromedriver path
# service = ChromeService(executable_path=CHROME_DRIVER_PATH)
# driver = webdriver.Chrome(service=service)

# Option 2: Automatic WebDriver management (recommended)
# This will automatically download and manage the correct chromedriver.
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game
driver.get(COOKIE_CLICKER_URL)

# Wait for the page to load and elements to be available
# Implicit wait can be set globally, or explicit waits can be used for specific elements.
# For simplicity, we'll use time.sleep initially.
time.sleep(2) # Give the page some time to load

# --- Locate Game Elements ---
try:
    # Locate the big cookie button
    big_cookie = driver.find_element(By.ID, "bigCookie")

    # Locate the upgrade items (initially, they might not be visible or clickable)
    # These are typically found by ID or CSS selector.
    # We'll get a list of all upgrade elements that are clickable.
    # The game dynamically adds/removes 'enabled' class to make them clickable.
    # We'll select by CSS selector for all elements that are products/upgrades.
    # The IDs for upgrades are typically 'buyGrandma', 'buyFactory', etc.
    # We'll reverse the list to prioritize buying the most expensive available upgrade.
    upgrade_ids = [
        "buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment",
        "buyAlchemy lab", "buyPortal", "buyTime machine", "buyAntimatter condenser",
        "buyPrism", "buyChancemaker", "buyFractal engine", "buyJavascript console",
        "buyIdleverse"
    ]
    # Filter for elements that actually exist on the page and are clickable
    # We'll fetch them dynamically inside the loop to get their current state.

except Exception as e:
    print(f"Error locating initial elements: {e}")
    driver.quit()
    exit()

# --- Game Loop ---
start_time = time.time()
next_upgrade_check_time = time.time() + CHECK_UPGRADES_INTERVAL

while time.time() < start_time + GAME_DURATION_SECONDS:
    # Continuously click the big cookie
    big_cookie.click()

    # Check for upgrades periodically
    if time.time() >= next_upgrade_check_time:
        # Get current cookie count
        try:
            cookie_count_str = driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", "")
            current_cookies = int(cookie_count_str)
        except Exception:
            # Handle cases where the cookie count format might be different or element not found
            current_cookies = 0 # Assume 0 if cannot parse
            # print("Could not parse cookie count.")

        # Find all available upgrades that are enabled (clickable)
        # Upgrades typically have a class like 'product unlocked enabled' when affordable.
        # We'll iterate through the known upgrade IDs in reverse order (most expensive first)
        purchased_an_upgrade = False
        for upgrade_id in reversed(upgrade_ids):
            try:
                upgrade_element = driver.find_element(By.ID, upgrade_id)
                # Check if the upgrade is enabled (affordable and available)
                class_attr = upgrade_element.get_attribute("class")
                if class_attr and "enabled" in class_attr:
                    # Get the price of the upgrade
                    price_element = upgrade_element.find_element(By.CLASS_NAME, "price")
                    # Clean the price string (remove commas) and convert to int
                    upgrade_price = int(price_element.text.replace(",", ""))

                    if current_cookies >= upgrade_price:
                        upgrade_element.click()
                        # print(f"Purchased {upgrade_id} for {upgrade_price} cookies.")
                        purchased_an_upgrade = True
                        break # Break after purchasing one upgrade to re-evaluate after purchase
            except Exception:
                # This handles cases where an upgrade might not be on the page yet
                # or its elements aren't found.
                pass # Simply skip if element not found or not clickable

        # Reset the timer for the next upgrade check if an upgrade was purchased
        # or if the interval has passed.
        if purchased_an_upgrade:
            next_upgrade_check_time = time.time() + 0.1 # Check again very soon after purchase
        else:
            next_upgrade_check_time = time.time() + CHECK_UPGRADES_INTERVAL


# --- Game End ---
# After the game duration, get the final cookie count
try:
    final_cookie_count = driver.find_element(By.ID, "cookies").text
    print(f"\nGame Over! Final cookie count: {final_cookie_count}")
except Exception as e:
    print(f"\nGame Over! Could not retrieve final cookie count: {e}")

# Close the browser
driver.quit()
