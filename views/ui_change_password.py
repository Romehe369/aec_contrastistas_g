# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_passwordxTKKNA.ui'
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


class Ui_changes_password(object):
    def setupUi(self, changes_password):
        if changes_password.objectName():
            changes_password.setObjectName(u"changes_password")
        changes_password.resize(353, 415)
        changes_password.setStyleSheet(u"")
        self.frame_contenedor = QFrame(changes_password)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setGeometry(QRect(0, 0, 353, 415))
        self.frame_contenedor.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(0, 0, 0) ;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"	border: 0px ;\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgba( 255, 255, 255, 0% );\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(83, 152, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(0, 0, 0) ;\n"
"font: 87 10pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"border:1px solid rgb(0, 0, 0) ;\n"
"background-color:white;\n"
"font: 87 10pt \"Segoe UI Black\"}")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.frame_superior = QFrame(self.frame_contenedor)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setGeometry(QRect(1, 1, 351, 46))
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 331, 25))
        self.label.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_control = QFrame(self.frame_contenedor)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setGeometry(QRect(1, 47, 351, 367))
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.btn_cancelar = QPushButton(self.frame_control)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(190, 300, 130, 32))
        self.new_password = QLineEdit(self.frame_control)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setGeometry(QRect(30, 120, 280, 32))
        self.new_password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.new_password.setAlignment(Qt.AlignCenter)
        self.confirm_new_password = QLineEdit(self.frame_control)
        self.confirm_new_password.setObjectName(u"confirm_new_password")
        self.confirm_new_password.setGeometry(QRect(30, 200, 280, 32))
        self.confirm_new_password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.confirm_new_password.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_control)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 331, 31))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.frame_control)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 50, 280, 32))
        self.password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.password.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 331, 31))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 89, 331, 31))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.btn_aceptar = QPushButton(self.frame_control)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(30, 300, 130, 32))
        self.confirm_contrasena_incorrecta = QLabel(self.frame_control)
        self.confirm_contrasena_incorrecta.setObjectName(u"confirm_contrasena_incorrecta")
        self.confirm_contrasena_incorrecta.setGeometry(QRect(40, 250, 261, 21))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.confirm_contrasena_incorrecta.setFont(font)
        self.confirm_contrasena_incorrecta.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.confirm_contrasena_incorrecta.setAlignment(Qt.AlignCenter)

        self.retranslateUi(changes_password)

        QMetaObject.connectSlotsByName(changes_password)
    # setupUi

    def retranslateUi(self, changes_password):
        changes_password.setWindowTitle(QCoreApplication.translate("changes_password", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("changes_password", u"Cambiar contrase\u00f1a", None))
        self.btn_cancelar.setText(QCoreApplication.translate("changes_password", u"Cancelar", None))
        self.new_password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Ingrese  contrase\u00f1a nueva", None))
        self.confirm_new_password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Confirma la nueva contrase\u00f1a", None))
        self.label_2.setText(QCoreApplication.translate("changes_password", u"Contrase\u00f1a antigua :", None))
        self.password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Escriba la contrase\u00f1a anterior", None))
        self.label_4.setText(QCoreApplication.translate("changes_password", u"Confirmar contrase\u00f1a :", None))
        self.label_3.setText(QCoreApplication.translate("changes_password", u"Contrase\u00f1a nueva :", None))
        self.btn_aceptar.setText(QCoreApplication.translate("changes_password", u"Aceptar", None))
        self.confirm_contrasena_incorrecta.setText("")
    # retranslateUi

