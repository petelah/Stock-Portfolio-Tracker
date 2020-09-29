from utils import StockDataReader, DataHandler


class Portfolio:

	def __init__(self):
		self.portfolio = self.load_portfolio()

	def input_questions(self):
		stock = input("Enter the stock ticker: ")
		price = int(input(f"What price did you buy {stock} at: "))
		amount = int(input("How many shares: "))
		date = input("Date of purchase(yyyy-mm-dd): ")
		return stock, price, amount, date

	def add_stock(self, stock, price, amount, date):
		# stock, price, amount, date = self.input_questions()
		last_price = StockDataReader.last_price(
			StockDataReader.get_data(stock))
		self.portfolio[stock] = {
			'Date': date,
			'Price': price,
			'Amount': amount,
			'Last Price': last_price,
			'Initial Investment': price * amount,
			'Return Pct': round((last_price / price) * 100, 2),
			'Return Dollar': round(last_price * amount, 2)
		}

	def load_portfolio(self):
		if DataHandler.check_portfolio_exists():
			return DataHandler.load_portfolio()
		else:
			return dict({})

	def create_portfolio(self):
		if DataHandler.check_portfolio_exists():
			return DataHandler.load_portfolio()
		else:
			print("Initialsing you portfolio!")
			stocks = input(
				"Enter stock tickers separated by ','(IBM, AAPL, SPY): ")
			stocks = DataHandler.cleaner(stocks)
			values = dict()
			for stock in stocks:
				price = int(input(f"What price did you buy {stock} at: "))
				amount = int(input("How many shares: "))
				date = input("Date of purchase(yyyy-mm-dd): ")
				last_price = StockDataReader.last_price(
					StockDataReader.get_data(stock))
				values[stock] = {
					'Date': date,
					'Price': price,
					'Amount': amount,
					'Last Price': last_price,
					'Initial Investment': price * amount,
					'Return Pct': round((last_price / price) * 100, 2),
					'Return Dollar': round(last_price * amount, 2)
				}
			return values

	def update_stock(self, key, data):
		key = key
		data = data
		last_price = StockDataReader.last_price(data)
		self.portfolio[key]['Last Price'] = last_price
		self.portfolio[key]['Return Pct'] = round(
			(last_price / self.portfolio[key]['Price']) * 100, 2)
		self.portfolio[key]['Return Dollar'] = round(
			last_price * self.portfolio[key]['Amount'], 2)
