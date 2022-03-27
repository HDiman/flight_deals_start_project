# # -- Adding new values
# a_city = rows['1']["iataCode"] # MOW
# b_city = rows['2']["iataCode"] # KGD
#


# for i in range(187):
#     # -- Creating today's date and next days
#     date_a = datetime.now() + timedelta(days=i+1)
#     date_b = datetime.now() + timedelta(days=i+2)
#     start_day = date_a.strftime('%Y-%m-%d')
#     back_day = date_b.strftime('%Y-%m-%d')
#     # print(search_day)
#
#     # -- Getting inf about flights
#     API_token = os.getenv("API_token")
#     headers = {'x-access-token': API_token}
#
#     end_point = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
#     params = {
#         "currency": "rub",
#         "origin": a_city,
#         "destination": b_city,
#         "departure_at": start_day,
#         "return_at": "",
#         "direct": "true",
#         "limit": "",
#         "sorting": "price",
#     }
#     # Find price back
#     response_end = requests.get(url=end_point, params=params, headers=headers)
#     response = response_end.json()['data'][0]['price']
#     lowest_price.append(response)
#














# from dotenv import load_dotenv
# import os
#
# # -- Loading virtual env
# load_dotenv()
#
# # -- API_token from .env
# API_token = os.getenv("API_token")
# headers = {'x-access-token': API_token}

# -- Getting inf about flights
# API_token = os.getenv("API_token")
# headers = {'x-access-token': API_token}
#
# end_point = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
# params = {
#     "origin": a_city,
#     "destination": b_city,
#     "currency": "rub",
#     "departure_at": "2022-03-27",
#     "return_at": "2022-03-29",
#     "sorting": "price",
#     "direct": "true",
#     "limit": "",
# }

# response_end = requests.get(url=end_point, params=params, headers=headers)
# response = response_end.json()['data']
# pprint(response)













# from data_manager import *
#
# print(rows['1']["city"])
# print(rows['2']["city"])

# URL search through aviasales
# url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=MOW&destination=DXB&currency=usd&departure_at=2022-03-01&return_at=2022-03-10&sorting=price&direct=true&limit=10&token=РазместитеЗдесьВашТокен"
# url = f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin={a_city}&destination={b_city}&currency=rub&departure_at=2022-03-26&return_at=2022-03-29&sorting=price&direct=true&limit=10&token={token}"


# import requests

#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

"""
APIs Required
Google Sheet Data Management - https://sheety.co/
Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
Twilio SMS API - https://www.twilio.com/docs/sms
"""

# ---------------------------------------------------------------

# New values for Google Sheet Block
# sheet_endpoint = "https://api.sheety.co/afd998d332f85c1909b2035741e296da/flightDeals/prices"
#
# # Google Sheet: getting information from sheet
# response_sheet = requests.get(url=sheet_endpoint)
# response = response_sheet.json()
# print(response)
# print(response["prices"][0]["city"])

# ---------------------------------------------------------------

# Google Sheet: adding new information to sheet CDG
# sheet_endpoint = sheet_endpoint + "/2"
# body = {
#     "price": {
#         "iataCode": "CDG",
#     }
# }
# response_sheet = requests.put(url=sheet_endpoint, json=body)
# response = response_sheet.json()
# print(response)

# ---------------------------------------------------------------

# Google Sheet: adding new information to sheet
# new_cities = ["Kaliningrad", "Saratov", "Saint Petersburg"]
# new_codes = ["KGD", "GSV", "LED"]
# new_prices = ["2000", "2000", "2000"]
# i = 2
# sheet_endpoint = sheet_endpoint + f"/{i+2}"
# body = {
#     "price": {
#         "city": new_cities[i],
#         "iataCode": new_codes[i],
#         "lowestPrice": new_prices[i],
#     }
# }
# response_sheet = requests.put(url=sheet_endpoint, json=body)
# response = response_sheet.json()
# print(response)

# ---------------------------------------------------------------

import asyncio
import time

async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')


async def main():
    task = asyncio.create_task(async_func())
    await task


asyncio.run(main())
