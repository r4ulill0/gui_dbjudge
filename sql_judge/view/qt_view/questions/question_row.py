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
        QuestionRow.resize(515, 112)
        self.gridLayoutWidget = QtWidgets.QWidget(QuestionRow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 482, 103))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.question_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
        self.question_label.setSizePolicy(sizePolicy)
        self.question_label.setText("")
        self.question_label.setObjectName("question_label")
        self.gridLayout.addWidget(self.question_label, 0, 1, 2, 1)
        self.answer_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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

        self.retranslateUi(QuestionRow)
        QtCore.QMetaObject.connectSlotsByName(QuestionRow)

    def retranslateUi(self, QuestionRow):
        _translate = QtCore.QCoreApplication.translate
        QuestionRow.setWindowTitle(_translate("QuestionRow", "Form"))
