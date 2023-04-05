import matplotlib.pyplot as plt
from data import get_data
from macd import get_macd_columns, get_signal_columns
from TradeBot import TradeBot
from macd import macd_iter, signal_iter
from rsi import get_rsi

trade_data = get_data()

dates = trade_data['Date'].to_numpy()
close = trade_data['Close'].to_numpy()
macd = get_macd_columns(close)
signal = get_signal_columns(macd)
rsi, rdv = get_rsi(close, dates)


bot = TradeBot()
buy_macd, sell_macd = bot.get_intersects(close[macd_iter[1] + signal_iter + 1:],
                                macd[signal_iter:], signal, dates[macd_iter[1] + signal_iter + 1:])
macd_gain = bot.buy_and_sell_macd(buy_macd, sell_macd)
macd_gain -= bot.startingFunds

# testing rsi indicator
bot.funds = bot.startingFunds
rsi_gain, buy_rsi, sell_rsi = bot.buy_and_sell_rsi(rdv)
rsi_gain -= bot.startingFunds



# plotting the results
plt.style.use('dark_background')
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# plot close prices
axs[0].plot(dates, close, 'g-', label='price')
axs[0].plot([], [], ' ', label=(f"gain: {macd_gain:.2f}$"))
axs[0].plot([], [], 'b^', label='Buy point')
axs[0].plot([], [], 'rv', label='Sell point')
for point in buy_macd:
    axs[0].plot(point.date, point.value, 'b^')
    # axs[0].text(point.date, point.value, f"{point.date}\n{point.value:.2f}", ha='center', va='bottom', fontsize=8)
for point in sell_macd:
    axs[0].plot(point.date, point.value, 'rv')
    # axs[0].text(point.date, point.value, f"{point.date}\n{point.value:.2f}", ha='center', va='bottom', fontsize=8)
axs[0].set_ylabel('Close value [$]')
axs[0].ticklabel_format(style='plain', axis='y', useOffset=False)
axs[0].legend(loc='upper left')

# plot macd
axs[1].plot(dates[macd_iter[1] + signal_iter + 1:], signal, 'tab:orange', label='signal')
axs[1].plot(dates[macd_iter[1] + 1:], macd, 'c-', label='macd')
axs[1].set_ylabel('MACD value')
axs[1].tick_params(axis='both', which='both', labelbottom=False, labeltop=False)
axs[1].legend(loc='upper left')

# plot rsi
axs[2].plot(dates[len(dates)-len(rsi)::], rsi, 'purple', label='rsi')
axs[2].plot([], [], ' ', label=(f"gain: {rsi_gain:.2f}$"))
axs[2].plot([], [], 'b^', label='Buy point') # for the label
axs[2].plot([], [], 'rv', label='Sell point')
axs[2].set_ylabel('RSI value')
axs[2].tick_params(axis='both', which='both', labelbottom=True, labeltop=False)
axs[2].legend(loc='upper left')
axs[2].axhline(y=30, color='yellow', linestyle='--', linewidth=1)
axs[2].axhline(y=70, color='cyan', linestyle='--', linewidth=1)
for point in buy_rsi:
    axs[2].plot(point.date, point.rsi, 'b^')
    # axs[2].text(point.date, point.rsi, f"{point.date}\n{point.value:.2f}", ha='center', va='bottom', fontsize=8)
for point in sell_rsi:
    axs[2].plot(point.date, point.rsi, 'rv')
    # axs[2].text(point.date, point.rsi, f"{point.date}\n{point.value:.2f}", ha='center', va='bottom', fontsize=8)
for ax in axs:
    ax.set_xticks(range(0, len(dates), 150))

fig.suptitle('MACD Analysis', fontsize=14)
plt.show()