import requests

SUPABASE_URL = "https://jnlfelelukyytqsxsfxy.supabase.co/rest/v1/portfolio?select=*"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpubGZlbGVsdWt5eXRxc3hzZnh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgwMTQ5MjYsImV4cCI6MjA1MzU5MDkyNn0.oETFSrSLYGneCS0_MiE1zfPa1DSXguqrtAPLyNu98KM"

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(SUPABASE_URL, headers=headers)

print(response.json())  # Should print your portfolio table data
