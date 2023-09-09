# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tkardexEmoyJY.ui'
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
        tkarded.resize(907, 625)
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
        self.gridLayout.setHorizontalSpacing(10)
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(0, 31))
        self.label_name.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_name, 2, 1, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 31))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_saldo = QLabel(self.frame)
        self.label_saldo.setObjectName(u"label_saldo")
        self.label_saldo.setMinimumSize(QSize(150, 31))
        self.label_saldo.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_saldo, 2, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.btn_viewdetals = QPushButton(self.frame)
        self.btn_viewdetals.setObjectName(u"btn_viewdetals")
        self.btn_viewdetals.setMinimumSize(QSize(0, 31))
        self.btn_viewdetals.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.btn_viewdetals, 0, 5, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 31))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)

        self.label_medida = QLabel(self.frame)
        self.label_medida.setObjectName(u"label_medida")
        self.label_medida.setMinimumSize(QSize(150, 0))
        self.label_medida.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.label_medida, 0, 3, 1, 1)

        self.lndt_codemat = QLineEdit(self.frame)
        self.lndt_codemat.setObjectName(u"lndt_codemat")
        self.lndt_codemat.setMinimumSize(QSize(0, 31))
        self.lndt_codemat.setMaximumSize(QSize(16777215, 16777215))
        self.lndt_codemat.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout.addWidget(self.lndt_codemat, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.label_codemat = QLabel(self.frame)
        self.label_codemat.setObjectName(u"label_codemat")
        self.label_codemat.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_codemat, 2, 5, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.table_showinfo = QTableWidget(self.frame)
        if (self.table_showinfo.columnCount() < 4):
            self.table_showinfo.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_showinfo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_showinfo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_showinfo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_showinfo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_showinfo.setObjectName(u"table_showinfo")
        self.table_showinfo.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.verticalLayout_3.addWidget(self.table_showinfo)

        self.table_qwk_new = QTableWidget(self.frame)
        if (self.table_qwk_new.columnCount() < 10):
            self.table_qwk_new.setColumnCount(10)
        font = QFont()
        font.setPointSize(12)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        __qtablewidgetitem4.setBackground(QColor(255, 255, 255));
        self.table_qwk_new.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.table_qwk_new.setHorizontalHeaderItem(9, __qtablewidgetitem13)
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
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_title)

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
        self.lndt_typeword = QLineEdit(self.frame_hide)
        self.lndt_typeword.setObjectName(u"lndt_typeword")
        self.lndt_typeword.setMinimumSize(QSize(0, 31))
        self.lndt_typeword.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lndt_typeword, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_hide)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 31))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.lndt_lote = QLineEdit(self.frame_hide)
        self.lndt_lote.setObjectName(u"lndt_lote")
        self.lndt_lote.setMinimumSize(QSize(0, 31))
        self.lndt_lote.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.lndt_lote, 0, 3, 1, 1)

        self.observations_ledt = QLineEdit(self.frame_hide)
        self.observations_ledt.setObjectName(u"observations_ledt")
        self.observations_ledt.setMinimumSize(QSize(0, 31))
        self.observations_ledt.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.observations_ledt, 2, 3, 1, 1)

        self.label_9 = QLabel(self.frame_hide)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_8 = QLabel(self.frame_hide)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

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
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(0, 0, 127)\n"
"}\n"
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
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_hide)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 31))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_5 = QLabel(self.frame_hide)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 31))
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.edit_cantidad = QLineEdit(self.frame_hide)
        self.edit_cantidad.setObjectName(u"edit_cantidad")
        self.edit_cantidad.setMinimumSize(QSize(0, 31))
        self.edit_cantidad.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.gridLayout_2.addWidget(self.edit_cantidad, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_hide)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lndt_responsable = QLineEdit(self.frame_hide)
        self.lndt_responsable.setObjectName(u"lndt_responsable")
        self.lndt_responsable.setMinimumSize(QSize(0, 31))
        self.lndt_responsable.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")

        self.verticalLayout_7.addWidget(self.lndt_responsable)

        self.lstw_name = QListWidget(self.frame_hide)
        self.lstw_name.setObjectName(u"lstw_name")
        self.lstw_name.setMinimumSize(QSize(0, 0))
        self.lstw_name.setMaximumSize(QSize(16777215, 63))
        self.lstw_name.setStyleSheet(u"QListWidget{\n"
"color: rgb(255, 37, 226);\n"
"border: 1px solid rgb(0, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_7.addWidget(self.lstw_name)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.verticalLayout_9.addWidget(self.frame_hide)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_show_btn = QFrame(self.frame_2)
        self.frame_show_btn.setObjectName(u"frame_show_btn")
        self.frame_show_btn.setMaximumSize(QSize(16777215, 16777215))
        self.frame_show_btn.setStyleSheet(u"border: none;")
        self.frame_show_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_show_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_show_btn)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_addmaterial = QPushButton(self.frame_show_btn)
        self.btn_addmaterial.setObjectName(u"btn_addmaterial")
        self.btn_addmaterial.setMinimumSize(QSize(0, 31))
        self.btn_addmaterial.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_addmaterial)

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


        self.horizontalLayout.addWidget(self.frame_show_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


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
        self.label_name.setText(QCoreApplication.translate("tkarded", u"No espefica", None))
        self.label_13.setText(QCoreApplication.translate("tkarded", u"NOMBRE:", None))
        self.label_saldo.setText(QCoreApplication.translate("tkarded", u"0", None))
        self.label_3.setText(QCoreApplication.translate("tkarded", u"SALDO :", None))
        self.btn_viewdetals.setText(QCoreApplication.translate("tkarded", u"VER DETALLES", None))
        self.label_12.setText(QCoreApplication.translate("tkarded", u" NOMBRE MATERIAL:", None))
        self.label.setText(QCoreApplication.translate("tkarded", u"MEDIDA :", None))
        self.label_2.setText(QCoreApplication.translate("tkarded", u"REGISTRO:", None))
        self.label_medida.setText(QCoreApplication.translate("tkarded", u"BLS", None))
        self.lndt_codemat.setText("")
        self.lndt_codemat.setPlaceholderText(QCoreApplication.translate("tkarded", u"Digite aqu\u00ed y presione ENTER", None))
        self.label_10.setText(QCoreApplication.translate("tkarded", u"HISTORIAL:", None))
        self.label_codemat.setText(QCoreApplication.translate("tkarded", u"XYZUD.8965", None))
        ___qtablewidgetitem = self.table_showinfo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tkarded", u"CODIGO MATERIAL", None));
        ___qtablewidgetitem1 = self.table_showinfo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tkarded", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_showinfo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tkarded", u"Cantidad", None));
        ___qtablewidgetitem3 = self.table_showinfo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tkarded", u"Medida", None));
        ___qtablewidgetitem4 = self.table_qwk_new.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tkarded", u"Fecha", None));
        ___qtablewidgetitem5 = self.table_qwk_new.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tkarded", u"Entradas", None));
        ___qtablewidgetitem6 = self.table_qwk_new.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tkarded", u"Salidas", None));
        ___qtablewidgetitem7 = self.table_qwk_new.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tkarded", u"Devoluciones", None));
        ___qtablewidgetitem8 = self.table_qwk_new.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tkarded", u"Saldo", None));
        ___qtablewidgetitem9 = self.table_qwk_new.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tkarded", u"Tipo de trabajo", None));
        ___qtablewidgetitem10 = self.table_qwk_new.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tkarded", u"Lote", None));
        ___qtablewidgetitem11 = self.table_qwk_new.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("tkarded", u"Responsable", None));
        ___qtablewidgetitem12 = self.table_qwk_new.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("tkarded", u"Observaciones", None));
        ___qtablewidgetitem13 = self.table_qwk_new.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("tkarded", u"Firma", None));
        self.label_title.setText(QCoreApplication.translate("tkarded", u"AGREGAR UNA SALIDA <=> DEVOLUCIONES", None))
        self.lndt_typeword.setPlaceholderText(QCoreApplication.translate("tkarded", u"Ingrese el tipo de trabajo", None))
        self.label_6.setText(QCoreApplication.translate("tkarded", u"TIPO DE TRABAJO:", None))
        self.lndt_lote.setPlaceholderText(QCoreApplication.translate("tkarded", u"Lote", None))
        self.observations_ledt.setPlaceholderText(QCoreApplication.translate("tkarded", u"Nombre de proyecto", None))
        self.label_9.setText(QCoreApplication.translate("tkarded", u"OBSERVACIONES:", None))
        self.label_8.setText(QCoreApplication.translate("tkarded", u"RESPONSABLE:", None))
        self.label_7.setText(QCoreApplication.translate("tkarded", u"LOTE:", None))
        self.label_5.setText(QCoreApplication.translate("tkarded", u"CANTIDAD : ", None))
        self.edit_cantidad.setPlaceholderText(QCoreApplication.translate("tkarded", u"Cantidad no mayor a saldo", None))
        self.label_4.setText(QCoreApplication.translate("tkarded", u"FECHA:", None))
        self.lndt_responsable.setText("")
        self.lndt_responsable.setPlaceholderText(QCoreApplication.translate("tkarded", u"Ingrese el nombre", None))
        self.btn_addmaterial.setText(QCoreApplication.translate("tkarded", u"AGREGAR", None))
        self.btn_out_material.setText(QCoreApplication.translate("tkarded", u"SALIDAS", None))
        self.btn_add_devoluciones.setText(QCoreApplication.translate("tkarded", u"DEVOLUCIONES", None))
    # retranslateUi

