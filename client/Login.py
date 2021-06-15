from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import LoginWindow
import requests
import json


class Login_Window(QtWidgets.QDialog, LoginWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(Login_Window, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.config = {}
        self.load_config()
        self.lg = None
        self.pswrd = None
        self.pushButton.clicked.connect(self.login)
        self.show()

    def load_config(self):
        with open('client/config.json', encoding='UTF-8') as conf:
            self.config = json.load(conf)

    def login(self):
        self.lg = self.lineLogin.text()
        self.pswrd = self.linePassword.text()
        if self.lg and self.pswrd:
            data = {
                'user_name': self.lg,
                'password': self.pswrd
            }
            if self.radioButton.isChecked():
                ip = self.config['defaultIP'] + self.config['loginIP']
            elif self.radioButton_2.isChecked():
                ip = self.config['defaultIP'] + self.config['registerIP']
            else:
                QMessageBox.critical(self, "ERROR", "Login or register must be chosen!", QMessageBox.Ok)
                return
            try:
                response = requests.post(ip, json=data)
                response_data = response.json()
                if response_data['status'] == 'success':
                    self.parent.update_user(user=response_data['data']['user_name'],
                                            status=response_data['data']['role'])
                    if response_data['data']['role'] == 'admin':
                        self.parent.updateIpInputStatus(False)
                    else:
                        self.parent.updateIpInputStatus()
                    self.close()
                else:
                    if self.radioButton.isChecked():
                        QMessageBox.critical(self, "ERROR", "Incorrect login or password!", QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "ERROR", "Login already in use!", QMessageBox.Ok)
            except:
                print('Something wrong!')
        else:
            QMessageBox.critical(self, "ERROR", "All fields must be filled!", QMessageBox.Ok)