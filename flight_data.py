import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    pass


# # Поддерживаемые направления
# url = "http://map.aviasales.ru/supported_directions.json?"
# param = "http://map.aviasales.ru/supported_directions.json?origin_iata=LED&one_way=false&locale=ru"

'''
Параметры запроса

origin_iata — IATA-код аэропорта/города, из которого ищутся билеты. 
IATA-код указывается буквами верхнего регистра, например MOW.
one_way — «true» для перелетов в одну сторону, «false» — для туда-обратно.
locale — язык поиска.

'''

# Directions
# sheet_endpoint = "https://api.sheety.co/afd998d332f85c1909b2035741e296da/flightDeals/prices"

# Поддерживаемые направления
url = "http://map.aviasales.ru/supported_directions.json?"
param = "http://map.aviasales.ru/supported_directions.json?origin_iata=LMOW&one_way=false&locale=ru"

# Google Sheet: getting information from sheet
response = requests.get(url=param)
print(response.text)
