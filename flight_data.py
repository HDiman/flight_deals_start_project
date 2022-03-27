from datetime import datetime
from datetime import timedelta

class FlightData:
    def __init__(self):
        self.today = datetime.now()

    def search_day(self, delta):
        next_day = self.today + timedelta(days=delta)
        return next_day.strftime('%Y-%m-%d')
