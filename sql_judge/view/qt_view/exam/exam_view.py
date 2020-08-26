# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/exam/exam_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exam(object):
    def setupUi(self, Exam):
        Exam.setObjectName("Exam")
        Exam.resize(634, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(Exam)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.exit_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.gridLayout.addWidget(self.exit_button, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        self.database_output = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.database_output.sizePolicy().hasHeightForWidth())
        self.database_output.setSizePolicy(sizePolicy)
        self.database_output.setObjectName("database_output")
        self.gridLayout.addWidget(self.database_output, 1, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 4, 1, 1)
        self.question = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setText("")
        self.question.setObjectName("question")
        self.gridLayout.addWidget(self.question, 0, 3, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 5, 1, 1)
        self.test_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.test_button.setObjectName("test_button")
        self.gridLayout.addWidget(self.test_button, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 2, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 2)
        self.question_list = QtWidgets.QListView(self.gridLayoutWidget)
        self.question_list.setObjectName("question_list")
        self.gridLayout.addWidget(self.question_list, 1, 0, 3, 1)

        self.retranslateUi(Exam)
        QtCore.QMetaObject.connectSlotsByName(Exam)

    def retranslateUi(self, Exam):
        _translate = QtCore.QCoreApplication.translate
        Exam.setWindowTitle(_translate("Exam", "Exam"))
        self.exit_button.setText(_translate("Exam", "Salir"))
        self.label_2.setText(_translate("Exam", "<html><head/><body><p><span style=\" font-size:16pt;\">Pregunta:</span></p></body></html>"))
        self.pushButton.setText(_translate("Exam", "Terminar y corregir preguntas"))
        self.test_button.setText(_translate("Exam", "Probar consulta"))
        self.label.setText(_translate("Exam", "<html><head/><body><p><span style=\" font-size:18pt;\">Introduce la consulta:</span></p></body></html>"))
