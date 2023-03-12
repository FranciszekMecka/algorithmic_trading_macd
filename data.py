import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_data():
    filepath = 'wig20_d.csv'
    total_rows = sum(1 for line in open(filepath)) - 1 # get the total number of rows in the file (excluding header)

    column_names = ['date', 'open', 'high', 'low', 'close', 'volume']

    raw_dataset = pd.read_csv(filepath, names=column_names, skiprows=total_rows-1000, nrows=1000)
    dataset = raw_dataset.dropna()

    return dataset

def inspect_data(dataset):
    print('Dataset shape:')
    print(dataset.shape)

    print('Tail')
    print(dataset.tail())

    print('Statistics')
    print(dataset.describe().transpose())

    sns.pairplot(dataset[['date', 'open', 'high', 'low', 'close', 'volume']], diag_kind='kde')
    plt.show()
