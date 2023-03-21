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
    
    def buy_and_sell(self, buy: list, sell: list):
        if buy[0][0] > sell[0][0]: # the sell intersection is first
            sell = sell[1::]
        number_of_stocks: float = 0
        for i in range(len(sell)):
            number_of_stocks = self.funds / buy[i][1] # value/ zapytaj sie o to
            self.funds -= number_of_stocks * buy[i][1] # xd

            self.funds += number_of_stocks * sell[i][1]

        return self.funds