# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tpaymentshRkgyd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tpayments(object):
    def setupUi(self, tpayments):
        if not tpayments.objectName():
            tpayments.setObjectName(u"tpayments")
        tpayments.resize(1066, 608)
        self.centralwidget = QWidget(tpayments)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_agregar = QFrame(self.centralwidget)
        self.frame_agregar.setObjectName(u"frame_agregar")
        self.frame_agregar.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(0, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox{\n"
"border: none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"border: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(170, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_agregar.setFrameShape(QFrame.StyledPanel)
        self.frame_agregar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_agregar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame_agregar)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 35))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(117, 117, 117);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 0))
        self.lbl_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_title)

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

        self.horizontalLayout.addWidget(self.btn_ampliar)

        self.btn_close = QPushButton(self.frame_superior)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(35, 35))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_3.addWidget(self.frame_superior)

        self.frame_princiapl = QFrame(self.frame_agregar)
        self.frame_princiapl.setObjectName(u"frame_princiapl")
        self.frame_princiapl.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_princiapl.setFrameShape(QFrame.StyledPanel)
        self.frame_princiapl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_princiapl)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, -1, 25, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dateEdit = QDateEdit(self.frame_princiapl)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 31))
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);\n"
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
"    min-width: 50px;\n"
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
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dateEdit, 1, 4, 1, 1)

        self.lineEdit_dni = QLineEdit(self.frame_princiapl)
        self.lineEdit_dni.setObjectName(u"lineEdit_dni")
        self.lineEdit_dni.setMinimumSize(QSize(0, 31))
        self.lineEdit_dni.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_dni.setFont(font)
        self.lineEdit_dni.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_dni, 0, 1, 1, 1)

        self.label_45 = QLabel(self.frame_princiapl)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_45, 0, 2, 1, 1)

        self.lineEdit_year = QLineEdit(self.frame_princiapl)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setMinimumSize(QSize(0, 31))
        self.lineEdit_year.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_year.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.lineEdit_year.setMaxLength(4)

        self.gridLayout_2.addWidget(self.lineEdit_year, 1, 1, 1, 1)

        self.btn_details = QPushButton(self.frame_princiapl)
        self.btn_details.setObjectName(u"btn_details")
        self.btn_details.setMinimumSize(QSize(250, 31))
        self.btn_details.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_details, 1, 3, 1, 1)

        self.comboBox_selection = QComboBox(self.frame_princiapl)
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.setObjectName(u"comboBox_selection")
        self.comboBox_selection.setMinimumSize(QSize(0, 31))
        self.comboBox_selection.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.comboBox_selection, 0, 0, 1, 1)

        self.comboBox_month = QComboBox(self.frame_princiapl)
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.setObjectName(u"comboBox_month")
        self.comboBox_month.setMinimumSize(QSize(0, 31))
        self.comboBox_month.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_month.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.comboBox_month, 0, 3, 1, 1)

        self.label_47 = QLabel(self.frame_princiapl)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_47, 1, 0, 1, 1)

        self.label_49 = QLabel(self.frame_princiapl)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_49, 1, 2, 1, 1)

        self.label_50 = QLabel(self.frame_princiapl)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_50, 0, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.btn_show_table = QPushButton(self.frame_princiapl)
        self.btn_show_table.setObjectName(u"btn_show_table")
        self.btn_show_table.setMinimumSize(QSize(0, 31))
        self.btn_show_table.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_show_table)

        self.layout_data = QVBoxLayout()
        self.layout_data.setSpacing(6)
        self.layout_data.setObjectName(u"layout_data")
        self.layout_data.setContentsMargins(20, -1, 20, 6)
        self.table_payments = QTableWidget(self.frame_princiapl)
        if (self.table_payments.columnCount() < 5):
            self.table_payments.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_payments.setObjectName(u"table_payments")
        self.table_payments.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.layout_data.addWidget(self.table_payments)

        self.table_detalls = QTableWidget(self.frame_princiapl)
        if (self.table_detalls.columnCount() < 12):
            self.table_detalls.setColumnCount(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_detalls.setHorizontalHeaderItem(11, __qtablewidgetitem16)
        self.table_detalls.setObjectName(u"table_detalls")
        self.table_detalls.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.layout_data.addWidget(self.table_detalls)


        self.verticalLayout_4.addLayout(self.layout_data)


        self.verticalLayout_3.addWidget(self.frame_princiapl)

        self.frame_pagos = QFrame(self.frame_agregar)
        self.frame_pagos.setObjectName(u"frame_pagos")
        self.frame_pagos.setMinimumSize(QSize(0, 0))
        self.frame_pagos.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"border-radius:0px;\n"
"}")
        self.frame_pagos.setFrameShape(QFrame.StyledPanel)
        self.frame_pagos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pagos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, 15)
        self.frame = QFrame(self.frame_pagos)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 3px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(25)
        self.gridLayout_4.setVerticalSpacing(6)
        self.label_periodo = QLabel(self.frame)
        self.label_periodo.setObjectName(u"label_periodo")
        self.label_periodo.setMinimumSize(QSize(0, 31))
        self.label_periodo.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_periodo, 1, 3, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(160, 25))
        self.label_35.setMaximumSize(QSize(16777215, 35))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_surnames = QLabel(self.frame)
        self.label_surnames.setObjectName(u"label_surnames")
        self.label_surnames.setMinimumSize(QSize(0, 31))
        self.label_surnames.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_surnames, 2, 1, 1, 1)

        self.label_46 = QLabel(self.frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_46, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 2, 4, 1, 1)

        self.label_48 = QLabel(self.frame)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 31))
        self.label_48.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)

        self.lndt_sdni = QLineEdit(self.frame)
        self.lndt_sdni.setObjectName(u"lndt_sdni")
        self.lndt_sdni.setMinimumSize(QSize(0, 31))
        self.lndt_sdni.setMaximumSize(QSize(300, 16777215))
        self.lndt_sdni.setFont(font)
        self.lndt_sdni.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.lndt_sdni.setMaxLength(8)

        self.gridLayout_4.addWidget(self.lndt_sdni, 0, 1, 1, 1)

        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(0, 31))
        self.label_name.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_name, 1, 1, 1, 1)

        self.label_total = QLabel(self.frame)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_total, 2, 5, 1, 1)

        self.label_month_add = QLabel(self.frame)
        self.label_month_add.setObjectName(u"label_month_add")
        self.label_month_add.setMinimumSize(QSize(0, 31))
        self.label_month_add.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_month_add, 0, 3, 1, 1)

        self.label_all_days = QLabel(self.frame)
        self.label_all_days.setObjectName(u"label_all_days")
        self.label_all_days.setMinimumSize(QSize(0, 31))
        self.label_all_days.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_all_days, 0, 5, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_days_pay = QLabel(self.frame)
        self.label_days_pay.setObjectName(u"label_days_pay")
        self.label_days_pay.setMinimumSize(QSize(150, 0))
        self.label_days_pay.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_days_pay, 1, 5, 1, 1)

        self.lndt_adelantos = QLineEdit(self.frame)
        self.lndt_adelantos.setObjectName(u"lndt_adelantos")
        self.lndt_adelantos.setMinimumSize(QSize(0, 31))
        self.lndt_adelantos.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.lndt_adelantos, 2, 3, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 2, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 3)
        self.gridLayout_4.setColumnStretch(4, 1)
        self.gridLayout_4.setColumnStretch(5, 4)

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.horizontalFrame = QFrame(self.frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_51 = QLabel(self.horizontalFrame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 31))
        self.label_51.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_51)

        self.lndt_observaciones = QLineEdit(self.horizontalFrame)
        self.lndt_observaciones.setObjectName(u"lndt_observaciones")
        self.lndt_observaciones.setMinimumSize(QSize(0, 31))
        self.lndt_observaciones.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.lndt_observaciones)

        self.label_53 = QLabel(self.horizontalFrame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 31))
        self.label_53.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_53)

        self.total_adelantos = QLabel(self.horizontalFrame)
        self.total_adelantos.setObjectName(u"total_adelantos")
        self.total_adelantos.setMaximumSize(QSize(200, 16777215))
        self.total_adelantos.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")

        self.horizontalLayout_5.addWidget(self.total_adelantos)

        self.label_52 = QLabel(self.horizontalFrame)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 31))
        self.label_52.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_52)

        self.label_porpagar = QLabel(self.horizontalFrame)
        self.label_porpagar.setObjectName(u"label_porpagar")
        self.label_porpagar.setMaximumSize(QSize(200, 16777215))
        self.label_porpagar.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")

        self.horizontalLayout_5.addWidget(self.label_porpagar)

        self.label_esta = QLabel(self.horizontalFrame)
        self.label_esta.setObjectName(u"label_esta")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.label_esta.setFont(font1)
        self.label_esta.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_esta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_esta)

        self.label_estado = QLabel(self.horizontalFrame)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setFont(font1)
        self.label_estado.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_estado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_estado)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_pagar_new = QPushButton(self.frame)
        self.btn_pagar_new.setObjectName(u"btn_pagar_new")
        self.btn_pagar_new.setMinimumSize(QSize(0, 31))
        self.btn_pagar_new.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_pagar_new)

        self.btn_dar_adelantos = QPushButton(self.frame)
        self.btn_dar_adelantos.setObjectName(u"btn_dar_adelantos")
        self.btn_dar_adelantos.setMinimumSize(QSize(0, 31))
        self.btn_dar_adelantos.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_dar_adelantos)

        self.btn_close_pframe = QPushButton(self.frame)
        self.btn_close_pframe.setObjectName(u"btn_close_pframe")
        self.btn_close_pframe.setMinimumSize(QSize(0, 31))
        self.btn_close_pframe.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close_pframe)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_pagos)


        self.horizontalLayout_2.addWidget(self.frame_agregar)

        tpayments.setCentralWidget(self.centralwidget)

        self.retranslateUi(tpayments)

        QMetaObject.connectSlotsByName(tpayments)
    # setupUi

    def retranslateUi(self, tpayments):
        tpayments.setWindowTitle(QCoreApplication.translate("tpayments", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("tpayments", u"T TAREO Y OTROS", None))
        self.btn_ampliar.setText(QCoreApplication.translate("tpayments", u"\u25a0", None))
        self.btn_close.setText(QCoreApplication.translate("tpayments", u"X", None))
        self.lineEdit_dni.setPlaceholderText(QCoreApplication.translate("tpayments", u"Selecione una opci\u00f3n y presione ENTER", None))
        self.label_45.setText(QCoreApplication.translate("tpayments", u"MES:", None))
        self.lineEdit_year.setText(QCoreApplication.translate("tpayments", u"2023", None))
        self.btn_details.setText(QCoreApplication.translate("tpayments", u"VER DETALLES", None))
        self.comboBox_selection.setItemText(0, QCoreApplication.translate("tpayments", u"MOSTRAR TODO", None))
        self.comboBox_selection.setItemText(1, QCoreApplication.translate("tpayments", u"DNI", None))
        self.comboBox_selection.setItemText(2, QCoreApplication.translate("tpayments", u"Nombre", None))
        self.comboBox_selection.setItemText(3, QCoreApplication.translate("tpayments", u"Apellidos", None))

        self.comboBox_month.setItemText(0, QCoreApplication.translate("tpayments", u"ENERO", None))
        self.comboBox_month.setItemText(1, QCoreApplication.translate("tpayments", u"FEBRERO", None))
        self.comboBox_month.setItemText(2, QCoreApplication.translate("tpayments", u"MARZO", None))
        self.comboBox_month.setItemText(3, QCoreApplication.translate("tpayments", u"ABRIL", None))
        self.comboBox_month.setItemText(4, QCoreApplication.translate("tpayments", u"MAYO", None))
        self.comboBox_month.setItemText(5, QCoreApplication.translate("tpayments", u"JUNIO", None))
        self.comboBox_month.setItemText(6, QCoreApplication.translate("tpayments", u"JULIO", None))
        self.comboBox_month.setItemText(7, QCoreApplication.translate("tpayments", u"AGOSTO", None))
        self.comboBox_month.setItemText(8, QCoreApplication.translate("tpayments", u"SETIEMBRE", None))
        self.comboBox_month.setItemText(9, QCoreApplication.translate("tpayments", u"OCTUBRE", None))
        self.comboBox_month.setItemText(10, QCoreApplication.translate("tpayments", u"NOVIEMBRE", None))
        self.comboBox_month.setItemText(11, QCoreApplication.translate("tpayments", u"DICIEMBRE", None))

        self.label_47.setText(QCoreApplication.translate("tpayments", u"PERIODO:", None))
        self.label_49.setText(QCoreApplication.translate("tpayments", u"DETALLES:", None))
        self.label_50.setText(QCoreApplication.translate("tpayments", u"FECHA", None))
        self.btn_show_table.setText(QCoreApplication.translate("tpayments", u"TABLA DE DATOS", None))
        ___qtablewidgetitem = self.table_payments.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tpayments", u"DNI", None));
        ___qtablewidgetitem1 = self.table_payments.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tpayments", u"Nombres", None));
        ___qtablewidgetitem2 = self.table_payments.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tpayments", u"Apellidos", None));
        ___qtablewidgetitem3 = self.table_payments.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tpayments", u"Cargo", None));
        ___qtablewidgetitem4 = self.table_payments.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tpayments", u"Diario", None));
        ___qtablewidgetitem5 = self.table_detalls.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tpayments", u"Fecha", None));
        ___qtablewidgetitem6 = self.table_detalls.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tpayments", u"DNI", None));
        ___qtablewidgetitem7 = self.table_detalls.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tpayments", u"Nombres", None));
        ___qtablewidgetitem8 = self.table_detalls.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tpayments", u"Apellidos", None));
        ___qtablewidgetitem9 = self.table_detalls.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tpayments", u"Cargo", None));
        ___qtablewidgetitem10 = self.table_detalls.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tpayments", u"Diario", None));
        ___qtablewidgetitem11 = self.table_detalls.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("tpayments", u"Total de dias", None));
        ___qtablewidgetitem12 = self.table_detalls.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("tpayments", u"Total Girar", None));
        ___qtablewidgetitem13 = self.table_detalls.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("tpayments", u"Adelantos", None));
        ___qtablewidgetitem14 = self.table_detalls.horizontalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("tpayments", u"Por pagar", None));
        ___qtablewidgetitem15 = self.table_detalls.horizontalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("tpayments", u"Observaciones", None));
        ___qtablewidgetitem16 = self.table_detalls.horizontalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("tpayments", u"Estado", None));
        self.label.setText(QCoreApplication.translate("tpayments", u"MENU PAGAR", None))
        self.label_periodo.setText(QCoreApplication.translate("tpayments", u"2023", None))
        self.label_35.setText(QCoreApplication.translate("tpayments", u"DNI:", None))
        self.label_3.setText(QCoreApplication.translate("tpayments", u"PERIODO", None))
        self.label_surnames.setText(QCoreApplication.translate("tpayments", u"No especifica", None))
        self.label_46.setText(QCoreApplication.translate("tpayments", u"NOMBRES:", None))
        self.label_9.setText(QCoreApplication.translate("tpayments", u"TOTAL:", None))
        self.label_48.setText(QCoreApplication.translate("tpayments", u"APELLIDOS:", None))
        self.label_2.setText(QCoreApplication.translate("tpayments", u"MES:", None))
        self.lndt_sdni.setPlaceholderText(QCoreApplication.translate("tpayments", u"Ingrese  el DNI", None))
        self.label_name.setText(QCoreApplication.translate("tpayments", u"No especifica", None))
        self.label_total.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.label_month_add.setText(QCoreApplication.translate("tpayments", u"ENERO", None))
        self.label_all_days.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.label_4.setText(QCoreApplication.translate("tpayments", u"TOTAL DE DIAS:", None))
        self.label_7.setText(QCoreApplication.translate("tpayments", u"POR DIA:", None))
        self.label_days_pay.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.lndt_adelantos.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.lndt_adelantos.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("tpayments", u"ADELANTOS:", None))
        self.label_51.setText(QCoreApplication.translate("tpayments", u"OBSERVACIONES:", None))
        self.lndt_observaciones.setText("")
        self.lndt_observaciones.setPlaceholderText(QCoreApplication.translate("tpayments", u"Escriba las observaciones", None))
        self.label_53.setText(QCoreApplication.translate("tpayments", u"TOTAL DE ADELANTOS:", None))
        self.total_adelantos.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.label_52.setText(QCoreApplication.translate("tpayments", u"TOTAL A PAGAR:", None))
        self.label_porpagar.setText(QCoreApplication.translate("tpayments", u"0", None))
        self.label_esta.setText(QCoreApplication.translate("tpayments", u"ESTADO:", None))
        self.label_estado.setText(QCoreApplication.translate("tpayments", u"NO PAGADO", None))
        self.btn_pagar_new.setText(QCoreApplication.translate("tpayments", u"PAGAR", None))
        self.btn_dar_adelantos.setText(QCoreApplication.translate("tpayments", u"DAR ADELANTOS", None))
        self.btn_close_pframe.setText(QCoreApplication.translate("tpayments", u"MOSTRAR SOLO TABLA", None))
    # retranslateUi

