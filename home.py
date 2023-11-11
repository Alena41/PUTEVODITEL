from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton

import hash_password
from test_button import Test
from name_profil import UpdateWindow
from Exit import LoginWindow

SCREEN_SIZE = [1000, 625]


class HOME(QMainWindow):
    def __init__(self, name, login, password):
        super().__init__()
        self.name = name[0]
        self.login = login
        self.password = hash_password.hash_pass(password)
        self.initUI()

    def initUI(self):
        # Создаём дизайн окна и делаем рабочие кнопки

        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Путеводитель для хорошего отдыха')

        self.pixmap1 = QPixmap('image_jpg/SAit.jpg')
        self.image1 = QLabel(self)
        self.image1.setGeometry(0, 0, *SCREEN_SIZE)
        self.image1.setPixmap(self.pixmap1)

        self.table = QLabel(self)
        font = QFont("Times New Roman", 28)
        self.table.setFont(font)
        self.table.setText("Добро пожаловать в путеводитель!")
        self.table.setGeometry(250, 1, 1000, 150)
        self.table.setStyleSheet("color: black;")

        self.text = QLabel(self)
        font1 = QFont("Times New Roman", 24)
        self.text.setFont(font1)
        self.text.setText("Хотите отдохнуть, но не знаете как?\n"
                          "Тогда вы обратились по адресу!")
        self.text.setGeometry(40, 120, 1000, 150)
        self.text.setStyleSheet("color: black;")

        self.text1 = QLabel(self)
        self.text1.setFont(font1)
        self.text1.setText("Пройдите ниже тест, чтобы"
                           " мы могли предложить вам \n"
                           "варианты отдыха, учитывая ваши пожелания")
        self.text1.setGeometry(120, 300, 1000, 150)
        self.text1.setStyleSheet("color: black;")

        self.text1_button = QPushButton('!пройти тест!', self)
        self.text1_button.setFont(font1)
        self.text1_button.setGeometry(400, 450, 200, 150)
        self.text1_button.clicked.connect(self.open_test_buttons)
        self.text1_button.setStyleSheet("background-color: "
                                        "rgba(50, 50, 50, 50%); color: white;")

        self.name_button = QPushButton('Изменить имя пользователя', self)
        self.name_button.setGeometry(830, 10, 150, 30)
        self.name_button.setStyleSheet("background-color: "
                                       "rgba(50, 50, 50, 50%); "
                                       "color: white;")
        self.name_button.clicked.connect(self.update)

        self.name_texti = QLabel(self)
        self.name_texti.setText(self.name)
        self.name_texti.setGeometry(830, 50, 150, 30)

        self.delete_button = QPushButton('Удалить профиль', self)
        self.delete_button.setGeometry(830, 90, 150, 30)
        self.delete_button.setStyleSheet("background-color: "
                                         "rgba(50, 50, 50, 50%); "
                                         "color: white;")
        self.delete_button.clicked.connect(self.delete)

    def delete(self):
        LoginWindow(self.login, self.password, self1=self).delete_me()

    def update(self):
        self.update_window = UpdateWindow(self.name_texti)
        self.update_window.show()

    def open_test_buttons(self):
        self.test_but = Test()
        self.test_but.show()
        self.close()
