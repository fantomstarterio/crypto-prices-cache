# Crypto Price Fetcher

This project fetches cryptocurrency prices (Bitcoin, Ethereum, and DAI) from the CoinGecko API every hour and commits the data to this repository. It uses GitHub Actions to automate the process.

## Files

- `fetch_crypto_prices.py`: A Python script that fetches the latest cryptocurrency prices and saves them to a JSON file.
- `.github/workflows/update_crypto_prices.yml`: A GitHub Actions workflow that runs the Python script every hour and commits the changes.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/crypto-price-fetcher.git
   cd crypto-price-fetcher
    ```

2. Install the required Python packages:

    ```bash
    pip install requests
    ```

3. Run the Python script to fetch the latest cryptocurrency prices:

    ```bash
    python fetch_crypto_prices.py
    ```

## GitHub Actions

The GitHub Actions workflow is defined in .github/workflows/update_crypto_prices.yml. It is triggered every hour and performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs the requests library.
4. Runs the fetch_crypto_prices.py script.
5. Commits and pushes the crypto_prices.json file to the repository.

If the workflow fails, it will retry after 5 minutes.

## Usage

You can use the crypto_prices.json file in your application to get the latest cryptocurrency prices without hitting the CoinGecko API directly. This helps to avoid rate limiting issues.

## Customization

If you want to fetch prices for different cryptocurrencies or use a different API, modify the fetch_crypto_prices.py script accordingly.
