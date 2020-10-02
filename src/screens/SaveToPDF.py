import npyscreen

class SaveToPDF(npyscreen.Popup):
    def create(self):
        self.add(
            npyscreen.FixedText,
            value="Please purchase premium to use this feature =).")

    def afterEditing(self):
        self.parentApp.switchForm("MAIN")