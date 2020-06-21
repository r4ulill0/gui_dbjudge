# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/custom_types/custom_type_row.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, CustomTypeRow):
        CustomTypeRow.setObjectName("CustomTypeRow")
        CustomTypeRow.setGeometry(QtCore.QRect(0, 0, 195, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomTypeRow.sizePolicy().hasHeightForWidth())
        CustomTypeRow.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CustomTypeRow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_label = QtWidgets.QLabel(CustomTypeRow)
        self.data_label.setObjectName("data_label")
        self.horizontalLayout.addWidget(self.data_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delete_sample_button = QtWidgets.QPushButton(CustomTypeRow)
        self.delete_sample_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/trash-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_sample_button.setIcon(icon)
        self.delete_sample_button.setObjectName("delete_sample_button")
        self.horizontalLayout.addWidget(self.delete_sample_button)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(CustomTypeRow)
        QtCore.QMetaObject.connectSlotsByName(CustomTypeRow)

    def retranslateUi(self, CustomTypeRow):
        _translate = QtCore.QCoreApplication.translate
        CustomTypeRow.setWindowTitle(_translate("Form", "Form"))
        self.data_label.setText(_translate("Form", "data"))
from . import resources
