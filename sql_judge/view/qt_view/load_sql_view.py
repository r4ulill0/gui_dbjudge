# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/load_sql_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadSqlView(object):
    def setupUi(self, LoadSqlView):
        LoadSqlView.setObjectName("LoadSqlView")
        LoadSqlView.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(LoadSqlView)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 621, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.load_file_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_file_button.setObjectName("load_file_button")
        self.gridLayout.addWidget(self.load_file_button, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.confirm_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout.addWidget(self.confirm_button, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        self.sql_text_input = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.sql_text_input.setObjectName("sql_text_input")
        self.gridLayout.addWidget(self.sql_text_input, 2, 2, 1, 3)

        self.retranslateUi(LoadSqlView)
        QtCore.QMetaObject.connectSlotsByName(LoadSqlView)

    def retranslateUi(self, LoadSqlView):
        _translate = QtCore.QCoreApplication.translate
        LoadSqlView.setWindowTitle(_translate("LoadSqlView", "Form"))
        self.load_file_button.setText(_translate("LoadSqlView", "Cargar desde archivo"))
        self.confirm_button.setText(_translate("LoadSqlView", "Confirmar"))

