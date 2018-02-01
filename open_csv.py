import pandas as pd
import matplotlib.pyplot as plt

kline_enum = {
    "open_time" : 0,
    "open": 1,
    "high": 2,
    "low": 3,
    "close": 4
}

data = pd.read_csv('csv/EOSETH.csv')
n = data.shape[0]
p = data.shape[1]

print("Shape {0}x{1}".format(n, p))
data = data.values

max_dev = ((data[:, kline_enum["high"]] - data[:, kline_enum["low"]])
           / data[:, kline_enum["low"]])*100

plt.plot(max_dev, '-b')
plt.show()