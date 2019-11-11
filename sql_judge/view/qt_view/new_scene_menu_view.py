# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/new_scene_menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewSceneMenu(object):
    def setupUi(self, NewSceneMenu):
        NewSceneMenu.setObjectName("NewSceneMenu")
        NewSceneMenu.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(NewSceneMenu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 80, 366, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scene_name_input_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.scene_name_input_text.setObjectName("scene_name_input_text")
        self.gridLayout.addWidget(self.scene_name_input_text, 1, 1, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.create_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.create_button.setObjectName("create_button")
        self.gridLayout.addWidget(self.create_button, 5, 2, 1, 1)
        self.extra_info_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.extra_info_label.setText("")
        self.extra_info_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.extra_info_label.setIndent(-1)
        self.extra_info_label.setObjectName("extra_info_label")
        self.gridLayout.addWidget(self.extra_info_label, 2, 0, 2, 3)
        self.scene_name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scene_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scene_name_label.setObjectName("scene_name_label")
        self.gridLayout.addWidget(self.scene_name_label, 0, 0, 1, 3)

        self.retranslateUi(NewSceneMenu)
        QtCore.QMetaObject.connectSlotsByName(NewSceneMenu)

    def retranslateUi(self, NewSceneMenu):
        _translate = QtCore.QCoreApplication.translate
        NewSceneMenu.setWindowTitle(_translate("NewSceneMenu", "Form"))
        self.return_button.setText(_translate("NewSceneMenu", "Volver"))
        self.create_button.setText(_translate("NewSceneMenu", "Crear"))
        self.scene_name_label.setText(_translate("NewSceneMenu", "Nombre del escenario:"))

