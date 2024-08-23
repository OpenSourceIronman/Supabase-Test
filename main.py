import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

print(f"URI = {url} and KEY = {key}")
supabase: Client = create_client(url, key)

