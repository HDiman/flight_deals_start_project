from datetime import datetime
from datetime import timedelta

class FlightData:
    def __init__(self):
        self.today = datetime.now()
        self.date_a = self.today + timedelta(days=i+1)
        self.date_b = self.today + timedelta(days=i+2)
        self.start_day = self.date_a.strftime('%Y-%m-%d')
        self.back_day = self.date_b.strftime('%Y-%m-%d')


