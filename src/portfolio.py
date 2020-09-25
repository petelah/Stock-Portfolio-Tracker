from src.utils import StockDataReader, DataHandler

class Portfolio:

	def __init__(self):
		self.portfolio = self.create_portfolio()

	def print_portfolio(self):
		for key, value in self.portfolio.items():
			print(f"{key}:")
			for k, v in self.portfolio[key].items():
				print(f"{k}: {v}")

	def add_stock(self):
		stock = input("Enter the stock ticker: ")
		price = int(input(f"What price did you buy {stock} at: "))
		amount = int(input(f"How many shares: "))
		date = input("Date of purchase(yyyy-mm-dd): ")
		last_price = StockDataReader.last_price(StockDataReader.get_data(stock))
		self.portfolio[stock] = {
			'Date': date,
			'Price': price,
			'Amount': amount,
			'Last Price': last_price,
			'Initial Investment': price*amount,
			'Return Pct': round((last_price / price) * 100, 2),
			'Return Dollar': round(last_price * amount, 2)
		}


	def create_portfolio(self):
		if DataHandler.check_portfolio_exists():
			return DataHandler.load_portfolio()
		else:
			print("Initialsing you portfolio!")
			stocks = input("Enter stock tickers separated by ','(IBM, AAPL, SPY): ")
			stocks = DataHandler.cleaner(stocks)
			values = dict()
			for stock in stocks:
				price = int(input(f"What price did you buy {stock} at: "))
				amount = int(input(f"How many shares: "))
				date = input("Date of purchase(yyyy-mm-dd): ")
				last_price = StockDataReader.last_price(StockDataReader.get_data(stock))
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

	def update_portfolio(self):
		for key, _ in self.portfolio.items():
			print(f"Updating: {key}")
			last_price = StockDataReader.last_price(StockDataReader.get_data(key))
			self.portfolio[key]['Last Price'] = last_price
			self.portfolio[key]['Return Pct'] = round((last_price / self.portfolio[key]['Price']) * 100, 2)
			self.portfolio[key]['Return Dollar'] = round(last_price * self.portfolio[key]['Amount'], 2)
		print("Update complete!")