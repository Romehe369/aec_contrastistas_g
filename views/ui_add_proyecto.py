# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_proyectoVvbaBh.ui'
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
        Dialog.resize(320, 361)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(186, 186, 186);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(100, 290, 191, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 451, 61))
        self.frame.setStyleSheet(u"background-color: rgb(121, 121, 121);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 291, 41))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Times New Roman\";")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 47, 13))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 47, 13))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 81, 16))
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 100, 251, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 160, 251, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 220, 161, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 220, 75, 31))

        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Agregar un proyecto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Lugar:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"DNI Responsable", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
    # retranslateUi

