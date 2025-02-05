import yfinance as yf
import plotly.graph_objects as go

ticker = input("Enter stock name:")
data = yf.download(ticker, start="2024-01-01", end="2024-12-31")

fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open = data['Open'],high_data = data['High'],
                                     low = data['Low'],close = data['Close'],
                                     increasing_line_color = 'cyan', 
                                     decreasing_line_color = 'gray')])

fig.update_layout(
    title = ticker + ' stock price in 2024',
    xaxis_title = 'Date',
    yaxis_title = 'Price',
    xaxis_rangeslider_visible = False
)

fig.show()