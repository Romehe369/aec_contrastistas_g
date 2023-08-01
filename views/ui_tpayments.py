# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tpaymentsYliSSo.ui'
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
        tpayments.resize(1066, 607)
        self.centralwidget = QWidget(tpayments)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_agregar = QFrame(self.centralwidget)
        self.frame_agregar.setObjectName(u"frame_agregar")
        self.frame_agregar.setStyleSheet(u"QFrame{\n"
"border: 3px solid rgb(0, 0, 127);\n"
"background-color: rgb(170, 170, 255);\n"
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
"	background-color: rgb(158, 158, 158);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 0))
        self.lbl_title.setStyleSheet(u"")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_title)

        self.btn_ampliar = QPushButton(self.frame_superior)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        self.btn_ampliar.setMaximumSize(QSize(35, 31))
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
        self.btn_close.setMaximumSize(QSize(35, 31))
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

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_3.addWidget(self.frame_superior)

        self.frame_princiapl = QFrame(self.frame_agregar)
        self.frame_princiapl.setObjectName(u"frame_princiapl")
        self.frame_princiapl.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_princiapl.setFrameShape(QFrame.StyledPanel)
        self.frame_princiapl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_princiapl)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_info = QHBoxLayout()
        self.layout_info.setSpacing(6)
        self.layout_info.setObjectName(u"layout_info")
        self.layout_info.setContentsMargins(20, -1, 20, -1)
        self.label_15 = QLabel(self.frame_princiapl)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(100, 100))
        self.label_15.setPixmap(QPixmap(u"../assets/icons/icono.png"))
        self.label_15.setScaledContents(True)

        self.layout_info.addWidget(self.label_15)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_6 = QLineEdit(self.frame_princiapl)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 31))
        self.lineEdit_6.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.lineEdit_year = QLineEdit(self.frame_princiapl)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setMinimumSize(QSize(0, 31))
        self.lineEdit_year.setMaximumSize(QSize(110, 16777215))
        self.lineEdit_year.setMaxLength(4)

        self.gridLayout.addWidget(self.lineEdit_year, 2, 1, 1, 1)

        self.label_45 = QLabel(self.frame_princiapl)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_45, 1, 0, 1, 1)

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
        self.comboBox_month.setMaximumSize(QSize(300, 16777215))
        self.comboBox_month.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.comboBox_month, 1, 1, 1, 1)

        self.btn_dar_adelantos = QPushButton(self.frame_princiapl)
        self.btn_dar_adelantos.setObjectName(u"btn_dar_adelantos")
        self.btn_dar_adelantos.setMinimumSize(QSize(0, 31))
        self.btn_dar_adelantos.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.btn_dar_adelantos, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.frame_princiapl)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.label_34 = QLabel(self.frame_princiapl)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(160, 25))
        self.label_34.setMaximumSize(QSize(16777215, 35))
        self.label_34.setFont(font)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_47 = QLabel(self.frame_princiapl)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_47, 2, 0, 1, 1)

        self.btn_pagar = QPushButton(self.frame_princiapl)
        self.btn_pagar.setObjectName(u"btn_pagar")
        self.btn_pagar.setMinimumSize(QSize(0, 31))
        self.btn_pagar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.btn_pagar, 2, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)

        self.layout_info.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.layout_info)

        self.layout_data = QVBoxLayout()
        self.layout_data.setSpacing(6)
        self.layout_data.setObjectName(u"layout_data")
        self.layout_data.setContentsMargins(20, -1, 20, -1)
        self.table_payments = QTableWidget(self.frame_princiapl)
        if (self.table_payments.columnCount() < 11):
            self.table_payments.setColumnCount(11)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_payments.setObjectName(u"table_payments")
        self.table_payments.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.layout_data.addWidget(self.table_payments)


        self.verticalLayout_2.addLayout(self.layout_data)


        self.verticalLayout_3.addWidget(self.frame_princiapl)

        self.frame_pagos = QFrame(self.frame_agregar)
        self.frame_pagos.setObjectName(u"frame_pagos")
        self.frame_pagos.setMinimumSize(QSize(0, 0))
        self.frame_pagos.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")
        self.frame_pagos.setFrameShape(QFrame.StyledPanel)
        self.frame_pagos.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_pagos)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_pagos)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.frame_pagos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_7 = QLabel(self.frame_pagos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_16 = QLabel(self.frame_pagos)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 31))
        self.label_16.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_16, 1, 3, 1, 1)

        self.label_8 = QLabel(self.frame_pagos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 1, 4, 1, 1)

        self.label_48 = QLabel(self.frame_pagos)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 31))
        self.label_48.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_35 = QLabel(self.frame_pagos)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(160, 25))
        self.label_35.setMaximumSize(QSize(16777215, 35))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_11 = QLabel(self.frame_pagos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 31))
        self.label_11.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_11, 2, 1, 1, 1)

        self.label_46 = QLabel(self.frame_pagos)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_46, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_pagos)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 31))
        self.label_10.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_10, 2, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_pagos)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 31))
        self.lineEdit_7.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_pagos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 2, 2, 1, 1)

        self.comboBox_month_2 = QComboBox(self.frame_pagos)
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.addItem("")
        self.comboBox_month_2.setObjectName(u"comboBox_month_2")
        self.comboBox_month_2.setMinimumSize(QSize(200, 31))
        self.comboBox_month_2.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_month_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.comboBox_month_2, 0, 3, 1, 1)

        self.label_9 = QLabel(self.frame_pagos)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 2, 4, 1, 1)

        self.label_5 = QLabel(self.frame_pagos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 31))
        self.label_5.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_pagos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_12 = QLabel(self.frame_pagos)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_12, 0, 5, 1, 1)

        self.label_13 = QLabel(self.frame_pagos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_13, 1, 5, 1, 1)

        self.label_14 = QLabel(self.frame_pagos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_4.addWidget(self.label_14, 2, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.label_6 = QLabel(self.frame_pagos)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.frame_pagos)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.btn_allow_pframe = QPushButton(self.frame_pagos)
        self.btn_allow_pframe.setObjectName(u"btn_allow_pframe")
        self.btn_allow_pframe.setMinimumSize(QSize(0, 31))
        self.btn_allow_pframe.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_allow_pframe)

        self.btn_close_pframe = QPushButton(self.frame_pagos)
        self.btn_close_pframe.setObjectName(u"btn_close_pframe")
        self.btn_close_pframe.setMinimumSize(QSize(0, 31))
        self.btn_close_pframe.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close_pframe)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


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
        self.label_15.setText("")
        self.label_45.setText(QCoreApplication.translate("tpayments", u"MES:", None))
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

        self.btn_dar_adelantos.setText(QCoreApplication.translate("tpayments", u"DAR ADELANTOS", None))
        self.pushButton.setText(QCoreApplication.translate("tpayments", u"OBTENER CODIGO", None))
        self.label_34.setText(QCoreApplication.translate("tpayments", u"CODIGO DE PROYECTO:", None))
        self.label_47.setText(QCoreApplication.translate("tpayments", u"PERIODO:", None))
        self.btn_pagar.setText(QCoreApplication.translate("tpayments", u"PAGAR", None))
        ___qtablewidgetitem = self.table_payments.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tpayments", u"DNI", None));
        ___qtablewidgetitem1 = self.table_payments.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tpayments", u"Nombres", None));
        ___qtablewidgetitem2 = self.table_payments.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tpayments", u"Apellidos", None));
        ___qtablewidgetitem3 = self.table_payments.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tpayments", u"Cargo", None));
        ___qtablewidgetitem4 = self.table_payments.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tpayments", u"Salario diario", None));
        ___qtablewidgetitem5 = self.table_payments.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tpayments", u"Total de dias", None));
        ___qtablewidgetitem6 = self.table_payments.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tpayments", u"Total Girar", None));
        ___qtablewidgetitem7 = self.table_payments.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tpayments", u"Adelantos", None));
        ___qtablewidgetitem8 = self.table_payments.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tpayments", u"Por pagar", None));
        ___qtablewidgetitem9 = self.table_payments.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tpayments", u"Observaciones", None));
        ___qtablewidgetitem10 = self.table_payments.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tpayments", u"Estado", None));
        self.label.setText(QCoreApplication.translate("tpayments", u"MENU PAGAR", None))
        self.label_2.setText(QCoreApplication.translate("tpayments", u"MES:", None))
        self.label_7.setText(QCoreApplication.translate("tpayments", u"POR DIA:", None))
        self.label_16.setText(QCoreApplication.translate("tpayments", u"2023", None))
        self.label_8.setText(QCoreApplication.translate("tpayments", u"ADELANTOS:", None))
        self.label_48.setText(QCoreApplication.translate("tpayments", u"APELLIDOS:", None))
        self.label_35.setText(QCoreApplication.translate("tpayments", u"DNI:", None))
        self.label_11.setText(QCoreApplication.translate("tpayments", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("tpayments", u"NOMBRES:", None))
        self.label_10.setText(QCoreApplication.translate("tpayments", u"23", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("tpayments", u"Ingrese  el DNI", None))
        self.label_4.setText(QCoreApplication.translate("tpayments", u"TOTAL DE DIAS:", None))
        self.comboBox_month_2.setItemText(0, QCoreApplication.translate("tpayments", u"ENERO", None))
        self.comboBox_month_2.setItemText(1, QCoreApplication.translate("tpayments", u"FEBRERO", None))
        self.comboBox_month_2.setItemText(2, QCoreApplication.translate("tpayments", u"MARZO", None))
        self.comboBox_month_2.setItemText(3, QCoreApplication.translate("tpayments", u"ABRIL", None))
        self.comboBox_month_2.setItemText(4, QCoreApplication.translate("tpayments", u"MAYO", None))
        self.comboBox_month_2.setItemText(5, QCoreApplication.translate("tpayments", u"JUNIO", None))
        self.comboBox_month_2.setItemText(6, QCoreApplication.translate("tpayments", u"JULIO", None))
        self.comboBox_month_2.setItemText(7, QCoreApplication.translate("tpayments", u"AGOSTO", None))
        self.comboBox_month_2.setItemText(8, QCoreApplication.translate("tpayments", u"SETIEMBRE", None))
        self.comboBox_month_2.setItemText(9, QCoreApplication.translate("tpayments", u"OCTUBRE", None))
        self.comboBox_month_2.setItemText(10, QCoreApplication.translate("tpayments", u"NOVIEMBRE", None))
        self.comboBox_month_2.setItemText(11, QCoreApplication.translate("tpayments", u"DICIEMBRE", None))

        self.label_9.setText(QCoreApplication.translate("tpayments", u"TOTAL:", None))
        self.label_5.setText(QCoreApplication.translate("tpayments", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("tpayments", u"PERIODO", None))
        self.label_12.setText(QCoreApplication.translate("tpayments", u"55", None))
        self.label_13.setText(QCoreApplication.translate("tpayments", u"560", None))
        self.label_14.setText(QCoreApplication.translate("tpayments", u"705=55*22-560", None))
        self.label_6.setText(QCoreApplication.translate("tpayments", u"ESTADO : NO PAGADO", None))
        self.pushButton_5.setText(QCoreApplication.translate("tpayments", u"PAGAR", None))
        self.btn_allow_pframe.setText(QCoreApplication.translate("tpayments", u"ACEPTAR", None))
        self.btn_close_pframe.setText(QCoreApplication.translate("tpayments", u"CANCELAR", None))
    # retranslateUi

