import numpy as np
import matplotlib.pyplot as plt


class trade_bot:
    def __init__(self, funds: float = 1000, date: str = '') -> None:
        self.funds = funds
        self.starting_date = date

    def get_intersects(self, stock_price: list, macd: list, signal: list, dates: list) -> list:
        buy_intersects = []
        sell_intersects = []

        for i in range (len(dates)):
            if macd[i] > signal[i] and macd[i-1] < signal[i-1]:
                buy_intersects.append((dates[i], stock_price[i]))
            elif macd[i] < signal[i] and macd[i-1] > signal[i-1]:
                sell_intersects.append((dates[i], stock_price[i]))

        return buy_intersects, sell_intersects