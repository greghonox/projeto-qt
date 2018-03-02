# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1182, 632)
        Main.setMinimumSize(QtCore.QSize(1182, 632))
        Main.setMaximumSize(QtCore.QSize(1182, 632))
        Main.setBaseSize(QtCore.QSize(0, 0))
        self.centralWidget = QtWidgets.QWidget(Main)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 581))
        self.label.setStyleSheet("image: url(:/img/img/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        Main.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1182, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuEstoque = QtWidgets.QMenu(self.menuBar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuRelat_rio = QtWidgets.QMenu(self.menuBar)
        self.menuRelat_rio.setObjectName("menuRelat_rio")
        self.menuUsuarios = QtWidgets.QMenu(self.menuBar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        Main.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.actionCadastrar = QtWidgets.QAction(Main)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionConsultar = QtWidgets.QAction(Main)
        self.actionConsultar.setObjectName("actionConsultar")
        self.actionConsulta = QtWidgets.QAction(Main)
        self.actionConsulta.setObjectName("actionConsulta")
        self.actionCadastrar_2 = QtWidgets.QAction(Main)
        self.actionCadastrar_2.setObjectName("actionCadastrar_2")
        self.actionConsultar_2 = QtWidgets.QAction(Main)
        self.actionConsultar_2.setObjectName("actionConsultar_2")
        self.actionBanco_de_Dados = QtWidgets.QAction(Main)
        self.actionBanco_de_Dados.setObjectName("actionBanco_de_Dados")
        self.actionBackup = QtWidgets.QAction(Main)
        self.actionBackup.setObjectName("actionBackup")
        self.actionFornecedor_CTRL_F = QtWidgets.QAction(Main)
        self.actionFornecedor_CTRL_F.setObjectName("actionFornecedor_CTRL_F")
        self.menuEstoque.addAction(self.actionCadastrar)
        self.menuEstoque.addAction(self.actionConsultar)
        self.menuEstoque.addSeparator()
        self.menuEstoque.addAction(self.actionFornecedor_CTRL_F)
        self.menuRelat_rio.addAction(self.actionConsulta)
        self.menuUsuarios.addAction(self.actionCadastrar_2)
        self.menuConfigura_es.addAction(self.actionBanco_de_Dados)
        self.menuConfigura_es.addAction(self.actionBackup)
        self.menuBar.addAction(self.menuEstoque.menuAction())
        self.menuBar.addAction(self.menuRelat_rio.menuAction())
        self.menuBar.addAction(self.menuConfigura_es.menuAction())
        self.menuBar.addAction(self.menuUsuarios.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "SISTEMA ESTOQUE-ARPROTECT"))
        self.menuEstoque.setTitle(_translate("Main", "Estoque"))
        self.menuRelat_rio.setTitle(_translate("Main", "Relatório"))
        self.menuUsuarios.setTitle(_translate("Main", "Usuarios"))
        self.menuConfigura_es.setTitle(_translate("Main", "Configurações"))
        self.actionCadastrar.setText(_translate("Main", "Cadastrar(CTRL+C)"))
        self.actionConsultar.setText(_translate("Main", "Consultar(CTRL+L)"))
        self.actionConsulta.setText(_translate("Main", "Consulta(CTRL+I)"))
        self.actionCadastrar_2.setText(_translate("Main", "Gerenciar(CTRL+U)"))
        self.actionConsultar_2.setText(_translate("Main", "Consultar"))
        self.actionBanco_de_Dados.setText(_translate("Main", "Banco de Dados"))
        self.actionBackup.setText(_translate("Main", "Backup"))
        self.actionFornecedor_CTRL_F.setText(_translate("Main", "Fornecedor(CTRL+F)"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

