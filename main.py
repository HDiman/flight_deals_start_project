import requests
from dotenv import load_dotenv
import os
from data_manager import *

load_dotenv()

a_city = rows['1']["iataCode"]
b_city = rows['2']["iataCode"]

print(a_city)
print(b_city)

# X-Access-Token
API_token = os.getenv("API_token")
headers = {'x-access-token': API_token}
# URL
end_point = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
params = {
    "origin": a_city,
    "destination": b_city,
    "currency": "rub",
    "departure_at": "2022-03-27",
    "return_at": "2022-03-29",
    "sorting": "price",
    "direct": "true",
    "limit": "10",
    }

response_end = requests.get(url=end_point, params=params, headers=headers)
response = response_end.json()['data']
print(response)

