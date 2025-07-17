# Day_053_Data_Entry_Job_Automation

This project is part of my 100 Days of Code journey.

## Project Description

On Day 53, the focus was on building a **Data Entry Automation Bot** that combines web scraping with automated form filling. This project demonstrates how to extract specific data from one website and then programmatically enter that data into a form on another website (e.g., a Google Form). Key concepts covered include:

1. **Web Scraping (Beautiful Soup & Requests):**
    
    - Making HTTP GET requests to a target website (e.g., property listings).
        
    - Parsing HTML content to extract structured data (e.g., addresses, prices, links).
        
2. **Web Automation (Selenium WebDriver):**
    
    - Controlling a web browser to navigate to a data entry form (e.g., a Google Form).
        
    - Locating specific form fields (input boxes, text areas) and buttons.
        
    - Sending extracted data to these form fields (`send_keys`).
        
    - Clicking the submit button.
        
3. **Data Flow Integration:** Seamlessly passing data from the scraping phase to the automation (form-filling) phase.
    
4. **Looping for Multiple Entries:** Automating the process of filling and submitting the form for multiple data entries (e.g., for each property scraped).
    
5. **Handling Dynamic Elements & Delays:** Using `time.sleep()` or explicit waits to ensure elements are loaded and interactive before attempting to interact with them.
    

This bot showcases a powerful application of web automation for automating repetitive data entry tasks, saving significant manual effort.

## How to Run

**CRITICAL PREREQUISITES:**

- **WebDriver:** This project requires **Selenium WebDriver** and a compatible web browser (e.g., Chrome). You'll need the corresponding WebDriver executable.
    
    - **Chrome:** Download `chromedriver` from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/ "null") (match your Chrome browser version). Place the executable in a directory included in your system's PATH, or use `webdriver_manager` as shown in the code.
        
- **Target Website:** Choose a website from which you want to scrape data (e.g., a real estate listing site).
    
- **Google Form:** Create your own Google Form with fields that correspond to the data you want to scrape (e.g., "Address", "Price", "Link"). Make sure the form is publicly accessible for submissions.
    

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_053_Data_Entry_Job_Automation
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install requests beautifulsoup4 selenium webdriver-manager
    ```
    
4. **Configure Parameters:** Open the `main.py` file and replace the placeholder values for:
    
    - `ZILLOW_URL` (the URL of the property listing site you want to scrape).
        
    - `GOOGLE_FORM_URL` (the URL of your Google Form for data entry).
        
    - **Crucially, you will need to inspect the HTML of both the scraping target website and your Google Form to find the correct CSS selectors or XPaths for all data points (addresses, prices, links) and form fields (input boxes, submit button).** The provided selectors are examples and are highly likely to change.
        
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will open a browser window and attempt to automate the specified actions. Keep an eye on the browser to see the scraping and form-filling process.)_
    

## Demo

When you run the script, a browser window will open.

1. It will first navigate to the specified property listing URL (e.g., Zillow).
    
2. It will scrape the addresses, prices, and links of the properties.
    
3. Then, for each scraped property, it will:
    
    - Navigate to your Google Form.
        
    - Fill in the "Address," "Price," and "Link" fields with the scraped data.
        
    - Submit the form.
        
    - Repeat for all properties.
        

You can then check your Google Sheet (linked to your Google Form) to see the automatically entered data.

## Ethical Considerations & Disclaimer

- **Terms of Service:** Be aware that scraping websites and automating form submissions may violate their terms of service. Use this knowledge responsibly.
    
- **Rate Limiting:** Avoid sending too many requests too quickly, which can lead to IP bans or detection.
    
- **Fragility:** Web automation scripts are inherently fragile and require frequent updates as target website structures change.
    

## Concepts Learned

- **Full Automation Workflow:** Combining web scraping and web automation for a complete data pipeline.
    
- **Data Extraction & Transformation:** Getting raw data from one source and formatting it for another.
    
- **Iterative Automation:** Looping through a list of data to perform repetitive form submissions.
    
- **Robust Element Locators:** Using precise selectors for both scraping and form filling.
    
- **Handling Network & UI Delays:** Implementing waits for page loads and element interactions.

## Author

[Musn0o](https://github.com/Musn0o)