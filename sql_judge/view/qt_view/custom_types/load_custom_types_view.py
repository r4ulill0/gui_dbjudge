# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/custom_types/load_custom_types_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadCustomTypesView(object):
    def setupUi(self, LoadCustomTypesView):
        LoadCustomTypesView.setObjectName("LoadCustomTypesView")
        LoadCustomTypesView.resize(640, 480)
        self.gridLayout_3 = QtWidgets.QGridLayout(LoadCustomTypesView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_file_button = QtWidgets.QPushButton(LoadCustomTypesView)
        self.load_file_button.setObjectName("load_file_button")
        self.horizontalLayout.addWidget(self.load_file_button)
        self.label = QtWidgets.QLabel(LoadCustomTypesView)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(LoadCustomTypesView)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.return_button = QtWidgets.QPushButton(LoadCustomTypesView)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 4, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(LoadCustomTypesView)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 612, 335))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.type_column_container = QtWidgets.QHBoxLayout()
        self.type_column_container.setObjectName("type_column_container")
        self.gridLayout_2.addLayout(self.type_column_container, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 1, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_button = QtWidgets.QPushButton(LoadCustomTypesView)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_2.addWidget(self.add_button)
        self.delete_button = QtWidgets.QPushButton(LoadCustomTypesView)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(LoadCustomTypesView)
        QtCore.QMetaObject.connectSlotsByName(LoadCustomTypesView)

    def retranslateUi(self, LoadCustomTypesView):
        _translate = QtCore.QCoreApplication.translate
        LoadCustomTypesView.setWindowTitle(_translate("LoadCustomTypesView", "Form"))
        self.load_file_button.setText(_translate("LoadCustomTypesView", "Cargar desde archivo"))
        self.label.setText(_translate("LoadCustomTypesView", "Ningún archivo seleccionado"))
        self.save_button.setText(_translate("LoadCustomTypesView", "Guardar tipos"))
        self.return_button.setText(_translate("LoadCustomTypesView", "Volver al menú"))
        self.add_button.setText(_translate("LoadCustomTypesView", "Añadir"))
        self.delete_button.setText(_translate("LoadCustomTypesView", "Eliminar"))
