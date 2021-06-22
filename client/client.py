import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Login import Login_Window
from Add import AddNew_Window
from Edit import Edit
from Find import Find
import ClientMainWindowUI
import json


class Client_App(QtWidgets.QMainWindow, ClientMainWindowUI.Ui_Client):
    def __init__(self):
        super().__init__()
        self.config = {}
        self.load_config()
        self.setupUi(self)

        self.authorized = False
        self.textServerIP.setPlaceholderText(self.config['defaultIP'])
        # try:
        #     self.updateTable(self.getAllSuppliers())
        # except:
        #     self.check_connection()
        # self.btnRefresh.setIcon(QIcon(self.config['refreshPng']))
        # if self.check_authorized():
        #     self.check_connection()
        # self.btnCheckConn.clicked.connect(self.check_connection)
        # self.updateTable(self.getAllSuppliers())
        self.btnLogin.clicked.connect(self.login)
        self.btnAdd.clicked.connect(self.addNew)
        self.btnEdit.clicked.connect(self.edit)
        self.btnFind.clicked.connect(self.find)
        self.btnDelete.clicked.connect(self.delete)
        self.btnRefresh.clicked.connect(self.refresh)

    def check_authorized(self):
        if self.authorized:
            self.btnRefresh.setEnabled(True)
            self.btnAdd.setEnabled(True)
            self.btnFind.setEnabled(True)
            self.btnEdit.setEnabled(True)
            self.btnDelete.setEnabled(True)
            self.btnCheckConn.setEnabled(True)
            return True
        else:
            return False

    def refresh(self):
        self.updateTable(self.getAllSuppliers())

    def update_btns_and_table(self):
        self.updateTable(self.getAllSuppliers())
        self.btnLogin.clicked.connect(self.login)
        self.btnAdd.clicked.connect(self.addNew)
        self.btnEdit.clicked.connect(self.edit)
        self.btnFind.clicked.connect(self.find)
        self.btnDelete.clicked.connect(self.delete)

    def load_config(self):
        with open('client/config.json', encoding='UTF-8') as conf:
            self.config = json.load(conf)

    def updateIpInputStatus(self, stat=True):
        self.textServerIP.setReadOnly(stat)

    def login(self):
        Login_Window(self)

    def find(self):
        Find(self)

    def update_user(self, user, status):
        self.labelLoginStatus.setText(f"Пользователь: {user} - {status}")

    def check_connection(self):
        if self.authorized:
            if self.textServerIP.toPlainText():
                self.config['defaultIP'] = self.textServerIP.toPlainText()
            try:
                response = requests.post(self.config['defaultIP'])
                # print(type(response.json()['server_status']))
                if response.json()['server_status'] == 'online':
                    pixmap = QPixmap(self.config['onlinePng'])
                    self.lableStatus.setPixmap(pixmap)
                    self.updateTable(self.getAllSuppliers())
                    # self.update_btns_and_table()
                else:
                    pixmap = QPixmap(self.config['offlinePng'])
                    self.lableStatus.setPixmap(pixmap)
            except:
                pixmap = QPixmap(self.config['offlinePng'])
                self.lableStatus.setPixmap(pixmap)

    def addNew(self):
        AddNew_Window(self)

    def edit(self):
        Edit(self, self.tableMain.currentRow())

    def updateTable(self, list_for_table):
        self.tableMain.setRowCount(0)
        header_id = {
            0: 'id',
            1: 'organisation',
            2: 'until',
            3: 'category',
            4: 'load_date',
            5: 'unload_date',
            6: 'responsible',
            7: 'comment'
        }
        for sup in list_for_table['suppliers']:
            row_pos = self.tableMain.rowCount()
            self.tableMain.insertRow(row_pos)
            for i in range(len(sup)):
                self.tableMain.setItem(row_pos, i, QTableWidgetItem(str(sup[header_id[i]])))
        self.tableMain.show()

    def getAllSuppliers(self):
        try:
            response = requests.get(self.config['defaultIP'] + self.config['getSuppliersListIP'])
            suppliers_list = response.json()
        except:
            return
        return suppliers_list

    def delete(self):
        try:
            if self.tableMain.currentRow() != -1:
                ip = self.config['defaultIP'] + self.config['getSuppliersListIP'] + '/' +\
                     self.tableMain.item(self.tableMain.currentRow(), 0).text()
                response = requests.delete(ip)
                if not response.json()['status'] == 'success':
                    QMessageBox.critical(self, "ERROR", "Something went wrong!", QMessageBox.Ok)
                else:
                    self.updateTable(self.getAllSuppliers())
            else:
                QMessageBox.critical(self, "ERROR", "Row doesnt selected!", QMessageBox.Ok)
        except:
            QMessageBox.critical(self, "ERROR", "Probably connection error!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Client_App()
    window.show()
    app.exec()
