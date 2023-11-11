from PyQt5.QtWidgets import (QMainWindow, QLabel, QLineEdit, QPushButton,
                             QMessageBox)
import sqlite3


class UpdateWindow(QMainWindow):

    def __init__(self, qlabel1):
        super().__init__()
        self.textii = qlabel1
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Смена имени пользователя")

        self.txt_current_name = QLineEdit(self)
        self.txt_current_name.setGeometry(100, 60, 100, 30)
        self.lbl_current_name = QLabel("Ваше имя:", self)
        self.lbl_current_name.setGeometry(20, 60, 100, 30)

        self.txt_new_name = QLineEdit(self)
        self.txt_new_name.setGeometry(100, 100, 100, 30)
        self.lbl_new_name = QLabel("Новое имя:", self)
        self.lbl_new_name.setGeometry(20, 100, 100, 30)

        self.txt_login = QLineEdit(self)
        self.txt_login.setGeometry(100, 20, 100, 30)
        self.txt_login_lbl = QLabel('Ваш логин:', self)
        self.txt_login_lbl.setGeometry(20, 20, 100, 30)

        self.btn_change = QPushButton("Изменить", self)
        self.btn_change.setGeometry(100, 150, 100, 30)
        self.btn_change.clicked.connect(self.change_name)

    def change_name(self):
        current_name = self.txt_current_name.text()
        new_name = self.txt_new_name.text()
        login = self.txt_login.text()

        conn = sqlite3.connect("passwords.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE login = ? AND name = ?",
                       (login, current_name))
        existing_user = cursor.fetchone()

        if existing_user:
            # Изменение имени в базе данных
            cursor.execute(
                "UPDATE users SET name = ? WHERE login = ? AND name = ?",
                (new_name, login, current_name))
            conn.commit()
            conn.close()
            self.txt_current_name.clear()
            self.txt_new_name.clear()
            self.textii.setText(new_name)

        else:
            QMessageBox.warning(self, "Ошибка",
                                "Такого логина с именем не существет")
