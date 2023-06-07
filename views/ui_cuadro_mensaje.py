# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuadro_mensajeuHuQyO.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(412, 509)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 361, 441))
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
"border-radius:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 160, 271, 50))
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        self.pushButton.setSizeIncrement(QSize(0, 50))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 100, 291, 50))
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setSizeIncrement(QSize(0, 50))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 310, 340, 50))
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setMaximumSize(QSize(16777215, 50))
        self.pushButton_3.setSizeIncrement(QSize(0, 50))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 240, 340, 50))
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setMaximumSize(QSize(16777215, 50))
        self.pushButton_4.setSizeIncrement(QSize(0, 50))
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 30, 321, 41))
        self.label_title.setStyleSheet(u"background-color:rgba(0,0,0,0%);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(100, 380, 161, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Llamar asistencia", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Ver lista", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Eliminar proyecto", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Actividades", None))
        self.label_title.setText(QCoreApplication.translate("Form", u"Proyecto", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

