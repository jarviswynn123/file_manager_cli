from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("TICKETMASTER_API_KEY")

url = f"https://app.ticketmaster.com/discovery/v2/events.json?city=Atlanta&countryCode=US&apikey={api_key}"

response = requests.get(url)
print("Status Code:", response.status_code)
print("JSON Response")
data = response.json()
print(json.dumps(data, indent=2))