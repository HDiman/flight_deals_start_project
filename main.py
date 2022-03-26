import requests
from data_manager import *

a_city = rows['1']["iataCode"]
b_city = rows['2']["iataCode"]

print(a_city)
print(b_city)

# X-Access-Token
token = "19da7d9afb744a1919d4468e2878003c"
# URL
url = f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin={a_city}&destination={b_city}&currency=rub&departure_at=2022-03-26&return_at=2022-03-29&sorting=price&direct=true&limit=10&token={token}"


response_end = requests.get(url=url)
response = (response_end.json())['data']
print(response)

