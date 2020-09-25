import threading
import termcolor

from src.utils import DataHandler
from src.portfolio import Portfolio


class MakeMenu:

	def __init__(self):
		pass


class ThreadHandler:

	@classmethod
	def spawn_thread(cls, data):
		pass

latest_portfolio = Portfolio()
print(latest_portfolio.portfolio)
DataHandler.save_portfolio(latest_portfolio.portfolio)


main_msg = """
What would you like to do?
1: Add stock to portfolio
2: View portfolio
3: Overall performance
4: Update portfolio
9: Exit
"""

while True:
	print(main_msg)
	selection = input("Enter your choice: ")
	if selection == "1":
		latest_portfolio.add_stock()
	elif selection == "2":
		latest_portfolio.print_portfolio()
	elif selection == "3":
		print("Performance")
	elif selection == "4":
		latest_portfolio.update_portfolio()
	elif selection == "9":
		break
	else:
		print("Please enter a valid selection!")

DataHandler.save_portfolio(latest_portfolio.portfolio)


