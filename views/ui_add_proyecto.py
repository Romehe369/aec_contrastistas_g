# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_proyectoAeuMDS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_project_new(object):
    def setupUi(self, add_project_new):
        if not add_project_new.objectName():
            add_project_new.setObjectName(u"add_project_new")
        add_project_new.resize(684, 627)
        self.frame_contenedor = QFrame(add_project_new)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setGeometry(QRect(9, 9, 666, 609))
        self.frame_contenedor.setStyleSheet(u"QFrame{\n"
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
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_contenedor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 131, 31))
        self.label_3 = QLabel(self.frame_contenedor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 146, 251, 20))
        self.label_4 = QLabel(self.frame_contenedor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 210, 151, 16))
        self.name_project_lineEdit = QLineEdit(self.frame_contenedor)
        self.name_project_lineEdit.setObjectName(u"name_project_lineEdit")
        self.name_project_lineEdit.setGeometry(QRect(30, 170, 611, 31))
        self.name_project_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.id_res_linetext = QLineEdit(self.frame_contenedor)
        self.id_res_linetext.setObjectName(u"id_res_linetext")
        self.id_res_linetext.setGeometry(QRect(30, 240, 211, 31))
        self.id_res_linetext.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.search_name_db = QPushButton(self.frame_contenedor)
        self.search_name_db.setObjectName(u"search_name_db")
        self.search_name_db.setGeometry(QRect(260, 240, 161, 31))
        self.allow_btn = QPushButton(self.frame_contenedor)
        self.allow_btn.setObjectName(u"allow_btn")
        self.allow_btn.setGeometry(QRect(130, 550, 180, 41))
        self.decline_btn = QPushButton(self.frame_contenedor)
        self.decline_btn.setObjectName(u"decline_btn")
        self.decline_btn.setGeometry(QRect(350, 550, 180, 41))
        self.label_9 = QLabel(self.frame_contenedor)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 360, 181, 16))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.frame_contenedor)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(245, 360, 191, 16))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.frame_contenedor)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 430, 151, 16))
        self.references_plainTextEdit = QPlainTextEdit(self.frame_contenedor)
        self.references_plainTextEdit.setObjectName(u"references_plainTextEdit")
        self.references_plainTextEdit.setGeometry(QRect(30, 450, 621, 81))
        self.references_plainTextEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.frame_contenedor)
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

        self.district_lineEdit.raise_()
        self.label_8.raise_()

        self.horizontalLayout.addWidget(self.frame_6)

        self.start_dateEdit = QDateEdit(self.frame_contenedor)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setGeometry(QRect(30, 390, 191, 31))
        self.end_dateEdit = QDateEdit(self.frame_contenedor)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setGeometry(QRect(245, 390, 191, 31))
        self.info_txt_lbl = QLabel(self.frame_contenedor)
        self.info_txt_lbl.setObjectName(u"info_txt_lbl")
        self.info_txt_lbl.setGeometry(QRect(260, 80, 371, 61))
        self.info_txt_lbl.setStyleSheet(u"QLabel{\n"
"	border: 2px solid red;\n"
"	border-radius:10px;\n"
"}")
        self.info_txt_lbl.setAlignment(Qt.AlignCenter)
        self.lbl_code_pro_random = QLabel(self.frame_contenedor)
        self.lbl_code_pro_random.setObjectName(u"lbl_code_pro_random")
        self.lbl_code_pro_random.setGeometry(QRect(30, 110, 181, 31))
        self.lbl_code_pro_random.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 0, 255);")
        self.name_project_label = QLabel(self.frame_contenedor)
        self.name_project_label.setObjectName(u"name_project_label")
        self.name_project_label.setGeometry(QRect(20, 20, 613, 33))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.name_project_label.setFont(font)
        self.name_project_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Times New Roman\";")
        self.name_project_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(add_project_new)

        QMetaObject.connectSlotsByName(add_project_new)
    # setupUi

    def retranslateUi(self, add_project_new):
        add_project_new.setWindowTitle(QCoreApplication.translate("add_project_new", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("add_project_new", u"Codigo proyecto:", None))
        self.label_3.setText(QCoreApplication.translate("add_project_new", u"Nombre del proyecto:", None))
        self.label_4.setText(QCoreApplication.translate("add_project_new", u"DNI Responsable:", None))
        self.search_name_db.setText(QCoreApplication.translate("add_project_new", u"Buscar por nombre", None))
        self.allow_btn.setText(QCoreApplication.translate("add_project_new", u"Aceptar", None))
        self.decline_btn.setText(QCoreApplication.translate("add_project_new", u"Cancelar", None))
        self.label_9.setText(QCoreApplication.translate("add_project_new", u"Fecha inicio:", None))
        self.label_10.setText(QCoreApplication.translate("add_project_new", u"Fecha fin:", None))
        self.label_11.setText(QCoreApplication.translate("add_project_new", u"Referencias:", None))
        self.references_plainTextEdit.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("add_project_new", u"Region", None))
        self.label_7.setText(QCoreApplication.translate("add_project_new", u"Provincia", None))
        self.label_8.setText(QCoreApplication.translate("add_project_new", u"Distrito", None))
        self.info_txt_lbl.setText(QCoreApplication.translate("add_project_new", u"El c\u00f3digo del proyecto se genera \n"
" automaticamente, no es editable, ni modificable.", None))
        self.lbl_code_pro_random.setText(QCoreApplication.translate("add_project_new", u"Codigo aleatorio", None))
        self.name_project_label.setText(QCoreApplication.translate("add_project_new", u"Agregar un proyecto", None))
    # retranslateUi

