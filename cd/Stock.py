import re
import time
import json
import requests

class Stock:
    API_ADDR = "https://api.binance.com"
    EXCHANGE_INFO = "/api/v1/exchangeInfo"
    TICKER = "/api/v1/ticker/24hr"
    KLINES = "/api/v1/klines"
    MARKET_REGEX = "^(.+)ETH$"

    def __init__(self):
        self.markets = {}
        self.get_markets()

    def get_markets(self):
        self.markets = {}
        r = requests.get(self.API_ADDR + self.EXCHANGE_INFO)
        if r.status_code == 200:
            js = json.loads(r.text)
            for symbol in js["symbols"]:
                # get only related with eth
                m = re.search(Stock.MARKET_REGEX, symbol["symbol"])
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

    @staticmethod
    def get_klines(coin, interval, start_date):
        payload = {"symbol": coin,
                   "interval" : interval,
                   "startTime": str(int(start_date)) + "000"
                }

        while True:
            r = requests.get(Stock.API_ADDR + Stock.KLINES, params=payload)
            if r.status_code == 200:
                return json.loads(r.text)
            print(r.text)
            time.sleep(5)
        return None