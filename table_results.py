from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTableWidget

SCREEN_SIZE = [400, 200]

# Классы отличаются только количествои колонок и текста, а так всё одинаково


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("Билет на самолёт:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 8350 рублей в одну сторону")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Отель: Pushkin 10")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 1062 рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Отель с животными: Agora")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("от 2000 рублей")
        self.table_widget.setItem(2, 1, item6)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(2)

        item1 = QTableWidgetItem("Билет на самолёт:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 5000 рублей в одну сторону")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Отель (с животными): Apartments Ivanovic")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 3100 рублей за двоих")
        self.table_widget.setItem(1, 1, item4)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("Билет на самолёт:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 35000 рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Отель: Jomtien Palm Beach Hotel & Resort")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 6000 рублей за двоих")
        self.table_widget.setItem(1, 1, item4)
        item3 = QTableWidgetItem("Отель с животными: Rabbit Resort")
        self.table_widget.setItem(2, 0, item3)
        item4 = QTableWidgetItem("от 11000 рублей за двоих")
        self.table_widget.setItem(2, 1, item4)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(2)

        item1 = QTableWidgetItem("Билет на самолёт:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 37 503 рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Отель: Old Palace Resort Sahl Hasheesh")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 13000 рублей за двоих")
        self.table_widget.setItem(1, 1, item4)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("Билет на самолёт за 48 дней:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 52 205 рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Билет на самолёт за 24 дня:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 842 930 рублей")
        self.table_widget.setItem(1, 1, item4)
        item3 = QTableWidgetItem("Отель (с животными): Four Seasons")
        self.table_widget.setItem(2, 0, item3)
        item4 = QTableWidgetItem("от 108000 рублей за двоих")
        self.table_widget.setItem(2, 1, item4)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(2)

        item1 = QTableWidgetItem("Билет на самолёт:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 35000 рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Отель: Mandarin Oriental Jumeira, Dubai")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("от 136000 рублей за двоих")
        self.table_widget.setItem(1, 1, item4)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(12)

        item1 = QTableWidgetItem("Стоимость аренды домика в будни:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("5000 рублей/сутки")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Стоимость аренды домика "
                                 "в Выходные/праздники:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("6000 рублей/сутки")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Весенне-летний период:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("Пойманная рыба оплачивается по "
                                 "прейскуранту")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Осенне-зимний период:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("безлимит")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("Аренда подсачника:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("100 рублей")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("Копчение рыбы")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("300 рублей/шт")
        self.table_widget.setItem(5, 1, item12)

        item13 = QTableWidgetItem("Аренда садка")
        self.table_widget.setItem(6, 0, item13)
        item14 = QTableWidgetItem("100 рублей")
        self.table_widget.setItem(6, 1, item14)

        item15 = QTableWidgetItem("Аренда снастей")
        self.table_widget.setItem(7, 0, item15)
        item16 = QTableWidgetItem("500 рублей")
        self.table_widget.setItem(7, 1, item16)

        item17 = QTableWidgetItem("Чистка рыбы")
        self.table_widget.setItem(8, 0, item17)
        item18 = QTableWidgetItem("150 рублей./шт")
        self.table_widget.setItem(8, 1, item18)

        item19 = QTableWidgetItem("Удочка для зимней ловли")
        self.table_widget.setItem(9, 0, item19)
        item20 = QTableWidgetItem("200 рублей")
        self.table_widget.setItem(9, 1, item20)

        item21 = QTableWidgetItem("Аренда бура")
        self.table_widget.setItem(10, 0, item21)
        item22 = QTableWidgetItem("300 рублей")
        self.table_widget.setItem(10, 1, item22)

        item23 = QTableWidgetItem("Аренда жерлиц, 1шт")
        self.table_widget.setItem(11, 0, item23)
        item24 = QTableWidgetItem("200 рублей")
        self.table_widget.setItem(11, 1, item24)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(9)

        item1 = QTableWidgetItem("с 5:00 до 20:00(залог "
                                 "500рублей обязательно):")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("3000  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("с 12:00 до 20:00(залог "
                                 "500рублей обязательно):")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("1500  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("за час, действует с 12:00(залог "
                                 "2000  рублей):")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("500  рублей")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Удочка, спиннинг или донка:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("500  рублей")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("Садок:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("200  рублей")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("Подсак")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("500 рублей")
        self.table_widget.setItem(5, 1, item12)

        item13 = QTableWidgetItem("Мангал")
        self.table_widget.setItem(6, 0, item13)
        item14 = QTableWidgetItem("500 рублей")
        self.table_widget.setItem(6, 1, item14)

        item15 = QTableWidgetItem("Сетка для барбекю")
        self.table_widget.setItem(7, 0, item15)
        item16 = QTableWidgetItem("500 рублей")
        self.table_widget.setItem(7, 1, item16)

        item17 = QTableWidgetItem("Шампур 1 шт")
        self.table_widget.setItem(8, 0, item17)
        item18 = QTableWidgetItem("50 рублей")
        self.table_widget.setItem(8, 1, item18)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("Котеджи, бани, рестораны, беседки и тд:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("Подробнее ознакомтесь на их сайте")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("в Пн, Вт, Ср, Чт, Пт - Стоимость :")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("3000  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("в Сб, Вс и праздничные дни:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("3000  рублей")
        self.table_widget.setItem(2, 1, item6)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(6)

        item1 = QTableWidgetItem("Стоимость аренды коттеджа на базе:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("начитается от 7000  рублей в сутки")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Аренда моторной лодки на 12 часов:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("4000  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Аренда катера на 2 часа:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("10000  рублей")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Прокат весельной лодки:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("800  рублей")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("Аренда удочки на 12 часов:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("100  рублей")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("Аренда снегохода на час:")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("от 2500  рублей")
        self.table_widget.setItem(5, 1, item12)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window11(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(5)

        item1 = QTableWidgetItem("Норма вылова не превышает сумму:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("2000  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Амур:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("450  рублей/кг")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Карп:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("400  рублей/кг")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Сом:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("600  рублей/кг")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("Щука:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("700  рублей/кг")
        self.table_widget.setItem(4, 1, item10)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window12(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("с 08:00 до 17:00 можно порыбачить за:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("4000  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("котеджи(будни, воскресенье):")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("47 000  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("котеджи(пятница, суббота):")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("56 000  рублей")
        self.table_widget.setItem(2, 1, item6)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window13(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(6)

        item1 = QTableWidgetItem("разовый подъем (будни/выходные):")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("150/200  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("1 час (только в будни):")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("500  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("3 часа (только в выходные):")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("1700  рублей")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("дневной тариф:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("1500/2400  рублей")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("вечерний тариф (пн-чт 19:00-22:00):")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("800  рублей за 3 часа")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("ночной тариф (пт/сб 21:00-00:00):")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("800/1200  рублей за 3 часа")
        self.table_widget.setItem(5, 1, item12)
        item13 = QTableWidgetItem("Отель Волна:")
        self.table_widget.setItem(5, 0, item13)
        item14 = QTableWidgetItem("от 4000  рублей")
        self.table_widget.setItem(5, 1, item14)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window14(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(10)

        item1 = QTableWidgetItem("Отель Ангел:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("от 4900  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("с 09:00 до 17:00:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("1500  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("с 17:00 до 22:00:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("1000  рублей")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("понедельник с 15:00 до 22:00:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("1000  рублей")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("выходной день с 09:00 до "
                                 "20:00:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("2600  рублей")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("два выходных дня:")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("4000  рублей")
        self.table_widget.setItem(5, 1, item12)
        item13 = QTableWidgetItem("1 час(будние/выходные и праздники):")
        self.table_widget.setItem(6, 0, item13)
        item14 = QTableWidgetItem("400/700  рублей")
        self.table_widget.setItem(6, 1, item14)
        item15 = QTableWidgetItem("2 часа:")
        self.table_widget.setItem(7, 0, item15)
        item16 = QTableWidgetItem("700/1100  рублей")
        self.table_widget.setItem(7, 1, item16)
        item17 = QTableWidgetItem("3 часа")
        self.table_widget.setItem(8, 0, item17)
        item18 = QTableWidgetItem("900/1500  рублей")
        self.table_widget.setItem(8, 1, item18)
        item19 = QTableWidgetItem("3 часа детский (5–12 лет):")
        self.table_widget.setItem(9, 0, item19)
        item20 = QTableWidgetItem("500/700  рублей")
        self.table_widget.setItem(9, 1, item20)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window15(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(6)

        item1 = QTableWidgetItem("Ски-пасс за разовый подъём:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("343  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("три подъема:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("860  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Однодневный ски-пасс:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("1891  рублей")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Ски-пасс на 6 дней:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("8699  рублей")
        self.table_widget.setItem(3, 1, item8)
        item9 = QTableWidgetItem("за один час пользования спортинвентарём:")
        self.table_widget.setItem(4, 0, item9)
        item10 = QTableWidgetItem("343  рублей")
        self.table_widget.setItem(4, 1, item10)
        item11 = QTableWidgetItem("Отель Villa Mtashi Bakuriani:")
        self.table_widget.setItem(5, 0, item11)
        item12 = QTableWidgetItem("за 11800  рублей")
        self.table_widget.setItem(5, 1, item12)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window16(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)

        item1 = QTableWidgetItem("Отель Suntower:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("за 4700  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("ski-pass:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("примерно 687  рублей")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("Аренда лыж и сноубордов на 1 день:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("859  рублей")
        self.table_widget.setItem(2, 1, item6)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window17(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(4)

        item1 = QTableWidgetItem("Отель Hotel Vereina:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("за 49600  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("взрослые за день платят:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("70 CHF")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("подростки:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("49 CHF")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("дети:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("28 CHF")
        self.table_widget.setItem(3, 1, item8)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')


class Window18(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Таблица с результатом')

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(4)

        item1 = QTableWidgetItem("Отель Les Suites de la Potinière:")
        self.table_widget.setItem(0, 0, item1)
        item2 = QTableWidgetItem("классический номер за "
                                 "86000  рублей")
        self.table_widget.setItem(0, 1, item2)
        item3 = QTableWidgetItem("Для взрослых:")
        self.table_widget.setItem(1, 0, item3)
        item4 = QTableWidgetItem("629/547 евро")
        self.table_widget.setItem(1, 1, item4)
        item5 = QTableWidgetItem("детей:")
        self.table_widget.setItem(2, 0, item5)
        item6 = QTableWidgetItem("503,20/437,60 евро")
        self.table_widget.setItem(2, 1, item6)
        item7 = QTableWidgetItem("Стоимость 2 взрослых и 2 детских "
                                 "скипассов на 6 дней:")
        self.table_widget.setItem(3, 0, item7)
        item8 = QTableWidgetItem("864 евро")
        self.table_widget.setItem(3, 1, item8)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                   'CSV файлы (*.csv)')

        if file_name:
            with open(file_name, 'w') as file:
                rows = self.table_widget.rowCount()
                columns = self.table_widget.columnCount()

                for row in range(rows):
                    for column in range(columns):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            text = item.text()
                            file.write(text + ',')
                    file.write('\n')
