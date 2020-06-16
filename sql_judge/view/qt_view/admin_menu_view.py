# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/admin_menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        AdminMenu.setObjectName("AdminMenu")
        AdminMenu.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(AdminMenu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 80, 351, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.administrate_users_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.administrate_users_button.setObjectName("administrate_users_button")
        self.gridLayout.addWidget(self.administrate_users_button, 8, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 11, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.load_custom_fakes_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_custom_fakes_button.setObjectName("load_custom_fakes_button")
        self.gridLayout.addWidget(self.load_custom_fakes_button, 6, 0, 1, 1)
        self.create_scene_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.create_scene_button.setObjectName("create_scene_button")
        self.gridLayout.addWidget(self.create_scene_button, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 1)
        self.add_questions_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_questions_button.setObjectName("add_questions_button")
        self.gridLayout.addWidget(self.add_questions_button, 3, 0, 1, 1)

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

    def retranslateUi(self, AdminMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Form"))
        self.administrate_users_button.setText(_translate("AdminMenu", "Editar tipos de relleno"))
        self.return_button.setText(_translate("AdminMenu", "Volver"))
        self.load_custom_fakes_button.setText(_translate("AdminMenu", "Importar tipos de relleno"))
        self.create_scene_button.setText(_translate("AdminMenu", "Crear escenario"))
        self.add_questions_button.setText(_translate("AdminMenu", "Editar escenarios"))
