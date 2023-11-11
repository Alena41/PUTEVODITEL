import sqlite3

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QMessageBox

from hash_password import hash_pass
from home import HOME

SCREEN_SIZE = [1000, 625]


class entrance(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hom = None
        self.initUI()

    def initUI(self):
        # Создаём дизайн окна

        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Вход')

        font = QFont("Times New Roman", 24)
        font1 = QFont("Times New Roman", 20)

        self.pixmap1 = QPixmap('image_jpg/reg.jpg')
        self.image1 = QLabel(self)
        self.image1.setGeometry(0, 0, *SCREEN_SIZE)
        self.image1.setPixmap(self.pixmap1)

        self.login_write = QLineEdit(self)
        self.login_write.setGeometry(370, 200, 270, 50)
        self.login_write.setFont(font1)
        self.login_write_lbl = QLabel(self)
        self.login_write_lbl.setText("Логин")
        self.login_write_lbl.move(250, 210)
        self.login_write_lbl.setFont(font)
        self.login_write.setStyleSheet("background-color: "
                                       "rgba(50, 50, 50, 50%); "
                                       "color: white;")
        self.login_write_lbl.setStyleSheet("color: white;")

        self.pasword_write = QLineEdit(self)
        self.pasword_write.setGeometry(370, 300, 270, 50)
        self.pasword_write.setFont(font1)
        self.pasword_write_lbl = QLabel(self)
        self.pasword_write_lbl.setText("Пароль")
        self.pasword_write_lbl.move(240, 310)
        self.pasword_write_lbl.setFont(font)
        self.pasword_write.setStyleSheet("background-color: "
                                         "rgba(50, 50, 50, 50%); "
                                         "color: white;")
        self.pasword_write_lbl.setStyleSheet("color: white;")

        self.go_button = QPushButton('Вход', self)
        self.go_button.setFont(font)
        self.go_button.setGeometry(650, 500, 200, 50)
        self.go_button.clicked.connect(self.login)
        self.go_button.setStyleSheet("background-color: "
                                     "rgba(50, 50, 50, 50%); color: white;")

    def login(self):

        login = self.login_write.text()
        password = self.pasword_write.text()

        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users WHERE login=? "
                       "AND password=?",
                       (login, hash_pass(password)))
        result = cursor.fetchone()

        if result:
            self.hom = HOME(result, login, password)
            self.hom.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

        cursor.close()
        connection.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = entrance()
    window.show()
    sys.exit(app.exec_())
