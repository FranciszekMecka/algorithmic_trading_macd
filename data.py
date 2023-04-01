import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_data():
    filepath = 'data/aapl_us_d.csv'
    with open(filepath, 'r') as f:
        column_names = f.readline().strip().split(',')

    raw_dataset = pd.read_csv(filepath, names=column_names, na_values='?', comment='\t',
                              sep=',', skipinitialspace=True, header=1)

    dataset = raw_dataset.dropna()
    dataset = raw_dataset.tail(1000) # amount of stock data
    return dataset

def inspect_data(dataset):
    print('Dataset shape:')
    print(dataset.shape)

    print('Tail:')
    print(dataset.tail())

    print('Statistics:')
    print(dataset.describe().transpose())

    sns.pairplot(dataset[['Date','Open','High','Low','Close','Volume']], diag_kind='kde')
    plt.show()
