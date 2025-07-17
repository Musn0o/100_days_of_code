# Day_050_Tinder_Swiping_Bot

This project is part of my 100 Days of Code journey.

## Project Description

On Day 50, the focus was on **Advanced Web Automation** using **Selenium WebDriver** to create a bot that automates swiping on Tinder. This project pushed the boundaries of web automation, covering:

1. **Selenium WebDriver Setup:** Configuring Selenium to control a web browser (e.g., Chrome).
    
2. **Browser Automation:** Navigating to Tinder, handling login flows (often involving third-party authentication like Facebook or Google), and interacting with dynamic elements.
    
3. **Locating Dynamic Web Elements:** Dealing with elements that may appear, disappear, or change attributes, often requiring more robust selectors or explicit waits.
    
4. **Simulating Clicks:** Programmatically clicking the "Like" (swipe right) and "Nope" (swipe left) buttons.
    
5. **Handling Pop-ups:** Implementing strategies to close various pop-ups that appear during the Tinder experience (e.g., location requests, notification requests, "Add to Home Screen" prompts).
    
6. **Timing and Delays:** Using `time.sleep()` and potentially explicit waits to ensure elements are loaded and interactive before attempting to click them.
    
7. **Looping Automation:** Continuously performing swipe actions for a set duration or until a condition is met.
    

This bot demonstrates the capability of Selenium to interact with highly dynamic and interactive single-page applications, performing repetitive user actions.

## How to Run

**CRITICAL PREREQUISITES:**

- **Manual Login First:** Due to the complexity of Tinder's login (especially with Facebook/Google pop-ups and security measures), it is highly recommended to **manually log into Tinder in your browser first** before running the script. Selenium can then often pick up the existing session.
    
- **WebDriver:** This project requires **Selenium WebDriver** and a compatible web browser (e.g., Chrome). You'll need the corresponding WebDriver executable.
    
    - **Chrome:** Download `chromedriver` from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/ "null") (match your Chrome browser version). Place the executable in a directory included in your system's PATH, or use `webdriver_manager` as shown in the code.
        

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_050_Tinder_Swiping_Bot
    ```

3. **Install Required Libraries:**
    
    ```
    pip install selenium webdriver-manager
    ```
    
4. **Configure Parameters:** Open the `main.py` file. You may need to update the `TINDER_URL` if it changes. The core challenge will be finding the correct CSS selectors for the "Like" and "Nope" buttons and any pop-ups.
    
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will open a browser window and attempt to automate the specified actions. Keep an eye on the browser to see if pop-ups are blocking interactions or if selectors need updating.)_
    

## Demo

When you run the script, a new Chrome (or chosen browser) window will open, navigating to Tinder.

- If you are already logged in, it will proceed directly to the swiping interface.
    
- If not, it will attempt to handle the login (which is often the most fragile part).
    
- Once on the main swiping screen, the bot will continuously click the "Nope" (swipe left) or "Like" (swipe right) button, handling various pop-ups that appear (e.g., location access, notifications, "Add to Home Screen" prompts).
    
- The script will run for a predefined duration or until manually stopped.
    
## Ethical Considerations & Disclaimer

- **Terms of Service:** Automating interactions on platforms like Tinder **likely violates their Terms of Service**. Use this knowledge responsibly and at your own risk. Automated accounts can be detected and banned.
    
- **Privacy:** Be mindful of privacy implications when interacting with personal data on dating apps.
    
- **Bot Detection:** Websites continuously update their defenses against bots. This script may stop working if Tinder's website structure or anti-bot measures change.
    
- **Fragility:** Web automation scripts, especially on dynamic sites, are inherently fragile and require frequent updates as the target website evolves.
    

## Concepts Learned

- **Robust Element Locators:** Strategies for finding elements on highly dynamic pages.
    
- **Handling Pop-ups/Alerts:** Techniques for dismissing various types of overlays.
    
- **Implicit vs. Explicit Waits:** Understanding when and how to use different waiting strategies for elements to become interactive.
    
- **Continuous Automation Loops:** Designing scripts that perform actions repeatedly.
    
- **Error Handling in Automation:** Using `try-except` blocks to manage unexpected elements or failures gracefully.
    
- **Advanced Browser Control:** More complex interactions beyond simple clicks and text entry.

## Author

[Musn0o](https://github.com/Musn0o)