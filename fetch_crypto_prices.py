import requests
import json
import os
from datetime import datetime
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get BASE_URL from environment variable
BASE_URL = os.getenv('BASE_URL')

# Setup retry strategy for network issues
retry_strategy = Retry(
    total=3,  # Retry 3 times
    backoff_factor=1,  # Wait between retries (exponential backoff)
    status_forcelist=[429, 500, 502, 503, 504],  # Retry on these HTTP status codes
    method_whitelist=["GET"]
)

# Attach the retry strategy to a session
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

def fetch_crypto_prices(crypto_ids=["dai", "ethereum", "bitcoin"], currency="usd"):
    """
    Fetch the latest crypto prices for the given crypto_ids.
    """
    if BASE_URL is None:
        logging.error("BASE_URL is not set in environment variables")
        return False
    
    url = f"{BASE_URL}/simple/price?ids={','.join(crypto_ids)}&vs_currencies={currency}"
    
    try:
        logging.info(f"Requesting crypto prices from {url}")
        response =_for_status()  # Raises exception for 4xx/5xx responses
        data = response.json()

        # Validate response
        if not all(crypto in data for crypto in crypto_ids):
            logging.error(f"Response is missing expected keys: {crypto_ids}")
            return False
        
        # Save the data with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'crypto_prices_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"Data successfully saved to {filename}")
        return True

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    success = fetch_crypto_prices()
    if not success:
        logging.error("Failed to fetch data")
        exit(1)
