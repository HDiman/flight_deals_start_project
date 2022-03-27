from datetime import datetime
from datetime import timedelta
from flight_search import *


class FlightData:
    def __init__(self):
        self.today = datetime.now()
        self.back_flight_date = FlightSearch()

    def search_day(self, delta):
        if self.back_flight_date.good_price_day > self.today.strftime('%Y-%m-%d'):
        next_day = self.today + timedelta(days=delta)
        return next_day.strftime('%Y-%m-%d')
