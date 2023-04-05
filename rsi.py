import numpy as np
from numpy import ndarray
from collections import namedtuple

rsi_period: int = 14

rsi_date_val = namedtuple('rsi_date_val', ('rsi', 'date' ,'value'))

def get_rs(data: ndarray, n: int = rsi_period) -> float:
    loses = []
    gains = []
    for i in range(1, len(data)):
        x = data[i] - data[i-1]
        if x >= 0:
            gains.append(x)
        elif x < 0:
            loses.append(abs(x))

    return (sum(gains)/n)/(sum(loses)/n)

def get_rsi(data: ndarray, dates: ndarray) -> tuple:
    rsi = []
    rdv = []
    for i in range(rsi_period, len(data)):
        temp_data = data[i - rsi_period:i]
        rs = get_rs(temp_data)
        x = 100. - 100./(1.+rs)

        rsi.append(x)
        rdv.append(rsi_date_val(x, dates[i], data[i]))

    return rsi, rdv
