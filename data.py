import random
import time

# Simulated stock data
stocks = [
    {"name": "ABC Pvt Ltd", "symbol": "A", "price": 100.0, "historical_prices": []},
    {"name": "XYZ LLC", "symbol": "B", "price": 150.0, "historical_prices": []},
    {"name": "GHI Ltd", "symbol": "C", "price": 75.0, "historical_prices": []},
]

# Function to simulate price changes and update historical prices
def simulate_price_changes():
    while True:
        for stock in stocks:
            price_change = random.uniform(-5, 5)
            stock["price"] += price_change
            stock["historical_prices"].append(stock["price"])
            if len(stock["historical_prices"]) > 100:
                stock["historical_prices"].pop(0)
        time.sleep(5)

def get_stock_data_by_symbol(symbol):
    for stock in stocks:
        if stock['symbol'] == symbol:
            return stock
    return None
