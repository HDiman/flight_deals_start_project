import requests

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

