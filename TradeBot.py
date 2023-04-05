from collections import namedtuple
from rsi import rsi_date_val

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
    
    def buy_and_sell_macd(self, buy: list, sell: list) -> float:
        if buy[0].date > sell[0].date: # the sell intersection is first date wise
            sell = sell[1::]
        number_of_stocks: float = 0
        for i in range(len(sell)):
            number_of_stocks = self.funds / buy[i].value
            self.funds -= number_of_stocks * buy[i].value
            self.funds += number_of_stocks * sell[i].value

        return self.funds
    
    def buy_and_sell_rsi(self, rdv: list[rsi_date_val]) -> tuple:
        number_of_stocks = 0
        buy_points = []
        sell_points = []
        for x in rdv:
            if x.rsi <= 30 and number_of_stocks == 0:
                number_of_stocks = self.funds / x.value
                self.funds = 0
                buy_points.append(x)
            elif x.rsi >= 70 and number_of_stocks > 0:
                self.funds = number_of_stocks * x.value
                number_of_stocks = 0
                sell_points.append(x)

        # any remaining stocks
        if number_of_stocks > 0:
            self.funds += number_of_stocks * rdv[-1].value
        return self.funds, buy_points, sell_points
    