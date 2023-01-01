// it uses trading view api

import requests
import matplotlib.pyplot as plt

# Replace YOUR_API_KEY with your actual TradingView API key
api_key = 'YOUR_API_KEY'

# Specify the parameters for the API request
symbol = 'COINBASE:ETHUSD'
resolution = 'D'  # D for daily data
from_date = '2022-01-01'  # start date in YYYY-MM-DD format
to_date = '2022-01-31'  # end date in YYYY-MM-DD format

# Send the request to the TradingView API
url = f'https://www.tradingview.com/chart/data/{symbol}/{resolution}/{from_date}/{to_date}'
headers = {'x-tradingview-key': api_key}
response = requests.get(url, headers=headers)

# Check the status code of the response
if response.status_code != 200:
    print(f'Error fetching data: {response.status_code}')
else:
    # Parse the response data
    data = response.json()
    t = data['t']  # timestamps
    c = data['c']  # close prices
    
    # Plot the data using Matplotlib
    plt.plot(t, c)
    plt.show()
