import time
import datetime
import numpy as np
from cd.Stock import Stock
from matplotlib.mlab import frange


class HistoryCollector:
    def __init__(self, coin, start_date, stop_date):
        self.coin = coin
        self.MAX_STEP = 500.0
        self.ONE_SECOND = 1000
        self.start_date = time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple())
        self.stop_date = time.mktime(datetime.datetime.strptime(stop_date, "%d/%m/%Y").timetuple())
        self.data = []

        self.tickers = {
            "1m": 60,
            "3m": 180,
            "5m": 300,
            "15m": 450
        }

    def run(self, c, path):
        # c = "LSKETH"
        with open(path + c + ".log", "w") as f:
            print(str(self.start_date) + " " + str(self.stop_date))
            time_delta = self.MAX_STEP * self.tickers["1m"]
            time_spans = frange(self.start_date, self.stop_date, time_delta)
            for index, span in enumerate(time_spans):
                print("loop " + str(index) + "/" + str(len(time_spans)))
                data = Stock.get_klines(c, "1m", span)
                for e in data:
                    f.write(str(e) + "\n")
                f.flush()


if __name__ == "__main__":
    start_date = "01/12/2017"
    stop_date = "01/01/2018"
    h = HistoryCollector("ETH", start_date, stop_date)
    j = h.run("LSKETH", "./out/")