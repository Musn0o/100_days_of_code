# Day_051_Internet_Speed_Twitter_Complaint_Bot

This project is part of my 100 Days of Code journey.

## Project Description

On Day 51, the focus was on building an **Internet Speed Twitter Complaint Bot** using **Selenium WebDriver**. This advanced automation project combines web scraping with social media interaction, covering:

1. **Selenium WebDriver Setup:** Configuring Selenium to control a web browser (e.g., Chrome).
    
2. **Internet Speed Testing:** Automating interaction with a speed test website (like Speedtest.net) to initiate a test and extract the download and upload speeds.
    
3. **Conditional Logic:** Comparing the measured speeds against predefined promised speeds from an Internet Service Provider (ISP).
    
4. **Twitter/X Automation:** If speeds fall below the threshold:
    
    - Navigating to Twitter/X.
        
    - Automating the login process (which can be complex).
        
    - Composing and sending a complaint tweet to the ISP.
        
5. **Handling Dynamic Elements & Pop-ups:** Dealing with various pop-ups, modals, and dynamically loaded content that often appear on modern websites.
    
6. **Error Handling:** Using `try-except` blocks to gracefully handle cases where elements might not be found or interactions fail.
    

This bot demonstrates the capability of Selenium to perform complex, multi-step automated tasks across different websites, reacting to real-time data.

## How to Run

**CRITICAL PREREQUISITES:**

- **WebDriver:** This project requires **Selenium WebDriver** and a compatible web browser (e.g., Chrome). You'll need the corresponding WebDriver executable.
    
    - **Chrome:** Download `chromedriver` from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/ "null") (match your Chrome browser version). Place the executable in a directory included in your system's PATH, or use `webdriver_manager` as shown in the code.
        
- **Twitter/X Login:** Automating Twitter/X login is notoriously difficult due to CAPTCHAs, 2FA, and dynamic elements. It's often easier to **manually log into Twitter/X in your browser first** before running the script, and let Selenium use the existing session. If you attempt to automate login, be prepared for it to be fragile.
    

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_051_Internet_Speed_Twitter_Complaint_Bot
    ```
     
3. **Install Required Libraries:**
    
    ```
    pip install selenium webdriver-manager
    ```
    
4. **Configure Parameters:** Open the `main.py` file and replace the placeholder values for:
    
    - `PROMISED_DOWN`, `PROMISED_UP` (your ISP's advertised speeds)
        
    - `TWITTER_EMAIL`, `TWITTER_PASSWORD` (your Twitter/X credentials)
        
    - `TWITTER_ISP_HANDLE` (your ISP's Twitter/X handle, e.g., `@YourISP`)
        
    - **Crucially, you will need to inspect the HTML of Speedtest.net and Twitter/X to find the correct CSS selectors or XPaths for all interactive elements (buttons, input fields, speed results, tweet button).** The provided selectors are examples and are highly likely to change.
        
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will open a browser window and attempt to automate the specified actions. Keep an eye on the browser to see if pop-ups are blocking interactions or if selectors need updating.)_
    

## Demo

When you run the script, a new Chrome (or chosen browser) window will open. The bot will:

1. Navigate to Speedtest.net.
    
2. Initiate the speed test.
    
3. Wait for the test to complete and extract the download and upload speeds.
    
4. Compare the speeds to your promised speeds.
    
5. If speeds are below threshold, it will navigate to Twitter/X, attempt to log in, and then compose and send a tweet to your ISP.
    
6. Finally, it will close the browser.
    
## Ethical Considerations & Disclaimer

- **Terms of Service:** Automating interactions on websites like Speedtest.net and Twitter/X **may violate their Terms of Service**. Use this knowledge responsibly and at your own risk. Automated accounts can be detected and banned.
    
- **Bot Detection:** Websites continuously update their defenses against bots. This script may stop working if the website structures or anti-bot measures change.
    
- **Fragility:** Web automation scripts, especially on dynamic sites, are inherently fragile and require frequent updates as the target website evolves.
    
- **Tweet Content:** Be mindful of the content of your automated tweets.
    

## Concepts Learned

- **Multi-Website Automation:** Controlling a browser to interact with different web applications sequentially.
    
- **Asynchronous Content Loading:** Handling web pages where content (like speed test results) loads over time.
    
- **Conditional Automation:** Triggering different actions based on extracted data.
    
- **Social Media Automation:** Programmatically interacting with social media platforms (with caveats).
    
- **Robust Element Locators:** Advanced techniques for finding elements on complex, dynamic pages.
    
- **Error Handling in Automation:** Making scripts more resilient to unexpected scenarios.

## Author

[Musn0o](https://github.com/Musn0o)