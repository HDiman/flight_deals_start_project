from pprint import pprint
from flight_search import *

ticket_price = FlightSearch()

def one_way(start, end):
    ticket_price.a_city = start
    ticket_price.b_city = end
    ticket_price.search_flight(365)

    print(ticket_price.lowest_price)
    print(f"{len(ticket_price.lowest_price)} days")
    print(f"Lowest price is: {min(ticket_price.lowest_price)} rub.")

moscow = "MOW"
moscow_vnukovo = "VKO"
moscow_sheremetyevo = "SVO"
moscow_domodedovo = "DME"
kaliningrad = "KGD"

one_way(start=moscow, end=kaliningrad) # trip to kaliningrad
one_way(start=kaliningrad, end=moscow_vnukovo) # trip to moscow
