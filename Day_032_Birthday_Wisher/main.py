from datetime import datetime
import pandas as pd
import random
import smtplib
import os

# --- Secure Credentials from Environment Variables ---
MY_EMAIL = os.environ["EMAIL_USER"]  # Will raise KeyError if missing
MY_PASSWORD = os.environ["EMAIL_PASS"]  # Explicitly requires these vars

PLACEHOLDER = "[NAME]"

# --- Get Today's Date ---
today = datetime.now()
today_tuple = (today.month, today.day)

# --- Load and Clean Birthday Data ---
try:
    data = pd.read_csv("Day_032_Birthday_Wisher/birthdays.csv").dropna()
    birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}
except FileNotFoundError:
    print("Error: 'birthdays.csv' file not found.")
    exit()

# --- Check for Matching Birthday ---
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # --- Try to Load a Random Letter Template ---
    file_path = (
        f"Day_032_Birthday_Wisher/letter_templates/letter_{random.randint(1, 3)}.txt"
    )
    try:
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(PLACEHOLDER, birthday_person["name"])
    except FileNotFoundError:
        print(f"Template file '{file_path}' not found. Using default message.")
        contents = f"Happy Birthday, {birthday_person['name']}!"

    # --- Try to Send Email ---
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            if not MY_EMAIL or not MY_PASSWORD:
                raise ValueError("Email credentials not configured in environment")
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday, {birthday_person['name']}!\n\n{contents}",
            )
        print(
            f"✅ Email sent to {birthday_person['name']} at {birthday_person['email']}"
        )
    except Exception as e:
        print("❌ Failed to send email:", e)
else:
    print("🎈 No birthdays today.")
