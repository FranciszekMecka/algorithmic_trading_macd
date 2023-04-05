import numpy as np
from numpy import ndarray

macd_iter = (12, 26) # how far should you calc macd
signal_iter = 9

def alpha(N: int) -> float:
    return 2/(N+1)

def get_ema(data: ndarray, N: int) -> float:
    data_cols = data[::-1] # inverting the order to get the first date at the beg
    data_cols = data_cols[:N+1]
    pows = np.arange(N+1)
    alphaOne = np.power(1 - alpha(N), pows)
    numerator = (alphaOne * data_cols).sum()
    denominator = alphaOne.sum()
    return numerator/denominator

def get_macd(data: ndarray, j: int, i: int) -> float:
    return get_ema(data, j) - get_ema(data, i)

def get_macd_columns(data: ndarray) -> ndarray:
    macd = []
    for i in range(macd_iter[1] + 1, len(data)):
        temp_data = data[i-(macd_iter[1] + 1):i]
        x = get_macd(temp_data, macd_iter[0], macd_iter[1])
        macd.append(x)
    return macd

def get_signal_columns(macd_cols: ndarray) -> ndarray:
    signal = []
    for i in range(signal_iter, len(macd_cols)):
        temp_data = macd_cols[i-signal_iter:i+1]
        x = get_ema(temp_data, signal_iter)
        signal.append(x)
    return signal
