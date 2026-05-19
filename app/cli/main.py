from colorama import Fore, init
from app.trading.order_manager import OrderManager

init(autoreset=True)

def start_cli():

    print(Fore.CYAN + "\n=== Binance Futures Testnet Bot ===\n")

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    quantity = float(input("Enter Quantity: "))

    manager = OrderManager()

    try:
        result = manager.place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity
        )

        print(Fore.GREEN + "\nOrder Executed Successfully!")
        print(result)

    except Exception as e:
        print(Fore.RED + f"\nError: {str(e)}")