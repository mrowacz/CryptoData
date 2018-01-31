import time
import datetime
import numpy as np
from Stock import Stock
from matplotlib.mlab import frange


class HistoryCollector:
    def __init__(self, coin, start_date, stop_date):
        self.coin = coin
        self.MAX_STEP = 500.0
        self.start_date = time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple())
        self.stop_date = time.mktime(datetime.datetime.strptime(stop_date, "%d/%m/%Y").timetuple())
        self.data = []

    def run(self):
        c = "LSKETH"
        with open(c + ".log", "w") as f:
            print(str(self.start_date) + " " + str(self.stop_date))
            time_spans = frange(self.start_date, self.stop_date, self.MAX_STEP)
            for index, span in enumerate(time_spans):
                print("loop " + str(index) + "/" + str(len(time_spans)))
                data = Stock.get_klines(c, "1m", span)
                print(data)
                for e in data:
                    f.write(str(e) + "\n")
                f.flush()


if __name__ == "__main__":
    start_date = "01/12/2017"
    stop_date = "01/01/2018"
    h = HistoryCollector("ETH", start_date, stop_date)
    j = h.run()