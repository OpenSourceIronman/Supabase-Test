import os
from twilio.rest import Client
from supabase import create_client, Client as SupabaseClient
import random
import sys

# Twilio and Supabase credentials
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

SUPABASE_URL = 'your_supabase_url'
SUPABASE_KEY = 'your_supabase_api_key'

# Initialize Supabase client
supabase: SupabaseClient = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_verification_code(phone_number: str) -> str:
    """Send an SMS verification code using Twilio."""
    verification_code = str(random.randint(100000, 999999))
    
    message = twilio_client.messages.create(
        body=f"Your verification code is {verification_code}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )

    print(f"Sent SMS to {phone_number}: {message.sid}")
    return verification_code


def signup_user(phone_number: str, verification_code: str):
    """Signup user after verifying the code."""
    print(f"Enter the verification code sent to {phone_number}: ")
    user_input_code = input()

    if user_input_code == verification_code:
        # Store user information in Supabase
        data = {"phone_number": phone_number}
        response = supabase.table("users").insert(data).execute()
        
        if response.status_code == 201:
            print("User signed up successfully!")
        else:
            print(f"Error signing up user: {response}")
    else:
        print("Invalid verification code. Signup failed.")


def main():
    print("Welcome to the SMS Signup CLI App!")
    
    phone_number = input("Please enter your phone number (with country code): ")
    
    # Send verification code
    verification_code = send_verification_code(phone_number)
    
    # Verify and sign up the user
    signup_user(phone_number, verification_code)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
