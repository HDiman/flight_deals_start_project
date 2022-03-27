class DataManager:
    def __init__(self):
        self.rows = {
            "1": {
                "city": "Moscow",
                "iataCode": "MOW",
                "lowest_price": "2000",
            },
            "2": {
                "city": "Kaliningrad",
                "iataCode": "KGD",
                "lowest_price": "2000",
            },
            "3": {
                "city": "Saratov",
                "iataCode": "GSV",
                "lowest_price": "2000",
            },
            "4": {
                "city": "Saint-Petersburg",
                "iataCode": "LED",
                "lowest_price": "2000",
            },
        }

# # -- Adding new values
# a_city = rows['1']["iataCode"] # MOW
# b_city = rows['2']["iataCode"] # KGD