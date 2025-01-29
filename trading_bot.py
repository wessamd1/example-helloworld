#!/usr/bin/env python3

import time
import requests

# Phantom Wallet Setup
WALLET_ADDRESS = "2ipLK4tKSfVg6qJKAb3VHhMQabyrYt8XFgpZE8JLFpRq"

# Trading Configurations
TRADE_AMOUNT = 0.01  # Amount per trade
STOP_LOSS = 5  # Stop loss percentage
TAKE_PROFIT = 20  # Take profit percentage

# Function to get SOL price from CoinGecko
def get_sol_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd")
        price = response.json()["solana"]["usd"]
        return price
    except Exception as e:
        print(f"Error fetching SOL price: {e}")
        return None

# Trading Function
def trade():
    print(f"✅ Starting trading bot for Phantom Wallet: {WALLET_ADDRESS}")
    while True:
        price = get_sol_price()
        if price:
            print(f"💰 Current SOL price: ${price}")
        else:
            print("❌ Error fetching price, retrying...")

        time.sleep(5)  # Check price every 5 seconds

# Run Trading Bot
if __name__ == "__main__":
    trade()
