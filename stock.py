import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

hsy_data = yf.download('HSY', start='2020-01-01', end='2023-12-31')

plt.figure(figsize=(10, 6))
plt.plot(hsy_data['Open'],
    label='Open Price', color='b')

plt.title('Hershey Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

