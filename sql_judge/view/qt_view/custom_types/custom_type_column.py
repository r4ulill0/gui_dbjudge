# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/custom_types/custom_type_column.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, CustomTypeColumn):
        CustomTypeColumn.setObjectName("CustomTypeColumn")
        CustomTypeColumn.setGeometry(QtCore.QRect(0, 0, 640, 480))
        CustomTypeColumn.setTabletTracking(False)
        self.gridLayout = QtWidgets.QGridLayout(CustomTypeColumn)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_column_button = QtWidgets.QPushButton(CustomTypeColumn)
        self.delete_column_button.setMinimumSize(QtCore.QSize(20, 0))
        self.delete_column_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/trash-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_column_button.setIcon(icon)
        self.delete_column_button.setAutoDefault(False)
        self.delete_column_button.setDefault(False)
        self.delete_column_button.setFlat(False)
        self.delete_column_button.setObjectName("delete_column_button")
        self.verticalLayout.addWidget(self.delete_column_button, 0, QtCore.Qt.AlignHCenter)
        self.column_title = QtWidgets.QLabel(CustomTypeColumn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.column_title.sizePolicy().hasHeightForWidth())
        self.column_title.setSizePolicy(sizePolicy)
        self.column_title.setFrameShape(QtWidgets.QFrame.Box)
        self.column_title.setObjectName("column_title")
        self.verticalLayout.addWidget(self.column_title, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(CustomTypeColumn)
        QtCore.QMetaObject.connectSlotsByName(CustomTypeColumn)

    def retranslateUi(self, CustomTypeColumn):
        _translate = QtCore.QCoreApplication.translate
        CustomTypeColumn.setWindowTitle(_translate("Form", "Form"))
        self.column_title.setText(_translate("Form", "Title"))
from . import resources
