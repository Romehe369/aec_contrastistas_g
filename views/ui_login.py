# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginibUtSt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(411, 350)
        icon = QIcon()
        icon.addFile(u"./assets/icono.png", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(450, 500))
        self.frame.setStyleSheet(u"border: 0px solid rgb(0, 0, 0) ;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setStyleSheet(u"border:none;\n"
"background-color: rgb(51, 0, 102);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 70))
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"border:0px;")
        self.label_4.setPixmap(QPixmap(u"./assets/icono.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:18pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.frame_ctrl = QFrame(self.frame)
        self.frame_ctrl.setObjectName(u"frame_ctrl")
        self.frame_ctrl.setStyleSheet(u"border:none;")
        self.frame_ctrl.setFrameShape(QFrame.StyledPanel)
        self.frame_ctrl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_ctrl)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_ctrl)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 32))
        self.label_2.setStyleSheet(u"font: 75 14pt \"Arial\";\n"
"background-color:rgba(0,0,0,0%);\n"
"border:none;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame_2 = QFrame(self.frame_ctrl)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 35))
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(24, 24))
        self.label_3.setToolTipDuration(-1)
        self.label_3.setStyleSheet(u"border:none;")
        self.label_3.setPixmap(QPixmap(u"./assets/usuario.png"))
        self.label_3.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label_3)

        self.users = QLineEdit(self.frame_2)
        self.users.setObjectName(u"users")
        self.users.setMinimumSize(QSize(0, 31))
        self.users.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.users)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.label = QLabel(self.frame_ctrl)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 32))
        self.label.setStyleSheet(u"font: 75 14pt \"Arial\";\n"
"background-color:rgba(0,0,0,0%);\n"
"border:none;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_ctrl)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 35))
        self.frame_3.setMaximumSize(QSize(16777215, 35))
        self.frame_3.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(24, 24))
        self.label_5.setStyleSheet(u"border:none;")
        self.label_5.setPixmap(QPixmap(u"./assets/contrase\u00f1a.png"))
        self.label_5.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.password = QLineEdit(self.frame_3)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 31))
        self.password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.progressBar = QProgressBar(self.frame_ctrl)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgba(0,0,0,0%);\n"
"border-radius:25px;\n"
"border: none;}\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0.443545, y1:0.517, x2:0.989, y2:0.5, stop:0 rgba(255, 59, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:25px;}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_7.addWidget(self.progressBar)

        self.frame_hac = QFrame(self.frame_ctrl)
        self.frame_hac.setObjectName(u"frame_hac")
        self.frame_hac.setStyleSheet(u"border:none;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_hac)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_ingresar = QPushButton(self.frame_hac)
        self.bt_ingresar.setObjectName(u"bt_ingresar")
        self.bt_ingresar.setMinimumSize(QSize(0, 31))
        self.bt_ingresar.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"background-color: rgb(0, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}")

        self.horizontalLayout_3.addWidget(self.bt_ingresar)

        self.btn_close = QPushButton(self.frame_hac)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 31))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"font: 87 10pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border:1px solid  rgb(83, 152, 255);\n"
"background-color:white;\n"
"font: 87 10pt \"Segoe UI Black\"}")
        self.btn_close.setCheckable(True)
        self.btn_close.setChecked(False)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout_7.addWidget(self.frame_hac)


        self.verticalLayout.addWidget(self.frame_ctrl)

        self.frame_infoaccces = QFrame(self.frame)
        self.frame_infoaccces.setObjectName(u"frame_infoaccces")
        self.frame_infoaccces.setStyleSheet(u"border:none;")
        self.frame_infoaccces.setFrameShape(QFrame.StyledPanel)
        self.frame_infoaccces.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_infoaccces)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_accessclave = QPushButton(self.frame_infoaccces)
        self.btn_accessclave.setObjectName(u"btn_accessclave")
        self.btn_accessclave.setMinimumSize(QSize(0, 31))
        self.btn_accessclave.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"border-radius:0px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(0,0,0,0%);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_accessclave.setIcon(icon1)
        self.btn_accessclave.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.btn_accessclave)

        self.frame_clave = QFrame(self.frame_infoaccces)
        self.frame_clave.setObjectName(u"frame_clave")
        self.frame_clave.setStyleSheet(u"border: none;")
        self.frame_clave.setFrameShape(QFrame.StyledPanel)
        self.frame_clave.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_clave)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lindt_clave = QLineEdit(self.frame_clave)
        self.lindt_clave.setObjectName(u"lindt_clave")
        self.lindt_clave.setMinimumSize(QSize(0, 31))
        self.lindt_clave.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);")
        self.lindt_clave.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lindt_clave)

        self.btn_acceder = QPushButton(self.frame_clave)
        self.btn_acceder.setObjectName(u"btn_acceder")
        self.btn_acceder.setMinimumSize(QSize(0, 31))
        self.btn_acceder.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"background-color: rgb(0, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}")

        self.verticalLayout_5.addWidget(self.btn_acceder)


        self.verticalLayout_6.addWidget(self.frame_clave)


        self.verticalLayout.addWidget(self.frame_infoaccces)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Inicio de administraci\u00f3n", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("login", u"Contratistas Generales E.I.R.L", None))
        self.label_7.setText(QCoreApplication.translate("login", u"Contruimos tu casa, tu construyes el futuro.", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Usuario:", None))
        self.label_3.setText("")
        self.users.setPlaceholderText(QCoreApplication.translate("login", u"Ingrese usuario", None))
        self.label.setText(QCoreApplication.translate("login", u"Contrase\u00f1a:", None))
        self.label_5.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("login", u"Ingrese la contrase\u00f1a", None))
        self.bt_ingresar.setText(QCoreApplication.translate("login", u"Iniciar sesi\u00f3n", None))
        self.btn_close.setText(QCoreApplication.translate("login", u"Cancelar", None))
        self.btn_accessclave.setText(QCoreApplication.translate("login", u"  Ingresar con clave", None))
        self.lindt_clave.setPlaceholderText(QCoreApplication.translate("login", u"XXXXX-XXXXX-XXXXX-XXXXX", None))
        self.btn_acceder.setText(QCoreApplication.translate("login", u"ACCEDER", None))
    # retranslateUi

