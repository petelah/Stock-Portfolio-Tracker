import npyscreen

from portfolio import current_portfolio
#from init_class import current_portfolio


class AddStock(npyscreen.ActionPopup):
    def create(self):
        self.symbol = self.add(
            npyscreen.TitleText,
            name="Symbol: ",
            begin_entry_at=8,
            use_two_lines=False)
        self.date = self.add(
            npyscreen.TitleText,
            name="Date Purchased: ",
            begin_entry_at=16,
            use_two_lines=False)
        self.amount = self.add(
            npyscreen.TitleText,
            name="Number of Shares: ",
            begin_entry_at=18,
            use_two_lines=False)
        self.price = self.add(
            npyscreen.TitleText,
            name="Price: ",
            begin_entry_at=7,
            use_two_lines=False)
        self.status_msg = self.add(npyscreen.FixedText, value="")

    def on_ok(self):
        if len(current_portfolio.portfolio) == 6:
            self.status_msg.value = "Max 6 stocks allowed. Please purchase premium version!"
        else:
            result = current_portfolio.add_stock(
                self.symbol.value,
                self.price.value,
                self.amount.value,
                self.date.value
            )
            if result == True:
                self.status_msg.value = f"Grabbing data for {self.symbol.value}"
                to_main = self.parentApp.getForm('MAIN')
                to_main.load_portfolio()
                to_main.load_performance()
                to_main.top_message.value = "Portfolio:"
                self.display()
                sleep(1.5)
                self.symbol.value = ""
                self.date.value = ""
                self.amount.value = ""
                self.price.value = ""
                self.status_msg.value = ""
                self.parentApp.switchForm("MAIN")
            else:
                self.status_msg.value = result
                self.display()

    def on_cancel(self):
        self.symbol.value = ""
        self.date.value = ""
        self.amount.value = ""
        self.price.value = ""
        self.status_msg.value = ""
        self.parentApp.getForm('MAIN')
        self.parentApp.switchForm("MAIN")