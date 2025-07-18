import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_overhead():
    try:
        print(f"[{datetime.now()}] Checking ISS position...")
        response = requests.get(
            url="http://api.open-notify.org/iss-now.json", timeout=10
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print("Failed to fetch ISS position:", e)
        return False

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


notified = False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        if not notified:
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL, MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg="Subject:ISS is Overhead\n\nThe ISS is above you in the sky!",
                    )
                print("✅ Notification sent.")
                notified = True
            except Exception as e:
                print("❌ Email failed:", e)
    else:
        notified = False  # Reset when ISS isn't overhead
