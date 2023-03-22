import numpy as np
import matplotlib.pyplot as plt
from data import get_data
from macd import get_macd_columns, get_signal_columns
from TradeBot import TradeBot
from macd import macd_iter, signal_iter

trade_data = get_data()

dates = trade_data['Date'].to_numpy()
close = trade_data['Close'].to_numpy()
macd = get_macd_columns(close)
signal = get_signal_columns(macd)

plt.style.use('dark_background')
plt.plot(dates, close, 'g-', label='price')
plt.plot(dates[macd_iter[1] + signal_iter + 1:], signal, 'tab:orange', label='signal')
plt.plot(dates[macd_iter[1] + 1:], macd, 'c-', label='macd')
plt.xlabel('Date [y-m-d]')
plt.ylabel('Close value [$]')
plt.xticks(range(0, len(dates), 100))
plt.ticklabel_format(style='plain', axis='y', useOffset=False)

bot = TradeBot()
buy, sell = bot.get_intersects(close[macd_iter[1] + signal_iter + 1:],
                                macd[signal_iter:], signal, dates[macd_iter[1] + signal_iter + 1:])

for point in buy:
    plt.plot(point.date, point.value, 'bx')

for point in sell:
    plt.plot(point.date, point.value, 'rx')

gain = bot.buy_and_sell(buy, sell)

plt.plot([], [], ' ', label=(f"{gain:.2f}$"))
plt.legend(loc='upper left')
plt.show()
