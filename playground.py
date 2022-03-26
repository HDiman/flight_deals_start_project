from data_manager import *

print(rows['1']["city"])
print(rows['2']["city"])

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
