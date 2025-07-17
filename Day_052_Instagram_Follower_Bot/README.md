# Day_052_Instagram_Follower_Bot

This project is part of my 100 Days of Code journey.

## Project Description

On Day 52, the focus was on **Advanced Web Automation** using **Selenium WebDriver** to create a bot that automates following users on Instagram. This project involved interacting with a complex social media platform and covered:

1. **Selenium WebDriver Setup:** Configuring Selenium to control a web browser (e.g., Chrome).
    
2. **Instagram Login Automation:** Navigating to Instagram and attempting to log in with provided credentials. (Note: Instagram's security measures make this part highly fragile).
    
3. **Navigating User Profiles:** Going to a specific target Instagram account's profile.
    
4. **Accessing Follower Lists:** Clicking on the "Followers" count to open the follower list modal.
    
5. **Scrolling Dynamic Content:** Implementing programmatic scrolling within the follower list modal to load more followers, as Instagram loads them dynamically.
    
6. **Locating Dynamic Web Elements:** Identifying the "Follow" buttons for individual users within the follower list.
    
7. **Simulating Clicks:** Clicking the "Follow" button for each user.
    
8. **Handling Pop-ups:** Dealing with various Instagram pop-ups (e.g., "Save Login Info," "Notifications").
    
9. **Error Handling:** Using `try-except` blocks to gracefully handle cases where elements might not be found, or interactions fail.
    

This bot demonstrates the capability of Selenium to automate repetitive tasks on highly dynamic social media platforms.

## How to Run

**CRITICAL PREREQUISITES:**

- **WebDriver:** This project requires **Selenium WebDriver** and a compatible web browser (e.g., Chrome). You'll need the corresponding WebDriver executable.
    
    - **Chrome:** Download `chromedriver` from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/ "null") (match your Chrome browser version). Place the executable in a directory included in your system's PATH, or use `webdriver_manager` as shown in the code.
        
- **Instagram Login:** Automating Instagram login is notoriously difficult due to CAPTCHAs, 2FA, and dynamic elements. It's often **highly recommended to manually log into Instagram in your browser first** before running the script, and let Selenium use the existing session. If you attempt to automate login, be prepared for it to be fragile and require frequent updates.
    

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_052_Instagram_Follower_Bot
    ```

3. **Install Required Libraries:**
    
    ```
    pip install selenium webdriver-manager
    ```
    
4. **Configure Parameters:** Open the `main.py` file and replace the placeholder values for:
    
    - `INSTAGRAM_USERNAME`, `INSTAGRAM_PASSWORD` (your Instagram credentials)
        
    - `TARGET_ACCOUNT` (the Instagram account whose followers you want to follow)
        
    - **Crucially, you will need to inspect the HTML of Instagram to find the correct CSS selectors or XPaths for all interactive elements (login fields, buttons, follower counts, "Follow" buttons, pop-up close buttons).** The provided selectors are examples and are highly likely to change.
        
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will open a browser window and attempt to automate the specified actions. Keep an eye on the browser to see if pop-ups are blocking interactions or if selectors need updating.)_
    

## Demo

When you run the script, a new Chrome (or chosen browser) window will open. The bot will:

1. Navigate to Instagram.
    
2. Attempt to log in.
    
3. Navigate to the `TARGET_ACCOUNT`'s profile.
    
4. Click on the "Followers" count.
    
5. Scroll down the follower list to load more users.
    
6. Iterate through the loaded followers and click their "Follow" buttons.
    
7. Handle various pop-ups that might appear.
    
8. Finally, it will close the browser.
    

## Ethical Considerations & Disclaimer

- **Terms of Service:** Automating interactions on platforms like Instagram **violates their Terms of Service**. Use this knowledge responsibly and at your own risk. Automated accounts can be detected and banned.
    
- **Bot Detection:** Instagram has sophisticated bot detection mechanisms. This script may stop working if the website structures or anti-bot measures change.
    
- **Fragility:** Web automation scripts, especially on dynamic social media sites, are inherently fragile and require frequent updates as the target website evolves.
    
- **Rate Limits:** Instagram has rate limits for actions like following. Rapidly following many users can lead to temporary blocks or account suspension.
    
- **Privacy:** Be mindful of privacy when interacting with other users' profiles.
    

## Concepts Learned

- **Advanced Web Automation:** Complex interaction with dynamic web applications.
    
- **Scrolling Automation:** Programmatically scrolling to load more content.
    
- **Handling Pop-ups/Modals:** Strategies for dismissing various types of overlays.
    
- **Robust Element Locators:** Techniques for finding elements on highly dynamic pages.
    
- **Error Handling in Automation:** Making scripts more resilient to unexpected scenarios.
    
- **Social Media Automation Challenges:** Understanding the difficulties and risks involved.

## Author

[Musn0o](https://github.com/Musn0o)