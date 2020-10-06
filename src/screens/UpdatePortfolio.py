import npyscreen
from time import sleep

from utilities import StockDataReader, DataHandler
from portfolio import current_portfolio


class UpdatePortfolio(npyscreen.Popup):
    def create(self):
        self.update_button = self.add(
            npyscreen.ButtonPress,
            name="Update",
            rely=1,
            relx=1,
            when_pressed_function=self.update_press)
        self.update_msg = self.add(
            npyscreen.FixedText,
            value="Press update to continue.")
        self.update_msg2 = self.add(npyscreen.FixedText, value="")

    def update_portfolio(self):
        length = len(current_portfolio.portfolio) - 1
        if length > 0:
            for idx, (key, _) in enumerate(
                    current_portfolio.portfolio.items()):
                data = StockDataReader.get_data(key)
                if not current_portfolio.update_stock(key, data):
                    self.update_msg.value = f"Waiting 60 seconds to update {key}..."
                    self.display()
                    sleep(55)
                    self.update_msg.value = "Don't forget to buy premium ;)..."
                    self.display()
                    sleep(6)
                    current_portfolio.update_stock(key, data)
                else:
                    self.update_msg.value = f"Updating {key}..."
                    self.display()
                    sleep(1)
            self.update_msg.value = "Update complete. Press OK to continue."
        else:
            self.update_msg.value = "No portfolio found. Please add stocks."
        self.display()

    def afterEditing(self):
        self.update_msg.value = " "
        to_main = self.parentApp.getForm('MAIN')
        if len(current_portfolio.portfolio) > 0:
            to_main.load_portfolio()
            to_main.load_performance()
        self.parentApp.switchForm("MAIN")

    def update_press(self):
        # Update portfolio
        self.update_portfolio()