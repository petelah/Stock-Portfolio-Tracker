import npyscreen

from portfolio import current_portfolio
from utilities import StockDataReader, DataHandler
from utilities.messages import *


class MainForm(npyscreen.FormBaseNewWithMenus):
    stock_object_list = []
    initial_investment = 0
    return_dollar = 0
    pct_return = 0

    def create(self):
        # ====================== Init portfolio ========================
        self.welcome_msg = self.add(npyscreen.FixedText, value=welcome, rely=2)
        self.welcome_msg2 = self.add(
            npyscreen.FixedText, value=welcome_line2, rely=3)
        self.top_message = self.add(
            npyscreen.FixedText, value="", relx=8, rely=4)

        # ====================== End init portfolio ====================

        # ====================== Menu section ==========================
        self.menu = self.new_menu(name="Main Menu", shortcut="m")
        self.menu.addItem(
            "1. Add stock to portfolio",
            self.change_form_add,
            "1")
        self.menu.addItem("2. Update Portfolio", self.change_form_update, "2")
        self.menu.addItem(
            "3. Save performance to PDF",
            self.change_form_save_pdf,
            "3")
        self.menu.addItem(
            "4. Delete Stock form portfolio",
            self.change_form_delete,
            "4")
        self.menu.addItem(
            "5. About",
            self.change_form_about,
            "5")
        # ====================== End menu section ======================

        # ====================== Main content section ==================
        self.add(npyscreen.FixedText, value="Performance:", relx=8, rely=26)

        self.main_ii = self.add(
            npyscreen.FixedText,
            value=f"Initial Investment: ${self.initial_investment}",
            relx=8,
            rely=27)
        self.main_rd = self.add(
            npyscreen.FixedText,
            value=f"Returned Amount: ${self.return_dollar}",
            relx=8,
            rely=28)
        self.main_pr = self.add(npyscreen.FixedText,
                                value=f"Returned Percent: {self.pct_return}%",
                                relx=8,
                                rely=29
                                )
        # ====================== End ain content section ===============

        self.exit_button = self.add(
            npyscreen.ButtonPress,
            name="Exit",
            rely=29,
            relx=106,
            when_pressed_function=self.exit_press)
        if not DataHandler.check_portfolio_exists():
            self.top_message.value = no_portfolio_msg
        else:
            self.top_message.value = "Portfolio:"
            self.load_portfolio()
            self.load_performance()

    def load_performance(self):
        for key, _ in current_portfolio.portfolio.items():
            self.initial_investment += current_portfolio.portfolio[key]["Initial Investment $"]
            self.return_dollar += current_portfolio.portfolio[key]["Return $"]
        self.pct_return = round(
            (self.return_dollar / self.initial_investment) * 100, 2)
        self.main_ii.value = f"Initial Investment: ${round(self.initial_investment, 2)}"
        self.main_rd.value = f"Returned Amount: ${round(self.return_dollar, 2)}"
        self.main_pr.value = f"Returned Percent: {round(self.pct_return, 2)}%"
        self.display()

    def exit_press(self):
        # Save portfolio
        DataHandler.save_portfolio(current_portfolio.portfolio)
        # Exit
        sys.exit(0)

    def change_form_add(self):
        self.parentApp.switchForm("ADD")

    def change_form_about(self):
        self.parentApp.switchForm("ABOUT")

    def change_form_save_pdf(self):
        self.parentApp.switchForm("SAVEPDF")

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
        for key, _ in current_portfolio.portfolio.items():
            stock_count += 1
            values = []
            for k, v in current_portfolio.portfolio[key].items():
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