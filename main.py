from flight_search import *
from data_manager import *

fl_search = FlightSearch()
dt_manager = DataManager()
days_to_search = 365

for i in range(4):
    start = dt_manager.rows[str(i+1)]['iataCode']
    end = dt_manager.rows['5']['iataCode']

    fl_search.one_way(start=start, end=end, days=days_to_search)
    print(f"Flight from {dt_manager.rows[str(i+1)]['city']} to {dt_manager.rows['5']['city']}")
