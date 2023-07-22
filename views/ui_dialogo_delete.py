# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_deletefPOPdg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_delete(object):
    def setupUi(self, Dialog_delete):
        if not Dialog_delete.objectName():
            Dialog_delete.setObjectName(u"Dialog_delete")
        Dialog_delete.resize(360, 268)
        Dialog_delete.setStyleSheet(u"QDialog{\n"
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
        self.btn_alow = QPushButton(Dialog_delete)
        self.btn_alow.setObjectName(u"btn_alow")
        self.btn_alow.setGeometry(QRect(30, 210, 141, 31))
        self.btn_decline = QPushButton(Dialog_delete)
        self.btn_decline.setObjectName(u"btn_decline")
        self.btn_decline.setGeometry(QRect(190, 210, 141, 31))
        self.lbl_mensaje = QLabel(Dialog_delete)
        self.lbl_mensaje.setObjectName(u"lbl_mensaje")
        self.lbl_mensaje.setGeometry(QRect(20, 40, 321, 121))
        font = QFont()
        font.setPointSize(12)
        self.lbl_mensaje.setFont(font)
        self.lbl_mensaje.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_delete)

        QMetaObject.connectSlotsByName(Dialog_delete)
    # setupUi

    def retranslateUi(self, Dialog_delete):
        Dialog_delete.setWindowTitle(QCoreApplication.translate("Dialog_delete", u"Dialog", None))
        self.btn_alow.setText(QCoreApplication.translate("Dialog_delete", u"SI", None))
        self.btn_decline.setText(QCoreApplication.translate("Dialog_delete", u"NO", None))
        self.lbl_mensaje.setText(QCoreApplication.translate("Dialog_delete", u"Una vez eliminado se perdera\n"
"toda la informacion de este proyecto \n"
" \u00bfDesea eliminar?", None))
    # retranslateUi

