from PyQt5.QtWidgets import QMainWindow, QCalendarWidget


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calendar = QCalendarWidget(self)
        self.setCentralWidget(self.calendar)
        self.setWindowTitle("Календарь")