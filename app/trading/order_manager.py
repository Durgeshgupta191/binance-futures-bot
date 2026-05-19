from binance.enums import *
from app.client.binance_client import get_client
from app.trading.validators import (
    validate_symbol,
    validate_quantity,
    validate_side
)
from app.utils.logger import logger


class OrderManager:

    def __init__(self):
        self.client = get_client()

    def place_market_order(self, symbol, side, quantity):

        try:
            validate_symbol(symbol)
            validate_quantity(quantity)
            validate_side(side)

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

            logger.info(f"Order placed successfully: {order}")

            return order

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise