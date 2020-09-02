# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/data_generation/data_generation_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataGeneration(object):
    def setupUi(self, DataGeneration):
        DataGeneration.setObjectName("DataGeneration")
        DataGeneration.resize(640, 480)
        self.gridLayout_2 = QtWidgets.QGridLayout(DataGeneration)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.return_button = QtWidgets.QPushButton(DataGeneration)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.generate_data_button = QtWidgets.QPushButton(DataGeneration)
        self.generate_data_button.setObjectName("generate_data_button")
        self.gridLayout.addWidget(self.generate_data_button, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 3)
        self.tabWidget = QtWidgets.QTabWidget(DataGeneration)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(DataGeneration)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DataGeneration)

    def retranslateUi(self, DataGeneration):
        _translate = QtCore.QCoreApplication.translate
        DataGeneration.setWindowTitle(_translate("DataGeneration", "Form"))
        self.return_button.setText(_translate("DataGeneration", "Volver"))
        self.generate_data_button.setText(_translate("DataGeneration", "Generar datos para todo el escenario"))
