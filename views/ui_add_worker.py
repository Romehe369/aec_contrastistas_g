# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_workerZOFFxN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_add_Trabajador(object):
    def setupUi(self, Dialog_add_Trabajador):
        if not Dialog_add_Trabajador.objectName():
            Dialog_add_Trabajador.setObjectName(u"Dialog_add_Trabajador")
        Dialog_add_Trabajador.resize(644, 542)
        font = QFont()
        font.setPointSize(11)
        Dialog_add_Trabajador.setFont(font)
        Dialog_add_Trabajador.setStyleSheet(u"")
        self.frame_3 = QFrame(Dialog_add_Trabajador)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 641, 531))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(144, 144, 144);\n"
"	border: 5px solid rgb(0, 0, 127);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDateEdit{\n"
"background-color: white;\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lblCelular = QLabel(self.frame_3)
        self.lblCelular.setObjectName(u"lblCelular")
        self.lblCelular.setGeometry(QRect(330, 400, 151, 31))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.lblCelular.setFont(font1)
        self.img_dni = QLabel(self.frame_3)
        self.img_dni.setObjectName(u"img_dni")
        self.img_dni.setGeometry(QRect(340, 90, 281, 191))
        self.img_dni.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 60, 111, 21))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_agregar_categoria = QPushButton(self.frame_3)
        self.btn_agregar_categoria.setObjectName(u"btn_agregar_categoria")
        self.btn_agregar_categoria.setGeometry(QRect(220, 400, 41, 31))
        self.btn_agregar_categoria.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0,0,0,0%);\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_categoria.setIcon(icon)
        self.btn_agregar_categoria.setIconSize(QSize(32, 32))
        self.lblCategoria = QLabel(self.frame_3)
        self.lblCategoria.setObjectName(u"lblCategoria")
        self.lblCategoria.setGeometry(QRect(30, 370, 111, 21))
        self.lblCategoria.setFont(font1)
        self.lineEdit_celular = QLineEdit(self.frame_3)
        self.lineEdit_celular.setObjectName(u"lineEdit_celular")
        self.lineEdit_celular.setGeometry(QRect(330, 430, 281, 31))
        self.lineEdit_celular.setFont(font1)
        self.lineEdit_celular.setMaxLength(9)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(350, 290, 261, 51))
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_cargar = QPushButton(self.frame_2)
        self.pushButton_cargar.setObjectName(u"pushButton_cargar")
        self.pushButton_cargar.setMinimumSize(QSize(0, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_cargar.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_cargar)

        self.pushButton_delete = QPushButton(self.frame_2)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(0, 31))
        self.pushButton_delete.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_delete)

        self.btn_aceptar = QPushButton(self.frame_3)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(150, 480, 141, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.btn_aceptar.setFont(font3)
        self.btn_aceptar.setAutoFillBackground(False)
        self.lineEditDNI = QLineEdit(self.frame_3)
        self.lineEditDNI.setObjectName(u"lineEditDNI")
        self.lineEditDNI.setGeometry(QRect(30, 80, 251, 31))
        self.lineEditDNI.setFont(font1)
        self.lineEditDNI.setMaxLength(8)
        self.label_fecha_inicio = QLabel(self.frame_3)
        self.label_fecha_inicio.setObjectName(u"label_fecha_inicio")
        self.label_fecha_inicio.setGeometry(QRect(30, 300, 111, 21))
        self.label_fecha_inicio.setFont(font1)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 10, 521, 45))
        self.frame.setStyleSheet(u"QFrame{\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_trabajador = QLabel(self.frame)
        self.label_trabajador.setObjectName(u"label_trabajador")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_trabajador.setFont(font4)
        self.label_trabajador.setStyleSheet(u"")
        self.label_trabajador.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_trabajador)

        self.dateEdit_fecha_init = QDateEdit(self.frame_3)
        self.dateEdit_fecha_init.setObjectName(u"dateEdit_fecha_init")
        self.dateEdit_fecha_init.setGeometry(QRect(30, 330, 181, 31))
        self.dateEdit_fecha_init.setFont(font2)
        self.dateEdit_fecha_init.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.dateEdit_fecha_init.setCalendarPopup(True)
        self.dateEdit_fecha_init.setDate(QDate(2023, 1, 1))
        self.comboBox_categoria = QComboBox(self.frame_3)
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.setObjectName(u"comboBox_categoria")
        self.comboBox_categoria.setGeometry(QRect(30, 400, 181, 31))
        self.comboBox_categoria.setFont(font1)
        self.comboBox_categoria.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.comboBox_sexo = QComboBox(self.frame_3)
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.setObjectName(u"comboBox_sexo")
        self.comboBox_sexo.setGeometry(QRect(30, 260, 181, 31))
        self.comboBox_sexo.setFont(font1)
        self.comboBox_sexo.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.lineEdit_Correo = QLineEdit(self.frame_3)
        self.lineEdit_Correo.setObjectName(u"lineEdit_Correo")
        self.lineEdit_Correo.setGeometry(QRect(330, 370, 281, 31))
        self.lineEdit_Correo.setFont(font1)
        self.label_sexo = QLabel(self.frame_3)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setGeometry(QRect(30, 240, 47, 13))
        self.label_sexo.setFont(font1)
        self.lblDNI = QLabel(self.frame_3)
        self.lblDNI.setObjectName(u"lblDNI")
        self.lblDNI.setGeometry(QRect(30, 60, 47, 13))
        self.lblDNI.setFont(font1)
        self.lblDNI.setStyleSheet(u"")
        self.lblName = QLabel(self.frame_3)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(30, 120, 81, 16))
        self.lblName.setFont(font1)
        self.lblSurname = QLabel(self.frame_3)
        self.lblSurname.setObjectName(u"lblSurname")
        self.lblSurname.setGeometry(QRect(30, 180, 81, 16))
        self.lblSurname.setFont(font1)
        self.lineEditSurname = QLineEdit(self.frame_3)
        self.lineEditSurname.setObjectName(u"lineEditSurname")
        self.lineEditSurname.setGeometry(QRect(30, 200, 251, 31))
        self.lineEditSurname.setFont(font1)
        self.label_correo = QLabel(self.frame_3)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setGeometry(QRect(330, 350, 61, 16))
        self.label_correo.setFont(font1)
        self.lineEditName = QLineEdit(self.frame_3)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(30, 140, 251, 31))
        self.lineEditName.setFont(font1)
        self.btn_cancelar = QPushButton(self.frame_3)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(310, 480, 161, 31))
        self.btn_cancelar.setFont(font3)

        self.retranslateUi(Dialog_add_Trabajador)

        QMetaObject.connectSlotsByName(Dialog_add_Trabajador)
    # setupUi

    def retranslateUi(self, Dialog_add_Trabajador):
        Dialog_add_Trabajador.setWindowTitle(QCoreApplication.translate("Dialog_add_Trabajador", u"Agregar un persona", None))
        self.lblCelular.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Celular o telefono:", None))
        self.img_dni.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"AGREGAR DNI", None))
        self.btn_agregar_categoria.setText("")
        self.lblCategoria.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Categoria", None))
        self.pushButton_cargar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Cargar", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Eliminar", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Aceptar", None))
        self.label_fecha_inicio.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Fecha de inicio", None))
        self.label_trabajador.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Agregar un trabajador", None))
        self.comboBox_categoria.setItemText(0, QCoreApplication.translate("Dialog_add_Trabajador", u"Operario", None))
        self.comboBox_categoria.setItemText(1, QCoreApplication.translate("Dialog_add_Trabajador", u"Ingenerio", None))
        self.comboBox_categoria.setItemText(2, QCoreApplication.translate("Dialog_add_Trabajador", u"Maestro", None))
        self.comboBox_categoria.setItemText(3, QCoreApplication.translate("Dialog_add_Trabajador", u"Ayudante", None))
        self.comboBox_categoria.setItemText(4, QCoreApplication.translate("Dialog_add_Trabajador", u"Oficial", None))

        self.comboBox_sexo.setItemText(0, QCoreApplication.translate("Dialog_add_Trabajador", u"Femenino", None))
        self.comboBox_sexo.setItemText(1, QCoreApplication.translate("Dialog_add_Trabajador", u"Masculino", None))

        self.label_sexo.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Sexo", None))
        self.lblDNI.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"DNI :", None))
        self.lblName.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Nombres:", None))
        self.lblSurname.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Apellidos:", None))
        self.label_correo.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Correo:", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Cancelar", None))
    # retranslateUi

