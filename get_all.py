from cd.HistoryCollector import HistoryCollector
from cd.Stock import Stock

if __name__ == "__main__":
    start_date = "01/08/2017"
    stop_date = "30/01/2018"
    h = HistoryCollector("ETH", start_date, stop_date)
    # j = h.run("LSKETH", "./out/")

    s = Stock()
    vol_map = {}

    with open("./cd/volumes.dat") as f:

        d = map(lambda x: x.split(" "), f.readlines())
        for e in d:
            if float(e[1]) > 10000.0:
                vol_map[e[0]] = float(e[1])

    print("Possible candidates for playing: " + str(len(vol_map)))

    for e in vol_map:
        print("Fetching " + e)
        h.run(s.markets[e]["symbol"], "./out/")