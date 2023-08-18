# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_workeriPspvW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_Trabajador(object):
    def setupUi(self, add_Trabajador):
        if not add_Trabajador.objectName():
            add_Trabajador.setObjectName(u"add_Trabajador")
        add_Trabajador.resize(906, 653)
        self.centralwidget = QWidget(add_Trabajador)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 35))
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


        self.verticalLayout_4.addWidget(self.frame_superior)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 0, 15, 0)
        self.lblName = QLabel(self.centralwidget)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setMinimumSize(QSize(0, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblName.setFont(font)
        self.lblName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblName, 1, 0, 1, 1)

        self.lblSurname = QLabel(self.centralwidget)
        self.lblSurname.setObjectName(u"lblSurname")
        self.lblSurname.setMinimumSize(QSize(0, 31))
        self.lblSurname.setFont(font)
        self.lblSurname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblSurname, 2, 0, 1, 1)

        self.lineEditName = QLineEdit(self.centralwidget)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setMinimumSize(QSize(0, 31))
        self.lineEditName.setFont(font)

        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)

        self.lineEditSurname = QLineEdit(self.centralwidget)
        self.lineEditSurname.setObjectName(u"lineEditSurname")
        self.lineEditSurname.setMinimumSize(QSize(0, 31))
        self.lineEditSurname.setFont(font)
        self.lineEditSurname.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEditSurname, 2, 1, 1, 1)

        self.comboBox_sexo = QComboBox(self.centralwidget)
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.setObjectName(u"comboBox_sexo")
        self.comboBox_sexo.setMinimumSize(QSize(0, 31))
        self.comboBox_sexo.setFont(font)
        self.comboBox_sexo.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.comboBox_sexo, 3, 1, 1, 1)

        self.lineEditDNI = QLineEdit(self.centralwidget)
        self.lineEditDNI.setObjectName(u"lineEditDNI")
        self.lineEditDNI.setMinimumSize(QSize(0, 31))
        self.lineEditDNI.setFont(font)
        self.lineEditDNI.setMaxLength(8)

        self.gridLayout.addWidget(self.lineEditDNI, 0, 1, 1, 1)

        self.label_sexo = QLabel(self.centralwidget)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setMinimumSize(QSize(0, 31))
        self.label_sexo.setFont(font)
        self.label_sexo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_sexo, 3, 0, 1, 1)

        self.label_fecha_inicio = QLabel(self.centralwidget)
        self.label_fecha_inicio.setObjectName(u"label_fecha_inicio")
        self.label_fecha_inicio.setMinimumSize(QSize(0, 31))
        self.label_fecha_inicio.setFont(font)
        self.label_fecha_inicio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_fecha_inicio, 4, 0, 1, 1)

        self.dateEdit_fecha_init = QDateEdit(self.centralwidget)
        self.dateEdit_fecha_init.setObjectName(u"dateEdit_fecha_init")
        self.dateEdit_fecha_init.setMinimumSize(QSize(0, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.dateEdit_fecha_init.setFont(font1)
        self.dateEdit_fecha_init.setStyleSheet(u"QCalendarWidget QWidget {\n"
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
        self.dateEdit_fecha_init.setCalendarPopup(True)
        self.dateEdit_fecha_init.setDate(QDate(2023, 1, 1))

        self.gridLayout.addWidget(self.dateEdit_fecha_init, 4, 1, 1, 1)

        self.lblDNI = QLabel(self.centralwidget)
        self.lblDNI.setObjectName(u"lblDNI")
        self.lblDNI.setMinimumSize(QSize(0, 31))
        self.lblDNI.setFont(font)
        self.lblDNI.setStyleSheet(u"")
        self.lblDNI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblDNI, 0, 0, 1, 1)

        self.lblCelular = QLabel(self.centralwidget)
        self.lblCelular.setObjectName(u"lblCelular")
        self.lblCelular.setMinimumSize(QSize(0, 31))
        self.lblCelular.setFont(font)
        self.lblCelular.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblCelular, 3, 2, 1, 1)

        self.lineEdit_celular = QLineEdit(self.centralwidget)
        self.lineEdit_celular.setObjectName(u"lineEdit_celular")
        self.lineEdit_celular.setMinimumSize(QSize(0, 31))
        self.lineEdit_celular.setFont(font)
        self.lineEdit_celular.setMaxLength(9)

        self.gridLayout.addWidget(self.lineEdit_celular, 3, 3, 1, 1)

        self.label_correo = QLabel(self.centralwidget)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setMinimumSize(QSize(0, 31))
        self.label_correo.setFont(font)
        self.label_correo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_correo, 2, 2, 1, 1)

        self.lineEdit_Correo = QLineEdit(self.centralwidget)
        self.lineEdit_Correo.setObjectName(u"lineEdit_Correo")
        self.lineEdit_Correo.setMinimumSize(QSize(0, 31))
        self.lineEdit_Correo.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_Correo, 2, 3, 1, 1)

        self.lblCategoria = QLabel(self.centralwidget)
        self.lblCategoria.setObjectName(u"lblCategoria")
        self.lblCategoria.setMinimumSize(QSize(0, 31))
        self.lblCategoria.setFont(font)
        self.lblCategoria.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblCategoria, 0, 2, 1, 1)

        self.comboBox_categoria = QComboBox(self.centralwidget)
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.setObjectName(u"comboBox_categoria")
        self.comboBox_categoria.setMinimumSize(QSize(0, 31))
        self.comboBox_categoria.setFont(font)
        self.comboBox_categoria.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.gridLayout.addWidget(self.comboBox_categoria, 0, 3, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 31))
        self.label_2.setStyleSheet(u"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.lineEdit_salario = QLineEdit(self.centralwidget)
        self.lineEdit_salario.setObjectName(u"lineEdit_salario")
        self.lineEdit_salario.setMinimumSize(QSize(0, 31))
        self.lineEdit_salario.setFont(font)
        self.lineEdit_salario.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_salario, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_sexo_2 = QLabel(self.centralwidget)
        self.label_sexo_2.setObjectName(u"label_sexo_2")
        self.label_sexo_2.setMinimumSize(QSize(0, 31))
        self.label_sexo_2.setMaximumSize(QSize(16777215, 31))
        self.label_sexo_2.setFont(font)
        self.label_sexo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_sexo_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.img_dni = QLabel(self.centralwidget)
        self.img_dni.setObjectName(u"img_dni")
        self.img_dni.setMinimumSize(QSize(400, 300))
        self.img_dni.setMaximumSize(QSize(500, 400))
        self.img_dni.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.img_dni.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_dni)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_cargar = QPushButton(self.centralwidget)
        self.pushButton_cargar.setObjectName(u"pushButton_cargar")
        self.pushButton_cargar.setMinimumSize(QSize(0, 31))
        self.pushButton_cargar.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_cargar)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(0, 31))
        self.pushButton_delete.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_sexo_3 = QLabel(self.centralwidget)
        self.label_sexo_3.setObjectName(u"label_sexo_3")
        self.label_sexo_3.setMinimumSize(QSize(0, 31))
        self.label_sexo_3.setMaximumSize(QSize(16777215, 31))
        self.label_sexo_3.setFont(font)
        self.label_sexo_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_sexo_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.img_dnireverse = QLabel(self.centralwidget)
        self.img_dnireverse.setObjectName(u"img_dnireverse")
        self.img_dnireverse.setMinimumSize(QSize(400, 300))
        self.img_dnireverse.setMaximumSize(QSize(500, 400))
        self.img_dnireverse.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.img_dnireverse.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.img_dnireverse)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_uplouddni = QPushButton(self.centralwidget)
        self.btn_uplouddni.setObjectName(u"btn_uplouddni")
        self.btn_uplouddni.setMinimumSize(QSize(0, 31))
        self.btn_uplouddni.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_uplouddni)

        self.btn_deletere = QPushButton(self.centralwidget)
        self.btn_deletere.setObjectName(u"btn_deletere")
        self.btn_deletere.setMinimumSize(QSize(0, 31))
        self.btn_deletere.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_deletere)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 15, -1)
        self.btn_aceptar = QPushButton(self.centralwidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setFont(font)
        self.btn_aceptar.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.btn_aceptar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        add_Trabajador.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_Trabajador)

        QMetaObject.connectSlotsByName(add_Trabajador)
    # setupUi

    def retranslateUi(self, add_Trabajador):
        add_Trabajador.setWindowTitle(QCoreApplication.translate("add_Trabajador", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("add_Trabajador", u"AGREGAR UN EMPLEADOR Y/O TRABAJDOR", None))
        self.btn_ampliar.setText(QCoreApplication.translate("add_Trabajador", u"\u25a0", None))
        self.btn_close.setText(QCoreApplication.translate("add_Trabajador", u"X", None))
        self.lblName.setText(QCoreApplication.translate("add_Trabajador", u"Nombres:", None))
        self.lblSurname.setText(QCoreApplication.translate("add_Trabajador", u"Apellidos:", None))
        self.lineEditName.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese los nombres", None))
        self.lineEditSurname.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese apellidos", None))
        self.comboBox_sexo.setItemText(0, QCoreApplication.translate("add_Trabajador", u"Femenino", None))
        self.comboBox_sexo.setItemText(1, QCoreApplication.translate("add_Trabajador", u"Masculino", None))

        self.lineEditDNI.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese DNI", None))
        self.label_sexo.setText(QCoreApplication.translate("add_Trabajador", u"Sexo:", None))
        self.label_fecha_inicio.setText(QCoreApplication.translate("add_Trabajador", u"Fecha de inicio", None))
        self.lblDNI.setText(QCoreApplication.translate("add_Trabajador", u"DNI :", None))
        self.lblCelular.setText(QCoreApplication.translate("add_Trabajador", u"Celular o telefono:", None))
        self.lineEdit_celular.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese n\u00famero celular o telef.", None))
        self.label_correo.setText(QCoreApplication.translate("add_Trabajador", u"Correo electronico:", None))
        self.lineEdit_Correo.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese correo electronico", None))
        self.lblCategoria.setText(QCoreApplication.translate("add_Trabajador", u"Categoria:", None))
        self.comboBox_categoria.setItemText(0, QCoreApplication.translate("add_Trabajador", u"Operario", None))
        self.comboBox_categoria.setItemText(1, QCoreApplication.translate("add_Trabajador", u"Ingenerio", None))
        self.comboBox_categoria.setItemText(2, QCoreApplication.translate("add_Trabajador", u"Maestro", None))
        self.comboBox_categoria.setItemText(3, QCoreApplication.translate("add_Trabajador", u"Ayudante", None))
        self.comboBox_categoria.setItemText(4, QCoreApplication.translate("add_Trabajador", u"Oficial", None))

        self.label_2.setText(QCoreApplication.translate("add_Trabajador", u"Salario diario:", None))
        self.lineEdit_salario.setPlaceholderText(QCoreApplication.translate("add_Trabajador", u"Ingrese salario por dia", None))
        self.label_sexo_2.setText(QCoreApplication.translate("add_Trabajador", u"FOTO DNI PRINCIPAL", None))
        self.img_dni.setText("")
        self.pushButton_cargar.setText(QCoreApplication.translate("add_Trabajador", u"Cargar", None))
        self.pushButton_delete.setText(QCoreApplication.translate("add_Trabajador", u"Limpiar", None))
        self.label_sexo_3.setText(QCoreApplication.translate("add_Trabajador", u"FOTO DNI REVERSO", None))
        self.img_dnireverse.setText("")
        self.btn_uplouddni.setText(QCoreApplication.translate("add_Trabajador", u"Cargar", None))
        self.btn_deletere.setText(QCoreApplication.translate("add_Trabajador", u"Limpiar", None))
        self.btn_aceptar.setText(QCoreApplication.translate("add_Trabajador", u"AGREGAR TRABAJADOR", None))
    # retranslateUi

