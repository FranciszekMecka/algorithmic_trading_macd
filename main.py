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

plt.plot(dates, close, 'r-', label='price')
plt.plot(dates[macd_iter[1] + 1:], macd, 'g-', label='macd')
plt.plot(dates[macd_iter[1] + signal_iter + 1:], signal, 'b-', label='signal')
plt.xlabel('Date [y-m-d]')
plt.ylabel('Close value [$]')
plt.xticks(range(0, len(dates), 100))
plt.ticklabel_format(style='plain', axis='y', useOffset=False)

bot = TradeBot()
buy, sell = bot.get_intersects(close[macd_iter[1] + signal_iter + 1:],
                                macd[signal_iter:], signal, dates[macd_iter[1] + signal_iter + 1:])
gain = bot.buy_and_sell(buy, sell)

plt.plot([], [], ' ', label=(str(gain) + "$"))
plt.legend(loc='upper left')
plt.show()
