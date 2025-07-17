import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Configuration ---
# URL of Tinder
TINDER_URL = "https://tinder.com/"

# Your Facebook/Google login details (if automating login, otherwise log in manually first)
# WARNING: Automating login for services like Tinder can be complex and fragile due to
# pop-ups, security measures, and frequent website changes.
# It's highly recommended to log in manually in your browser before running the script,
# and let Selenium use the existing session.
# If you must automate, provide your credentials here.
FACEBOOK_EMAIL = "YOUR_FACEBOOK_EMAIL"
FACEBOOK_PASSWORD = "YOUR_FACEBOOK_PASSWORD"

# Duration for the bot to swipe (in seconds)
SWIPING_DURATION_SECONDS = 3600 # 1 hour (adjust as needed)

# --- WebDriver Setup ---
# Automatically download and manage the correct chromedriver.
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window() # Maximize window for better visibility and interaction

# Open Tinder
driver.get(TINDER_URL)
time.sleep(5) # Give the page ample time to load

# --- Step 1: Handle Login (Highly simplified and fragile) ---
# IMPORTANT: It is often easier to manually log in to Tinder in your browser
# before running this script. Selenium will then use the existing session.
# The following login automation is provided as an example but is prone to breaking.
print("Attempting to handle login...")
try:
    # Click "Log in" button
    # Selector might change, inspect Tinder's page.
    login_button = driver.find_element(By.XPATH, '//*[@id="q-163273418"]/div[1]/div/div/div/div[1]/div/div[2]/div[1]/button')
    login_button.click()
    time.sleep(2)

    # Click "Log in with Facebook" or "Log in with Google"
    # Inspect the pop-up/modal for the correct button.
    # Example for Facebook login:
    fb_login_button = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    fb_login_button.click()
    time.sleep(2)

    # Switch to the Facebook login pop-up window
    # Tinder's login often opens a new window.
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title) # Should show "Facebook" or similar

    # Enter Facebook credentials (these selectors are for Facebook's login page)
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")
    email_field.send_keys(FACEBOOK_EMAIL)
    password_field.send_keys(FACEBOOK_PASSWORD)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)

    # Switch back to the main Tinder window
    driver.switch_to.window(base_window)
    print("Switched back to Tinder window.")
    time.sleep(5) # Wait for Tinder to load after Facebook login

except Exception as e:
    print(f"Error during login or initial setup: {e}")
    print("Consider logging in manually to Tinder in your browser before running the script.")
    # If login fails, you might want to quit or handle it differently
    # driver.quit()
    # exit()

# --- Step 2: Handle Pop-ups (Location, Notifications, "Add to Home Screen") ---
print("Handling pop-ups...")
try:
    # Allow Location (if prompted)
    # Selector for "Allow" button in location pop-up
    allow_location_button = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div/div/div[3]/button[1]')
    allow_location_button.click()
    time.sleep(2)
except Exception:
    print("Location pop-up not found or already handled.")

try:
    # Disallow Notifications (if prompted)
    # Selector for "Not interested" or "No thanks" button in notification pop-up
    disallow_notifications_button = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div/div/div[3]/button[2]')
    disallow_notifications_button.click()
    time.sleep(2)
except Exception:
    print("Notifications pop-up not found or already handled.")

try:
    # Decline "Add Tinder to Home Screen" pop-up
    # Selector for "No thanks" button
    add_to_home_screen_popup = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div/div[2]/button[2]')
    add_to_home_screen_popup.click()
    time.sleep(2)
except Exception:
    print("Add to home screen pop-up not found or already handled.")

print("Pop-ups handled (or not present).")
time.sleep(5) # Give some time for the main swiping interface to load fully

# --- Step 3: Start Swiping ---
print("Starting swiping...")
start_time = time.time()
while time.time() < start_time + SWIPING_DURATION_SECONDS:
    try:
        # Find the "Nope" button (swipe left)
        # Inspect Tinder's page to find the correct selector for the "Nope" button.
        # It's often a button with a specific data-testid or aria-label.
        # Example XPath for 'Nope' button (may change):
        nope_button = driver.find_element(By.XPATH, '//*[@id="q-163273418"]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/button[1]')
        # Find the "Like" button (swipe right)
        # Example XPath for 'Like' button (may change):
        like_button = driver.find_element(By.XPATH, '//*[@id="q-163273418"]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/button[3]')

        # Randomly choose to like or nope (e.g., 50/50 chance)
        if random.random() < 0.5: # 50% chance to like
            like_button.click()
            # print("Swiped right (Liked).")
        else: # 50% chance to nope
            nope_button.click()
            # print("Swiped left (Noped).")

        time.sleep(1) # Short pause between swipes

    except Exception as e:
        # Handle potential pop-ups that might interrupt swiping (e.g., "It's a Match!", "Get Gold")
        # These selectors are highly dynamic and will likely need frequent updates.
        print(f"Error during swiping: {e}. Attempting to handle pop-ups or continue.")
        try:
            # Try to find and close a "Match" pop-up
            match_popup_close_button = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div/div[1]/div[1]/div/div[3]/button')
            match_popup_close_button.click()
            print("Closed match pop-up.")
            time.sleep(1)
        except Exception:
            pass # Match pop-up not found

        try:
            # Try to find and close a "Get Gold/Premium" pop-up
            gold_popup_close_button = driver.find_element(By.XPATH, '//*[@id="q-1422730104"]/main/div[1]/div[2]/button')
            gold_popup_close_button.click()
            print("Closed Gold pop-up.")
            time.sleep(1)
        except Exception:
            pass # Gold pop-up not found

        # If no specific pop-up was handled, just wait a bit longer and try again
        time.sleep(3) # Wait longer if an error occurred, hoping elements load

    finally:
        print("\nSwiping duration ended. Closing browser.")
        driver.quit()

