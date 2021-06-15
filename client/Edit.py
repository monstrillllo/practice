import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import EditWindow
import json


class Edit(QtWidgets.QDialog, EditWindow.Ui_DialogEdit):
    def __init__(self, parent=None, selected=None):
        super(Edit, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.selected = selected
        self.config = {}
        self.load_config()
        self.load_not_edited_data()
        self.id = self.parent.tableMain.item(self.selected, 0).text()
        self.org = None
        self.before = None
        self.product = None
        self.load = None
        self.unload = None
        self.responsible = None
        self.comment = None
        self.pushButton.clicked.connect(self.edit)
        self.show()

    def load_config(self):
        with open('client/config.json', encoding='UTF-8') as conf:
            self.config = json.load(conf)

    def load_not_edited_data(self):
        textFields = [self.textOrg, self.textBefore, self.textProduct, self.textLoad, self.textUnload,
                      self.textResponsible, self.textComment]
        # for col in range(1, self.parent.tableMain.columnCount()):
        col = 1
        for field in textFields:
            not_edited = self.parent.tableMain.item(self.selected, col).text()
            field.setText(not_edited)
            col += 1

    def load_from_form(self):
        self.org = self.textOrg.toPlainText()
        self.before = self.textBefore.toPlainText()
        self.product = self.textProduct.toPlainText()
        self.load = self.textLoad.toPlainText()
        self.unload = self.textUnload.toPlainText()
        self.responsible = self.textResponsible.toPlainText()
        self.comment = self.textComment.toPlainText()

    def edit(self):
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
            ip = self.config['defaultIP']+self.config['getSuppliersListIP']+'/'+self.id
            response = requests.put(ip, json=data)
            if response.json()['status'] == 'success':
                self.parent.updateTable(self.parent.getAllSuppliers())
                self.close()
            else:
                QMessageBox.critical(self, "ERROR", "Something wrong!", QMessageBox.Ok)
        except:
            print('Something wrong while editing!')

