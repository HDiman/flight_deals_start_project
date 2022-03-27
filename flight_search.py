import requests
from dotenv import load_dotenv
import os
from flight_data import *
from data_manager import *


# -- Loading virtual env
load_dotenv()

class FlightSearch:
    def __init__(self):
        self.fl_data = FlightData()
        self.airport_code = DataManager()
        self.back_day = ""
        self.second_start = 0

    def search_flight(self, days):
        # Creating loop for 187 days
        self.ticket_prices = []
        try:
            for i in range(days):
                # -- Creating today's date and next days
                self.start_day = self.fl_data.search_day(i + 1 + self.second_start)
                # print(f"dates: {self.start_day}")
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
                # Find price through requests
                response_end = requests.get(url=end_point, params=params, headers=headers)
                response = response_end.json()['data'][0]['price']
                self.ticket_prices.append(response)
        except IndexError:
            pass

    def one_way(self, start, end, days):
        self.a_city = start
        self.b_city = end
        self.search_flight(days)

        # print(self.ticket_prices)
        print(f"{len(self.ticket_prices)} days")
        good_price = min(self.ticket_prices)
        print(f"Lowest price is: {good_price} rub.")

        # Finding second_start of the lowest value in list
        self.index_min = int(min(range(len(self.ticket_prices)), key=self.ticket_prices.__getitem__))
        self.good_price_day = self.fl_data.search_day(self.index_min + 1 + self.second_start)
        self.second_start = self.index_min
        print(f"Date for flight is: {self.good_price_day}")

