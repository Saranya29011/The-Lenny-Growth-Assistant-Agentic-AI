from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Connected!")

try:
    response = supabase.table("sessions").select("*").execute()
    print(response.data)
except Exception as e:
    print(e)