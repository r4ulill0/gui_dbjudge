# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/main_menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(MainMenu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 100, 261, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.user_menu_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.user_menu_button.setObjectName("user_menu_button")
        self.gridLayout.addWidget(self.user_menu_button, 2, 0, 1, 1)
        self.admin_menu_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.admin_menu_button.setObjectName("admin_menu_button")
        self.gridLayout.addWidget(self.admin_menu_button, 5, 0, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Form"))
        self.label.setText(_translate("MainMenu", "Bienvenido"))
        self.user_menu_button.setText(_translate("MainMenu", "Ponte a prueba"))
        self.admin_menu_button.setText(_translate("MainMenu", "Administración"))
