import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

def alpha(N: int) -> float:
    return 2/(N+1)

def get_ema(data: ndarray, N: int) -> float:
    data_close = data
    data_cols = data_close[:N+1]
    data_cols = data_cols[::-1] # inverting the order to get the first date at the beg
    pow = np.arange(N+1)
    alphaOne = np.power(1 - alpha(N), pow)
    numerator = (alphaOne * data_cols).sum()
    denominator = alphaOne.sum()
    return numerator/denominator

def get_macd(data: ndarray, i: int, j: int) -> float:
    return get_ema(data, i) - get_ema(data, j)

def get_macd_columns(data: ndarray) -> ndarray:
    macd = []
    for i in range(27, len(data)):
        temp_data = data[i-27:i]
        x = get_macd(temp_data, 12, 26) # instructed values
        macd.append(x)
    return macd

def get_signal_columns(macd_cols: ndarray) -> ndarray:
    #TODO
    signal = []
    for i in range(9, len(macd_cols)):
        temp_data = macd_cols[i-9:i+1]
        x = get_macd(temp_data, 9, 0)
        signal.append(x)
    return signal