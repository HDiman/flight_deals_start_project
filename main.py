from pprint import pprint
from flight_search import *
from data_manager import *

fl_search = FlightSearch()
dt_manager = DataManager()
days_to_search = 10

moscow = "MOW"
moscow_vnukovo = "VKO"
moscow_sheremetyevo = "SVO"
moscow_domodedovo = "DME"
kaliningrad = "KGD"

fl_search.one_way(start=kaliningrad, end=moscow_vnukovo, days=days_to_search) # trip to moscow
# fl_search.one_way(start=moscow_domodedovo, end=kaliningrad, days=days_to_search) # trip to kaliningrad

