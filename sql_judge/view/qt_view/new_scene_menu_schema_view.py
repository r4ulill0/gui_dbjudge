# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/raul/OS/Users/king_/Desktop/carrera/curso2018-2019/2oCuatri/TFG/gui_dbjudge/sql_judge/view/qt_view/new_scene_menu_schema_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewSceneMenuSchema(object):
    def setupUi(self, NewSceneMenuSchema):
        NewSceneMenuSchema.setObjectName("NewSceneMenuSchema")
        NewSceneMenuSchema.resize(819, 528)
        self.gridLayoutWidget = QtWidgets.QWidget(NewSceneMenuSchema)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 808, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.confirm_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_5.addWidget(self.confirm_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.return_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_5.addWidget(self.return_button)
        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.scene_name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.scene_name_input.setObjectName("scene_name_input")
        self.horizontalLayout_2.addWidget(self.scene_name_input)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.navigation_bar = QtWidgets.QWidget(self.gridLayoutWidget)
        self.navigation_bar.setObjectName("navigation_bar")
        self.gridLayout.addWidget(self.navigation_bar, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/inscription-50.png"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.text_editor = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.text_editor.setObjectName("text_editor")
        self.horizontalLayout_6.addWidget(self.text_editor)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.load_file_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_file_button.sizePolicy().hasHeightForWidth())
        self.load_file_button.setSizePolicy(sizePolicy)
        self.load_file_button.setObjectName("load_file_button")
        self.horizontalLayout_3.addWidget(self.load_file_button)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.navbar_schema = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.navbar_schema.setEnabled(False)
        self.navbar_schema.setObjectName("navbar_schema")
        self.horizontalLayout_4.addWidget(self.navbar_schema)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.navbar_gen_data = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.navbar_gen_data.setObjectName("navbar_gen_data")
        self.horizontalLayout_4.addWidget(self.navbar_gen_data)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.navbar_questions = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.navbar_questions.setEnabled(False)
        self.navbar_questions.setObjectName("navbar_questions")
        self.horizontalLayout_4.addWidget(self.navbar_questions)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)

        self.retranslateUi(NewSceneMenuSchema)
        QtCore.QMetaObject.connectSlotsByName(NewSceneMenuSchema)

    def retranslateUi(self, NewSceneMenuSchema):
        _translate = QtCore.QCoreApplication.translate
        NewSceneMenuSchema.setWindowTitle(_translate("NewSceneMenuSchema", "Form"))
        self.confirm_button.setText(_translate("NewSceneMenuSchema", "Confirmar esquema"))
        self.return_button.setText(_translate("NewSceneMenuSchema", "Volver al menú"))
        self.label_6.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Puedes introducir o modificar la definición manualmente en este área de texto:</span></p></body></html>"))
        self.label_5.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Carga la definicion de las tablas desde un archivo:</span></p></body></html>"))
        self.label_2.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Paso 1 elige el nombre del escenario e introduce el DDL:</span></p></body></html>"))
        self.label_3.setText(_translate("NewSceneMenuSchema", "Nombre del escenario:"))
        self.load_file_button.setText(_translate("NewSceneMenuSchema", "Cargar archivo"))
        self.label_4.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:12pt;\">Ningún archivo seleccionado.</span></p></body></html>"))
        self.navbar_schema.setText(_translate("NewSceneMenuSchema", "Esquema"))
        self.label_9.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:26pt;\">➤</span></p></body></html>"))
        self.navbar_gen_data.setText(_translate("NewSceneMenuSchema", "Generar datos"))
        self.label_10.setText(_translate("NewSceneMenuSchema", "<html><head/><body><p><span style=\" font-size:26pt;\">➤</span></p></body></html>"))
        self.navbar_questions.setText(_translate("NewSceneMenuSchema", "Configurar preguntas"))
from . import resources
