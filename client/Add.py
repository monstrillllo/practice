import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import AddWindow
import json


class AddNew_Window(QtWidgets.QDialog, AddWindow.Ui_DialogAddNew):
    def __init__(self, parent=None):
        super(AddNew_Window, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.config = {}
        self.load_config()
        self.org = None
        self.before = None
        self.product = None
        self.load = None
        self.unload = None
        self.responsible = None
        self.comment = None
        self.pushButton.clicked.connect(self.add)
        self.show()

    def load_config(self):
        with open('client/config.json', encoding='UTF-8') as conf:
            self.config = json.load(conf)

    def load_from_form(self):
        self.org = self.textOrg.toPlainText()
        self.before = self.textBefore.toPlainText()
        self.product = self.textProduct.toPlainText()
        self.load = self.textLoad.toPlainText()
        self.unload = self.textUnload.toPlainText()
        self.responsible = self.textResponsible.toPlainText()
        self.comment = self.textComment.toPlainText()

    def add(self):
        self.load_from_form()
        data = {
            'organisation': self.org,
            'until': self.before,
            'category': self.product,
            'load_date': self.load,
            'unload_date': self.unload,
            'responsible': self.responsible,
            'comment': self.comment
        }
        try:
            response = requests.post(self.config['defaultIP']+self.config['addNewIP'], json=data)
            if response.json()['status'] == 'success':
                self.parent.updateTable(self.parent.getAllSuppliers())
                self.close()
            else:
                QMessageBox.critical(self, "ERROR", "Something wrong!", QMessageBox.Ok)
        except:
            print('Something wrong while adding!')
