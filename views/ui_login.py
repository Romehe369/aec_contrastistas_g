# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logindAEdWd.ui'
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


class Ui_login(object):
    def setupUi(self, login):
        if login.objectName():
            login.setObjectName(u"login")
        login.resize(448, 523)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 5px solid rgb(0, 0, 0) ;\n"
"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 20, 101, 91))
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"border:0px;")
        self.label_4.setPixmap(QPixmap(u"./assets/icons/icono.png"))
        self.label_4.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 130, 431, 41))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Arial\";\n"
"background-color:rgba(0,0,0,0%);\n"
"border:none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.users = QLineEdit(self.frame)
        self.users.setObjectName(u"users")
        self.users.setGeometry(QRect(90, 170, 251, 31))
        self.users.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.users.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(90, 260, 251, 31))
        self.password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.password.setAlignment(Qt.AlignCenter)
        self.bt_ingresar = QPushButton(self.frame)
        self.bt_ingresar.setObjectName(u"bt_ingresar")
        self.bt_ingresar.setGeometry(QRect(120, 330, 171, 41))
        self.bt_ingresar.setStyleSheet(u"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"background-color: rgb(0, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border:4px solid #000000;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}")
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(150, 452, 111, 31))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(83, 152, 255);\n"
"border:1px solid  rgb(83, 152, 255);\n"
"font: 87 10pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border:1px solid  rgb(83, 152, 255);\n"
"background-color:white;\n"
"font: 87 10pt \"Segoe UI Black\"}")
        self.btn_close.setCheckable(True)
        self.btn_close.setChecked(False)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 400, 371, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgba(0,0,0,0%);\n"
"border-radius:25px;\n"
"border: 1px solid #00007f;}\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0.443545, y1:0.517, x2:0.989, y2:0.5, stop:0 rgba(255, 59, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:25px;}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 220, 141, 41))
        self.label.setStyleSheet(u"font: 75 16pt \"Arial\";\n"
"background-color:rgba(0,0,0,0%);\n"
"border:none;")
        self.label.setAlignment(Qt.AlignCenter)
        self.usuario_incorrecto = QLabel(self.frame)
        self.usuario_incorrecto.setObjectName(u"usuario_incorrecto")
        self.usuario_incorrecto.setGeometry(QRect(150, 210, 131, 17))
        self.usuario_incorrecto.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;")
        self.usuario_incorrecto.setAlignment(Qt.AlignCenter)
        self.contrasena_incorrecta = QLabel(self.frame)
        self.contrasena_incorrecta.setObjectName(u"contrasena_incorrecta")
        self.contrasena_incorrecta.setGeometry(QRect(150, 300, 131, 17))
        self.contrasena_incorrecta.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;")
        self.contrasena_incorrecta.setAlignment(Qt.AlignCenter)
        self.cargando = QLabel(self.frame)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(150, 410, 151, 31))
        self.cargando.setStyleSheet(u"QLabel{\n"
"background-color: rgba(0,0,0,0%);\n"
"font: 12pt \"Segoe Print\";\n"
"border:0px;\n"
"}")
        self.cargando.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"Usuario", None))
        self.users.setPlaceholderText(QCoreApplication.translate("login", u"Ingrese su correo", None))
        self.password.setPlaceholderText(QCoreApplication.translate("login", u"Ingrese su contrase\u00f1a", None))
        self.bt_ingresar.setText(QCoreApplication.translate("login", u"Iniciar sesi\u00f3n", None))
        self.btn_close.setText(QCoreApplication.translate("login", u"Salir", None))
        self.label.setText(QCoreApplication.translate("login", u"Contrase\u00f1a", None))
        self.usuario_incorrecto.setText("")
        self.contrasena_incorrecta.setText("")
        self.cargando.setText("")
    # retranslateUi

