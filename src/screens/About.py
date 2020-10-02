import npyscreen

class About(npyscreen.Popup):
    def create(self):
        self.add(
            npyscreen.FixedText,
            value="Created by Peter Seabrook.")
        self.add(
            npyscreen.FixedText,
            value="www.peterseabrook.com")
        self.add(
            npyscreen.FixedText,
            value="www.github.com/petelah")
        self.add(
            npyscreen.FixedText,
            value="This app is free to use under GNU license.")
        self.add(
            npyscreen.FixedText,
            value="Copyright Peter Seabrook 2020.")

    def afterEditing(self):
        self.parentApp.switchForm("MAIN")