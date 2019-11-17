# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/data_generation/tables_data_generation_tab_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TablesDataGenerationTab(object):
    def setupUi(self, TablesDataGenerationTab):
        TablesDataGenerationTab.setObjectName("TablesDataGenerationTab")
        TablesDataGenerationTab.resize(640, 480)
        self.scrollArea = QtWidgets.QScrollArea(TablesDataGenerationTab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 571, 321))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 569, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 561, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TablesDataGenerationTab)
        QtCore.QMetaObject.connectSlotsByName(TablesDataGenerationTab)

    def retranslateUi(self, TablesDataGenerationTab):
        _translate = QtCore.QCoreApplication.translate
        TablesDataGenerationTab.setWindowTitle(_translate("TablesDataGenerationTab", "TabWidget"))

