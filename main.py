import numpy as np
import matplotlib.pyplot as plt
from data import get_data, inspect_data
from macd import get_macd_columns, get_signal_columns

trade_data = get_data()

# inspect_data(trade_data)
dates = trade_data['Date'].to_numpy()
close = trade_data['Close'].to_numpy()
macd = get_macd_columns(close)
signal = get_signal_columns(macd)

plt.plot(dates, close, 'r-', label='price')
plt.plot(dates[27:], macd, 'g-', label='macd')
plt.plot(dates[36:], signal, 'b-', label='signal')
plt.xlabel('Date')
plt.ylabel('Close value [$]')
plt.xticks(range(0, len(dates), 100))
plt.legend(loc='upper left')
plt.ticklabel_format(style='plain', axis='y', useOffset=False)

plt.show()