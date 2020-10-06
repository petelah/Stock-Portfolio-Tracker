import npyscreen

from screens import MainForm, SaveToPDF, About, AddStock, UpdatePortfolio, DeleteStock


class App(npyscreen.NPSAppManaged):

    def onStart(self):
        self.addForm(
            'MAIN',
            MainForm,
            name="Stock Tracker - By Peter Seabrook - V0.2.2",
            lines=32,
            columns=122)
        self.addForm('ADD', AddStock, name="Add a stock")
        self.addForm('UPDATEPORT', UpdatePortfolio, name="Portfolio Updating")
        self.addForm('DELETE', DeleteStock, name="Delete Stocks")
        self.addForm('SAVEPDF', SaveToPDF, name="Save to PDF")
        self.addForm('ABOUT', About, name="About")

    class InputBox(npyscreen.BoxTitle):
        # MultiLineEdit now will be surrounded by boxing
        _contained_widget = npyscreen.MultiLineEdit