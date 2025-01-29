import time
import requests

# Phantom Wallet Setup
WALLET_ADDRESS = "YOUR_PHANTOM_WALLET_HERE"

# Trading Configurations
TRADE_AMOUNT = 0.01  # Amount per trade
STOP_LOSS = 5  # Stop loss percentage
TAKE_PROFIT = 20  # Take profit percentage

# Simple Trading Function
def trade():
    print(f"Starting trade for wallet: {WALLET_ADDRESS}")
    while True:
        price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd").json()["solana"]["usd"]
        print(f"Current SOL price: ${price}")
        time.sleep(5)  # Wait before next check

# Run Trading Bot
trade()
