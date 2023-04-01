from collections import namedtuple
from numpy import ndarray

class TradeBot:
    date_val = namedtuple('date_val', ('date', 'value'))

    def __init__(self, funds: float = 1000) -> None:
        self.funds = funds
        self.startingFunds = funds # this is used to calculate gain

    def get_intersects(self, stock_price: list, macd: list, signal: list, dates: list) -> tuple:
        buy_intersects = []
        sell_intersects = []

        for i in range(len(dates)):
            if macd[i] > signal[i] and macd[i-1] < signal[i-1]:
                x = self.date_val(dates[i], stock_price[i])
                buy_intersects.append(x)
            elif macd[i] < signal[i] and macd[i-1] > signal[i-1]:
                x = self.date_val(dates[i], stock_price[i])
                sell_intersects.append(x)

        return buy_intersects, sell_intersects
    
    def buy_and_sell(self, buy: list, sell: list) -> float:
        if buy[0].date > sell[0].date: # the sell intersection is first date wise
            sell = sell[1::]
        number_of_stocks: float = 0
        for i in range(len(sell)):
            number_of_stocks = self.funds / buy[i].value
            self.funds -= number_of_stocks * buy[i].value
            self.funds += number_of_stocks * sell[i].value

        return self.funds
    
    def react_to_rsi(self, rsi: ndarray):
        pass