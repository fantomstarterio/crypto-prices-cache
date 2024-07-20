import requests
import json
import os
from datetime import datetime

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=dai,ethereum,bitcoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Save the data to a JSON file
        with open('crypto_prices.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False

if __name__ == "__main__":
    success = fetch_crypto_prices()
    if not success:
        print("Failed to fetch data")
        exit(1)