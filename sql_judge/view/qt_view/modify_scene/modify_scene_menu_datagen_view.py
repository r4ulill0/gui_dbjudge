# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/modify_scene/modify_scene_menu_datagen_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifySceneMenuDatagen(object):
    def setupUi(self, ModifySceneMenuDatagen):
        ModifySceneMenuDatagen.setObjectName("ModifySceneMenuDatagen")
        ModifySceneMenuDatagen.resize(819, 528)
        self.gridLayout_2 = QtWidgets.QGridLayout(ModifySceneMenuDatagen)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ModifySceneMenuDatagen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(ModifySceneMenuDatagen)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.generate_data_button = QtWidgets.QPushButton(ModifySceneMenuDatagen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_data_button.sizePolicy().hasHeightForWidth())
        self.generate_data_button.setSizePolicy(sizePolicy)
        self.generate_data_button.setObjectName("generate_data_button")
        self.horizontalLayout.addWidget(self.generate_data_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.return_button = QtWidgets.QPushButton(ModifySceneMenuDatagen)
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_5.addWidget(self.return_button)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.navbar_config = QtWidgets.QPushButton(ModifySceneMenuDatagen)
        self.navbar_config.setEnabled(True)
        self.navbar_config.setObjectName("navbar_config")
        self.horizontalLayout_4.addWidget(self.navbar_config)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.navbar_gen_data = QtWidgets.QPushButton(ModifySceneMenuDatagen)
        self.navbar_gen_data.setEnabled(False)
        self.navbar_gen_data.setObjectName("navbar_gen_data")
        self.horizontalLayout_4.addWidget(self.navbar_gen_data)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.navbar_questions = QtWidgets.QPushButton(ModifySceneMenuDatagen)
        self.navbar_questions.setObjectName("navbar_questions")
        self.horizontalLayout_4.addWidget(self.navbar_questions)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(ModifySceneMenuDatagen)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ModifySceneMenuDatagen)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ModifySceneMenuDatagen)

    def retranslateUi(self, ModifySceneMenuDatagen):
        _translate = QtCore.QCoreApplication.translate
        ModifySceneMenuDatagen.setWindowTitle(_translate("ModifySceneMenuDatagen", "Form"))
        self.label.setText(_translate("ModifySceneMenuDatagen", "Seleccione escenario: "))
        self.generate_data_button.setText(_translate("ModifySceneMenuDatagen", "Generar datos"))
        self.return_button.setText(_translate("ModifySceneMenuDatagen", "Volver al menú"))
        self.navbar_config.setText(_translate("ModifySceneMenuDatagen", "Configuración general"))
        self.navbar_gen_data.setText(_translate("ModifySceneMenuDatagen", "Generar datos"))
        self.navbar_questions.setText(_translate("ModifySceneMenuDatagen", "Configurar preguntas"))
from view.qt_view import resources
