import unittest
from src.utils import StockDataReader
from src.utils import DataHandler

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
