import requests

# New values for Google Sheet Block
sheet_endpoint = "https://api.sheety.co/afd998d332f85c1909b2035741e296da/flightDeals/prices"

# Google Sheet: getting information from sheet
response_sheet = requests.get(url=sheet_endpoint)
response = response_sheet.json()
print(response)

