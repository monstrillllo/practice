import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import FindWindowUI
import json


class Find(QtWidgets.QDialog, FindWindowUI.Ui_DialogFind):
    def __init__(self, parent=None):
        super(Find, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.findData = {}
        self.config = {}
        self.load_config()
        self.rus_en_heders = {
            '№': '№',
            'organisation': 'организация',
            'until': 'контракт до',
            'category': 'категория товара',
            'load_date': 'дата погрузки',
            'unload_date': 'дата разгрузки',
            'responsible': 'отв. лицо',
            'comment': 'комментарий'
        }
        self.btnAddMoreTypes.setIcon(QIcon(self.config['addTypesToFindPng']))
        self.btnAddMoreTypes.setIconSize(QSize(40, 40))
        self.comboBoxFindType.insertItems(0, [x for x in self.rus_en_heders.values()])
        self.findingBars = [
            [self.comboBoxFindType, self.lineFindValue]
        ]
        self.btnFind.clicked.connect(self.find)
        self.btnAddMoreTypes.clicked.connect(self.addType)
        self.show()

    def load_config(self):
        with open('client/config.json', encoding='UTF-8') as conf:
            self.config = json.load(conf)

    def find(self):
        for text in self.findingBars:
            current_type = str(text[0].currentText())
            current_value = str(text[1].text())
            if current_type not in self.findData.keys():
                self.findData[current_type] = [current_value]
            else:
                self.findData[current_type].append(current_value)
        try:
            res = requests.get(self.config['defaultIP']+self.config['findIP'], json=self.findData).json()
            if res['suppliers']:
                # print(self.parent.getAllSuppliers())
                # print(res)
                self.parent.updateTable(res)
                self.close()
            else:
                QMessageBox.critical(self, "ERROR", "Cant find!", QMessageBox.Ok)
                self.findData = {}
        except:
            QMessageBox.critical(self, "ERROR", "Probably connection error!", QMessageBox.Ok)
            self.findData = {}

    def createFindBars(self):
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(self.findingBars[-1][0].geometry().left(),
                                               self.findingBars[-1][0].geometry().top() + 40, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.insertItems(0, [x for x in self.rus_en_heders.values()])

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(self.findingBars[-1][1].geometry().left(),
                                               self.findingBars[-1][1].geometry().top() + 40, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineFindValue.setFont(font)

        self.findingBars.append([self.comboBox, self.lineEdit])

    def addType(self):
        self.resize(self.size().width(), self.size().height() + 40)
        self.btnFind.setGeometry(QtCore.QRect(self.btnFind.geometry().left(),
                                              self.btnFind.geometry().top() + 40, 130, 50))
        self.btnAddMoreTypes.setGeometry(QtCore.QRect(self.btnAddMoreTypes.geometry().left(),
                                                      self.btnAddMoreTypes.geometry().top() + 40, 40, 40))

        self.createFindBars()
        for box in self.findingBars:
            box[0].show()
            box[1].show()
