# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuadro_mensajerRrjnd.ui'
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


class Ui_add_cuadro(object):
    def setupUi(self, add_cuadro):
        if add_cuadro.objectName():
            add_cuadro.setObjectName(u"add_cuadro")
        add_cuadro.resize(360, 468)
        self.frame = QFrame(add_cuadro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 351, 441))
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
        self.btn_call_list.setGeometry(QRect(30, 180, 290, 50))
        self.btn_call_list.setMinimumSize(QSize(0, 50))
        self.btn_call_list.setMaximumSize(QSize(16777215, 50))
        self.btn_call_list.setSizeIncrement(QSize(0, 50))
        self.btn_view_list = QPushButton(self.frame)
        self.btn_view_list.setObjectName(u"btn_view_list")
        self.btn_view_list.setGeometry(QRect(30, 120, 290, 50))
        self.btn_view_list.setMinimumSize(QSize(0, 50))
        self.btn_view_list.setSizeIncrement(QSize(0, 50))
        self.btn_delete_project = QPushButton(self.frame)
        self.btn_delete_project.setObjectName(u"btn_delete_project")
        self.btn_delete_project.setGeometry(QRect(30, 310, 290, 50))
        self.btn_delete_project.setMinimumSize(QSize(0, 50))
        self.btn_delete_project.setMaximumSize(QSize(16777215, 50))
        self.btn_delete_project.setSizeIncrement(QSize(0, 50))
        self.btn_actividades = QPushButton(self.frame)
        self.btn_actividades.setObjectName(u"btn_actividades")
        self.btn_actividades.setGeometry(QRect(30, 250, 290, 50))
        self.btn_actividades.setMinimumSize(QSize(0, 50))
        self.btn_actividades.setMaximumSize(QSize(16777215, 50))
        self.btn_actividades.setSizeIncrement(QSize(0, 50))
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 20, 321, 71))
        self.label_title.setStyleSheet(u"background-color:rgba(0,0,0,0%);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.btn_decline = QPushButton(self.frame)
        self.btn_decline.setObjectName(u"btn_decline")
        self.btn_decline.setGeometry(QRect(100, 380, 161, 41))

        self.retranslateUi(add_cuadro)

        QMetaObject.connectSlotsByName(add_cuadro)
    # setupUi

    def retranslateUi(self, add_cuadro):
        add_cuadro.setWindowTitle(QCoreApplication.translate("add_cuadro", u"Form", None))
        self.btn_call_list.setText(QCoreApplication.translate("add_cuadro", u"Llamar asistencia", None))
        self.btn_view_list.setText(QCoreApplication.translate("add_cuadro", u"Ver lista", None))
        self.btn_delete_project.setText(QCoreApplication.translate("add_cuadro", u"Eliminar proyecto", None))
        self.btn_actividades.setText(QCoreApplication.translate("add_cuadro", u"Actividades", None))
        self.label_title.setText(QCoreApplication.translate("add_cuadro", u"Proyecto", None))
        self.btn_decline.setText(QCoreApplication.translate("add_cuadro", u"Cancelar", None))
    # retranslateUi

