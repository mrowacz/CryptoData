import ast
import sys
import matplotlib.pyplot as plt

class Kline:
    def __init__(self, kl):
        self.open_time = kl[0]
        self.open = kl[1]
        self.high = kl[2]
        self.low = kl[3]
        self.close = kl[4]
        self.volume = kl[5]
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
        step = 500
        data = f.readlines()
        data = data[1::step]
        print("Read " + str(len(data)) + " lines")
        kl = list(map(lambda k: Kline(ast.literal_eval(k)), data))

        plt.plot(list(map(lambda x: x.open_time, kl)))
        plt.show()
        # diff = -sys.maxsize-1
        # for index, val in enumerate(kl):
        #     if index != 0:
        #         v = abs(kl[index-1].open_time - kl[index].open_time)
        #         if v > diff:
        #             diff = v
        #             print(v)
        # print(diff)