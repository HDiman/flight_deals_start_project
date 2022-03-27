import requests
from dotenv import load_dotenv
import os
from data_manager import *
from pprint import pprint
from datetime import datetime
from datetime import timedelta
from flight_search import *


# -- Adding new values
a_city = rows['1']["iataCode"] # MOW
b_city = rows['2']["iataCode"] # KGD



ticket_price = FlightSearch()

# ticket_price.b_city = "GSV"
ticket_price.search_flight(10)

print(ticket_price.lowest_price)
pprint(min(ticket_price.lowest_price))

