# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/monstrillllo/PycharmProjects/flaskProject/AddWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddNew(object):
    def setupUi(self, DialogAddNew):
        DialogAddNew.setObjectName("DialogAddNew")
        DialogAddNew.resize(420, 504)
        DialogAddNew.setMinimumSize(QtCore.QSize(420, 504))
        DialogAddNew.setMaximumSize(QtCore.QSize(420, 504))
        self.labelOrg = QtWidgets.QLabel(DialogAddNew)
        self.labelOrg.setGeometry(QtCore.QRect(10, 10, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelOrg.setFont(font)
        self.labelOrg.setObjectName("labelOrg")
        self.labelBefore = QtWidgets.QLabel(DialogAddNew)
        self.labelBefore.setGeometry(QtCore.QRect(10, 60, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelBefore.setFont(font)
        self.labelBefore.setObjectName("labelBefore")
        self.labelProduct = QtWidgets.QLabel(DialogAddNew)
        self.labelProduct.setGeometry(QtCore.QRect(10, 110, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelProduct.setFont(font)
        self.labelProduct.setObjectName("labelProduct")
        self.labelLoad = QtWidgets.QLabel(DialogAddNew)
        self.labelLoad.setGeometry(QtCore.QRect(10, 160, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelLoad.setFont(font)
        self.labelLoad.setObjectName("labelLoad")
        self.labelUnload = QtWidgets.QLabel(DialogAddNew)
        self.labelUnload.setGeometry(QtCore.QRect(10, 210, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelUnload.setFont(font)
        self.labelUnload.setObjectName("labelUnload")
        self.labelResponsible = QtWidgets.QLabel(DialogAddNew)
        self.labelResponsible.setGeometry(QtCore.QRect(10, 260, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelResponsible.setFont(font)
        self.labelResponsible.setObjectName("labelResponsible")
        self.labelComment = QtWidgets.QLabel(DialogAddNew)
        self.labelComment.setGeometry(QtCore.QRect(10, 310, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelComment.setFont(font)
        self.labelComment.setObjectName("labelComment")
        self.textOrg = QtWidgets.QTextEdit(DialogAddNew)
        self.textOrg.setGeometry(QtCore.QRect(150, 10, 260, 40))
        self.textOrg.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textOrg.setObjectName("textOrg")
        self.textBefore = QtWidgets.QTextEdit(DialogAddNew)
        self.textBefore.setGeometry(QtCore.QRect(150, 60, 260, 40))
        self.textBefore.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBefore.setObjectName("textBefore")
        self.textProduct = QtWidgets.QTextEdit(DialogAddNew)
        self.textProduct.setGeometry(QtCore.QRect(150, 110, 260, 40))
        self.textProduct.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textProduct.setObjectName("textProduct")
        self.textResponsible = QtWidgets.QTextEdit(DialogAddNew)
        self.textResponsible.setGeometry(QtCore.QRect(150, 260, 260, 40))
        self.textResponsible.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textResponsible.setObjectName("textResponsible")
        self.textComment = QtWidgets.QTextEdit(DialogAddNew)
        self.textComment.setGeometry(QtCore.QRect(150, 310, 260, 40))
        self.textComment.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textComment.setObjectName("textComment")
        self.textUnload = QtWidgets.QTextEdit(DialogAddNew)
        self.textUnload.setGeometry(QtCore.QRect(150, 210, 260, 40))
        self.textUnload.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textUnload.setObjectName("textUnload")
        self.textLoad = QtWidgets.QTextEdit(DialogAddNew)
        self.textLoad.setGeometry(QtCore.QRect(150, 160, 260, 40))
        self.textLoad.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textLoad.setObjectName("textLoad")
        self.pushButton = QtWidgets.QPushButton(DialogAddNew)
        self.pushButton.setGeometry(QtCore.QRect(85, 387, 250, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DialogAddNew)
        QtCore.QMetaObject.connectSlotsByName(DialogAddNew)

    def retranslateUi(self, DialogAddNew):
        _translate = QtCore.QCoreApplication.translate
        DialogAddNew.setWindowTitle(_translate("DialogAddNew", "Add new"))
        self.labelOrg.setText(_translate("DialogAddNew", "Орагнизация"))
        self.labelBefore.setText(_translate("DialogAddNew", "Контракт до"))
        self.labelProduct.setText(_translate("DialogAddNew", "Товар"))
        self.labelLoad.setText(_translate("DialogAddNew", "Дата погрузки"))
        self.labelUnload.setText(_translate("DialogAddNew", "Дата разгрузки"))
        self.labelResponsible.setText(_translate("DialogAddNew", "Ответ. лицо"))
        self.labelComment.setText(_translate("DialogAddNew", "Комментарий"))
        self.pushButton.setText(_translate("DialogAddNew", "Add"))
