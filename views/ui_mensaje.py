# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mensajehsSVXF.ui'
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


class Ui_View_Mensaje(object):
    def setupUi(self, View_Mensaje):
        if View_Mensaje.objectName():
            View_Mensaje.setObjectName(u"View_Mensaje")
        View_Mensaje.resize(268, 259)
        View_Mensaje.setStyleSheet(u"QDialog{\n"
"background-color: rgb(138, 138, 138);\n"
"border: 2px solid rgb(0, 0, 0) ;\n"
"}\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
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
        self.pButton_alow = QPushButton(View_Mensaje)
        self.pButton_alow.setObjectName(u"pButton_alow")
        self.pButton_alow.setGeometry(QRect(60, 210, 141, 31))
        self.label_mensaje = QLabel(View_Mensaje)
        self.label_mensaje.setObjectName(u"label_mensaje")
        self.label_mensaje.setGeometry(QRect(20, 20, 231, 161))
        font = QFont()
        font.setPointSize(12)
        self.label_mensaje.setFont(font)
        self.label_mensaje.setAlignment(Qt.AlignCenter)

        self.retranslateUi(View_Mensaje)

        QMetaObject.connectSlotsByName(View_Mensaje)
    # setupUi

    def retranslateUi(self, View_Mensaje):
        View_Mensaje.setWindowTitle(QCoreApplication.translate("View_Mensaje", u"Dialog", None))
        self.pButton_alow.setText(QCoreApplication.translate("View_Mensaje", u"Aceptar", None))
        self.label_mensaje.setText(QCoreApplication.translate("View_Mensaje", u"Ingrese \n"
" su \n"
" texto", None))
    # retranslateUi

