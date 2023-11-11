from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit

SCREEN_SIZE = [235, 440]
font = QFont("Times New Roman", 28)


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Калькулятор')

        # Создаем QLabel для отображения текущего выражения
        self.result = QLineEdit(self)
        self.result.setGeometry(1, 1, 234, 140)
        self.result.setEnabled(False)
        self.result.setFont(font)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(30, 145, 100, 50)
        self.clear_button.clicked.connect(self.cleared)

        self.num1 = QPushButton('1', self)
        self.num1.setGeometry(1, 200, 50, 50)
        self.num1.clicked.connect(self.update_result)
        self.num2 = QPushButton('2', self)
        self.num2.setGeometry(55, 200, 50, 50)
        self.num2.clicked.connect(self.update_result)
        self.num3 = QPushButton('3', self)
        self.num3.setGeometry(110, 200, 50, 50)
        self.num3.clicked.connect(self.update_result)
        self.num4 = QPushButton('4', self)
        self.num4.setGeometry(1, 255, 50, 50)
        self.num4.clicked.connect(self.update_result)
        self.num5 = QPushButton('5', self)
        self.num5.setGeometry(55, 255, 50, 50)
        self.num5.clicked.connect(self.update_result)
        self.num6 = QPushButton('6', self)
        self.num6.setGeometry(110, 255, 50, 50)
        self.num6.clicked.connect(self.update_result)
        self.num7 = QPushButton('7', self)
        self.num7.setGeometry(1, 310, 50, 50)
        self.num7.clicked.connect(self.update_result)
        self.num8 = QPushButton('8', self)
        self.num8.setGeometry(55, 310, 50, 50)
        self.num8.clicked.connect(self.update_result)
        self.num9 = QPushButton('9', self)
        self.num9.setGeometry(110, 310, 50, 50)
        self.num9.clicked.connect(self.update_result)
        self.num0 = QPushButton('0', self)
        self.num0.setGeometry(1, 365, 70, 50)
        self.num0.clicked.connect(self.update_result)

        self.dot_button = QPushButton('.', self)
        self.dot_button.setGeometry(75, 365, 50, 50)
        self.dot_button.clicked.connect(self.update_result)

        self.plus = QPushButton('+', self)
        self.plus.setGeometry(170, 145, 50, 50)

        self.minus = QPushButton('-', self)
        self.minus.setGeometry(170, 200, 50, 50)

        self.mnohzitel = QPushButton('*', self)
        self.mnohzitel.setGeometry(170, 255, 50, 50)

        self.delit = QPushButton('/', self)
        self.delit.setGeometry(170, 310, 50, 50)

        # Создаем кнопку "равно"
        self.equals_button = QPushButton('=', self)
        self.equals_button.setGeometry(130, 365, 100, 50)
        self.equals_button.clicked.connect(self.evaluate_expression)

        self.plus.clicked.connect(self.add)
        self.minus.clicked.connect(self.subtraction)
        self.mnohzitel.clicked.connect(self.multiplication)
        self.delit.clicked.connect(self.division)

    def cleared(self):
        self.result.clear()

    def update_result(self):
        sender = self.sender()
        self.result.setText(self.result.text() + sender.text())

    def add(self):
        expression = self.result.text()
        if not expression.endswith('+'):
            self.result.setText(expression + '+')

    def subtraction(self):
        expression = self.result.text()
        if not expression.endswith('-'):
            self.result.setText(expression + '-')

    def multiplication(self):
        expression = self.result.text()
        if not expression.endswith('*'):
            self.result.setText(expression + '*')

    def division(self):
        expression = self.result.text()
        if not expression.endswith('/'):
            self.result.setText(expression + '/')

    def evaluate_expression(self):
        expression = self.result.text()
        try:
            result = eval(expression)
            self.result.setText(str(result))
        except Exception as e:
            self.result.setText('Ошибка')
