import requests
from datetime import timezone
import datetime

with open("secrets/space_UUID.txt", "r") as f:
    space_UUID = f.readline()
with open("secrets/token.txt", "r") as f:
    token = f.readline()

connectionString = f"https://paper-trading.lemon.markets/rest/v1/spaces/{ space_UUID }/"
portfolioString = connectionString + "portfolio/"
orderString = connectionString + "orders/"
header = {"Authorization": f"Bearer { token }"}


body = {"isin": None,   "valid_until": None,    "side" : None,   "quantity": 0}
#       US62914V1061    valid_time in seconds   "buy" or "sell"     Integer

request = requests.get(connectionString, data= body, headers= header )

print(request.json())



request = requests.get(portfolioString,
			headers= header)

portfolio = request.json()








# Classes
class Portfolio():
    def __init__(self, space_uuid, token):
        self.portfolio = {}
        self.url = f"https://paper-trading.lemon.markets/rest/v1/spaces/{ space_uuid }/"
        self.header = {"Authorization": f"Bearer { token }"}

    def update(self):
        self.portfolio = requests.get(self.url, headers= self.header).json()

    def get(self):
        return self.portfolio