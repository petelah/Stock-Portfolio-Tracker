from utils import StockDataReader, DataHandler


class Portfolio:

	def __init__(self):
		self.portfolio = self.load_portfolio()

	def add_stock(self, stock, price, amount, date):
		last_price = StockDataReader.last_price(
			StockDataReader.get_data(stock))
		self.portfolio[stock] = {
			'Date': date,
			'Price $': price,
			'Amount': amount,
			'Last Price $': last_price,
			'Initial Investment $': price * amount,
			'Return %': round((last_price / price) * 100, 2),
			'Return $': round(last_price * amount, 2)
		}

	def load_portfolio(self):
		if DataHandler.check_portfolio_exists():
			return DataHandler.load_portfolio()
		else:
			return dict({})

	def update_stock(self, key, data):
		key = key
		data = data
		last_price = StockDataReader.last_price(data)
		self.portfolio[key]['Last Price $'] = last_price
		self.portfolio[key]['Return %'] = round(
			(last_price / self.portfolio[key]['Price $']) * 100, 2)
		self.portfolio[key]['Return $'] = round(
			last_price * self.portfolio[key]['Amount'], 2)
