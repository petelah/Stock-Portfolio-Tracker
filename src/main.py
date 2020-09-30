import npyscreen
import sys
from os import system

from utils import DataHandler, StockDataReader
from portfolio import Portfolio
from messages import *
from time import sleep

# Set the console lines
system('mode con: cols=122 lines=32')
current_portoflio = Portfolio()

class SaveToPDF(npyscreen.ActionPopup):
	def create(self):
		self.add(npyscreen.FixedText, value="Please purchase premium to use this feature =).")

	def on_ok(self):
		self.parentApp.switchForm("MAIN")


class DeleteStock(npyscreen.ActionPopup):
	list_stocks = []

	def create(self):
		self.add(npyscreen.FixedText, value="Type in symbole to delete.")
		self.symbol = self.add(npyscreen.TitleText, name="Symbol: ", begin_entry_at=8, use_two_lines=False)
		self.status_msg = self.add(npyscreen.FixedText, value="")

	def on_ok(self):
		if current_portoflio.delete_stock(self.symbol.value):
			self.symbol.value = ""
			to_main = self.parentApp.getForm('MAIN')
			to_main.load_portfolio()
			to_main.load_performance()
			self.parentApp.switchForm("MAIN")
		else:
			self.status_msg.value = "Symbol not found."
		self.display()


class UpdatePortfolio(npyscreen.Popup):
	def create(self):
		self.update_button = self.add(npyscreen.ButtonPress, name="Update", rely=1, relx=1,
		                              when_pressed_function=self.update_press)
		self.update_msg = self.add(npyscreen.FixedText, value="Press update to continue.")
		self.update_msg2 = self.add(npyscreen.FixedText, value="")

	def update_portfolio(self):
		length = len(current_portoflio.portfolio)-1
		if length > 0:
			for idx, (key, _) in enumerate(current_portoflio.portfolio.items()):
				if idx == 4:
					self.update_msg.value = f"Waiting 60 seconds to update {key}..."
					self.update_msg.value = f"Don't forget to buy premium ;)..."
					self.display()
				data = StockDataReader.get_data(key)
				self.update_msg.value = f"Updating {key}..."
				self.display()

				# if "Note" in data.json():
				# 	self.update_msg.value = f"Waiting 60 seconds to update {key}..."
				# 	self.update_msg.value = f"Don't forget to buy premium ;)..."
				# 	self.display()
				# 	sleep(60)
				# 	data = StockDataReader.get_data(key)
				current_portoflio.update_stock(key, data)
			self.update_msg.value = f"Update complete. Press OK to continue."
		else:
			self.update_msg.value = f"No portfolio found. Please add stocks."
		self.display()

	def afterEditing(self):
		self.update_msg.value = f" "
		to_main = self.parentApp.getForm('MAIN')
		if len(current_portoflio.portfolio) > 0:
			to_main.load_portfolio()
			to_main.load_performance()
		self.parentApp.switchForm("MAIN")

	def update_press(self):
		# Update portfolio
		self.update_portfolio()


class AddStock(npyscreen.ActionPopup):
	def create(self):
		self.symbol = self.add(npyscreen.TitleText, name="Symbol: ", begin_entry_at=8, use_two_lines=False)
		self.date = self.add(npyscreen.TitleText, name="Date Purchased: ", begin_entry_at=16, use_two_lines=False)
		self.amount = self.add(npyscreen.TitleText, name="Number of Shares: ", begin_entry_at=18, use_two_lines=False)
		self.price = self.add(npyscreen.TitleText, name="Price: ", begin_entry_at=7, use_two_lines=False)
		self.status_msg = self.add(npyscreen.FixedText, value="")

	def on_ok(self):
		if len(current_portoflio.portfolio) == 6:
			self.status_msg.value = "Max 6 stocks allowed. Please purchase premium version!"
		else:
			last_price = StockDataReader.last_price(StockDataReader.get_data(self.symbol.value))
			validation = DataHandler.validate_entry(self.symbol.value, self.date.value, self.amount.value,
			                                        self.price.value, last_price)
			if validation != True:
				self.status_msg.value = validation
				self.display()
			else:
				current_portoflio.add_stock(
					self.symbol.value,
					float(self.price.value),
					float(self.amount.value),
					self.date.value

				)
				self.status_msg.value = f"Grabbing data for {self.symbol.value}"
				to_main = self.parentApp.getForm('MAIN')
				to_main.load_portfolio()
				to_main.load_performance()
				to_main.top_message.value = "Portfolio:"
				self.display()
				sleep(1.5)
				self.parentApp.switchForm("MAIN")

	def afterEditing(self):
		self.symbol.value = ""
		self.date.value = ""
		self.amount.value = ""
		self.price.value = ""
		self.display()

	def on_cancel(self):
		self.symbol.value = ""
		self.date.value = ""
		self.amount.value = ""
		self.price.value = ""
		self.display()
		self.parentApp.getForm('MAIN')
		self.parentApp.switchForm("MAIN")


