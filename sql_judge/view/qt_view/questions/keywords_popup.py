# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/questions/keywords_popup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeywordsPopup(object):
    def setupUi(self, KeywordsPopup):
        KeywordsPopup.setObjectName("KeywordsPopup")
        KeywordsPopup.resize(640, 480)
        KeywordsPopup.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(KeywordsPopup)
        self.gridLayout.setObjectName("gridLayout")
        self.delete_button = QtWidgets.QPushButton(KeywordsPopup)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.listView = QtWidgets.QListView(KeywordsPopup)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 6)
        self.allowance_combobox = QtWidgets.QComboBox(KeywordsPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allowance_combobox.sizePolicy().hasHeightForWidth())
        self.allowance_combobox.setSizePolicy(sizePolicy)
        self.allowance_combobox.setObjectName("allowance_combobox")
        self.gridLayout.addWidget(self.allowance_combobox, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.keyword_combobox = QtWidgets.QComboBox(KeywordsPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyword_combobox.sizePolicy().hasHeightForWidth())
        self.keyword_combobox.setSizePolicy(sizePolicy)
        self.keyword_combobox.setObjectName("keyword_combobox")
        self.gridLayout.addWidget(self.keyword_combobox, 0, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(KeywordsPopup)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 0, 3, 1, 1)
        self.confirm_button = QtWidgets.QPushButton(KeywordsPopup)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout.addWidget(self.confirm_button, 2, 5, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(KeywordsPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 2, 0, 1, 1)

        self.retranslateUi(KeywordsPopup)
        QtCore.QMetaObject.connectSlotsByName(KeywordsPopup)

    def retranslateUi(self, KeywordsPopup):
        _translate = QtCore.QCoreApplication.translate
        KeywordsPopup.setWindowTitle(_translate("KeywordsPopup", "Dialog"))
        self.delete_button.setText(_translate("KeywordsPopup", "Eliminar"))
        self.add_button.setText(_translate("KeywordsPopup", "Añadir"))
        self.confirm_button.setText(_translate("KeywordsPopup", "Confirmar"))
        self.cancel_button.setText(_translate("KeywordsPopup", "Cancelar"))
