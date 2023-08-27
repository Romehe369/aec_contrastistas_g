# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_proyectoUsDvqU.ui'
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
        add_project_new.resize(800, 520)
        self.centralwidget = QWidget(add_project_new)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
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
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDateEdit{\n"
"background-color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color : lightgreen;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    /* delete default icons */\n"
" "
                        "   min-width: 50px;\n"
"    max-height: 33px;\n"
"	/* set background transparent */\n"
"}\n"
"#qt_calendar_navigationbar {\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	width: 110px;\n"
"	height: 31px;\n"
"}\n"
"#qt_calendar_yearbutton {\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	width: 70px;\n"
"	height: 31px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"	background-color: rgb(158, 158, 158);\n"
"}")
        self.layout_principal = QHBoxLayout(self.frame_superior)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setObjectName(u"layout_principal")
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.lbl_title)

        self.btn_ampliar = QPushButton(self.frame_superior)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        self.btn_ampliar.setMaximumSize(QSize(35, 35))
        self.btn_ampliar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_ampliar)

        self.btn_close = QPushButton(self.frame_superior)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(35, 35))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, 15, -1)
        self.number_of_days = QLineEdit(self.centralwidget)
        self.number_of_days.setObjectName(u"number_of_days")
        self.number_of_days.setMinimumSize(QSize(0, 31))
        self.number_of_days.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.gridLayout.addWidget(self.number_of_days, 6, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 31))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.checkBox_numbers_of_days = QCheckBox(self.centralwidget)
        self.checkBox_numbers_of_days.setObjectName(u"checkBox_numbers_of_days")
        self.checkBox_numbers_of_days.setMinimumSize(QSize(0, 31))
        self.checkBox_numbers_of_days.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")

        self.gridLayout.addWidget(self.checkBox_numbers_of_days, 5, 2, 1, 1)

        self.lineEdit_dni_admin = QLineEdit(self.centralwidget)
        self.lineEdit_dni_admin.setObjectName(u"lineEdit_dni_admin")
        self.lineEdit_dni_admin.setMinimumSize(QSize(0, 31))
        self.lineEdit_dni_admin.setStyleSheet(u"")
        self.lineEdit_dni_admin.setMaxLength(8)

        self.gridLayout.addWidget(self.lineEdit_dni_admin, 2, 1, 1, 1)

        self.comboBox_province = QComboBox(self.centralwidget)
        self.comboBox_province.setObjectName(u"comboBox_province")
        self.comboBox_province.setMinimumSize(QSize(0, 31))
        self.comboBox_province.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.comboBox_province, 4, 1, 1, 1)

        self.search_name_db = QPushButton(self.centralwidget)
        self.search_name_db.setObjectName(u"search_name_db")
        self.search_name_db.setMinimumSize(QSize(0, 31))
        self.search_name_db.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.search_name_db, 2, 2, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 31))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 31))
        self.label_3.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.comboBox_district = QComboBox(self.centralwidget)
        self.comboBox_district.setObjectName(u"comboBox_district")
        self.comboBox_district.setMinimumSize(QSize(0, 31))
        self.comboBox_district.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.comboBox_district, 4, 2, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 31))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.lbl_code_pro_random = QLabel(self.centralwidget)
        self.lbl_code_pro_random.setObjectName(u"lbl_code_pro_random")
        self.lbl_code_pro_random.setMinimumSize(QSize(0, 31))
        self.lbl_code_pro_random.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 0, 255);")

        self.gridLayout.addWidget(self.lbl_code_pro_random, 0, 1, 1, 1)

        self.comboBox_region = QComboBox(self.centralwidget)
        self.comboBox_region.setObjectName(u"comboBox_region")
        self.comboBox_region.setMinimumSize(QSize(250, 31))
        self.comboBox_region.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.comboBox_region, 4, 0, 1, 1)

        self.end_dateEdit = QDateEdit(self.centralwidget)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setMinimumSize(QSize(0, 31))
        self.end_dateEdit.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.end_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.end_dateEdit, 6, 1, 1, 1)

        self.name_project_lineEdit = QLineEdit(self.centralwidget)
        self.name_project_lineEdit.setObjectName(u"name_project_lineEdit")
        self.name_project_lineEdit.setMinimumSize(QSize(0, 31))
        self.name_project_lineEdit.setStyleSheet(u"")

        self.gridLayout.addWidget(self.name_project_lineEdit, 1, 1, 1, 1)

        self.start_dateEdit = QDateEdit(self.centralwidget)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setMinimumSize(QSize(0, 31))
        self.start_dateEdit.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.start_dateEdit.setProperty("showGroupSeparator", False)
        self.start_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.start_dateEdit, 6, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 31))
        self.label_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, -1, 15, 15)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 31))

        self.verticalLayout.addWidget(self.label_11)

        self.references_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.references_plainTextEdit.setObjectName(u"references_plainTextEdit")
        self.references_plainTextEdit.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.references_plainTextEdit)

        self.allow_btn = QPushButton(self.centralwidget)
        self.allow_btn.setObjectName(u"allow_btn")
        self.allow_btn.setMinimumSize(QSize(0, 31))

        self.verticalLayout.addWidget(self.allow_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        add_project_new.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_project_new)

        QMetaObject.connectSlotsByName(add_project_new)
    # setupUi

    def retranslateUi(self, add_project_new):
        add_project_new.setWindowTitle(QCoreApplication.translate("add_project_new", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("add_project_new", u"Agregar un proyecto", None))
        self.btn_ampliar.setText(QCoreApplication.translate("add_project_new", u"\u25a0", None))
        self.btn_close.setText(QCoreApplication.translate("add_project_new", u"X", None))
        self.number_of_days.setPlaceholderText(QCoreApplication.translate("add_project_new", u"Active \"Cantidad de d\u00edas\"", None))
        self.label_5.setText(QCoreApplication.translate("add_project_new", u"Region", None))
        self.checkBox_numbers_of_days.setText(QCoreApplication.translate("add_project_new", u"Cantidad de d\u00edas", None))
        self.lineEdit_dni_admin.setPlaceholderText(QCoreApplication.translate("add_project_new", u"DNI del responsable de la obra", None))
        self.search_name_db.setText(QCoreApplication.translate("add_project_new", u"Buscar por nombre", None))
        self.label_7.setText(QCoreApplication.translate("add_project_new", u"Provincia", None))
        self.label_4.setText(QCoreApplication.translate("add_project_new", u"DNI Responsable:", None))
        self.label_3.setText(QCoreApplication.translate("add_project_new", u"Nombre del proyecto:", None))
        self.label_8.setText(QCoreApplication.translate("add_project_new", u"Distrito", None))
        self.label_9.setText(QCoreApplication.translate("add_project_new", u"Fecha inicio", None))
        self.label_10.setText(QCoreApplication.translate("add_project_new", u"Fecha fin", None))
        self.lbl_code_pro_random.setText(QCoreApplication.translate("add_project_new", u"Codigo aleatorio", None))
        self.name_project_lineEdit.setPlaceholderText(QCoreApplication.translate("add_project_new", u"Ingrese el nombre del proyecto", None))
        self.label_2.setText(QCoreApplication.translate("add_project_new", u"Codigo proyecto", None))
        self.label_11.setText(QCoreApplication.translate("add_project_new", u"Referencias:", None))
        self.references_plainTextEdit.setPlainText("")
        self.references_plainTextEdit.setPlaceholderText("")
        self.allow_btn.setText(QCoreApplication.translate("add_project_new", u"Aceptar", None))
    # retranslateUi

