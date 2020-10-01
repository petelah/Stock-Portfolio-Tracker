import requests
import json

from time import sleep
from datetime import date
from os.path import isfile
from os import environ


class StockDataReader:
	"""
	Class of class methods used to get the data from Alphavantage API
	"""
	apikey = environ.get('API_KEY')
	url = "https://www.alphavantage.co/query?"

	@classmethod
	def get_data(cls, symbol: str):
		"""
		This classmethod gets the data using requests get URL method.
		Class variables are passed into the URL.
		:param symbol: string representing a stock symbol
		:return: requests object for validation and data manipulating
		"""
		stock_data = requests.get(
			f"{cls.url}function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol.upper()}&outputsize=compact&apikey={cls.apikey}")
		return stock_data

	@classmethod
	def last_price(cls, data):
		"""
		This will take a requests object, extract the json data and find the last price of the stock
		to store in the portfolio.
		:param data: requests object
		:return: dict or string "error"
		"""
		data = data.json()
		try:
			time_series = data["Time Series (Daily)"].items()
			ret_data = float(list(time_series)[0][1]['4. close'])
			if "Note" in time_series:
				symbol = data["Meta Data"]["2. Symbol"]
				print("Too many requests, waiting 60 seconds.")
				sleep(61)
				data = cls.get_data(symbol).json()
				time_series = data["Time Series (Daily)"].items()
				ret_data = float(list(time_series)[0][1]['4. close'])
			return ret_data
		except:
			return "error"


class DataHandler:
	"""
	Standard library for the handling of our data.
	"""
	@staticmethod
	def check_portfolio_exists() -> bool:
		"""
		Simple function to check if there is a portfolio file or not.
		:return: bool
		"""
		if isfile('portfolio.json'):
			return True
		return False

	@staticmethod
	def load_portfolio():
		"""
		Loads the portfolio.
		:return: dict or empty dict
		"""
		try:
			with open('portfolio.json', 'r') as file:
				ret_data = file.readline()
				return json.loads(ret_data)
		except json.JSONDecodeError as e:
			print(e)
			return dict({})
		except Exception as e:
			print(f"Error: {e}")
			return dict({})

	@staticmethod
	def save_portfolio(data: dict):
		"""
		Saves the portfolio to JSON.
		:param data: dict
		:return:
		"""
		if not DataHandler.check_portfolio_exists():
			with open('portfolio.json', 'w') as file:
				file.write(json.dumps(data))
		else:
			with open('portfolio.json', 'w') as file:
				file.write(json.dumps(data))

	@staticmethod
	def validate_entry(symbol: str, date: str, amount, price, last_price: float):
		"""
		Thi function is used to validate user input to add a stock.
		:param symbol: str
		:param date: str
		:param amount: int or float
		:param price: int or float
		:param last_price: int or float
		:return: str containing error msg or bool
		"""
		if last_price == "error":
			return "Please enter a valid symbol."
		if not isinstance(symbol, str):
			return "Symbol must be letters only."
		if not DataHandler.date_validation(date):
			return "Date format: YYYY-MM-DD and must not be a future date."
		try:
			amount = float(amount)
		except ValueError:
			return "Number of shares must be a number: '45'."
		try:
			price = float(price)
		except ValueError:
			return "Price must be a number: 45.5."
		return True

	@staticmethod
	def date_validation(input_date: str) -> bool:
		"""
		Simple date verification function to validate the user has put
		in the correct format and that the date is not in the future.
		:param input_date:
		:return: bool
		"""
		if not isinstance(input_date, str) and len(input_date) < 10:
			return False
		try:
			date.fromisoformat(input_date)
		except ValueError:
			return False
		if date.fromisoformat(input_date) > date.today():
			return False
		return True