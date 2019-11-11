# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/admin_menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        AdminMenu.setObjectName("AdminMenu")
        AdminMenu.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(AdminMenu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 100, 351, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_questions_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_questions_button.setObjectName("add_questions_button")
        self.gridLayout.addWidget(self.add_questions_button, 1, 0, 1, 1)
        self.administrate_scenes_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.administrate_scenes_button.setObjectName("administrate_scenes_button")
        self.gridLayout.addWidget(self.administrate_scenes_button, 3, 0, 1, 1)
        self.administrate_users_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.administrate_users_button.setObjectName("administrate_users_button")
        self.gridLayout.addWidget(self.administrate_users_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.new_scene_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.new_scene_button.setObjectName("new_scene_button")
        self.gridLayout.addWidget(self.new_scene_button, 2, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 5, 0, 1, 1)

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

    def retranslateUi(self, AdminMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Form"))
        self.add_questions_button.setText(_translate("AdminMenu", "Añadir preguntas"))
        self.administrate_scenes_button.setText(_translate("AdminMenu", "Administrar escenarios"))
        self.administrate_users_button.setText(_translate("AdminMenu", "Administrar usuarios"))
        self.new_scene_button.setText(_translate("AdminMenu", "Nuevo escenario"))
        self.return_button.setText(_translate("AdminMenu", "Volver"))

