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

bot = TradeBot()
buy, sell = bot.get_intersects(close[macd_iter[1] + signal_iter + 1:],
                                macd[signal_iter:], signal, dates[macd_iter[1] + signal_iter + 1:])

gain = bot.buy_and_sell(buy, sell) - bot.startingFunds

# plotting the data
plt.style.use('dark_background')
plt.plot(dates, close, 'g-', label='price')
plt.plot(dates[macd_iter[1] + signal_iter + 1:], signal, 'tab:orange', label='signal')
plt.plot(dates[macd_iter[1] + 1:], macd, 'c-', label='macd')
plt.xlabel('Date [yyyy-mm-dd]')
plt.ylabel('Close value [$]')
plt.xticks(range(0, len(dates), 100))
plt.ticklabel_format(style='plain', axis='y', useOffset=False)

for point in buy:
    plt.plot(point.date, point.value, 'b^')
    plt.text(point.date, point.value, f"{point.date}\n{point.value:.2f}", ha='center', va='bottom', fontsize=8)

for point in sell:
    plt.plot(point.date, point.value, 'rv')
    plt.text(point.date, point.value, f"{point.date}\n{point.value:.2f}", ha='center', va='top', fontsize=8)


plt.plot([], [], 'b^', label='Buy point') # for the label
plt.plot([], [], 'rv', label='Sell point')
plt.plot([], [], ' ', label=(f"gain: {gain:.2f}$"))
plt.legend(loc='upper left')
plt.show()
