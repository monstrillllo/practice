# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/monstrillllo/PycharmProjects/flaskProject/client/FindWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogFind(object):
    def setupUi(self, DialogFind):
        DialogFind.setObjectName("DialogFind")
        DialogFind.resize(420, 180)
        self.comboBoxFindType = QtWidgets.QComboBox(DialogFind)
        self.comboBoxFindType.setGeometry(QtCore.QRect(20, 20, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxFindType.setFont(font)
        self.comboBoxFindType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxFindType.setObjectName("comboBoxFindType")
        self.lineFindValue = QtWidgets.QLineEdit(DialogFind)
        self.lineFindValue.setGeometry(QtCore.QRect(230, 20, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineFindValue.setFont(font)
        self.lineFindValue.setObjectName("lineFindValue")
        self.btnFind = QtWidgets.QPushButton(DialogFind)
        self.btnFind.setGeometry(QtCore.QRect(145, 110, 130, 50))
        self.btnFind.setObjectName("btnFind")
        self.btnAddMoreTypes = QtWidgets.QPushButton(DialogFind)
        self.btnAddMoreTypes.setGeometry(QtCore.QRect(190, 60, 40, 40))
        self.btnAddMoreTypes.setText("")
        self.btnAddMoreTypes.setObjectName("btnAddMoreTypes")

        self.retranslateUi(DialogFind)
        QtCore.QMetaObject.connectSlotsByName(DialogFind)

    def retranslateUi(self, DialogFind):
        _translate = QtCore.QCoreApplication.translate
        DialogFind.setWindowTitle(_translate("DialogFind", "Find"))
        self.btnFind.setText(_translate("DialogFind", "Find"))
