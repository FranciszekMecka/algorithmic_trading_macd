import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from data import get_data, inspect_data

trade_data = get_data()

inspect_data(trade_data)
dates = trade_data['Date'].to_numpy()
volumes = trade_data['Close'].to_numpy()

plt.plot(dates, volumes)
plt.xticks(range(0, 100, 10))
plt.ticklabel_format(style='plain', axis='y', useOffset=False)
plt.show()