import unittest
from unittest import mock

from src.utils import StockDataReader, DataHandler
from src.portfolio import Portfolio


class TestApi(unittest.TestCase):
	def test_get(self):
		"""
		Standard API testing, returning correct status code and data structures.
		"""
		result = StockDataReader.get_data("IBM")
		self.assertEqual(result.status_code, 200, msg=f"Status code was {result.status_code} not 200.")

		result = StockDataReader.get_data("IBM")
		if "Error Message" in result.json():
			self.assertTrue(result.json()['Meta Data'], True)

	def test_last_price(self):
		"""
		Testing that the last price of an individual stock gets returned.
		"""
		result = StockDataReader.last_price(StockDataReader.get_data("IBM"))
		self.assertIsInstance(result, float)

	def test_portfolio(self):
		"""
		Testing portfolio creation. initialisation and user input.
		"""
		if DataHandler.check_portfolio_exists():
			result = Portfolio()
			self.assertIsInstance(result.portfolio, dict)
		else:
			mock_args = ["AA", 10, 50, "2010-04-03"]
			with mock.patch('builtins.input') as mocked_input:
				mocked_input.side_effect = mock_args
				result = Portfolio()
			self.assertTrue(result.portfolio['AA'], True)

	def test_add_stock(self):
		"""
		Testing adding a stock after portfolio has been initialised.
		Must init a new portfolio if portfolio.json not found.
		:return:
		"""
		if not DataHandler.check_portfolio_exists():
			mock_args1 = ["AA", 10, 50, "2010-04-03"]
			mock_args2 = ["FB", 10, 50, "2010-04-03"]
			with mock.patch('builtins.input') as mocked_input:
				mocked_input.side_effect = mock_args1
				result = Portfolio()
				mocked_input.side_effect = mock_args2
				result.add_stock()
			self.assertTrue(result.portfolio['FB'], True)
		else:
			mock_args = ["FB", 10, 50, "2010-04-03"]
			result = Portfolio()
			with mock.patch('builtins.input') as mocked_input:
				mocked_input.side_effect = mock_args
				result.add_stock()
			self.assertTrue(result.portfolio['FB'], True)
