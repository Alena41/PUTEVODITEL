import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QLabel
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtWidgets import QPushButton, QRadioButton

from read_sait_places import BeachMin, BeachAvg, BeachMax, FishingMin
from read_sait_places import FishingAvg, FishingMax, SkiingMin, SkiingAvg
from read_sait_places import SkiingMax

SCREEN_SIZE = [1000, 625]


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Путеводитель для хорошего отдыха')
        font = QFont("Times New Roman", 24)
        font1 = QFont("Times New Roman", 28)

        self.table = QLabel(self)
        self.table.setFont(font1)
        self.table.setText("!Ответьте на вопросы!")
        self.table.setGeometry(350, 0, 1000, 100)

        self.place_groupbox = QButtonGroup()
        self.money_groupbox = QButtonGroup()

        self.qveshion1 = QLabel(self)
        self.qveshion1.setFont(font)
        self.qveshion1.setText("Выберите место, которое хотели бы посетить:")
        self.qveshion1.setGeometry(20, 80, 1000, 100)

        self.beach_button = QRadioButton("Пляж", self)
        self.beach_button.setGeometry(20, 150, 100, 40)
        self.beach_button.setFont(font)

        self.fishing_button = QRadioButton("Рыбалка", self)
        self.fishing_button.setGeometry(140, 150, 160, 40)
        self.fishing_button.setFont(font)

        self.skiing_button = QRadioButton("Лыжи", self)
        self.skiing_button.setGeometry(300, 150, 120, 40)
        self.skiing_button.setFont(font)

        self.place_groupbox.addButton(self.beach_button)
        self.place_groupbox.addButton(self.fishing_button)
        self.place_groupbox.addButton(self.skiing_button)

        self.qveshion2 = QLabel(self)
        self.qveshion2.setFont(font)
        self.qveshion2.setText("Выберите бюджет, который вас устроит:")
        self.qveshion2.setGeometry(20, 200, 1000, 100)

        self.money_min = QRadioButton("Минимальная сумма", self)
        self.money_min.setGeometry(20, 280, 300, 40)
        self.money_min.setFont(font)
        self.money_sp = QRadioButton("Средняя сумма", self)
        self.money_sp.setGeometry(350, 280, 300, 40)
        self.money_sp.setFont(font)
        self.money_max = QRadioButton("Большая сумма", self)
        self.money_max.setGeometry(610, 280, 300, 40)
        self.money_max.setFont(font)

        self.money_groupbox.addButton(self.money_min)
        self.money_groupbox.addButton(self.money_sp)
        self.money_groupbox.addButton(self.money_max)

        self.generation = QPushButton('Сгенерировать результат', self)
        self.generation.setGeometry(1, 340, 998, 40)
        self.generation.clicked.connect(self.generate_result)
        self.generation.setStyleSheet("background-color: "
                                      "rgba(50, 50, 50, 50%); color: white;")

        self.result = QLineEdit(self)
        self.result.setGeometry(1, 390, 998, 150)
        self.result.setFont(font)
        # Выравнивание текста по центру
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setEnabled(False)
        self.result.setStyleSheet("color: black;")

        self.read_bautton = QPushButton('Прочитать подробнее...', self)
        self.read_bautton.setGeometry(1, 560, 998, 40)
        self.read_bautton.clicked.connect(self.read_sait)
        self.read_bautton.setStyleSheet("background-color: "
                                        "rgba(50, 50, 50, 50%); color: white;")

    def generate_result(self):
        connection = sqlite3.connect('butt_tests.db')
        cursor = connection.cursor()

        # Получение выделенных кнопок
        selected_place = self.place_groupbox.checkedButton()
        selected_money = self.money_groupbox.checkedButton()

        # Проверка, что все кнопки выбраны
        if not selected_place or not selected_money:
            QMessageBox.warning(self, "Генератор",
                                "Ответьте на все вопросы!")
        else:
            place_text = selected_place.text()
            money_text = selected_money.text()
            query = """
                    SELECT name
                    FROM places
                    WHERE place = ? AND money = ?
                    """

            cursor.execute(query, (place_text, money_text))
            results = cursor.fetchall()

            names = [elem[0] for elem in results]
            result_text = ", ".join(names)

            connection.close()

            self.result.setText(result_text)

    def read_sait(self):
        selected_place = self.place_groupbox.checkedButton()
        selected_money = self.money_groupbox.checkedButton()
        if selected_place and selected_money:
            if (selected_place.text() == "Пляж" and
                    selected_money.text() == "Минимальная сумма"):
                self.beach_min = BeachMin()
                self.beach_min.show()
                self.close()
            elif (selected_place.text() == "Пляж" and
                  selected_money.text() == "Средняя сумма"):
                self.beach_avg = BeachAvg()
                self.beach_avg.show()
                self.close()
            elif (selected_place.text() == "Пляж" and
                  selected_money.text() == "Большая сумма"):
                self.beach_max = BeachMax()
                self.beach_max.show()
                self.close()
            elif (selected_place.text() == "Рыбалка" and
                  selected_money.text() == "Минимальная сумма"):
                self.fishing_min = FishingMin()
                self.fishing_min.show()
                self.close()
            elif (selected_place.text() == "Рыбалка" and
                  selected_money.text() == "Средняя сумма"):
                self.fishing_avg = FishingAvg()
                self.fishing_avg.show()
                self.close()
            elif (selected_place.text() == "Рыбалка" and
                  selected_money.text() == "Большая сумма"):
                self.fishing_max = FishingMax()
                self.fishing_max.show()
                self.close()
            elif (selected_place.text() == "Лыжи" and
                  selected_money.text() == "Минимальная сумма"):
                self.skiing_min = SkiingMin()
                self.skiing_min.show()
                self.close()
            elif (selected_place.text() == "Лыжи" and
                  selected_money.text() == "Средняя сумма"):
                self.skiing_avg = SkiingAvg()
                self.skiing_avg.show()
                self.close()
            elif (selected_place.text() == "Лыжи" and
                  selected_money.text() == "Большая сумма"):
                self.skiing_max = SkiingMax()
                self.skiing_max.show()
                self.close()
        else:
            QMessageBox.warning(self, "Ошибка",
                                "Пожалуйста, выберите место и сумму")
