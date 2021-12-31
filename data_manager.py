import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ['FLIGHT_DEAL_SHEETY_ENDPOINT']


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["flights"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "flight": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def update_lowest_price(self, id, price):
        new_data = {
            "flight": {
                "lowestPrice": price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{id}",
            json=new_data
            )
