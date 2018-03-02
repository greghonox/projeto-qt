# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(235, 153)
        self.entrar = QtWidgets.QPushButton(Dialog)
        self.entrar.setGeometry(QtCore.QRect(10, 120, 83, 25))
        self.entrar.setObjectName("entrar")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 181, 17))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 83, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 51, 195, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usuario = QtWidgets.QLineEdit(self.layoutWidget)
        self.usuario.setObjectName("usuario")
        self.gridLayout.addWidget(self.usuario, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.senha = QtWidgets.QLineEdit(self.layoutWidget)
        self.senha.setObjectName("senha")
        self.gridLayout.addWidget(self.senha, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(self.senha.clear)
        self.pushButton_2.clicked.connect(self.usuario.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usuario, self.senha)
        Dialog.setTabOrder(self.senha, self.entrar)
        Dialog.setTabOrder(self.entrar, self.pushButton_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ARPROTECT"))
        self.entrar.setText(_translate("Dialog", "ENTRAR"))
        self.label_3.setText(_translate("Dialog", "SISTEMA ESTOQUE"))
        self.pushButton_2.setText(_translate("Dialog", "CANCELAR"))
        self.label.setText(_translate("Dialog", "NOME"))
        self.label_2.setText(_translate("Dialog", "SENHA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

