# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_proyectoHzToHh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(684, 627)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	border: 5px solid rgb(0, 0, 127);\n"
"	border-radius:10px;\n"
"	background-color: rgb(144, 144, 144);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox{\n"
"background-color: white;\n"
"}\n"
"QDateEdit{\n"
"background-color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 631, 51))
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Times New Roman\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 131, 31))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 150, 251, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 210, 151, 16))
        self.Name_project_lineEdit = QLineEdit(self.frame_2)
        self.Name_project_lineEdit.setObjectName(u"Name_project_lineEdit")
        self.Name_project_lineEdit.setGeometry(QRect(30, 170, 611, 31))
        self.Name_project_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.id_res_linetext = QLineEdit(self.frame_2)
        self.id_res_linetext.setObjectName(u"id_res_linetext")
        self.id_res_linetext.setGeometry(QRect(30, 240, 211, 31))
        self.id_res_linetext.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 240, 161, 31))
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 550, 180, 41))
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 550, 180, 41))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 360, 181, 16))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 360, 151, 16))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 430, 151, 16))
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 450, 621, 81))
        self.plainTextEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 290, 621, 61))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.region_lineEdit = QLineEdit(self.frame_4)
        self.region_lineEdit.setObjectName(u"region_lineEdit")
        self.region_lineEdit.setMinimumSize(QSize(0, 31))
        self.region_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.region_lineEdit)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.province_lineEdit = QLineEdit(self.frame_5)
        self.province_lineEdit.setObjectName(u"province_lineEdit")
        self.province_lineEdit.setMinimumSize(QSize(0, 31))
        self.province_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.province_lineEdit)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.district_lineEdit = QLineEdit(self.frame_6)
        self.district_lineEdit.setObjectName(u"district_lineEdit")
        self.district_lineEdit.setMinimumSize(QSize(0, 31))
        self.district_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.district_lineEdit)


        self.horizontalLayout.addWidget(self.frame_6)

        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 390, 171, 31))
        self.dateEdit_2 = QDateEdit(self.frame_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(300, 390, 151, 31))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 90, 381, 61))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	border: 2px solid red;\n"
"	border-radius:10px;\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lbl_code_pro_random = QLabel(self.frame_2)
        self.lbl_code_pro_random.setObjectName(u"lbl_code_pro_random")
        self.lbl_code_pro_random.setGeometry(QRect(30, 110, 171, 31))

        self.verticalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Agregar un proyecto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Codigo proyecto:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nombre del proyecto:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"DNI Responsable:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Buscar por nombre", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Fecha inicio:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Fecha fin:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Referencias:", None))
        self.plainTextEdit.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Region", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Provincia", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Distrito", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"El c\u00f3digo del proyecto se genera \n"
" automaticamente, no es editable, ni modificable.", None))
        self.lbl_code_pro_random.setText(QCoreApplication.translate("Dialog", u"Codigo aleatorio", None))
    # retranslateUi

