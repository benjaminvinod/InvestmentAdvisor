import requests
from datetime import datetime

# Replace with your own Alpha Vantage API key
API_KEY = 'Q8AAEEHORIPJHW3K'

# Fetch Daily Time Series (last 10 days)
def get_daily_stock_data(symbol):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        timestamps = sorted(time_series.keys())[-10:]  # Last 10 days (oldest to newest)

        labels = []
        open_prices = []
        high_prices = []
        low_prices = []
        close_prices = []
        volumes = []

        for timestamp in timestamps:
            dt = datetime.strptime(timestamp, "%Y-%m-%d")
            labels.append(dt.strftime("%Y-%m-%d"))
            open_prices.append(float(time_series[timestamp]['1. open']))
            high_prices.append(float(time_series[timestamp]['2. high']))
            low_prices.append(float(time_series[timestamp]['3. low']))
            close_prices.append(float(time_series[timestamp]['4. close']))
            volumes.append(int(time_series[timestamp]['5. volume']))

        return {
            'labels': labels,
            'open': open_prices,
            'high': high_prices,
            'low': low_prices,
            'close': close_prices,
            'volume': volumes
        }

    # ✅ Error fallback
    return {
        'error': 'Could not retrieve stock data',
        'message': data.get('Note') or data.get('Error Message') or 'Unknown error',
        'raw': data
    }

# ✅ Fetch Intraday (5min interval) data (last 10 points)
def get_intraday_stock_data(symbol):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'Time Series (5min)' in data:
        time_series = data['Time Series (5min)']
        timestamps = sorted(time_series.keys())[-10:]  # Last 10 points (oldest to newest)

        labels = []
        open_prices = []
        high_prices = []
        low_prices = []
        close_prices = []
        volumes = []

        for timestamp in timestamps:
            dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            labels.append(dt.strftime("%H:%M"))  # Format time only
            open_prices.append(float(time_series[timestamp]['1. open']))
            high_prices.append(float(time_series[timestamp]['2. high']))
            low_prices.append(float(time_series[timestamp]['3. low']))
            close_prices.append(float(time_series[timestamp]['4. close']))
            volumes.append(int(time_series[timestamp]['5. volume']))

        return {
            'labels': labels,
            'open': open_prices,
            'high': high_prices,
            'low': low_prices,
            'close': close_prices,
            'volume': volumes
        }

    # Error fallback
    return {
        'error': 'Could not retrieve stock data',
        'message': data.get('Note') or data.get('Error Message') or 'Unknown error',
        'raw': data
    }
