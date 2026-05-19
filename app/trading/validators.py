def validate_symbol(symbol: str):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs allowed.")

def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

def validate_side(side: str):
    valid_sides = ["BUY", "SELL"]

    if side.upper() not in valid_sides:
        raise ValueError("Side must be BUY or SELL.")