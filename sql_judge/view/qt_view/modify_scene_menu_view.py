# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/modify_scene_menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifySceneMenu(object):
    def setupUi(self, ModifySceneMenu):
        ModifySceneMenu.setObjectName("ModifySceneMenu")
        ModifySceneMenu.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(ModifySceneMenu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 110, 261, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.load_sql_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_sql_button.setObjectName("load_sql_button")
        self.gridLayout.addWidget(self.load_sql_button, 3, 0, 1, 3)
        self.generate_data_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generate_data_button.setObjectName("generate_data_button")
        self.gridLayout.addWidget(self.generate_data_button, 5, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 8, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 1)
        self.add_questions_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_questions_button.setObjectName("add_questions_button")
        self.gridLayout.addWidget(self.add_questions_button, 6, 0, 1, 3)
        self.scene_combo_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.scene_combo_box.setObjectName("scene_combo_box")
        self.gridLayout.addWidget(self.scene_combo_box, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.retranslateUi(ModifySceneMenu)
        QtCore.QMetaObject.connectSlotsByName(ModifySceneMenu)

    def retranslateUi(self, ModifySceneMenu):
        _translate = QtCore.QCoreApplication.translate
        ModifySceneMenu.setWindowTitle(_translate("ModifySceneMenu", "Form"))
        self.load_sql_button.setText(_translate("ModifySceneMenu", "Cargar SQL"))
        self.generate_data_button.setText(_translate("ModifySceneMenu", "Generar datos"))
        self.return_button.setText(_translate("ModifySceneMenu", "Volver"))
        self.add_questions_button.setText(_translate("ModifySceneMenu", "Añadir preguntas"))
        self.label.setText(_translate("ModifySceneMenu", "Selecciona el escenario a modificar:"))

