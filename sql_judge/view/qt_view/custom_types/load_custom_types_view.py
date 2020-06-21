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
        self.gridLayoutWidget = QtWidgets.QWidget(LoadCustomTypesView)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 611, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_file_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_file_button.setObjectName("load_file_button")
        self.horizontalLayout.addWidget(self.load_file_button)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 4, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 601, 357))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.type_column_container = QtWidgets.QHBoxLayout()
        self.type_column_container.setObjectName("type_column_container")
        self.gridLayout_2.addLayout(self.type_column_container, 0, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 1, 1, 4)

        self.retranslateUi(LoadCustomTypesView)
        QtCore.QMetaObject.connectSlotsByName(LoadCustomTypesView)

    def retranslateUi(self, LoadCustomTypesView):
        _translate = QtCore.QCoreApplication.translate
        LoadCustomTypesView.setWindowTitle(_translate("LoadCustomTypesView", "Form"))
        self.load_file_button.setText(_translate("LoadCustomTypesView", "Cargar desde archivo"))
        self.label.setText(_translate("LoadCustomTypesView", "Ningún archivo seleccionado"))
        self.save_button.setText(_translate("LoadCustomTypesView", "Guardar tipos"))
        self.return_button.setText(_translate("LoadCustomTypesView", "Volver al menú"))
