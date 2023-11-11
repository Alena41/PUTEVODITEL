import sqlite3

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QMessageBox
from hash_password import hash_pass
from errors import *
from entrance import entrance

SCREEN_SIZE = [1000, 625]


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Регистрация или Вход')

        # Создаём дизайн окна и кнопки с полями ввода

        self.pixmap1 = QPixmap('image_jpg/reg.jpg')
        self.image1 = QLabel(self)
        self.image1.setGeometry(0, 0, *SCREEN_SIZE)
        self.image1.setPixmap(self.pixmap1)

        font = QFont("Times New Roman", 24)
        font1 = QFont("Times New Roman", 20)

        self.entry = QPushButton("Войти", self)
        self.entry.setFont(font)
        self.entry.setGeometry(750, 40, 200, 50)
        self.entry_lbl = QLabel(self)
        self.entry_lbl.setText("Войдите, если есть аккаунт")
        self.entry_lbl.setGeometry(650, 80, 350, 50)
        self.entry_lbl.setFont(font1)
        self.entry.clicked.connect(self.entrance)
        self.entry.setStyleSheet("background-color: "
                                 "rgba(50, 50, 50, 50%); color: white;")
        self.entry_lbl.setStyleSheet("color: white;")

        self.register_button = QPushButton('Зарегистрироваться', self)
        self.register_button.setFont(font)
        self.register_button.setGeometry(650, 500, 300, 50)
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("background-color: "
                                           "rgba(50, 50, 50, 50%); color: "
                                           "white;")

        self.login_write1 = QLineEdit(self)
        self.login_write1.setGeometry(370, 200, 270, 50)
        self.login_write1.setFont(font1)
        self.login_write_lbl1 = QLabel(self)
        self.login_write_lbl1.setText("Логин")
        self.login_write_lbl1.move(270, 210)
        self.login_write_lbl1.setFont(font)
        self.login_write1.setStyleSheet("background-color: "
                                        "rgba(50, 50, 50, 50%); color: white;")
        self.login_write_lbl1.setStyleSheet("color: white;")

        self.pasword_write2 = QLineEdit(self)
        self.pasword_write2.setGeometry(370, 300, 270, 50)
        self.pasword_write2.setFont(font1)
        self.pasword_write_lbl2 = QLabel(self)
        self.pasword_write_lbl2.setText("Пароль")
        self.pasword_write_lbl2.move(250, 310)
        self.pasword_write_lbl2.setFont(font)
        self.pasword_write2.setStyleSheet("background-color: "
                                          "rgba(50, 50, 50, 50%); color: "
                                          "white;")
        self.pasword_write_lbl2.setStyleSheet("color: white;")

        self.pasword_write3 = QLineEdit(self)
        self.pasword_write3.setGeometry(370, 400, 270, 50)
        self.pasword_write3.setFont(font1)
        self.pasword_write_lbl3 = QLabel(self)
        self.pasword_write_lbl3.setText("Повторите пароль")
        self.pasword_write_lbl3.setGeometry(110, 400, 270, 50)
        self.pasword_write_lbl3.setFont(font)
        self.pasword_write3.setStyleSheet("background-color: "
                                          "rgba(50, 50, 50, 50%); color: "
                                          "white;")
        self.pasword_write_lbl3.setStyleSheet("color: white;")

        self.name = QLineEdit(self)
        self.name.setGeometry(370, 100, 270, 50)
        self.name.setFont(font1)
        self.name_lbl = QLabel(self)
        self.name_lbl.setText("Введите имя пользователя")
        self.name_lbl.setGeometry(10, 100, 360, 50)
        self.name_lbl.setFont(font)
        self.name.setStyleSheet("background-color: "
                                "rgba(50, 50, 50, 50%); color: white;")
        self.name_lbl.setStyleSheet("color: white;")

    def register(self):
        # Запоминаем имя, пароль и логин из полей ввода
        name = self.name.text()
        login = self.login_write1.text()
        password = self.pasword_write2.text()
        repeat_password = self.pasword_write3.text()
        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        try:
            # проверка длины пароля
            if len(password) < 8:
                raise LengthError("Пароль должен содержать не менее 8 "
                                  "символов!")

            # Проверка длины логина
            if len(login) < 5:
                raise LengthError("Логин должен сожержать не менее 5 "
                                  "символов!")

            # проверка на наличие как минимум одной заглавной и строчной буквы
            if not any(c.islower() for c in password):
                raise CapitalLetterError("Пароль должен содержать хотя "
                                         "бы одну "
                                         "букву маленького регистра")

            if not any(c.isupper() for c in password):
                raise CapitalLetterError("Пароль должен содержать "
                                         "хотя бы одну "
                                         "букву большого регистра")

            # проверка наличия числа
            if not any(c.isdigit() for c in password):
                raise NumberError("Пароль должен содержать "
                                  "хотя бы одну цифру!")

            # проверка на наличие специального символа
            if not any(not c.isalnum() for c in password):
                raise SpecialCharError("Пароль должен содержать "
                                       "хотя бы один специальный символ!")

            # проверка на русские буквы в логине и пароле
            if (any(c.isalpha() and ord(c) > 127 for c in password)
                    or any(c.isalpha() and ord(c) > 127 for c in login)):
                raise RussianCharError("Логин и пароль не "
                                       "должны содержать русские буквы!")

            # Проверка совпадают ли пароли
            if repeat_password != password:
                raise PasswordsIsNotCorrect("Пароли не совпадают!")

            # проверка на существование логина в бд
            cursor.execute("SELECT * FROM users WHERE login=?",
                           (login.lower(),))
            if cursor.fetchone():
                raise LoginAlreadyExists("Такой логин уже существует!")

            cursor.execute("INSERT INTO users (name, login, password)"
                           " VALUES (?, ?, ?)",
                           (name, login, hash_pass(password)))
            connection.commit()
            QMessageBox.information(self, "Регистрация",
                                    "Регистрация произошла успешно!")
            self.Entrance = entrance()
            self.Entrance.show()
            self.close()

        except (
                LengthError, RussianCharError,
                CapitalLetterError, NumberError, SpecialCharError,
                LoginAlreadyExists, PasswordsIsNotCorrect) as error:
            QMessageBox.warning(self, "Регистрация", str(error))

    def entrance(self):
        self.Entrance = entrance()
        self.Entrance.show()
        self.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
