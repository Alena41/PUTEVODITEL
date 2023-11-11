import sqlite3

from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox,
                             QInputDialog)
from PyQt5.QtWidgets import QLineEdit
from hash_password import hash_pass

SCREEN_SIZE = [500, 100]


class LoginWindow(QMainWindow):
    def __init__(self, login, password, self1):
        self.self1 = self1
        super().__init__()
        self.login = login
        self.password = password
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, *SCREEN_SIZE)
        self.setWindowTitle('Удаление аккаунта')

    def delete_me(self):
        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        reply = QMessageBox.question(self, 'Подтвердить удаление',
                                     'Вы уверены, что хотите '
                                     'удалить свой профиль?',
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            password, ok = QInputDialog.getText(self,
                                                'Проверка пароля',
                                                'Введите ваш пароль:',
                                                QLineEdit.Password)
            if ok:
                cursor.execute(
                    "SELECT password FROM users WHERE login = ?",
                    (self.login,))
                correct_password = cursor.fetchone()
                if (correct_password and correct_password[0] ==
                        hash_pass(password)):
                    try:

                        cursor.execute("DELETE FROM "
                                       "users WHERE login=?",
                                       (self.login,))

                        connection.commit()
                        QMessageBox.information(self, 'Удалено',
                                                'Вы успешно '
                                                'удалили свой профиль')
                        connection.close()
                        self.close()
                        self.self1.close()

                    except sqlite3.Error as error:
                        print(f"Ошибка: {error}")
                else:
                    QMessageBox.critical(self, 'Ошибка', 'Пароль неверный')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
