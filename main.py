EMAIL = 0
PHONE = 1

import os
from supabase import create_client, Client
#from twilio.rest import Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
#print(f"URI = {url} and KEY = {key}")
supabase: Client = create_client(url, key)


def sign_up(type, username, password):
    if (type == EMAIL):
        response = supabase.auth.sign_up(
            {"email": "blaze.d.a.sanders@gmail.com", "password": "password"}
        )
        print(f"Email Sign Up: {response}")
    
    if (type == PHONE):
        response = supabase.auth.sign_up(
            {"phone": "17196390839", "password": "password"}
        )
        print(f"Phone Sign Up: {response}")


response = supabase.auth.sign_in_with_password(
    {"phone": "+17196390839", "password": "password"}
)




response = supabase.table("Vehicles").select("*").execute()
print(f"All Vehicles in database: {response}")

#response = (
#    supabase.table("Vehicles")
#    .insert({"id": 2, "created_at": "2024-08-23 21:58:58.788+00", "make": "Tesla", "model": "Cybertruck", "year":"2024", "color": 7, "vin": "RN113395937"})
#    .execute()
#)
