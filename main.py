from flight_search import *
from data_manager import *

fl_search = FlightSearch()
dt_manager = DataManager()
days_to_search = 30

def getting_price_and_date(a, b):
    # Cheapest flight ticket from A to B
    start = dt_manager.rows[from_city]['iataCode']
    end = dt_manager.rows[to_city]['iataCode']

    fl_search.one_way(start=start, end=end, days=days_to_search)
    print(f"Flight from {dt_manager.rows[str(from_city)]['city']} to {dt_manager.rows[to_city]['city']}")


# From Moscow to Kaliningrad
from_city = '1'
to_city = '5'
getting_price_and_date(a=from_city, b=to_city)

# # From Kaliningrad to Moscow
# from_city = '1'
# to_city = '5'
# getting_price_and_date(a=from_city, b=to_city)