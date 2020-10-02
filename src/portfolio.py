from utils import StockDataReader, DataHandler


class Portfolio:
    """
    Portfolio class to hold all the data and main operations of
    that data.
    """

    def __init__(self):
        self.portfolio = self.load_portfolio()

    def add_stock(self, stock: str, price, amount: int, date: str):
        """
        Adds a stock to the portfolio based on user input.
        :param stock: str
        :param price: number
        :param amount: number
        :param date: str
        :return: str or bool
        """
        last_price = StockDataReader.last_price(
            StockDataReader.get_data(stock))
        validation = DataHandler.validate_entry(
            stock,
            date,
            amount,
            price,
            last_price)
        if validation != True:
            return validation
        self.portfolio[stock] = {
            'Date': date,
            'Price $': price,
            'Amount': float(amount),
            'Last Price $': last_price,
            'Initial Investment $': float(price) * float(amount),
            'Return %': round((last_price / float(price)) * 100, 2),
            'Return $': round(last_price * float(amount), 2)
        }
        return True

    def load_portfolio(self) -> dict:
        """
        Loads portfolio into the class checking first if the portfolio exists.
        :return: dict
        """
        if DataHandler.check_portfolio_exists():
            return DataHandler.load_portfolio()
        else:
            return dict({})

    def update_stock(self, key: str, data):
        """
        Function to update a stock inside the portfolio.
        :param key: str
        :param data: requests object
        :return: N/A
        """
        key = key
        data = data
        last_price = StockDataReader.last_price(data)
        self.portfolio[key]['Last Price $'] = last_price
        self.portfolio[key]['Return %'] = round(
            (last_price / self.portfolio[key]['Price $']) * 100, 2)
        self.portfolio[key]['Return $'] = round(
            last_price * self.portfolio[key]['Amount'], 2)

    def delete_stock(self, symbol: str) -> bool:
        """
        Simple pop a symbol from the dictionary if it exists.
        :param symbol: str
        :return: bool
        """
        symbol = symbol.upper()
        try:
            self.portfolio.pop(symbol)
            return True
        except KeyError:
            return False
