# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuadro_mensajeHsaQod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_cuadro(object):
    def setupUi(self, add_cuadro):
        if not add_cuadro.objectName():
            add_cuadro.setObjectName(u"add_cuadro")
        add_cuadro.resize(406, 494)
        self.frame = QFrame(add_cuadro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 401, 471))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 147, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 3px solid rgb(0, 0, 0) ;\n"
"border-radius:5px;\n"
"}\n"
"QLabel{\n"
"background-color:rgba(0,0,0,0%);\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"	background-color: rgb(170, 255, 255);\n"
"	background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_call_list = QPushButton(self.frame)
        self.btn_call_list.setObjectName(u"btn_call_list")
        self.btn_call_list.setGeometry(QRect(30, 210, 341, 50))
        self.btn_call_list.setMinimumSize(QSize(0, 50))
        self.btn_call_list.setMaximumSize(QSize(16777215, 50))
        self.btn_call_list.setSizeIncrement(QSize(0, 50))
        self.btn_view_list = QPushButton(self.frame)
        self.btn_view_list.setObjectName(u"btn_view_list")
        self.btn_view_list.setGeometry(QRect(30, 150, 341, 50))
        self.btn_view_list.setMinimumSize(QSize(0, 50))
        self.btn_view_list.setSizeIncrement(QSize(0, 50))
        self.btn_delete_project = QPushButton(self.frame)
        self.btn_delete_project.setObjectName(u"btn_delete_project")
        self.btn_delete_project.setGeometry(QRect(30, 340, 341, 50))
        self.btn_delete_project.setMinimumSize(QSize(0, 50))
        self.btn_delete_project.setMaximumSize(QSize(16777215, 50))
        self.btn_delete_project.setSizeIncrement(QSize(0, 50))
        self.btn_actividades = QPushButton(self.frame)
        self.btn_actividades.setObjectName(u"btn_actividades")
        self.btn_actividades.setGeometry(QRect(30, 280, 341, 50))
        self.btn_actividades.setMinimumSize(QSize(0, 50))
        self.btn_actividades.setMaximumSize(QSize(16777215, 50))
        self.btn_actividades.setSizeIncrement(QSize(0, 50))
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 60, 361, 71))
        font = QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"background-color:rgba(0,0,0,0%);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.btn_decline = QPushButton(self.frame)
        self.btn_decline.setObjectName(u"btn_decline")
        self.btn_decline.setGeometry(QRect(120, 410, 161, 41))
        self.label_code_project = QLabel(self.frame)
        self.label_code_project.setObjectName(u"label_code_project")
        self.label_code_project.setGeometry(QRect(70, 20, 271, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_code_project.setFont(font1)
        self.label_code_project.setAlignment(Qt.AlignCenter)

        self.retranslateUi(add_cuadro)

        QMetaObject.connectSlotsByName(add_cuadro)
    # setupUi

    def retranslateUi(self, add_cuadro):
        add_cuadro.setWindowTitle(QCoreApplication.translate("add_cuadro", u"Form", None))
        self.btn_call_list.setText(QCoreApplication.translate("add_cuadro", u"Llamar asistencia", None))
        self.btn_view_list.setText(QCoreApplication.translate("add_cuadro", u"Ver lista", None))
        self.btn_delete_project.setText(QCoreApplication.translate("add_cuadro", u"Eliminar proyecto", None))
        self.btn_actividades.setText(QCoreApplication.translate("add_cuadro", u"Actividades", None))
        self.label_title.setText(QCoreApplication.translate("add_cuadro", u"el desarrollo de una persona\n"
" normal en tiempor de covid", None))
        self.btn_decline.setText(QCoreApplication.translate("add_cuadro", u"Cancelar", None))
        self.label_code_project.setText(QCoreApplication.translate("add_cuadro", u"TextLabel", None))
    # retranslateUi

