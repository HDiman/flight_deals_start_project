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

# Google Sheet: getting information from sheet
sheet_endpoint = "https://api.sheety.co/afd998d332f85c1909b2035741e296da/flightDeals/prices"
response_sheet = requests.get(url=sheet_endpoint)
response = response_sheet.json()
print(response["prices"][0])
print(response["prices"][0]["city"])

# Google Sheet: adding new information to sheet
sheet_endpoint = "https://api.sheety.co/afd998d332f85c1909b2035741e296da/flightDeals/prices"

response_sheet = requests.get(url=sheet_endpoint)
response = response_sheet.json()
print(response["prices"][0])

# response_sheet = requests.get(url=sheet_endpoint, headers=headers)



