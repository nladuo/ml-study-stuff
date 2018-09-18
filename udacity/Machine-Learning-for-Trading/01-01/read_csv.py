import pandas as pd


def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    # print df[10:21]
    print df.head()

if __name__ == '__main__':
    test_run()
