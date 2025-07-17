from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # For automatic driver management
import time

# --- Configuration ---
# URL of the job board you want to automate
JOB_BOARD_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102277492&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&searchId=null&sortBy=R" # Example LinkedIn URL
# Replace with your actual email and password for the job board
MY_EMAIL = "YOUR_EMAIL@example.com"
MY_PASSWORD = "YOUR_PASSWORD"

# --- WebDriver Setup ---
# Automatically download and manage the correct chromedriver.
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window() # Maximize window for better visibility and interaction

# Open the job board website
driver.get(JOB_BOARD_URL)
time.sleep(2) # Give the page some time to load

# --- Step 1: Log In (Example for LinkedIn) ---
print("Attempting to log in...")
try:
    # Find the sign-in button (this selector might vary, inspect the page)
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()
    time.sleep(2)

    # Find email and password fields
    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter credentials
    email_field.send_keys(MY_EMAIL)
    password_field.send_keys(MY_PASSWORD)
    password_field.send_keys(Keys.ENTER) # Press Enter to submit form
    time.sleep(5) # Wait for login to complete and dashboard to load

    print("Login successful (if credentials were correct).")

except Exception as e:
    print(f"Error during login: {e}")
    print("Please check your login selectors or if you're already logged in.")
    # If login fails, you might want to quit or continue with limited functionality
    # driver.quit()
    # exit()

# --- Step 2: Search for Jobs (Example for LinkedIn, assuming search is already in URL) ---
# For this example, we assume the JOB_BOARD_URL already contains the search parameters.
# If not, you would find the search bar, enter keywords, and click search.
# Example:
# search_bar = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
# search_bar.send_keys("Python Developer")
# search_bar.send_keys(Keys.ENTER)
# time.sleep(3)

# --- Step 3: Iterate through Job Listings and Apply ---
print("Searching for job listings...")
try:
    # Find all job listings (this selector is highly dependent on the website)
    # For LinkedIn, job cards are often in a list with specific classes.
    # You'll need to inspect the HTML of the job search results page to find the correct selector.
    job_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

    if not job_listings:
        print("No job listings found with the current selector. Please inspect the page.")

    for job_listing in job_listings:
        try:
            # Click on each job listing to view details
            job_listing.click()
            time.sleep(2) # Wait for job details to load

            # Find the "Easy Apply" or "Apply" button
            # This selector also varies greatly between websites.
            # Look for buttons that trigger the application process.
            apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button") # Common LinkedIn selector
            if apply_button.is_displayed() and apply_button.is_enabled():
                print(f"Found apply button for job: {job_listing.text.splitlines()[0]}")
                apply_button.click()
                time.sleep(2) # Wait for application modal to appear

                # --- Step 4: Handle Application Form (Highly Simplified) ---
                # This part is highly dependent on the specific job board's application form.
                # Real forms can have multiple pages, CAPTCHAs, file uploads, etc.
                # This is a very basic example for a simple form.
                try:
                    # Example: Find a "Next" or "Submit" button in the application modal
                    # You'll need to inspect the modal's HTML to find these.
                    # For LinkedIn Easy Apply, it often has a 'Next' button.
                    submit_button = driver.find_element(By.CSS_SELECTOR, "footer button[type='submit']")
                    if submit_button.is_displayed() and submit_button.is_enabled():
                        print("Attempting to submit application (simplified).")
                        submit_button.click() # Click 'Next' or 'Submit'
                        time.sleep(2)
                        # Handle potential confirmation or final submit button
                        # For LinkedIn, there might be a "Review" then "Submit application"
                        # This would require more sophisticated logic.
                        # For now, just assume one click is enough for demonstration.
                        print("Application step completed.")
                    else:
                        print("Submit/Next button not found or not clickable in application form.")

                    # Close the application modal if it's still open (e.g., if application completed)
                    # Look for a close button or 'X' icon.
                    try:
                        close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
                        close_button.click()
                        print("Closed application modal.")
                        time.sleep(1)
                    except:
                        pass # No close button found or modal already closed

                except Exception as form_e:
                    print(f"Error interacting with application form: {form_e}")
                    # Try to close the modal if an error occurs
                    try:
                        cancel_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss") # Common close button
                        cancel_button.click()
                        print("Closed application modal due to error.")
                        time.sleep(1)
                    except:
                        pass
            else:
                print("Apply button not found or not clickable for this job.")

        except Exception as job_e:
            print(f"Error processing job listing: {job_e}")
            # Continue to the next job if one fails

except Exception as list_e:
    print(f"Error iterating through job listings: {list_e}")

finally:
    print("\nAutomation complete. Closing browser.")
    driver.quit()

