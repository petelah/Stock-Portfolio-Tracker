import npyscreen

from portfolio import current_portfolio


class DeleteStock(npyscreen.ActionPopup):
    list_stocks = []

    def create(self):
        self.add(npyscreen.FixedText, value="Type in symbole to delete.")
        self.symbol = self.add(
            npyscreen.TitleText,
            name="Symbol: ",
            begin_entry_at=8,
            use_two_lines=False)
        self.status_msg = self.add(npyscreen.FixedText, value="")

    def on_ok(self):
        if current_portfolio.delete_stock(self.symbol.value):
            self.symbol.value = ""
            to_main = self.parentApp.getForm('MAIN')
            to_main.load_portfolio()
            to_main.load_performance()
            self.parentApp.switchForm("MAIN")
        else:
            self.status_msg.value = "Symbol not found."
        self.display()