import numpy as np
from numpy import ndarray

rsi_period: int = 14

# this doesn't work fix this, run this and see

def get_rs(data: ndarray, n: int = rsi_period) -> float:
    data = data[:n + 1]
    loses = []
    gains = []

    for i in range(1, len(data)):

        x = data[i] - data[i-1]
        if x > 0:
            gains.append(x)
        elif x < 0:
            loses.append(abs(x))
    return (sum(gains) / n) / (sum(loses) / n)

def get_rsi(data: ndarray) -> ndarray:
    rsi = []
    for i in range(len(data) - rsi_period):
        temp_data = data[i:]
        rs = get_rs(temp_data)
        x = 100. - 100./(1.+rs)
        rsi.append(x)

    return rsi
