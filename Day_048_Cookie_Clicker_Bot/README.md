# Day_048_Cookie_Clicker_Bot

This project is part of my 100 Days of Code journey.

## Project Description

On Day 48, the focus was on **Web Automation** using **Selenium WebDriver** by building a bot to play the classic "Cookie Clicker" game. This project introduced and reinforced:

1. **Selenium WebDriver Setup:** Configuring Selenium to control a web browser (e.g., Chrome, Firefox).
    
2. **Browser Automation:** Opening URLs, interacting with web elements, and navigating pages programmatically.
    
3. **Locating Web Elements:** Using various strategies to find elements on a webpage (e.g., by ID, class name, CSS selector, XPath).
    
4. **Simulating Clicks:** Programmatically clicking buttons and other interactive elements.
    
5. **Timing and Delays:** Using Python's `time` module to introduce pauses and control the speed of interactions, crucial for game automation.
    
6. **Game Logic Automation:** Implementing a strategy to continuously click the main cookie and periodically check for and purchase available upgrades.
    
7. **Error Handling (Implicit):** Dealing with elements that might not be immediately available or change their state.
    

The bot automates the process of clicking the cookie and buying upgrades in the Cookie Clicker game, aiming to achieve a high score without manual intervention.

## How to Run

This project requires **Selenium WebDriver** and a compatible web browser (e.g., Chrome, Firefox). You'll also need the corresponding WebDriver executable.

1. **Install WebDriver:**
    
    - **Chrome:** Download `chromedriver` from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/ "null") (match your Chrome browser version). Place the executable in a directory included in your system's PATH, or specify its path in the script.
        
    - **Firefox:** Download `geckodriver` from [Mozilla GitHub](https://github.com/mozilla/geckodriver/releases "null").
        
    - **Edge:** Download `msedgedriver` from [Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "null").
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_048_Cookie_Clicker_Bot
    ```

4. **Install Required Libraries:**
    
    ```
    pip install selenium
    ```
    
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will open a browser window and start playing the game automatically.)_
    

## Demo

When you run the script, a new Chrome (or chosen browser) window will open, navigating to the Cookie Clicker game. The bot will immediately start clicking the large cookie. Every few seconds, it will check the available upgrades and purchase the most expensive one it can afford. This will continue until the game ends (e.g., after a set duration in the script).

## Concepts Learned

- **Browser Automation:** Programmatic control of web browsers.
    
- **Dynamic Web Interaction:** Interacting with elements that change state (e.g., price, availability).
    
- **Web Element Locators:** Mastering various techniques to identify elements on a page.
    
- **Implicit vs. Explicit Waits (Conceptual):** Understanding the need for delays when interacting with dynamic web content.
    
- **Game Automation Strategy:** Developing algorithms to play a simple game.
    
- **Debugging Web Automation:** Troubleshooting issues related to element not found or timing.

## Author

[Musn0o](https://github.com/Musn0o)