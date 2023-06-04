# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_materialPMWTrw.ui'
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
        Dialog.resize(490, 474)
        Dialog.setStyleSheet(u"QLabel{\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(144, 144, 144);\n"
"}\n"
"QPushButton{\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
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
        self.btn_aceptar = QPushButton(Dialog)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(60, 420, 161, 41))
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(260, 420, 181, 41))
        self.label_trabajador = QLabel(Dialog)
        self.label_trabajador.setObjectName(u"label_trabajador")
        self.label_trabajador.setGeometry(QRect(0, 20, 481, 43))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_trabajador.setFont(font)
        self.label_trabajador.setAlignment(Qt.AlignCenter)
        self.lbl_material = QLabel(Dialog)
        self.lbl_material.setObjectName(u"lbl_material")
        self.lbl_material.setGeometry(QRect(20, 330, 161, 21))
        self.lbl_material.setFont(font)
        self.lineEdit_estado = QLineEdit(Dialog)
        self.lineEdit_estado.setObjectName(u"lineEdit_estado")
        self.lineEdit_estado.setGeometry(QRect(20, 100, 451, 32))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_estado.setFont(font1)
        self.lineEdit_estado.setMaxLength(8)
        self.lbl_tipo = QLabel(Dialog)
        self.lbl_tipo.setObjectName(u"lbl_tipo")
        self.lbl_tipo.setGeometry(QRect(20, 200, 101, 21))
        self.lbl_tipo.setFont(font)
        self.lblDNI = QLabel(Dialog)
        self.lblDNI.setObjectName(u"lblDNI")
        self.lblDNI.setGeometry(QRect(20, 75, 61, 21))
        self.lblDNI.setFont(font)
        self.lblDNI.setStyleSheet(u"")
        self.lbl_fecha = QLabel(Dialog)
        self.lbl_fecha.setObjectName(u"lbl_fecha")
        self.lbl_fecha.setGeometry(QRect(20, 140, 71, 16))
        self.lbl_fecha.setFont(font)
        self.label_precio = QLabel(Dialog)
        self.label_precio.setObjectName(u"label_precio")
        self.label_precio.setGeometry(QRect(20, 270, 91, 16))
        self.label_precio.setFont(font)
        self.lineEdit_fecha = QLineEdit(Dialog)
        self.lineEdit_fecha.setObjectName(u"lineEdit_fecha")
        self.lineEdit_fecha.setGeometry(QRect(20, 160, 451, 32))
        self.lineEdit_fecha.setFont(font1)
        self.lineEdit_tipo = QLineEdit(Dialog)
        self.lineEdit_tipo.setObjectName(u"lineEdit_tipo")
        self.lineEdit_tipo.setGeometry(QRect(20, 230, 451, 32))
        self.lineEdit_tipo.setFont(font1)
        self.lineEdit_precio = QLineEdit(Dialog)
        self.lineEdit_precio.setObjectName(u"lineEdit_precio")
        self.lineEdit_precio.setGeometry(QRect(20, 290, 451, 32))
        self.lineEdit_precio.setFont(font1)
        self.lineEdit_material = QLineEdit(Dialog)
        self.lineEdit_material.setObjectName(u"lineEdit_material")
        self.lineEdit_material.setGeometry(QRect(20, 360, 451, 32))
        self.lineEdit_material.setFont(font1)
        self.lineEdit_material.setMaxLength(9)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_trabajador.setText(QCoreApplication.translate("Dialog", u"Agregar material", None))
        self.lbl_material.setText(QCoreApplication.translate("Dialog", u"Material", None))
        self.lbl_tipo.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
        self.lblDNI.setText(QCoreApplication.translate("Dialog", u"Estado", None))
        self.lbl_fecha.setText(QCoreApplication.translate("Dialog", u"Fecha", None))
        self.label_precio.setText(QCoreApplication.translate("Dialog", u"Precio", None))
    # retranslateUi

