import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Configuration ---
INSTAGRAM_URL = "https://www.instagram.com/"

# Your Instagram credentials
INSTAGRAM_USERNAME = "YOUR_INSTAGRAM_USERNAME"
INSTAGRAM_PASSWORD = "YOUR_INSTAGRAM_PASSWORD"

# The target Instagram account whose followers you want to follow
TARGET_ACCOUNT = "chefsteps" # Example: a public account to get followers from

# --- InstagramFollowerBot Class ---
class InstagramFollowerBot:
    def __init__(self):
        # Automatically download and manage the correct chromedriver.
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window() # Maximize window for better visibility

    def login(self):
        """Navigates to Instagram and attempts to log in."""
        print("Navigating to Instagram...")
        self.driver.get(INSTAGRAM_URL)
        time.sleep(3) # Give page time to load

        print("Attempting to log in...")
        try:
            # Find username and password fields
            # These selectors are examples and might change. Inspect Instagram's login page.
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.driver.find_element(By.NAME, "password")

            username_input.send_keys(INSTAGRAM_USERNAME)
            password_input.send_keys(INSTAGRAM_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5) # Wait for login to process

            # Handle "Save Your Login Info?" pop-up
            try:
                # Selector for "Not Now" button on "Save Your Login Info?" pop-up
                not_now_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_button.click()
                print("Clicked 'Not Now' on save login info pop-up.")
                time.sleep(2)
            except Exception:
                print("No 'Save Login Info' pop-up found or already handled.")

            # Handle "Turn on Notifications" pop-up
            try:
                # Selector for "Not Now" button on "Turn on Notifications" pop-up
                not_now_notifications = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_notifications.click()
                print("Clicked 'Not Now' on notifications pop-up.")
                time.sleep(2)
            except Exception:
                print("No 'Turn on Notifications' pop-up found or already handled.")

            print("Login successful (if credentials were correct and pop-ups handled).")

        except Exception as e:
            print(f"Error during login: {e}")
            print("Please check your login selectors, credentials, or if you're already logged in.")
            # If login fails, you might want to quit or continue with limited functionality
            self.driver.quit()
            exit()

    def find_followers(self, target_account):
        """Navigates to a target account and opens their follower list."""
        print(f"Navigating to {target_account}'s profile...")
        self.driver.get(f"{INSTAGRAM_URL}{target_account}/")
        time.sleep(3) # Wait for profile page to load

        print(f"Opening followers list for {target_account}...")
        try:
            # Find and click the "followers" link/button
            # Selector for followers count link (inspect Instagram profile page)
            followers_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{target_account}/followers/')]"))
            )
            followers_link.click()
            time.sleep(3) # Wait for the followers modal to open

            # Find the scrollable modal for followers
            # This selector is crucial for scrolling. Inspect the followers modal.
            # It's often a div with a specific role or class.
            # Example: //div[@role='dialog']/div/div[2]/div/div/div[1]/div[1]/div[2]
            # Or a div with a specific class for scrollable content.
            # This is a common pattern for scrollable lists in Instagram modals.
            follower_modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"))
            )
            # You might need to adjust the XPath or CSS selector for the scrollable container.
            # A more robust way might be to find the div with `role="dialog"` then navigate its children.

            # Scroll down to load more followers
            print("Scrolling to load more followers...")
            for i in range(10): # Scroll 10 times (adjust as needed)
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_modal)
                time.sleep(2) # Wait for content to load after scroll
                print(f"Scrolled {i+1} times.")

        except Exception as e:
            print(f"Error finding or scrolling followers: {e}")
            print("Please check selectors for followers link or the scrollable modal.")
            self.driver.quit()
            exit()

    def follow(self):
        """Iterates through loaded followers and clicks their follow buttons."""
        print("Starting to follow users...")
        try:
            # Find all "Follow" buttons within the follower modal
            # Selector for "Follow" buttons (inspect elements within the follower list modal)
            # These buttons often have specific text or data-testid.
            # Example: //button[text()='Follow']
            # Or by data-testid: //button[@data-testid='follow-button']
            follow_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Follow']")

            if not follow_buttons:
                print("No 'Follow' buttons found. They might already be followed or selectors are wrong.")
                return

            for button in follow_buttons:
                if button.is_displayed() and button.is_enabled():
                    try:
                        button.click()
                        print("Clicked 'Follow'.")
                        time.sleep(random.randint(1, 3)) # Random delay to mimic human behavior
                    except Exception as e:
                        print(f"Could not click follow button: {e}")
                        # This might happen if the button goes out of view or becomes disabled.
                        # You might need to scroll again or handle specific pop-ups.
                else:
                    print("Follow button not displayed or enabled.")
            print("Finished attempting to follow visible users.")

        except Exception as e:
            print(f"Error during following process: {e}")
            print("Please check selectors for 'Follow' buttons.")

    def quit_driver(self):
        """Closes the browser."""
        self.driver.quit()

# --- Main Execution ---
bot = InstagramFollowerBot()
bot.login()
bot.find_followers(TARGET_ACCOUNT)
bot.follow()
bot.quit_driver()

