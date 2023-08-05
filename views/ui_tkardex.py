# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tkardexCbBAGZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tkarded(object):
    def setupUi(self, tkarded):
        if not tkarded.objectName():
            tkarded.setObjectName(u"tkarded")
        tkarded.resize(859, 546)
        self.centralwidget = QWidget(tkarded)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_agregar = QFrame(self.centralwidget)
        self.frame_agregar.setObjectName(u"frame_agregar")
        self.frame_agregar.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(0, 0, 127);\n"
"background-color: rgb(252, 252, 252);\n"
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
        self.verticalLayout_6 = QVBoxLayout(self.frame_agregar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame_agregar)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(117, 117, 117);\n"
"}")
        self.layout_principal = QHBoxLayout(self.frame_superior)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setObjectName(u"layout_principal")
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMaximumSize(QSize(16777215, 40))
        self.lbl_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.lbl_title)

        self.btn_ampliar = QPushButton(self.frame_superior)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        self.btn_ampliar.setMaximumSize(QSize(35, 40))
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
        self.btn_close.setMaximumSize(QSize(35, 40))
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


        self.verticalLayout_6.addWidget(self.frame_superior)

        self.frame = QFrame(self.frame_agregar)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 31))
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 31))
        self.lineEdit_4.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_4.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 31))
        self.label_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 31))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 31))
        self.label_13.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.table_qwk_new = QTableWidget(self.frame)
        if (self.table_qwk_new.columnCount() < 11):
            self.table_qwk_new.setColumnCount(11)
        font = QFont()
        font.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        self.table_qwk_new.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_qwk_new.setObjectName(u"table_qwk_new")
        self.table_qwk_new.setMaximumSize(QSize(16777215, 16777215))
        self.table_qwk_new.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.table_qwk_new.setAutoScrollMargin(16)

        self.verticalLayout_3.addWidget(self.table_qwk_new)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_add_data = QFrame(self.frame_agregar)
        self.frame_add_data.setObjectName(u"frame_add_data")
        self.frame_add_data.setMinimumSize(QSize(0, 0))
        self.frame_add_data.setStyleSheet(u"border:none;")
        self.frame_add_data.setFrameShape(QFrame.StyledPanel)
        self.frame_add_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_add_data)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, -1, 15, -1)
        self.frame_2 = QFrame(self.frame_add_data)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"border: 2px solid rgb(0, 0, 127);\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, -1, 15, -1)
        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_title)

        self.frame_hide = QFrame(self.frame_2)
        self.frame_hide.setObjectName(u"frame_hide")
        self.frame_hide.setStyleSheet(u"border: none;")
        self.frame_hide.setFrameShape(QFrame.StyledPanel)
        self.frame_hide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_hide)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.frame_hide)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 31))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_9 = QLabel(self.frame_hide)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_hide)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 31))
        self.lineEdit_9.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 3, 1, 1)

        self.label_6 = QLabel(self.frame_hide)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 31))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_hide)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 31))
        self.lineEdit_6.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self.frame_hide)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 31))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_hide)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame_hide)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_hide)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 31))
        self.lineEdit_8.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 3, 1, 1)

        self.label_5 = QLabel(self.frame_hide)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 31))
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_hide)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 31))
        self.lineEdit_5.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_hide)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 31))
        self.lineEdit_7.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.verticalLayout_7.addWidget(self.frame_hide)

        self.frame_delete = QFrame(self.frame_2)
        self.frame_delete.setObjectName(u"frame_delete")
        self.frame_delete.setStyleSheet(u"border: none;")
        self.frame_delete.setFrameShape(QFrame.StyledPanel)
        self.frame_delete.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_delete)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.frame_delete)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(300, 31))
        self.comboBox_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.lineEdit_10 = QLineEdit(self.frame_delete)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 31))
        self.lineEdit_10.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.horizontalLayout_2.addWidget(self.lineEdit_10)


        self.verticalLayout_7.addWidget(self.frame_delete)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirm_delete = QPushButton(self.frame_2)
        self.btn_confirm_delete.setObjectName(u"btn_confirm_delete")
        self.btn_confirm_delete.setMinimumSize(QSize(0, 31))
        self.btn_confirm_delete.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_confirm_delete)

        self.frame_show_btn = QFrame(self.frame_2)
        self.frame_show_btn.setObjectName(u"frame_show_btn")
        self.frame_show_btn.setStyleSheet(u"border: none;")
        self.frame_show_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_show_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_show_btn)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_out_material = QPushButton(self.frame_show_btn)
        self.btn_out_material.setObjectName(u"btn_out_material")
        self.btn_out_material.setMinimumSize(QSize(0, 31))
        self.btn_out_material.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_out_material)

        self.btn_add_devoluciones = QPushButton(self.frame_show_btn)
        self.btn_add_devoluciones.setObjectName(u"btn_add_devoluciones")
        self.btn_add_devoluciones.setMinimumSize(QSize(0, 31))
        self.btn_add_devoluciones.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_add_devoluciones)

        self.btn_delete_rmaterial = QPushButton(self.frame_show_btn)
        self.btn_delete_rmaterial.setObjectName(u"btn_delete_rmaterial")
        self.btn_delete_rmaterial.setMinimumSize(QSize(0, 31))
        self.btn_delete_rmaterial.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_delete_rmaterial)


        self.horizontalLayout.addWidget(self.frame_show_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.frame_add_data)


        self.verticalLayout.addWidget(self.frame_agregar)

        tkarded.setCentralWidget(self.centralwidget)

        self.retranslateUi(tkarded)

        QMetaObject.connectSlotsByName(tkarded)
    # setupUi

    def retranslateUi(self, tkarded):
        tkarded.setWindowTitle(QCoreApplication.translate("tkarded", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("tkarded", u"T KARDEX MATERIAL", None))
        self.btn_ampliar.setText(QCoreApplication.translate("tkarded", u"\u25a0", None))
        self.btn_close.setText(QCoreApplication.translate("tkarded", u"X", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("tkarded", u"Codigo Material", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("tkarded", u"Nombre Material", None))

        self.label.setText(QCoreApplication.translate("tkarded", u"MEDIDA :", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("tkarded", u"Digite aqu\u00ed y presione ENTER", None))
        self.label_11.setText(QCoreApplication.translate("tkarded", u"BLS", None))
        self.label_3.setText(QCoreApplication.translate("tkarded", u"SALDO :", None))
        self.label_2.setText(QCoreApplication.translate("tkarded", u"120", None))
        self.label_12.setText(QCoreApplication.translate("tkarded", u"NOMBRE:", None))
        self.label_13.setText(QCoreApplication.translate("tkarded", u"No espefica", None))
        ___qtablewidgetitem = self.table_qwk_new.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tkarded", u"Codigo proyecto", None));
        ___qtablewidgetitem1 = self.table_qwk_new.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tkarded", u"Fecha", None));
        ___qtablewidgetitem2 = self.table_qwk_new.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tkarded", u"Entradas", None));
        ___qtablewidgetitem3 = self.table_qwk_new.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tkarded", u"Salidas", None));
        ___qtablewidgetitem4 = self.table_qwk_new.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tkarded", u"Devoluciones", None));
        ___qtablewidgetitem5 = self.table_qwk_new.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tkarded", u"Saldo", None));
        ___qtablewidgetitem6 = self.table_qwk_new.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tkarded", u"Tipo de trabajo", None));
        ___qtablewidgetitem7 = self.table_qwk_new.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tkarded", u"Lote", None));
        ___qtablewidgetitem8 = self.table_qwk_new.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tkarded", u"Responsable", None));
        ___qtablewidgetitem9 = self.table_qwk_new.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tkarded", u"Observaciones", None));
        ___qtablewidgetitem10 = self.table_qwk_new.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tkarded", u"Firma", None));
        self.label_title.setText(QCoreApplication.translate("tkarded", u"AGREGAR UNA SALIDA <=> DEVOLUCIONES", None))
        self.label_7.setText(QCoreApplication.translate("tkarded", u"LOTE:", None))
        self.label_9.setText(QCoreApplication.translate("tkarded", u"OBSERVACIONES:", None))
        self.label_6.setText(QCoreApplication.translate("tkarded", u"TIPO DE TRABAJO:", None))
        self.label_8.setText(QCoreApplication.translate("tkarded", u"RESPONSABLE:", None))
        self.label_4.setText(QCoreApplication.translate("tkarded", u"FECHA:", None))
        self.label_5.setText(QCoreApplication.translate("tkarded", u"CODIGO DE PROYECTO : ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("tkarded", u"Eliminar un registro por codigo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("tkarded", u"Eliminar un registro por nombre", None))

        self.btn_confirm_delete.setText(QCoreApplication.translate("tkarded", u"CONFIRMAR ELIMINACION", None))
        self.btn_out_material.setText(QCoreApplication.translate("tkarded", u"SALIDAS", None))
        self.btn_add_devoluciones.setText(QCoreApplication.translate("tkarded", u"DEVOLUCIONES", None))
        self.btn_delete_rmaterial.setText(QCoreApplication.translate("tkarded", u"IR A ELIMINAR", None))
    # retranslateUi

