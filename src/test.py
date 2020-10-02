import unittest

from utilities import StockDataReader, DataHandler
from portfolio import Portfolio


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
		Testing portfolio creation. initialisation and add stock.
		"""
		if DataHandler.check_portfolio_exists():
			result = Portfolio()
			self.assertIsInstance(result.portfolio, dict)
		else:
			result = Portfolio()
			result.add_stock("AA", 10, 50, "2010-04-03")
			self.assertTrue(result.portfolio['AA'], True)


	# def test_update(self):
	# 	"""
	# 	Testing portfolio creation. initialisation and add stock.
	# 	"""
	# 	if DataHandler.check_portfolio_exists():
	# 		result = Portfolio()
	# 		self.assertIsInstance(result.portfolio, dict)
	# 	else:
	# 		result = Portfolio()
	# 		result.add_stock("AA", 10, 50, "2010-04-03")
	# 		data = StockDataReader.get_data("AA")
	# 		last_price = StockDataReader.last_price(data)
	# 		result.update_stock("AA", data)
	# 		if last_price == result.portfolio['AA']['Last Price $']:
	# 			assertion = True
	# 		else:
	# 			assertion = False
	# 		self.assertTrue(assertion, True)

	def test_delete(self):
		"""
		Testing deletion of stock.
		"""
		result = Portfolio()
		result.add_stock("AA", 10, 50, "2010-04-03")
		self.assertTrue(result.delete_stock("AA"), True)

	def test_verification(self):
		"""
		Testing verification method
		"""
		# Passing correct data
		result = DataHandler.validate_entry('IBM', '2020-03-03', 45, 60.5, 112.8)
		self.assertTrue(result, True)

		# Passing invalid price data
		result = DataHandler.validate_entry('IBM', '2020-03-03', 45, 'ff', 'error')
		self.assertEqual(result, "Please enter a valid symbol.")

		# Passing invalid symbol data
		result = DataHandler.validate_entry(45, '2020-03-03', 45, 60.5, 112.8)
		self.assertEqual(result, "Symbol must be string.")

		# Passing invalid date data
		result = DataHandler.validate_entry('IBM', '2020-25-03', 45, 60.5, 112.8)
		self.assertEqual(result, "Date format: YYYY-MM-DD and must not be a future date.")

		# Passing invalid amount data
		result = DataHandler.validate_entry('IBM', '2020-03-03', '45f', 60.5, 112.8)
		self.assertEqual(result, "Number of shares must be a number: '45'.")

		# Passing invalid price data
		result = DataHandler.validate_entry('IBM', '2020-03-03', 45, 'ff', 112.8)
		self.assertEqual(result, "Price must be a number: '45.5'.")
