# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/questions/question_row.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestionRow(object):
    def setupUi(self, QuestionRow):
        QuestionRow.setObjectName("QuestionRow")
        QuestionRow.resize(736, 112)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QuestionRow.sizePolicy().hasHeightForWidth())
        QuestionRow.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(QuestionRow)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.answer_label = QtWidgets.QLabel(QuestionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_label.sizePolicy().hasHeightForWidth())
        self.answer_label.setSizePolicy(sizePolicy)
        self.answer_label.setMinimumSize(QtCore.QSize(40, 40))
        self.answer_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.answer_label.setText("")
        self.answer_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.answer_label.setObjectName("answer_label")
        self.gridLayout.addWidget(self.answer_label, 0, 2, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.keywords_button = QtWidgets.QPushButton(QuestionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keywords_button.sizePolicy().hasHeightForWidth())
        self.keywords_button.setSizePolicy(sizePolicy)
        self.keywords_button.setObjectName("keywords_button")
        self.gridLayout_3.addWidget(self.keywords_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(QuestionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout_3.addWidget(self.delete_button, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 4, 2, 1)
        self.question_label = QtWidgets.QLabel(QuestionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
        self.question_label.setSizePolicy(sizePolicy)
        self.question_label.setMinimumSize(QtCore.QSize(40, 40))
        self.question_label.setText("")
        self.question_label.setObjectName("question_label")
        self.gridLayout.addWidget(self.question_label, 0, 0, 2, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(QuestionRow)
        QtCore.QMetaObject.connectSlotsByName(QuestionRow)

    def retranslateUi(self, QuestionRow):
        _translate = QtCore.QCoreApplication.translate
        QuestionRow.setWindowTitle(_translate("QuestionRow", "Form"))
        self.keywords_button.setText(_translate("QuestionRow", "Palabras clave"))
        self.delete_button.setText(_translate("QuestionRow", "Borrar pregunta"))
