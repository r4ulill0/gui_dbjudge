# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/exam/results_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(943, 434)
        self.gridLayout_3 = QtWidgets.QGridLayout(Results)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.question_list = QtWidgets.QListView(Results)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.question_list.sizePolicy().hasHeightForWidth())
        self.question_list.setSizePolicy(sizePolicy)
        self.question_list.setSizeIncrement(QtCore.QSize(0, 0))
        self.question_list.setObjectName("question_list")
        self.gridLayout.addWidget(self.question_list, 2, 0, 3, 1)
        spacerItem = QtWidgets.QSpacerItem(
            5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.return_button = QtWidgets.QPushButton(Results)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 6, 6, 1, 1)
        self.question_stats = QtWidgets.QWidget(Results)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.question_stats.sizePolicy().hasHeightForWidth())
        self.question_stats.setSizePolicy(sizePolicy)
        self.question_stats.setObjectName("question_stats")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.question_stats)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.keywords_list = QtWidgets.QListWidget(self.question_stats)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.keywords_list.sizePolicy().hasHeightForWidth())
        self.keywords_list.setSizePolicy(sizePolicy)
        self.keywords_list.setSizeIncrement(QtCore.QSize(0, 0))
        self.keywords_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.keywords_list.setObjectName("keywords_list")
        self.gridLayout_2.addWidget(self.keywords_list, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.question_stats)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.question_stats)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.excess_tables_list = QtWidgets.QListWidget(self.question_stats)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.excess_tables_list.sizePolicy().hasHeightForWidth())
        self.excess_tables_list.setSizePolicy(sizePolicy)
        self.excess_tables_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.excess_tables_list.setObjectName("excess_tables_list")
        self.gridLayout_2.addWidget(self.excess_tables_list, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.question_stats)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.question_stats)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.question_stats, 2, 2, 3, 5)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Results)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.question = QtWidgets.QLabel(Results)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setText("")
        self.question.setObjectName("question")
        self.gridLayout.addWidget(self.question, 1, 3, 1, 4)
        self.total_result_label = QtWidgets.QLabel(Results)
        self.total_result_label.setObjectName("total_result_label")
        self.gridLayout.addWidget(self.total_result_label, 0, 0, 1, 7)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Results"))
        self.return_button.setText(_translate("Results", "Volver al menu"))
        self.label_4.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:12pt;\">Tablas innecesarias usadas</span></p></body></html>"))
        self.label_5.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:12pt;\">Requisitos de palabras clave</span></p></body></html>"))
        self.label.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:16pt;\">Pregunta resuelta correctamente:</span></p></body></html>"))
        self.label_3.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:16pt;\">Resultado de la consulta:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:16pt;\">Pregunta:</span></p></body></html>"))
        self.total_result_label.setText(_translate(
            "Results", "<html><head/><body><p><span style=\" font-size:20pt;\">0/0 Preguntas resueltas correctamente</span></p></body></html>"))
