# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/new_scene_menu_questions_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewSceneMenuQuestions(object):
    def setupUi(self, NewSceneMenuQuestions):
        NewSceneMenuQuestions.setObjectName("NewSceneMenuQuestions")
        NewSceneMenuQuestions.resize(1017, 592)
        self.gridLayout_3 = QtWidgets.QGridLayout(NewSceneMenuQuestions)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 2)
        self.question_input = QtWidgets.QPlainTextEdit(NewSceneMenuQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.question_input.sizePolicy().hasHeightForWidth())
        self.question_input.setSizePolicy(sizePolicy)
        self.question_input.setObjectName("question_input")
        self.gridLayout_2.addWidget(self.question_input, 1, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_question_button = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.add_question_button.setMaximumSize(QtCore.QSize(120, 30))
        self.add_question_button.setObjectName("add_question_button")
        self.horizontalLayout_6.addWidget(self.add_question_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 6, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.return_button = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.return_button.setMaximumSize(QtCore.QSize(100, 30))
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_2.addWidget(self.return_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 2)
        self.label = QtWidgets.QLabel(NewSceneMenuQuestions)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.answer_input = QtWidgets.QPlainTextEdit(NewSceneMenuQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.answer_input.sizePolicy().hasHeightForWidth())
        self.answer_input.setSizePolicy(sizePolicy)
        self.answer_input.setObjectName("answer_input")
        self.gridLayout_2.addWidget(self.answer_input, 1, 5, 1, 3)
        self.label_4 = QtWidgets.QLabel(NewSceneMenuQuestions)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 5, 1, 3)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.gridLayout_2.setColumnStretch(6, 2)
        self.gridLayout_2.setColumnStretch(7, 3)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 6)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(NewSceneMenuQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 985, 173))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(280, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.navbar_schema = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.navbar_schema.setEnabled(True)
        self.navbar_schema.setObjectName("navbar_schema")
        self.horizontalLayout_4.addWidget(self.navbar_schema)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(NewSceneMenuQuestions)
        self.label_9.setMaximumSize(QtCore.QSize(80, 100))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.navbar_gen_data = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.navbar_gen_data.setEnabled(True)
        self.navbar_gen_data.setObjectName("navbar_gen_data")
        self.horizontalLayout_4.addWidget(self.navbar_gen_data)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.label_10 = QtWidgets.QLabel(NewSceneMenuQuestions)
        self.label_10.setMaximumSize(QtCore.QSize(80, 100))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.navbar_questions = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.navbar_questions.setEnabled(False)
        self.navbar_questions.setObjectName("navbar_questions")
        self.horizontalLayout_4.addWidget(self.navbar_questions)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.finish_button = QtWidgets.QPushButton(NewSceneMenuQuestions)
        self.finish_button.setMaximumSize(QtCore.QSize(120, 30))
        self.finish_button.setObjectName("finish_button")
        self.horizontalLayout_8.addWidget(self.finish_button)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(NewSceneMenuQuestions)
        self.label_3.setEnabled(True)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/inscription-50.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(NewSceneMenuQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 2, 4)
        self.gridLayout.setRowStretch(3, 10)
        self.gridLayout.setRowStretch(4, 15)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(NewSceneMenuQuestions)
        QtCore.QMetaObject.connectSlotsByName(NewSceneMenuQuestions)

    def retranslateUi(self, NewSceneMenuQuestions):
        _translate = QtCore.QCoreApplication.translate
        NewSceneMenuQuestions.setWindowTitle(_translate("NewSceneMenuQuestions", "Form"))
        self.add_question_button.setText(_translate("NewSceneMenuQuestions", "Añadir pregunta"))
        self.return_button.setText(_translate("NewSceneMenuQuestions", "Volver al menú"))
        self.label.setText(_translate("NewSceneMenuQuestions", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Pregunta</span></p></body></html>"))
        self.label_4.setText(_translate("NewSceneMenuQuestions", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Consulta correcta</span></p></body></html>"))
        self.navbar_schema.setText(_translate("NewSceneMenuQuestions", "Esquema"))
        self.label_9.setText(_translate("NewSceneMenuQuestions", "<html><head/><body><p><span style=\" font-size:26pt;\">➤</span></p></body></html>"))
        self.navbar_gen_data.setText(_translate("NewSceneMenuQuestions", "Generar datos"))
        self.label_10.setText(_translate("NewSceneMenuQuestions", "<html><head/><body><p><span style=\" font-size:26pt;\">➤</span></p></body></html>"))
        self.navbar_questions.setText(_translate("NewSceneMenuQuestions", "Configurar preguntas"))
        self.finish_button.setText(_translate("NewSceneMenuQuestions", "Terminar"))
        self.label_2.setText(_translate("NewSceneMenuQuestions", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Paso 3 - Añade las preguntas</span></p></body></html>"))
from . import resources
