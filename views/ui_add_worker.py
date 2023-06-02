# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_workerDUUiUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDate)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog_add_Trabajador(object):
    def setupUi(self, Dialog_add_Trabajador):
        if Dialog_add_Trabajador.objectName():
            Dialog_add_Trabajador.setObjectName(u"Dialog_add_Trabajador")
        Dialog_add_Trabajador.resize(613, 509)
        font = QFont()
        font.setPointSize(11)
        Dialog_add_Trabajador.setFont(font)
        Dialog_add_Trabajador.setStyleSheet(u"QLabel{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(144, 144, 144);\n"
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
"}\n"
"QComboBox{\n"
"background-color: white;\n"
"}\n"
"QDateEdit{\n"
"background-color: white;\n"
"}")
        self.lineEditName = QLineEdit(Dialog_add_Trabajador)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(30, 130, 251, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEditName.setFont(font1)
        self.lblCelular = QLabel(Dialog_add_Trabajador)
        self.lblCelular.setObjectName(u"lblCelular")
        self.lblCelular.setGeometry(QRect(330, 380, 111, 21))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.lblCelular.setFont(font2)
        self.comboBox_sexo = QComboBox(Dialog_add_Trabajador)
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.addItem("")
        self.comboBox_sexo.setObjectName(u"comboBox_sexo")
        self.comboBox_sexo.setGeometry(QRect(30, 240, 161, 31))
        self.comboBox_sexo.setFont(font1)
        self.btn_aceptar = QPushButton(Dialog_add_Trabajador)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(150, 460, 141, 31))
        self.btn_aceptar.setFont(font1)
        self.btn_aceptar.setAutoFillBackground(False)
        self.lblSurname = QLabel(Dialog_add_Trabajador)
        self.lblSurname.setObjectName(u"lblSurname")
        self.lblSurname.setGeometry(QRect(30, 160, 61, 16))
        self.lblSurname.setFont(font2)
        self.dateEdit_fecha_init = QDateEdit(Dialog_add_Trabajador)
        self.dateEdit_fecha_init.setObjectName(u"dateEdit_fecha_init")
        self.dateEdit_fecha_init.setGeometry(QRect(30, 310, 161, 31))
        self.dateEdit_fecha_init.setFont(font1)
        self.dateEdit_fecha_init.setCalendarPopup(True)
        self.dateEdit_fecha_init.setDate(QDate(2023, 1, 1))
        self.lblName = QLabel(Dialog_add_Trabajador)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(30, 110, 51, 16))
        self.lblName.setFont(font2)
        self.lineEdit_celular = QLineEdit(Dialog_add_Trabajador)
        self.lineEdit_celular.setObjectName(u"lineEdit_celular")
        self.lineEdit_celular.setGeometry(QRect(330, 410, 251, 21))
        self.lineEdit_celular.setFont(font1)
        self.lineEdit_celular.setMaxLength(9)
        self.lblDNI = QLabel(Dialog_add_Trabajador)
        self.lblDNI.setObjectName(u"lblDNI")
        self.lblDNI.setGeometry(QRect(30, 60, 47, 13))
        self.lblDNI.setFont(font2)
        self.lblDNI.setStyleSheet(u"")
        self.label_fecha_inicio = QLabel(Dialog_add_Trabajador)
        self.label_fecha_inicio.setObjectName(u"label_fecha_inicio")
        self.label_fecha_inicio.setGeometry(QRect(30, 280, 111, 21))
        self.label_fecha_inicio.setFont(font2)
        self.label_sexo = QLabel(Dialog_add_Trabajador)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setGeometry(QRect(30, 220, 47, 13))
        self.label_sexo.setFont(font2)
        self.lineEditSurname = QLineEdit(Dialog_add_Trabajador)
        self.lineEditSurname.setObjectName(u"lineEditSurname")
        self.lineEditSurname.setGeometry(QRect(30, 190, 251, 21))
        self.lineEditSurname.setFont(font1)
        self.label_correo = QLabel(Dialog_add_Trabajador)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setGeometry(QRect(330, 330, 47, 13))
        self.label_correo.setFont(font2)
        self.lineEdit_Correo = QLineEdit(Dialog_add_Trabajador)
        self.lineEdit_Correo.setObjectName(u"lineEdit_Correo")
        self.lineEdit_Correo.setGeometry(QRect(330, 350, 251, 21))
        self.lineEdit_Correo.setFont(font1)
        self.btn_cancelar = QPushButton(Dialog_add_Trabajador)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(310, 460, 161, 31))
        self.btn_cancelar.setFont(font1)
        self.lineEditDNI = QLineEdit(Dialog_add_Trabajador)
        self.lineEditDNI.setObjectName(u"lineEditDNI")
        self.lineEditDNI.setGeometry(QRect(30, 80, 251, 21))
        self.lineEditDNI.setFont(font1)
        self.lineEditDNI.setMaxLength(8)
        self.frame_2 = QFrame(Dialog_add_Trabajador)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 280, 251, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_cargar = QPushButton(self.frame_2)
        self.pushButton_cargar.setObjectName(u"pushButton_cargar")
        self.pushButton_cargar.setGeometry(QRect(10, 10, 75, 23))
        self.pushButton_cambiar = QPushButton(self.frame_2)
        self.pushButton_cambiar.setObjectName(u"pushButton_cambiar")
        self.pushButton_cambiar.setGeometry(QRect(90, 10, 75, 23))
        self.pushButton_delete = QPushButton(self.frame_2)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(170, 10, 75, 23))
        self.img_dni = QLabel(Dialog_add_Trabajador)
        self.img_dni.setObjectName(u"img_dni")
        self.img_dni.setGeometry(QRect(340, 90, 251, 181))
        self.img_dni.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QLabel(Dialog_add_Trabajador)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 60, 111, 21))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(Dialog_add_Trabajador)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 10, 521, 45))
        self.frame.setStyleSheet(u"QFrame{\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
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
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_trabajador.setFont(font3)
        self.label_trabajador.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_trabajador)

        self.lblCategoria = QLabel(Dialog_add_Trabajador)
        self.lblCategoria.setObjectName(u"lblCategoria")
        self.lblCategoria.setGeometry(QRect(30, 350, 111, 21))
        self.lblCategoria.setFont(font2)
        self.comboBox_categoria = QComboBox(Dialog_add_Trabajador)
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.setObjectName(u"comboBox_categoria")
        self.comboBox_categoria.setGeometry(QRect(30, 380, 161, 31))
        self.comboBox_categoria.setFont(font1)

        self.retranslateUi(Dialog_add_Trabajador)

        QMetaObject.connectSlotsByName(Dialog_add_Trabajador)
    # setupUi

    def retranslateUi(self, Dialog_add_Trabajador):
        Dialog_add_Trabajador.setWindowTitle(QCoreApplication.translate("Dialog_add_Trabajador", u"Agregar un persona", None))
        self.lblCelular.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Celular o telefono", None))
        self.comboBox_sexo.setItemText(0, QCoreApplication.translate("Dialog_add_Trabajador", u"Femenino", None))
        self.comboBox_sexo.setItemText(1, QCoreApplication.translate("Dialog_add_Trabajador", u"Masculino", None))

        self.btn_aceptar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Aceptar", None))
        self.lblSurname.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Apellidos", None))
        self.lblName.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Nombre", None))
        self.lblDNI.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"DNI :", None))
        self.label_fecha_inicio.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Fecha de inicio", None))
        self.label_sexo.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Sexo", None))
        self.label_correo.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Correo", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Cancelar", None))
        self.pushButton_cargar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Cargar", None))
        self.pushButton_cambiar.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Cambiar", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Eliminar", None))
        self.img_dni.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"AGREGAR DNI", None))
        self.label_trabajador.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Agregar un trabajador", None))
        self.lblCategoria.setText(QCoreApplication.translate("Dialog_add_Trabajador", u"Categoria", None))
        self.comboBox_categoria.setItemText(0, QCoreApplication.translate("Dialog_add_Trabajador", u"Operario", None))
        self.comboBox_categoria.setItemText(1, QCoreApplication.translate("Dialog_add_Trabajador", u"Ingenerio", None))
        self.comboBox_categoria.setItemText(2, QCoreApplication.translate("Dialog_add_Trabajador", u"Maestro", None))
        self.comboBox_categoria.setItemText(3, QCoreApplication.translate("Dialog_add_Trabajador", u"Ayudante", None))
        self.comboBox_categoria.setItemText(4, QCoreApplication.translate("Dialog_add_Trabajador", u"Oficial", None))

    # retranslateUi

