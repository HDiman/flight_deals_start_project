import requests
from dotenv import load_dotenv
import os
from data_manager import *
from pprint import pprint
from datetime import datetime
from datetime import timedelta

# -- Loading virtual env
load_dotenv()

class FlightSearch:
    def __init__(self):
        self.a_city = "MOW"
        self.b_city = "KGD"
        self.lowest_price = []

    def search_flight(self, days):
        # Creating loop for 187 days
        for i in range(days):
            # -- Creating today's date and next days
            self.date_a = datetime.now() + timedelta(days=i+1)
            self.date_b = datetime.now() + timedelta(days=i+2)
            self.start_day = self.date_a.strftime('%Y-%m-%d')
            self.back_day = self.date_b.strftime('%Y-%m-%d')
            # print(search_day)

            # -- Getting inf about flights
            API_token = os.getenv("API_token")
            headers = {'x-access-token': API_token}

            end_point = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
            params = {
                "currency": "rub",
                "origin": self.a_city,
                "destination": self.b_city,
                "departure_at": self.start_day,
                "return_at": self.back_day,
                "direct": "true",
                "limit": "",
                "sorting": "price",
            }
            # Find price back
            response_end = requests.get(url=end_point, params=params, headers=headers)
            response = response_end.json()['data'][0]['price']
            self.lowest_price.append(response)


# ticket_price = FlightSearch()
# ticket_price.search_flight(30)
#
# print(ticket_price.lowest_price)
# pprint(min(ticket_price.lowest_price))
