# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/monstrillllo/PycharmProjects/flaskProject/LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 450)
        Dialog.setMinimumSize(QtCore.QSize(390, 450))
        Dialog.setMaximumSize(QtCore.QSize(390, 450))
        self.labelLogin = QtWidgets.QLabel(Dialog)
        self.labelLogin.setGeometry(QtCore.QRect(125, 30, 140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(125, 85, 112, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(125, 130, 112, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineLogin = QtWidgets.QLineEdit(Dialog)
        self.lineLogin.setGeometry(QtCore.QRect(120, 200, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineLogin.setFont(font)
        self.lineLogin.setObjectName("lineLogin")
        self.linePassword = QtWidgets.QLineEdit(Dialog)
        self.linePassword.setGeometry(QtCore.QRect(120, 260, 150, 30))
        self.linePassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.labelLogin_2 = QtWidgets.QLabel(Dialog)
        self.labelLogin_2.setGeometry(QtCore.QRect(70, 200, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelLogin_2.setFont(font)
        self.labelLogin_2.setObjectName("labelLogin_2")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(40, 260, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.labelLogin.setText(_translate("Dialog", "Login/Register"))
        self.radioButton.setText(_translate("Dialog", "Login"))
        self.radioButton_2.setText(_translate("Dialog", "Register"))
        self.labelLogin_2.setText(_translate("Dialog", "Login"))
        self.labelPassword.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Accept"))