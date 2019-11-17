# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/data_generation/data_generation_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataGeneration(object):
    def setupUi(self, DataGeneration):
        DataGeneration.setObjectName("DataGeneration")
        DataGeneration.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(DataGeneration)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 0, 0, 1, 1)
        self.generate_data_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generate_data_button.setObjectName("generate_data_button")
        self.gridLayout.addWidget(self.generate_data_button, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 3)

        self.retranslateUi(DataGeneration)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DataGeneration)

    def retranslateUi(self, DataGeneration):
        _translate = QtCore.QCoreApplication.translate
        DataGeneration.setWindowTitle(_translate("DataGeneration", "Form"))
        self.return_button.setText(_translate("DataGeneration", "Volver"))
        self.generate_data_button.setText(_translate("DataGeneration", "Generar datos para todo el escenario"))

