from pprint import pprint
from flight_search import *

ticket_price = FlightSearch()

ticket_price.a_city = "KGD"
ticket_price.b_city = "VKO"

ticket_price.search_flight(10)

print(ticket_price.lowest_price)
print(f"{len(ticket_price.lowest_price)} days")
print(f"Lowest price is: {min(ticket_price.lowest_price)}")

