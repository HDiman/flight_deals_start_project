import requests
from dotenv import load_dotenv
import os
from data_manager import *
from pprint import pprint
from datetime import datetime
from datetime import timedelta


# -- Loading virtual env
load_dotenv()

# -- Adding new values
a_city = rows['1']["iataCode"] # MOW
b_city = rows['2']["iataCode"] # KGD
lowest_price = []

# Creating loop for 187 days
for i in range(187):
    # -- Creating today's date and next days
    date = datetime.now() + timedelta(days=i+1)
    search_day = date.strftime('%Y-%m-%d')
    # print(search_day)

    # -- Getting inf about flights
    API_token = os.getenv("API_token")
    headers = {'x-access-token': API_token}

    end_point = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
    params = {
        "currency": "rub",
        "origin": a_city,
        "destination": b_city,
        "departure_at": search_day,
        "return_at": "",
        "direct": "true",
        "limit": "",
        "sorting": "price",
        }

    response_end = requests.get(url=end_point, params=params, headers=headers)
    response = response_end.json()['data'][0]['price']
    lowest_price.append(response)

print(lowest_price)
pprint(min(lowest_price))

