import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Sample data
stock_data = [
    (100, 105, 95, 105),
    (110, 115, 105, 115),
    (105, 110, 95, 110),
    (115, 120, 105, 120),
    (120, 125, 115, 125)
]
time_period = range(len(stock_data))

# Create the plot
fig, ax = plt.subplots()
candlestick_ohlc(ax, stock_data, time_period, width=0.5)

# Format the x-axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Show the plot
plt.show()
