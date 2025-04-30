import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,dogecoin",  # List cryptocurrencies here
    "vs_currencies": "usd"  # Change currency if needed (e.g., "eur", "btc")
}

def get_crypto_prices():
    """ Fetch live crypto prices """
    response = requests.get(COINGECKO_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching prices: {response.status_code}")
        return {"error": "Failed to fetch prices"}