class MainForm(npyscreen.FormBaseNewWithMenus):
	stock_object_list = []
	initial_investment = 0
	return_dollar = 0
	pct_return = 0

	def create(self):
		# ====================== Init portfolio ========================
		self.welcome_msg = self.add(npyscreen.FixedText, value=welcome, rely=2)
		self.welcome_msg2 = self.add(npyscreen.FixedText, value=welcome_line2, rely=3)
		self.top_message = self.add(npyscreen.FixedText, value="", relx=8, rely=4)

		# ====================== End init portfolio ====================

		# ====================== Menu section ==========================
		self.menu = self.new_menu(name="Main Menu", shortcut="m")
		self.menu.addItem("1. Add stock to portfolio", self.change_form_add, "1")
		self.menu.addItem("2. Update Portfolio", self.change_form_update, "2")
		self.menu.addItem("3. Save performance to PDF", self.change_form_add, "3")
		self.menu.addItem("4. Delete Stock form portfolio", self.change_form_delete, "4")
		# ====================== End menu section ======================

		self.add(npyscreen.FixedText, value="Performance:", relx=8, rely=26)

		self.main_ii = self.add(npyscreen.FixedText, value=f"Initial Investment: ${self.initial_investment}", relx=8, rely=27)
		self.main_rd = self.add(npyscreen.FixedText, value=f"Returned Amount: ${self.return_dollar}", relx=8,
		         rely=28)
		self.main_pr = self.add(npyscreen.FixedText, value=f"Returned Percent: {self.pct_return}%", relx=8,
		         rely=29)

		self.exit_button = self.add(npyscreen.ButtonPress, name="Exit", rely=29, relx=106,
		                            when_pressed_function=self.exit_press)
		if not DataHandler.check_portfolio_exists():
			self.top_message.value = no_portfolio_msg
		else:
			self.top_message.value = "Portfolio:"
			self.load_portfolio()
			self.load_performance()

	def load_performance(self):
		for key, _ in current_portoflio.portfolio.items():
			self.initial_investment += current_portoflio.portfolio[key]["Initial Investment $"]
			self.return_dollar += current_portoflio.portfolio[key]["Return $"]
		self.pct_return = round((self.return_dollar / self.initial_investment) * 100, 2)
		self.main_ii.value = f"Initial Investment: ${self.initial_investment}"
		self.main_rd.value = f"Returned Amount: ${self.return_dollar}"
		self.main_pr.value = f"Returned Percent: {self.pct_return}%"
		self.display()

	def exit_press(self):
		# Save portfolio
		DataHandler.save_portfolio(current_portoflio.portfolio)
		# Exit
		sys.exit(0)

	def change_form_add(self):
		self.parentApp.getForm('ADD')
		self.parentApp.switchForm("ADD")

	def change_form_update(self):
		self.parentApp.switchForm("UPDATEPORT")

	def change_form_delete(self):
		self.parentApp.switchForm("DELETE")

	def load_portfolio(self):
		for obj in self.stock_object_list:
			if obj.value not in self.stock_object_list:
				obj.hidden = True
		self.stock_object_list = []
		stock_count = 0
		rely = 5
		relx = 8
		for key, _ in current_portoflio.portfolio.items():
			stock_count += 1
			values = []
			for k, v in current_portoflio.portfolio[key].items():
				values.append(f"{k}: {v}")
			if stock_count > 1 and stock_count % 2 != 0:
				relx += 35
				rely = 5
			self.stock_object_list.append(
				self.add(npyscreen.BoxTitle, name=f"{key}",
				         values=values,
				         relx=relx,
				         rely=rely,
				         max_width=35,
				         max_height=10
				         )
			)
			rely += 10
		self.display()


class App(npyscreen.NPSAppManaged):

	def onStart(self):
		self.addForm('MAIN', MainForm, name="Stock Tracker - By Peter Seabrook - V0.2.2", lines=32, columns=122)
		self.addForm('ADD', AddStock, name="Add a stock")
		self.addForm('UPDATEPORT', UpdatePortfolio, name="Portfolio Updating")
		self.addForm('DELETE', DeleteStock, name="Delete Stocks")
		self.addForm('SAVEPDF', SaveToPDF, name="Save to PDF")

	class InputBox(npyscreen.BoxTitle):
		# MultiLineEdit now will be surrounded by boxing
		_contained_widget = npyscreen.MultiLineEdit


app = App().run()
