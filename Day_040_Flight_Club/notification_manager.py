# --- notification_manager.py ---
# This file defines the NotificationManager class for sending SMS via Twilio.

from twilio.rest import Client

# Twilio SMS Service Configuration
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Replace with your Account SID
TWILIO_AUTH_TOKEN = "your_auth_token_here" # Replace with your Auth Token
TWILIO_PHONE_NUMBER = "+1234567890" # Replace with your Twilio phone number
MY_PHONE_NUMBER = "+19876543210" # Replace with your personal phone number

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        """
        Sends an SMS message using Twilio.
        """
        print("Attempting to send SMS...")
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=MY_PHONE_NUMBER
            )
            print(f"SMS sent successfully. Message SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS. Check Twilio credentials or network. Error: {e}")

