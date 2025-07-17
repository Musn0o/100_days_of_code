from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Configuration ---
# Your promised internet speeds from your ISP (in Mbps)
PROMISED_DOWN = 150
PROMISED_UP = 10

# Your Twitter/X credentials
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"
# Your ISP's Twitter/X handle (e.g., "@ATT", "@VerizonSupport")
TWITTER_ISP_HANDLE = "@YourISP" # Replace with your actual ISP's handle

# URLs
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login" # Direct login flow URL

# --- SpeedTestBot Class ---
class InternetSpeedTwitterBot:
    def __init__(self):
        # Automatically download and manage the correct chromedriver.
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window() # Maximize window for better visibility

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Navigates to Speedtest.net, runs the test, and extracts speeds."""
        print("Navigating to Speedtest.net...")
        self.driver.get(SPEEDTEST_URL)
        time.sleep(5) # Give page time to load

        try:
            # Accept cookies/privacy policy if present (selector might vary)
            # Inspect the Speedtest.net page for the cookie consent button.
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
            print("Accepted cookies.")
            time.sleep(2)
        except Exception:
            print("No cookie consent pop-up found or already handled.")

        try:
            # Click the "Go" button to start the test (selector might vary)
            # Inspect the Speedtest.net page for the "Go" button.
            go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
            go_button.click()
            print("Starting speed test...")
            time.sleep(60) # Wait for the test to complete (adjust as needed)

            # Extract download speed (selector might vary)
            # Inspect the Speedtest.net results page for the download speed element.
            self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
            # Extract upload speed (selector might vary)
            # Inspect the Speedtest.net results page for the upload speed element.
            self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)

            print(f"Download Speed: {self.down} Mbps")
            print(f"Upload Speed: {self.up} Mbps")

        except Exception as e:
            print(f"Error during speed test: {e}")
            print("Could not get internet speed. Check Speedtest.net selectors or wait times.")
            self.down = 0 # Set to 0 if an error occurs
            self.up = 0

    def tweet_at_provider(self):
        """Logs into Twitter/X and sends a complaint tweet."""
        if self.down >= PROMISED_DOWN and self.up >= PROMISED_UP:
            print("Internet speed is good. No complaint tweet needed.")
            return

        print("Navigating to Twitter/X...")
        self.driver.get(TWITTER_URL)
        time.sleep(5) # Give page time to load

        try:
            # Enter email/username (selector might vary)
            # Inspect Twitter/X login page.
            email_input = self.driver.find_element(By.NAME, "text")
            email_input.send_keys(TWITTER_EMAIL)
            email_input.send_keys(Keys.ENTER)
            time.sleep(3)

            # Enter password (selector might vary)
            # Inspect Twitter/X password page.
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5) # Wait for login to complete

            print("Logged into Twitter/X (if credentials were correct).")

            # Compose the tweet (selector might vary)
            # Inspect Twitter/X compose tweet box.
            tweet_compose_box = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
            tweet_message = (
                f"Hey {TWITTER_ISP_HANDLE}, why is my internet speed {self.down}down/{self.up}up Mbps "
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up Mbps?"
            )
            tweet_compose_box.send_keys(tweet_message)
            time.sleep(2)

            # Click the tweet button (selector might vary)
            # Inspect Twitter/X tweet button.
            tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
            tweet_button.click()
            print("Tweet sent successfully!")
            time.sleep(5) # Wait for tweet to send

        except Exception as e:
            print(f"Error during Twitter/X automation: {e}")
            print("Could not send tweet. Check Twitter/X selectors, login, or if a CAPTCHA/2FA blocked it.")

    def quit_driver(self):
        """Closes the browser."""
        self.driver.quit()

# --- Main Execution ---
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
bot.quit_driver()

