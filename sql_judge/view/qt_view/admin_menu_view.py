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
        self.gridLayout_2 = QtWidgets.QGridLayout(AdminMenu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.create_scene_button = QtWidgets.QPushButton(AdminMenu)
        self.create_scene_button.setObjectName("create_scene_button")
        self.gridLayout.addWidget(self.create_scene_button, 0, 0, 1, 1)
        self.edit_custom_fakes_button = QtWidgets.QPushButton(AdminMenu)
        self.edit_custom_fakes_button.setObjectName("edit_custom_fakes_button")
        self.gridLayout.addWidget(self.edit_custom_fakes_button, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.load_custom_fakes_button = QtWidgets.QPushButton(AdminMenu)
        self.load_custom_fakes_button.setObjectName("load_custom_fakes_button")
        self.gridLayout.addWidget(self.load_custom_fakes_button, 6, 0, 1, 1)
        self.edit_scene_button = QtWidgets.QPushButton(AdminMenu)
        self.edit_scene_button.setObjectName("edit_scene_button")
        self.gridLayout.addWidget(self.edit_scene_button, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 10, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(AdminMenu)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 11, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

    def retranslateUi(self, AdminMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Form"))
        self.create_scene_button.setText(_translate("AdminMenu", "Crear escenario"))
        self.edit_custom_fakes_button.setText(_translate("AdminMenu", "Editar tipos de relleno"))
        self.load_custom_fakes_button.setText(_translate("AdminMenu", "Importar tipos de relleno"))
        self.edit_scene_button.setText(_translate("AdminMenu", "Editar escenarios"))
        self.return_button.setText(_translate("AdminMenu", "Volver"))
