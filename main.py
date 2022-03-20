import requests

rows = {
    "1": {
        "city": "Kaliningrad",
        "iataCode": "KGD",
        "lowest_price": "2000",
    },
    "2": {
        "city": "Saratov",
        "iataCode": "GSV",
        "lowest_price": "2000",
    },
    "3": {
        "city": "Saint Petersburg",
        "iataCode": "LED",
        "lowest_price": "2000",
    },
}

print(rows['1']["city"])
