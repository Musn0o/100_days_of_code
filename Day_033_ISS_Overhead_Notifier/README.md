# Day_033_ISS_Overhead_Notifier

This project is part of my 100 Days of Code journey.

## Project Description

On Day 33, I built an **ISS Overhead Notifier** that tells you when the International Space Station (ISS) is overhead and visible from your location. This project focuses on working with **APIs** to fetch real-time data and using Python to send email notifications.

- **API Integration:** Fetches the current position of the ISS from the Open Notify API.
- **Sunrise/Sunset Data:** Retrieves sunrise and sunset times for your location from the OpenWeatherMap API.
- **Location Check:** Compares the ISS position with your current location.
- **Visibility Check:** Determines if it's dark enough to see the ISS.
- **Email Notification:** Sends an email when the ISS is overhead and visible.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_033_ISS_Overhead_Notifier
    ```

3. **Configure Email Credentials and Location:**
    - Open `main.py` and replace `MY_EMAIL`, `MY_PASSWORD`, `MY_LAT`, and `MY_LONG` with your actual email credentials and latitude/longitude.

4. **Run the Main Python Script:**
    
    ```
    python main.py
    ```

## Demo

When you run the script, it will continuously check the position of the ISS and your local time. If the ISS is within 5 degrees of your current location and it's dark outside, you will receive an email notification.

## Concepts Learned

- **API Endpoints:** Making GET requests to retrieve data from APIs.
- **JSON Data:** Parsing JSON responses from APIs.
- **`requests` module:** Sending HTTP requests.
- **`datetime` module:** Working with time and converting timestamps.
- **`smtplib`:** Sending email notifications.
- **Environmental Variables:** (Optional) Storing sensitive information like API keys and email passwords securely.

## Author

[Musn0o](https://github.com/Musn0o)
