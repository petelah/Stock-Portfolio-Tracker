import requests
import json

from time import time, sleep
from os.path import isfile
from os import environ


def once_a_minute(func, last_time, counter):
	def wrapper(*args, **kwargs):
		time_now = time()
		if not last_time:
			func_val = func(*args, **kwargs)
			return func_val
		elif counter >= 5:
			print(f"Please wait {time_now - last_time} seconds before requesting again.")
			print(f"Sleeping for {time_now - last_time}")
			sleep(61)
			print("Loading next value")
			counter = 0
		func_val = func(*args, **kwargs)
		return func_val, counter
	return wrapper


class StockDataReader:
	apikey = environ.get('API_KEY')
	url = "https://www.alphavantage.co/query?"

	@classmethod
	def get_data(cls, symbol: str) -> str:
		stock_data = requests.get(
			f"{cls.url}function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={cls.apikey}")
		return stock_data

	@classmethod
	def last_price(cls, data):
		data = data.json()
		try:
			time_series = data["Time Series (Daily)"].items()
			ret_data = float(list(time_series)[0][1]['4. close'])
			return ret_data
		except:
			return "error"

class DataHandler:

	@staticmethod
	def cleaner(string):
		return string.split(', ')

	@staticmethod
	def check_portfolio_exists():
		if isfile('portfolio.json'):
			return True
		return False

	@staticmethod
	def load_portfolio():
		try:
			with open('portfolio.json', 'r') as file:
				ret_data = file.readline()
				return json.loads(ret_data)
		except json.JSONDecodeError as e:
			print(e)
			return []
		except Exception as e:
			print(f"Error: {e}")
			return []

	@staticmethod
	def save_portfolio(data):
		if not DataHandler.check_portfolio_exists():
			with open('portfolio.json', 'w') as file:
				file.write(json.dumps(data))
		else:
			with open('portfolio.json', 'w') as file:
				file.write(json.dumps(data))

	@staticmethod
	def validate_entry(symbol, date, amount, price, last_price):
		if last_price == "error":
			return "Please enter a valid symbol."
		if not isinstance(symbol, str):
			return "Symbol must be letters only."
		if not isinstance(date, str) and len(date) < 10:
			return "Date must be format: YYYY-MM-DD"
		try:
			amount = float(amount)
		except ValueError:
			return "Number of shares must be a number: '45'."
		try:
			price = float(price)
		except ValueError:
			return "Price must be a number: 45.5."
		return True