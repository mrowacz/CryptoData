import re
import json
import requests

class Stock:
    def __init__(self):
        self.API_ADDR = "https://api.binance.com"
        self.EXCHANGE_INFO="/api/v1/exchangeInfo"
        self.TICKER="/api/v1/ticker/24hr"
        self.market_regex = "^(.+)ETH$"
        self.markets = {}
        self.get_markets()

    def get_markets(self):
        self.markets = {}
        r = requests.get(self.API_ADDR + self.EXCHANGE_INFO)
        if r.status_code == 200:
            js = json.loads(r.text)
            for symbol in js["symbols"]:
                # get only related with eth
                m = re.search(self.market_regex, symbol["symbol"])
                if m:
                    self.markets[m.group(1)] = symbol
            print("Found " + str(len(self.markets)))

    def get_ticker(self, coin):
        payload = {"symbol": coin}
        r = requests.get(self.API_ADDR + self.TICKER, params=payload)
        if r.status_code == 200:
            return json.loads(r.text)
        return None

    def get_volumens(self):
        with open("volumes.dat", "w") as f:
            for e in self.markets:
                print("Fetching ticker for " + e)
                js = self.get_ticker(self.markets[e]["symbol"])
                f.write(e + " " + js["volume"] + "\n")
