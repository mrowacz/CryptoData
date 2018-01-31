import ast
import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class Kline:
    def __init__(self, kl):
        self.open_time = kl[0]
        self.open = float(kl[1])
        self.high = float(kl[2])
        self.low = float(kl[3])
        self.close = float(kl[4])
        self.volume = float(kl[5])
        self.close_time = kl[6]
        self.quote_asset_volume = kl[7]
        self.number_trades = kl[8]
        self.taker_buy_base_asset = kl[9]
        self.taker_buy_quote_asset = kl[10]
        self.ignore = kl[11]

    def __lt__(self, other):
        return self.open_time < other.open_time

if __name__ == "__main__":
    with open("LSKETH.log", "r") as f:
        step = 1
        data = f.readlines()
        data = data[1:60*24*16:step]
        print("Read " + str(len(data)) + " lines")
        kl = list(map(lambda k: Kline(ast.literal_eval(k)), data))

        # calc max percent change in 24h window
        percent_ch = []
        for index, v in enumerate(kl):
            block = kl[index::24*60]
            result = max(map(lambda x: ((x.high-v.low)/v.low)*100, block))

            percent_ch.append(result)

        plt.figure(1)
        plt.plot(list(map(lambda x: (x.close + x.open)/2, kl)))

        plt.figure(2)
        plt.plot(percent_ch)

        plt.figure(3)
        n, bins, patches = plt.hist(percent_ch, 50, normed=1, facecolor='green', alpha=0.75)

        number_of_entries = sum(bins[6:])*len(percent_ch)
        print("Number of entries: " + str(number_of_entries))

        plt.xlabel('Profit')
        plt.ylabel('Probability')
        plt.title('lisk market possible profit')
        plt.axis([0, 40, 0, 0.1])
        plt.grid(True)

        diff = -sys.maxsize-1
        for index, val in enumerate(kl):
            if index != 0:
                v = abs(kl[index-1].open_time - kl[index].open_time)
                if v > diff:
                    diff = v
                    print(v)
        print(diff)

        plt.show()
