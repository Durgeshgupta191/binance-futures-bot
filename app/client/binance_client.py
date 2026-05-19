from binance.client import Client
from app.config.settings import API_KEY, API_SECRET

def get_client():
    client = Client(API_KEY, API_SECRET)

    # Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client