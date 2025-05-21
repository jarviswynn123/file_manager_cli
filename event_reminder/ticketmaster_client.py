from dotenv import load_dotenv
import os
import requests

def get_user_info():
    load_dotenv()
    api_token = os.getenv("EVENTBRITE_API_TOKEN")

    url = "https://www.eventbriteapi.com/v3/users/me/"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("JSON Response")
    print(response.json())
    

def get_events(start_date, end_date):



    
get_user_info()