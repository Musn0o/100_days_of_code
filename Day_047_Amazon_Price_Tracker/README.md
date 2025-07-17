# Day_047_Amazon_Price_Tracker

This project is part of my 100 Days of Code journey.

## Project Description

On Day 47, the focus was on building an **Amazon Price Tracker**. This application leverages web scraping to monitor the price of a specific product on Amazon and sends an email notification if the price drops below a desired threshold. Key concepts covered include:

1. **Web Scraping (Beautiful Soup & Requests):**
    
    - Making HTTP GET requests to Amazon product pages.
        
    - Handling HTTP headers, especially the `User-Agent`, to avoid being blocked by the website.
        
    - Parsing complex HTML structures with `BeautifulSoup` to locate and extract the product's price.
        
2. **Price Extraction and Cleaning:** Extracting the numerical price value from the scraped text, which often includes currency symbols and commas, and converting it to a float.
    
3. **Email Automation (`smtplib`):**
    
    - Setting up an SMTP client to connect to an email server (e.g., Gmail's SMTP).
        
    - Composing and sending automated email notifications.
        
    - Understanding the need for app-specific passwords for email services (e.g., for Gmail).
        
4. **Conditional Alerting:** Implementing logic to compare the current scraped price with a predefined target price.
    
5. **Automation (Conceptual):** Discussing how this script could be run periodically (e.g., using a cron job or cloud scheduler) to continuously monitor prices.
    

The application allows you to track the price of an Amazon product you're interested in and receive an email alert when it becomes affordable.

## How to Run

This project requires an Amazon product URL, a target price, and email credentials for sending notifications.

1. **Choose an Amazon Product:**
    
    - Find a product on Amazon.
        
    - Copy its full URL.
        
2. **Set up Email for Sending:**
    
    - If using Gmail, you'll likely need to generate an "App password" for your account, as direct password login for third-party apps is often blocked for security reasons. (Search "Gmail app password" for instructions).
        
3. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
4. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_047_Amazon_Price_Tracker
    ```

5. **Install Required Libraries:**
    
    ```
    pip install requests beautifulsoup4
    ```
    
6. **Configure Parameters:** Open the `main.py` file and replace the placeholder values for `PRODUCT_URL`, `TARGET_PRICE`, `MY_EMAIL`, `MY_PASSWORD`, and `RECIPIENT_EMAIL` with your actual details.
    
7. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will connect to the Amazon product page, scrape the current price, and compare it to your `TARGET_PRICE`.

- If the current price is below or equal to the `TARGET_PRICE`, it will print a confirmation message to the console and attempt to send an email notification.
    
- If the price is still too high, it will print a message indicating that.
    

```
Checking price for [Product Name]...
Current price: $150.00
Target price: $100.00
Price is still too high. No email sent.
```

OR

```
Checking price for [Product Name]...
Current price: $95.00
Target price: $100.00
Price has dropped! Sending email notification...
Email sent successfully!
```

## Concepts Learned

- **Advanced Web Scraping:** Handling dynamic content and website defenses (like User-Agent).
    
- **Data Parsing and Cleaning:** Extracting numerical data from text and preparing it for comparison.
    
- **Email Automation:** Programmatically sending emails for alerts.
    
- **SMTP Protocol:** Basic understanding of how email clients communicate with mail servers.
    
- **Security for Credentials:** The importance of not hardcoding sensitive information and using app passwords.
    
- **Real-World Automation:** Building a practical tool for personal finance or shopping.

## Author

[Musn0o](https://github.com/Musn0o)