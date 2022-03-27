from flight_search import *
from data_manager import *

fl_search = FlightSearch()
dt_manager = DataManager()
days_to_search = 365

from_city = '1'
where_city = '5'

# Cheapest flight ticket from Moscow Kaliningrad
start = dt_manager.rows[from_city]['iataCode']
end = dt_manager.rows[where_city]['iataCode']

fl_search.one_way(start=start, end=end, days=days_to_search)
print(f"Flight from {dt_manager.rows[str(from_city)]['city']} to {dt_manager.rows[where_city]['city']}")
