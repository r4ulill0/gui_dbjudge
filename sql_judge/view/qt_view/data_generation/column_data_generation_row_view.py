# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/data_generation/column_data_generation_row_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColumnDataGenerationRow(object):
    def setupUi(self, ColumnDataGenerationRow):
        ColumnDataGenerationRow.setObjectName("ColumnDataGenerationRow")
        ColumnDataGenerationRow.resize(796, 112)
        self.gridLayout_2 = QtWidgets.QGridLayout(ColumnDataGenerationRow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.custom_type_radio_button = QtWidgets.QRadioButton(ColumnDataGenerationRow)
        self.custom_type_radio_button.setMinimumSize(QtCore.QSize(20, 30))
        self.custom_type_radio_button.setObjectName("custom_type_radio_button")
        self.gridLayout.addWidget(self.custom_type_radio_button, 2, 3, 1, 1)
        self.output_information_label = QtWidgets.QLabel(ColumnDataGenerationRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_information_label.sizePolicy().hasHeightForWidth())
        self.output_information_label.setSizePolicy(sizePolicy)
        self.output_information_label.setMinimumSize(QtCore.QSize(40, 40))
        self.output_information_label.setText("")
        self.output_information_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_information_label.setObjectName("output_information_label")
        self.gridLayout.addWidget(self.output_information_label, 0, 9, 3, 1)
        self.default_type_radio_button = QtWidgets.QRadioButton(ColumnDataGenerationRow)
        self.default_type_radio_button.setChecked(True)
        self.default_type_radio_button.setObjectName("default_type_radio_button")
        self.gridLayout.addWidget(self.default_type_radio_button, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(ColumnDataGenerationRow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 7, 1, 1)
        self.regex_max_len_input = QtWidgets.QLineEdit(ColumnDataGenerationRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regex_max_len_input.sizePolicy().hasHeightForWidth())
        self.regex_max_len_input.setSizePolicy(sizePolicy)
        self.regex_max_len_input.setMinimumSize(QtCore.QSize(20, 0))
        self.regex_max_len_input.setMaximumSize(QtCore.QSize(50, 16777215))
        self.regex_max_len_input.setObjectName("regex_max_len_input")
        self.gridLayout.addWidget(self.regex_max_len_input, 0, 8, 1, 1)
        self.regex_input = QtWidgets.QLineEdit(ColumnDataGenerationRow)
        self.regex_input.setEnabled(False)
        self.regex_input.setObjectName("regex_input")
        self.gridLayout.addWidget(self.regex_input, 0, 5, 1, 1)
        self.column_name_label = QtWidgets.QLabel(ColumnDataGenerationRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.column_name_label.sizePolicy().hasHeightForWidth())
        self.column_name_label.setSizePolicy(sizePolicy)
        self.column_name_label.setText("")
        self.column_name_label.setObjectName("column_name_label")
        self.gridLayout.addWidget(self.column_name_label, 0, 1, 3, 1)
        self.regex_radio_button = QtWidgets.QRadioButton(ColumnDataGenerationRow)
        self.regex_radio_button.setMinimumSize(QtCore.QSize(20, 30))
        self.regex_radio_button.setObjectName("regex_radio_button")
        self.gridLayout.addWidget(self.regex_radio_button, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 6, 1, 1)
        self.custom_type_input = QtWidgets.QComboBox(ColumnDataGenerationRow)
        self.custom_type_input.setEnabled(False)
        self.custom_type_input.setObjectName("custom_type_input")
        self.gridLayout.addWidget(self.custom_type_input, 2, 5, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ColumnDataGenerationRow)
        QtCore.QMetaObject.connectSlotsByName(ColumnDataGenerationRow)

    def retranslateUi(self, ColumnDataGenerationRow):
        _translate = QtCore.QCoreApplication.translate
        ColumnDataGenerationRow.setWindowTitle(_translate("ColumnDataGenerationRow", "Form"))
        self.custom_type_radio_button.setText(_translate("ColumnDataGenerationRow", "Tipo personalizado"))
        self.default_type_radio_button.setText(_translate("ColumnDataGenerationRow", "Aleatorio"))
        self.label.setText(_translate("ColumnDataGenerationRow", "Longitud máxima:"))
        self.regex_radio_button.setText(_translate("ColumnDataGenerationRow", "Regex"))
