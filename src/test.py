import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock
import builtins

from src.utils import StockDataReader, DataHandler
from src.portfolio import Portfolio

class TestApi(unittest.TestCase):
	def test_get(self):

		result = StockDataReader.get_data("IBM")
		self.assertEqual(result.status_code, 200, msg=f"Status code was {result.status_code} not 200.")

		result = StockDataReader.get_data("IBM")
		if "Error Message" in result.json():
			self.assertTrue(result.json()['Meta Data'], True)

	def test_last_price(self):

		result = StockDataReader.last_price(StockDataReader.get_data("IBM"))
		self.assertIsInstance(result, float)

	def test_portfolio(self):

		if DataHandler.check_portfolio_exists():
			result = Portfolio()
			self.assertIsInstance(result.portfolio, dict)

	def test_add_stock(self):
		mock_args = ["AA", 10, 50, "2010-04-03"]
		# result = Portfolio()
		with mock.patch('builtins.input') as mocked_input:
			mocked_input.side_effect = mock_args
			#result.add_stock()
			result = Portfolio()
		self.assertTrue(result.portfolio['AA'], True)
