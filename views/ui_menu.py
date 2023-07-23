# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuiJyeQz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sistema(object):
    def setupUi(self, sistema):
        if not sistema.objectName():
            sistema.setObjectName(u"sistema")
        sistema.resize(956, 916)
        sistema.setMinimumSize(QSize(400, 0))
        sistema.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(sistema)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(117, 117, 117);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(117, 117, 117);\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.frame_superior.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 40))
        self.bt_menu.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.bt_menu.setFont(font)
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(117, 117, 117);\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.btn_ocultar = QPushButton(self.frame_superior)
        self.btn_ocultar.setObjectName(u"btn_ocultar")
        self.btn_ocultar.setMinimumSize(QSize(150, 40))
        self.btn_ocultar.setMaximumSize(QSize(150, 16777215))
        self.btn_ocultar.setSizeIncrement(QSize(200, 50))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        self.btn_ocultar.setFont(font1)
        self.btn_ocultar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(117, 117, 117);\n"
"font: 87 10pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 10pt \"Arial Black\";\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_ocultar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_titulo = QLabel(self.frame_superior)
        self.label_titulo.setObjectName(u"label_titulo")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_titulo.setFont(font2)
        self.label_titulo.setStyleSheet(u"color: rgb(170, 255, 0);")

        self.horizontalLayout_2.addWidget(self.label_titulo)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(0, 0))
        self.bt_minimizar.setMaximumSize(QSize(35, 16777215))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))
        self.bt_minimizar.setFlat(False)

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(35, 16777215))
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.bt_restaurar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setEnabled(True)
        self.bt_maximizar.setMaximumSize(QSize(35, 16777215))
        self.bt_maximizar.setAutoFillBackground(False)
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:red;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.frame_inferior.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(200, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setToolTipDuration(-1)
        self.frame_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"font: 75 12pt \"Arial Narrow\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-radius:10px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.frame_lateral.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_proyectos = QPushButton(self.frame_lateral)
        self.btn_proyectos.setObjectName(u"btn_proyectos")
        self.btn_proyectos.setMinimumSize(QSize(0, 40))
        self.btn_proyectos.setStyleSheet(u"")
        self.btn_proyectos.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.btn_proyectos)

        self.btn_asistencia = QPushButton(self.frame_lateral)
        self.btn_asistencia.setObjectName(u"btn_asistencia")
        self.btn_asistencia.setMinimumSize(QSize(0, 40))
        self.btn_asistencia.setStyleSheet(u"")
        self.btn_asistencia.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_asistencia)

        self.btn_kardex = QPushButton(self.frame_lateral)
        self.btn_kardex.setObjectName(u"btn_kardex")
        self.btn_kardex.setMinimumSize(QSize(0, 40))
        self.btn_kardex.setStyleSheet(u"")
        self.btn_kardex.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_kardex)

        self.btn_pagos = QPushButton(self.frame_lateral)
        self.btn_pagos.setObjectName(u"btn_pagos")
        self.btn_pagos.setMinimumSize(QSize(0, 40))
        self.btn_pagos.setStyleSheet(u"")
        self.btn_pagos.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_pagos)

        self.btn_reportes = QPushButton(self.frame_lateral)
        self.btn_reportes.setObjectName(u"btn_reportes")
        self.btn_reportes.setMinimumSize(QSize(0, 40))
        self.btn_reportes.setStyleSheet(u"")
        self.btn_reportes.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_reportes)

        self.btn_registro = QPushButton(self.frame_lateral)
        self.btn_registro.setObjectName(u"btn_registro")
        self.btn_registro.setMinimumSize(QSize(0, 40))
        self.btn_registro.setToolTipDuration(0)
        self.btn_registro.setStyleSheet(u"")
        self.btn_registro.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_registro)

        self.btn_admin = QPushButton(self.frame_lateral)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setMinimumSize(QSize(0, 40))
        self.btn_admin.setStyleSheet(u"")
        self.btn_admin.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_admin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_lateral)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.frame_contenedor.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setStyleSheet(u"background-color: rgb(29, 151, 202);")
        self.verticalLayout_16 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.page_inicio)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgba(0,0,0,0%);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_28)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_4 = QLabel(self.frame_28)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_4)

        self.label_50 = QLabel(self.frame_28)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 255);")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_50)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(50, 10, 50, 10)
        self.horizontalSpacer_3 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.label_49 = QLabel(self.frame_29)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u"./assets/icons/icono.png"))

        self.horizontalLayout_17.addWidget(self.label_49)

        self.horizontalSpacer_4 = QSpacerItem(7, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.verticalLayout_36.addWidget(self.frame_29)


        self.verticalLayout_16.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.page_inicio)
        self.page_add_administrator = QWidget()
        self.page_add_administrator.setObjectName(u"page_add_administrator")
        self.page_add_administrator.setStyleSheet(u"QWidget{\n"
"background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.page_add_administrator)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.page_add_administrator)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setMaximumSize(QSize(16777215, 50))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"background-color: rgb(66, 66, 66);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(0, 0, 127);\n"
"	border-radius:10px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_24)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_24)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_35)


        self.verticalLayout_9.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.page_add_administrator)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(0, 0, 127);\n"
"	border-radius:10px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_23)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.add_admin_frame = QFrame(self.frame_23)
        self.add_admin_frame.setObjectName(u"add_admin_frame")
        self.add_admin_frame.setFrameShape(QFrame.StyledPanel)
        self.add_admin_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.add_admin_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.add_admin_frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_26)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 40))
        self.label_38.setStyleSheet(u"background-color: rgb(255, 240, 125);")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_38)

        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_46)

        self.lineEdit_add_users = QLineEdit(self.frame_26)
        self.lineEdit_add_users.setObjectName(u"lineEdit_add_users")
        self.lineEdit_add_users.setMinimumSize(QSize(0, 31))
        self.lineEdit_add_users.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.lineEdit_add_users)

        self.label_41 = QLabel(self.frame_26)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_41)

        self.lndt_add_password = QLineEdit(self.frame_26)
        self.lndt_add_password.setObjectName(u"lndt_add_password")
        self.lndt_add_password.setMinimumSize(QSize(0, 31))
        self.lndt_add_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.lndt_add_password)

        self.btn_add_confirm_admin = QPushButton(self.frame_26)
        self.btn_add_confirm_admin.setObjectName(u"btn_add_confirm_admin")
        self.btn_add_confirm_admin.setMinimumSize(QSize(0, 40))

        self.verticalLayout_34.addWidget(self.btn_add_confirm_admin)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_11)


        self.horizontalLayout_14.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.add_admin_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_25)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_39 = QLabel(self.frame_25)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 40))
        self.label_39.setStyleSheet(u"background-color: rgb(255, 240, 125);")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_39)

        self.label_42 = QLabel(self.frame_25)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_42)

        self.lineEdit_26 = QLineEdit(self.frame_25)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(0, 31))
        self.lineEdit_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.lineEdit_26)

        self.label_43 = QLabel(self.frame_25)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 0))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_43)

        self.lndt_add_cntrls = QLineEdit(self.frame_25)
        self.lndt_add_cntrls.setObjectName(u"lndt_add_cntrls")
        self.lndt_add_cntrls.setMinimumSize(QSize(0, 31))
        self.lndt_add_cntrls.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.lndt_add_cntrls)

        self.add_admin_btn_ctrls = QPushButton(self.frame_25)
        self.add_admin_btn_ctrls.setObjectName(u"add_admin_btn_ctrls")
        self.add_admin_btn_ctrls.setMinimumSize(QSize(0, 40))

        self.verticalLayout_35.addWidget(self.add_admin_btn_ctrls)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_12)


        self.horizontalLayout_14.addWidget(self.frame_25)


        self.verticalLayout_32.addWidget(self.add_admin_frame)

        self.delete_admin_frame = QFrame(self.frame_23)
        self.delete_admin_frame.setObjectName(u"delete_admin_frame")
        self.delete_admin_frame.setMinimumSize(QSize(0, 0))
        self.delete_admin_frame.setFrameShape(QFrame.StyledPanel)
        self.delete_admin_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.delete_admin_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_40 = QLabel(self.delete_admin_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 40))
        self.label_40.setStyleSheet(u"background-color: rgb(255, 240, 125);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_40)

        self.label_44 = QLabel(self.delete_admin_frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_44)

        self.lndt_delete_id = QLineEdit(self.delete_admin_frame)
        self.lndt_delete_id.setObjectName(u"lndt_delete_id")
        self.lndt_delete_id.setMinimumSize(QSize(0, 31))
        self.lndt_delete_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.lndt_delete_id)

        self.delete_admin_ctrl_btn = QPushButton(self.delete_admin_frame)
        self.delete_admin_ctrl_btn.setObjectName(u"delete_admin_ctrl_btn")
        self.delete_admin_ctrl_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_33.addWidget(self.delete_admin_ctrl_btn)

        self.verticalSpacer_13 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_13)


        self.verticalLayout_32.addWidget(self.delete_admin_frame)


        self.verticalLayout_9.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.page_add_administrator)
        self.page_registro = QWidget()
        self.page_registro.setObjectName(u"page_registro")
        self.page_registro.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}\n"
"QComboBox.showPopup{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}\n"
"QDateEdit{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_registro)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_registro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(117, 117, 117);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.btn_agregar_trabajador = QPushButton(self.frame)
        self.btn_agregar_trabajador.setObjectName(u"btn_agregar_trabajador")
        self.btn_agregar_trabajador.setMinimumSize(QSize(0, 35))
        self.btn_agregar_trabajador.setMaximumSize(QSize(16777215, 35))
        self.btn_agregar_trabajador.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.btn_agregar_trabajador)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))
        self.pushButton_2.setMaximumSize(QSize(16777215, 35))
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 35))
        self.pushButton_9.setMaximumSize(QSize(16777215, 35))
        self.pushButton_9.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButton_9)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(800, 0))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 60))
        self.frame_9.setMaximumSize(QSize(16777215, 60))
        self.frame_9.setStyleSheet(u"border: None;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_7)


        self.verticalLayout_19.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setMaximumSize(QSize(170, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, 0, 0)
        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 31))
        self.label_14.setFont(font5)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 31))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 31))
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 31))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 31))
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 31))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 31))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 31))
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 31))
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_22)

        self.verticalSpacer_3 = QSpacerItem(20, 186, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(6, -1, 9, -1)
        self.comboBox = QComboBox(self.frame_15)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 31))
        self.comboBox.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.frame_15)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_2)

        self.date_emision = QDateEdit(self.frame_15)
        self.date_emision.setObjectName(u"date_emision")
        self.date_emision.setMinimumSize(QSize(0, 31))
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(9)
        self.date_emision.setFont(font6)
        self.date_emision.setStyleSheet(u"")
        self.date_emision.setCalendarPopup(True)

        self.verticalLayout_23.addWidget(self.date_emision)

        self.comboBox_3 = QComboBox(self.frame_15)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame_15)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_4)

        self.lineEdit_11 = QLineEdit(self.frame_15)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 31))
        font7 = QFont()
        font7.setPointSize(12)
        self.lineEdit_11.setFont(font7)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.verticalLayout_23.addWidget(self.lineEdit_11)

        self.comboBox_5 = QComboBox(self.frame_15)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.frame_15)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_6)

        self.comboBox_7 = QComboBox(self.frame_15)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.comboBox_7)

        self.pushButton_3 = QPushButton(self.frame_15)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))

        self.verticalLayout_23.addWidget(self.pushButton_3)

        self.verticalSpacer_5 = QSpacerItem(20, 136, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addWidget(self.frame_15)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, 9, -1)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(185, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_31 = QLabel(self.frame_18)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 31))
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_18)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 31))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_32)

        self.label_29 = QLabel(self.frame_18)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 31))
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_18)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 31))
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_30)

        self.label_28 = QLabel(self.frame_18)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 31))
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_28)

        self.verticalSpacer_6 = QSpacerItem(20, 316, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_6)


        self.horizontalLayout_10.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(250, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_17)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.lineEdit_23 = QLineEdit(self.frame_17)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(0, 31))
        self.lineEdit_23.setFont(font7)

        self.verticalLayout_21.addWidget(self.lineEdit_23)

        self.datetime_decline = QDateEdit(self.frame_17)
        self.datetime_decline.setObjectName(u"datetime_decline")
        self.datetime_decline.setMinimumSize(QSize(0, 31))
        self.datetime_decline.setStyleSheet(u"")
        self.datetime_decline.setCalendarPopup(True)

        self.verticalLayout_21.addWidget(self.datetime_decline)

        self.comboBox_8 = QComboBox(self.frame_17)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 31))

        self.verticalLayout_21.addWidget(self.comboBox_8)

        self.lineEdit_20 = QLineEdit(self.frame_17)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 31))
        self.lineEdit_20.setFont(font7)

        self.verticalLayout_21.addWidget(self.lineEdit_20)

        self.lineEdit_24 = QLineEdit(self.frame_17)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(0, 31))
        self.lineEdit_24.setFont(font7)

        self.verticalLayout_21.addWidget(self.lineEdit_24)

        self.pushButton_13 = QPushButton(self.frame_17)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 35))

        self.verticalLayout_21.addWidget(self.pushButton_13)

        self.verticalSpacer_4 = QSpacerItem(20, 275, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addWidget(self.frame_17)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.horizontalLayout_8.setStretch(0, 2)

        self.verticalLayout_19.addWidget(self.frame_11)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setMaximumSize(QSize(350, 16777215))
        self.frame_7.setStyleSheet(u"QLabel{\n"
"border: 0px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_8)

        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_48)

        self.lineEdit_21 = QLineEdit(self.frame_7)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 31))
        self.lineEdit_21.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_21)

        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_23)

        self.lineEdit_15 = QLineEdit(self.frame_7)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 31))
        self.lineEdit_15.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_15)

        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_24)

        self.lineEdit_16 = QLineEdit(self.frame_7)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 31))
        self.lineEdit_16.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_16)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_25)

        self.lineEdit_17 = QLineEdit(self.frame_7)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 31))
        self.lineEdit_17.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_17)

        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_26)

        self.lineEdit_18 = QLineEdit(self.frame_7)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 31))
        self.lineEdit_18.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_18)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_27)

        self.lineEdit_19 = QLineEdit(self.frame_7)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 31))
        self.lineEdit_19.setFont(font7)

        self.verticalLayout_18.addWidget(self.lineEdit_19)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame{\n"
"border: 0xp;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_12 = QPushButton(self.frame_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_7.addWidget(self.pushButton_12)

        self.pushButton_14 = QPushButton(self.frame_8)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_7.addWidget(self.pushButton_14)


        self.verticalLayout_18.addWidget(self.frame_8)

        self.verticalSpacer_2 = QSpacerItem(20, 169, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_13.addWidget(self.frame_3)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 7)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalLayout_4.setStretch(0, 11)
        self.stackedWidget.addWidget(self.page_registro)
        self.page_asistencia = QWidget()
        self.page_asistencia.setObjectName(u"page_asistencia")
        self.page_asistencia.setStyleSheet(u"background-color: rgb(140, 140, 140);")
        self.verticalLayout_5 = QVBoxLayout(self.page_asistencia)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_asistencia = QFrame(self.page_asistencia)
        self.frame_asistencia.setObjectName(u"frame_asistencia")
        self.frame_asistencia.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_asistencia.setFrameShape(QFrame.StyledPanel)
        self.frame_asistencia.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_asistencia)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(70, -1, 70, -1)
        self.label = QLabel(self.frame_asistencia)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_asistencia)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font7)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.btn_search_call_list = QPushButton(self.frame_asistencia)
        self.btn_search_call_list.setObjectName(u"btn_search_call_list")
        self.btn_search_call_list.setEnabled(True)
        self.btn_search_call_list.setMinimumSize(QSize(120, 50))
        self.btn_search_call_list.setMaximumSize(QSize(120, 50))
        self.btn_search_call_list.setSizeIncrement(QSize(120, 50))
        self.btn_search_call_list.setFont(font7)

        self.horizontalLayout_3.addWidget(self.btn_search_call_list)


        self.verticalLayout_5.addWidget(self.frame_asistencia)

        self.frm_asistencia = QFrame(self.page_asistencia)
        self.frm_asistencia.setObjectName(u"frm_asistencia")
        self.frm_asistencia.setFrameShape(QFrame.StyledPanel)
        self.frm_asistencia.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frm_asistencia)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frm_asistencia)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(250, 16777215))
        self.frame_6.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 127);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, -1, 9, -1)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.label_13)

        self.change_code_project = QLabel(self.frame_6)
        self.change_code_project.setObjectName(u"change_code_project")
        self.change_code_project.setMinimumSize(QSize(0, 30))
        self.change_code_project.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.change_code_project)

        self.label_33 = QLabel(self.frame_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.label_33)

        self.change_name_project = QLabel(self.frame_6)
        self.change_name_project.setObjectName(u"change_name_project")
        self.change_name_project.setMinimumSize(QSize(0, 30))
        self.change_name_project.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.change_name_project)

        self.label_37 = QLabel(self.frame_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.label_37)

        self.change_responsible_name = QLabel(self.frame_6)
        self.change_responsible_name.setObjectName(u"change_responsible_name")
        self.change_responsible_name.setMinimumSize(QSize(0, 30))
        self.change_responsible_name.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.change_responsible_name)

        self.label_36 = QLabel(self.frame_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.label_36)

        self.dt_fecha_list = QDateEdit(self.frame_6)
        self.dt_fecha_list.setObjectName(u"dt_fecha_list")
        self.dt_fecha_list.setMinimumSize(QSize(0, 35))
        self.dt_fecha_list.setFont(font5)
        self.dt_fecha_list.setCalendarPopup(True)
        self.dt_fecha_list.setDate(QDate(2023, 1, 1))

        self.verticalLayout_12.addWidget(self.dt_fecha_list)

        self.verticalSpacer_7 = QSpacerItem(20, 137, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)


        self.horizontalLayout_11.addWidget(self.frame_6)

        self.frame_19 = QFrame(self.frm_asistencia)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_19)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.table_asistencia = QTableWidget(self.frame_19)
        if (self.table_asistencia.columnCount() < 6):
            self.table_asistencia.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_asistencia.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_asistencia.setObjectName(u"table_asistencia")
        self.table_asistencia.setStyleSheet(u"")
        self.table_asistencia.setAutoScrollMargin(16)
        self.table_asistencia.setRowCount(0)
        self.table_asistencia.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_25.addWidget(self.table_asistencia)


        self.horizontalLayout_11.addWidget(self.frame_19)


        self.verticalLayout_5.addWidget(self.frm_asistencia)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)
        self.stackedWidget.addWidget(self.page_asistencia)
        self.page_kardex = QWidget()
        self.page_kardex.setObjectName(u"page_kardex")
        self.page_kardex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_6 = QVBoxLayout(self.page_kardex)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_kardex = QFrame(self.page_kardex)
        self.frame_kardex.setObjectName(u"frame_kardex")
        self.frame_kardex.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_kardex.setFrameShape(QFrame.StyledPanel)
        self.frame_kardex.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_kardex)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(70, -1, 70, -1)
        self.label_6 = QLabel(self.frame_kardex)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(160, 50))
        self.label_6.setFont(font7)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.frame_kardex)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font7)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(self.frame_kardex)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QSize(120, 50))
        self.pushButton_4.setMaximumSize(QSize(120, 50))
        self.pushButton_4.setSizeIncrement(QSize(120, 50))
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(108, 241, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_6.addWidget(self.frame_kardex)

        self.frame_kardex_contenedor = QFrame(self.page_kardex)
        self.frame_kardex_contenedor.setObjectName(u"frame_kardex_contenedor")
        self.frame_kardex_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_kardex_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_kardex_contenedor)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.table_qwk_new = QTableWidget(self.frame_kardex_contenedor)
        if (self.table_qwk_new.columnCount() < 11):
            self.table_qwk_new.setColumnCount(11)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font7);
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        self.table_qwk_new.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font7);
        self.table_qwk_new.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        self.table_qwk_new.setObjectName(u"table_qwk_new")
        self.table_qwk_new.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.table_qwk_new.setAutoScrollMargin(16)

        self.verticalLayout_17.addWidget(self.table_qwk_new)


        self.verticalLayout_6.addWidget(self.frame_kardex_contenedor)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 11)
        self.stackedWidget.addWidget(self.page_kardex)
        self.page_pagos = QWidget()
        self.page_pagos.setObjectName(u"page_pagos")
        self.page_pagos.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(153, 153, 153);\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.page_pagos)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_pagos = QFrame(self.page_pagos)
        self.frame_pagos.setObjectName(u"frame_pagos")
        self.frame_pagos.setMaximumSize(QSize(16777215, 52))
        self.frame_pagos.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"QLabel{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_pagos.setFrameShape(QFrame.StyledPanel)
        self.frame_pagos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_pagos)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.label_45 = QLabel(self.frame_pagos)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_12.addWidget(self.label_45)

        self.comboBox_month = QComboBox(self.frame_pagos)
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.setObjectName(u"comboBox_month")
        self.comboBox_month.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_month.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_12.addWidget(self.comboBox_month)

        self.label_47 = QLabel(self.frame_pagos)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_12.addWidget(self.label_47)

        self.lineEdit_year = QLineEdit(self.frame_pagos)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setMaximumSize(QSize(110, 16777215))
        self.lineEdit_year.setMaxLength(4)

        self.horizontalLayout_12.addWidget(self.lineEdit_year)

        self.label_34 = QLabel(self.frame_pagos)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(160, 25))
        self.label_34.setMaximumSize(QSize(16777215, 35))
        self.label_34.setFont(font6)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_34)

        self.lineEdit_6 = QLineEdit(self.frame_pagos)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font6)
        self.lineEdit_6.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.lineEdit_6)

        self.pushButton_15 = QPushButton(self.frame_pagos)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setMinimumSize(QSize(120, 40))
        self.pushButton_15.setMaximumSize(QSize(120, 40))
        self.pushButton_15.setSizeIncrement(QSize(120, 40))
        self.pushButton_15.setFont(font7)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_15)


        self.verticalLayout_7.addWidget(self.frame_pagos)

        self.frame_10 = QFrame(self.page_pagos)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.table_payments = QTableWidget(self.frame_10)
        if (self.table_payments.columnCount() < 11):
            self.table_payments.setColumnCount(11)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_payments.setHorizontalHeaderItem(10, __qtablewidgetitem27)
        self.table_payments.setObjectName(u"table_payments")

        self.verticalLayout_27.addWidget(self.table_payments)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 11)
        self.stackedWidget.addWidget(self.page_pagos)
        self.page_reportes = QWidget()
        self.page_reportes.setObjectName(u"page_reportes")
        self.page_reportes.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_8 = QVBoxLayout(self.page_reportes)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_reportes = QFrame(self.page_reportes)
        self.frame_reportes.setObjectName(u"frame_reportes")
        self.frame_reportes.setMinimumSize(QSize(0, 50))
        self.frame_reportes.setMaximumSize(QSize(16777215, 50))
        self.frame_reportes.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_reportes.setFrameShape(QFrame.StyledPanel)
        self.frame_reportes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_reportes)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_9 = QLabel(self.frame_reportes)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_9)


        self.verticalLayout_8.addWidget(self.frame_reportes)

        self.frame_12 = QFrame(self.page_reportes)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame{\n"
"background-color: rgb(117, 117, 117);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(70, -1, 70, -1)
        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_20)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 40))
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 40))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_12)

        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_10)

        self.verticalSpacer_8 = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_8)


        self.horizontalLayout_13.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_21)
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lineEdit_4 = QLineEdit(self.frame_21)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 31))
        self.lineEdit_4.setFont(font7)

        self.verticalLayout_30.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_21)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 31))
        self.lineEdit_5.setFont(font7)

        self.verticalLayout_30.addWidget(self.lineEdit_5)

        self.lineEdit_3 = QLineEdit(self.frame_21)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 31))
        self.lineEdit_3.setFont(font7)

        self.verticalLayout_30.addWidget(self.lineEdit_3)

        self.verticalSpacer_9 = QSpacerItem(20, 370, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_9)


        self.horizontalLayout_13.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_12)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(200, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_22)
        self.verticalLayout_28.setSpacing(9)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_11 = QPushButton(self.frame_22)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 35))
        self.pushButton_11.setFont(font7)

        self.verticalLayout_28.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_22)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 35))
        self.pushButton_10.setFont(font7)

        self.verticalLayout_28.addWidget(self.pushButton_10)

        self.pushButton_8 = QPushButton(self.frame_22)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 35))
        self.pushButton_8.setFont(font7)

        self.verticalLayout_28.addWidget(self.pushButton_8)

        self.verticalSpacer_10 = QSpacerItem(20, 382, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_10)


        self.horizontalLayout_13.addWidget(self.frame_22)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.verticalLayout_8.setStretch(0, 1)
        self.stackedWidget.addWidget(self.page_reportes)
        self.page_proyectos = QWidget()
        self.page_proyectos.setObjectName(u"page_proyectos")
        self.verticalLayout_10 = QVBoxLayout(self.page_proyectos)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_proyectos = QFrame(self.page_proyectos)
        self.frame_proyectos.setObjectName(u"frame_proyectos")
        self.frame_proyectos.setMaximumSize(QSize(16777215, 50))
        self.frame_proyectos.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_proyectos.setFrameShape(QFrame.StyledPanel)
        self.frame_proyectos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_proyectos)
        self.horizontalLayout_15.setSpacing(9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(70, 0, 70, 0)
        self.label_3 = QLabel(self.frame_proyectos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0%);")

        self.horizontalLayout_15.addWidget(self.label_3)

        self.lineEdit_buscar_pro = QLineEdit(self.frame_proyectos)
        self.lineEdit_buscar_pro.setObjectName(u"lineEdit_buscar_pro")
        self.lineEdit_buscar_pro.setFont(font5)
        self.lineEdit_buscar_pro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_15.addWidget(self.lineEdit_buscar_pro)

        self.btn_agregar_pro = QPushButton(self.frame_proyectos)
        self.btn_agregar_pro.setObjectName(u"btn_agregar_pro")
        self.btn_agregar_pro.setMinimumSize(QSize(150, 40))
        self.btn_agregar_pro.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.btn_agregar_pro)


        self.verticalLayout_10.addWidget(self.frame_proyectos)

        self.frame_contenedor_data = QFrame(self.page_proyectos)
        self.frame_contenedor_data.setObjectName(u"frame_contenedor_data")
        self.frame_contenedor_data.setMinimumSize(QSize(0, 0))
        self.frame_contenedor_data.setStyleSheet(u"background-color: rgb(117, 117, 117);")
        self.frame_contenedor_data.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_contenedor_data)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_contenedor_pro = QFrame(self.frame_contenedor_data)
        self.frame_contenedor_pro.setObjectName(u"frame_contenedor_pro")
        self.frame_contenedor_pro.setMinimumSize(QSize(0, 0))
        self.frame_contenedor_pro.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor_pro.setFrameShadow(QFrame.Raised)
        self.gridLayout_add_frame = QGridLayout(self.frame_contenedor_pro)
        self.gridLayout_add_frame.setObjectName(u"gridLayout_add_frame")
        self.frame_27 = QFrame(self.frame_contenedor_pro)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(30, 146, 255);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.gridLayout_add_frame.addWidget(self.frame_27, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_contenedor_pro)

        self.v_ScrollBar_project = QScrollBar(self.frame_contenedor_data)
        self.v_ScrollBar_project.setObjectName(u"v_ScrollBar_project")
        self.v_ScrollBar_project.setMaximumSize(QSize(16777215, 16777215))
        self.v_ScrollBar_project.setOrientation(Qt.Vertical)

        self.horizontalLayout_16.addWidget(self.v_ScrollBar_project)


        self.verticalLayout_10.addWidget(self.frame_contenedor_data)

        self.verticalLayout_10.setStretch(0, 1)
        self.stackedWidget.addWidget(self.page_proyectos)
        self.frame_contenedor_data.raise_()
        self.frame_proyectos.raise_()
        self.page_adminstracion = QWidget()
        self.page_adminstracion.setObjectName(u"page_adminstracion")
        self.page_adminstracion.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(185, 185, 185);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(185, 185, 185);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.page_adminstracion)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_administrador = QFrame(self.page_adminstracion)
        self.frame_administrador.setObjectName(u"frame_administrador")
        self.frame_administrador.setStyleSheet(u"QFrame{\n"
"background-color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_administrador.setFrameShape(QFrame.StyledPanel)
        self.frame_administrador.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_administrador)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.frame_administrador)
        self.label_5.setObjectName(u"label_5")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_5.setFont(font8)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)


        self.verticalLayout_11.addWidget(self.frame_administrador)

        self.frame_2 = QFrame(self.page_adminstracion)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:0.386, x2:1, y2:0, stop:0 rgba(116, 157, 152, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 87 12pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border:4px solid #000000;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(150, -1, 150, -1)
        self.btn_changes_password = QPushButton(self.frame_2)
        self.btn_changes_password.setObjectName(u"btn_changes_password")

        self.verticalLayout_14.addWidget(self.btn_changes_password)

        self.btn_add_admin_ctrl = QPushButton(self.frame_2)
        self.btn_add_admin_ctrl.setObjectName(u"btn_add_admin_ctrl")

        self.verticalLayout_14.addWidget(self.btn_add_admin_ctrl)

        self.btn_delete_admin_ctrl = QPushButton(self.frame_2)
        self.btn_delete_admin_ctrl.setObjectName(u"btn_delete_admin_ctrl")

        self.verticalLayout_14.addWidget(self.btn_delete_admin_ctrl)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_14.addWidget(self.pushButton_7)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 11)
        self.stackedWidget.addWidget(self.page_adminstracion)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        sistema.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(sistema)
        self.statusBar.setObjectName(u"statusBar")
        sistema.setStatusBar(self.statusBar)

        self.retranslateUi(sistema)

        self.bt_menu.setDefault(False)
        self.btn_registro.setDefault(False)
        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(sistema)
    # setupUi

    def retranslateUi(self, sistema):
        sistema.setWindowTitle(QCoreApplication.translate("sistema", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("sistema", u"    MENU ", None))
        self.btn_ocultar.setText(QCoreApplication.translate("sistema", u"OCULTAR \n"
" ENCABEZADO", None))
        self.label_titulo.setText(QCoreApplication.translate("sistema", u"SISTEMA AEC CONTRATISTAS GENERALES", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.btn_proyectos.setText(QCoreApplication.translate("sistema", u"PROYECTOS", None))
        self.btn_asistencia.setText(QCoreApplication.translate("sistema", u"ASISTENCIA", None))
        self.btn_kardex.setText(QCoreApplication.translate("sistema", u"KARDEX", None))
        self.btn_pagos.setText(QCoreApplication.translate("sistema", u"TAREO Y OTROS", None))
        self.btn_reportes.setText(QCoreApplication.translate("sistema", u"REPORTES", None))
        self.btn_registro.setText(QCoreApplication.translate("sistema", u"AGREGAR  TRABAJORES \n"
" MATERIALES", None))
        self.btn_admin.setText(QCoreApplication.translate("sistema", u"ADMINISTRADOR", None))
        self.label_2.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS \n"
" GENERALES", None))
        self.label_4.setText(QCoreApplication.translate("sistema", u"BIENVENIDO", None))
        self.label_50.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS GENERALES", None))
        self.label_49.setText("")
        self.label_35.setText(QCoreApplication.translate("sistema", u"Agregar un administrador", None))
        self.label_38.setText(QCoreApplication.translate("sistema", u"Agregar un administrador del sistema:", None))
        self.label_46.setText(QCoreApplication.translate("sistema", u"Usuario:", None))
        self.label_41.setText(QCoreApplication.translate("sistema", u"Contrase\u00f1a:", None))
        self.btn_add_confirm_admin.setText(QCoreApplication.translate("sistema", u"Agregar administrador", None))
        self.label_39.setText(QCoreApplication.translate("sistema", u"Agregar un controlador de asistencia en la web:", None))
        self.label_42.setText(QCoreApplication.translate("sistema", u"DNI:", None))
        self.label_43.setText(QCoreApplication.translate("sistema", u"Contrase\u00f1a:", None))
        self.add_admin_btn_ctrls.setText(QCoreApplication.translate("sistema", u"Agregar administrador de asistencia", None))
        self.label_40.setText(QCoreApplication.translate("sistema", u"Eliminar un administrador del sistema o controlador de asistencia en la web", None))
        self.label_44.setText(QCoreApplication.translate("sistema", u"DNI o Usuario", None))
        self.delete_admin_ctrl_btn.setText(QCoreApplication.translate("sistema", u"Eliminar administrador", None))
        self.btn_agregar_trabajador.setText(QCoreApplication.translate("sistema", u"Aregar un trabajador", None))
        self.pushButton_2.setText(QCoreApplication.translate("sistema", u"Requerimientos de materiales", None))
        self.pushButton_9.setText(QCoreApplication.translate("sistema", u"Otros", None))
        self.label_7.setText(QCoreApplication.translate("sistema", u"Registro de ingresos y egresos", None))
        self.label_14.setText(QCoreApplication.translate("sistema", u"Mes :", None))
        self.label_15.setText(QCoreApplication.translate("sistema", u"Tipo de documento :", None))
        self.label_16.setText(QCoreApplication.translate("sistema", u"Fecha de emision :", None))
        self.label_17.setText(QCoreApplication.translate("sistema", u"Girado A :", None))
        self.label_18.setText(QCoreApplication.translate("sistema", u"Detalle :", None))
        self.label_19.setText(QCoreApplication.translate("sistema", u"Monto total (S/) :", None))
        self.label_20.setText(QCoreApplication.translate("sistema", u"Medio de pago :", None))
        self.label_21.setText(QCoreApplication.translate("sistema", u"Centro de costo :", None))
        self.label_22.setText(QCoreApplication.translate("sistema", u"Responsable :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("sistema", u"ENERO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("sistema", u"FEBRERO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("sistema", u"MARZO", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("sistema", u"ABRIL", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("sistema", u"MAYO", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("sistema", u"JUNIO", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("sistema", u"JULIO", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("sistema", u"AGOSTO", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("sistema", u"SETIEMBRE", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("sistema", u"OCTUBRE", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("sistema", u"NOVIEMBRE", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("sistema", u"DICIEMBRE", None))

        self.pushButton_3.setText(QCoreApplication.translate("sistema", u"Ingresar nuevo gasto", None))
        self.label_31.setText(QCoreApplication.translate("sistema", u"Nro de documento :", None))
        self.label_32.setText(QCoreApplication.translate("sistema", u"Fecha de cancelacion :", None))
        self.label_29.setText(QCoreApplication.translate("sistema", u"Tipo de egreso :", None))
        self.label_30.setText(QCoreApplication.translate("sistema", u"Observacion :", None))
        self.label_28.setText(QCoreApplication.translate("sistema", u"Codigo de documento :", None))
        self.pushButton_13.setText(QCoreApplication.translate("sistema", u"Registrar", None))
        self.label_8.setText(QCoreApplication.translate("sistema", u"Registro de materiales", None))
        self.label_48.setText(QCoreApplication.translate("sistema", u"Codigo material :", None))
        self.label_23.setText(QCoreApplication.translate("sistema", u"Nombre material :", None))
        self.label_24.setText(QCoreApplication.translate("sistema", u"Cantidad:", None))
        self.label_25.setText(QCoreApplication.translate("sistema", u"Costo Unitario :", None))
        self.label_26.setText(QCoreApplication.translate("sistema", u"Guia de remision :", None))
        self.label_27.setText(QCoreApplication.translate("sistema", u"Codigo financiero", None))
        self.pushButton_12.setText(QCoreApplication.translate("sistema", u"Nuevo", None))
        self.pushButton_14.setText(QCoreApplication.translate("sistema", u"Actualizar \n"
" Material", None))
        self.label.setText(QCoreApplication.translate("sistema", u"Codigo o nombre \n"
"de Proyecto", None))
        self.btn_search_call_list.setText(QCoreApplication.translate("sistema", u"Buscar", None))
        self.label_13.setText(QCoreApplication.translate("sistema", u"Codigo de proyecto:", None))
        self.change_code_project.setText(QCoreApplication.translate("sistema", u"Proyecto", None))
        self.label_33.setText(QCoreApplication.translate("sistema", u"Nombre del proeyecto:", None))
        self.change_name_project.setText(QCoreApplication.translate("sistema", u"Nombre", None))
        self.label_37.setText(QCoreApplication.translate("sistema", u"Responsable:", None))
        self.change_responsible_name.setText(QCoreApplication.translate("sistema", u"Responsable", None))
        self.label_36.setText(QCoreApplication.translate("sistema", u"Seleccione la fecha:", None))
        ___qtablewidgetitem = self.table_asistencia.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sistema", u"Asistencia", None));
        ___qtablewidgetitem1 = self.table_asistencia.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sistema", u"DNI", None));
        ___qtablewidgetitem2 = self.table_asistencia.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sistema", u"Nombres", None));
        ___qtablewidgetitem3 = self.table_asistencia.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sistema", u"Apellidos", None));
        ___qtablewidgetitem4 = self.table_asistencia.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("sistema", u"Observaci\u00f3n", None));
        ___qtablewidgetitem5 = self.table_asistencia.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("sistema", u"Justificaci\u00f3n", None));
        self.label_6.setText(QCoreApplication.translate("sistema", u"Codigo o nombre \n"
" material", None))
        self.pushButton_4.setText(QCoreApplication.translate("sistema", u"Buscar", None))
        ___qtablewidgetitem6 = self.table_qwk_new.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("sistema", u"Codigo proyecto", None));
        ___qtablewidgetitem7 = self.table_qwk_new.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("sistema", u"Fecha", None));
        ___qtablewidgetitem8 = self.table_qwk_new.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("sistema", u"Entradas", None));
        ___qtablewidgetitem9 = self.table_qwk_new.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("sistema", u"Salidas", None));
        ___qtablewidgetitem10 = self.table_qwk_new.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("sistema", u"Devoluciones", None));
        ___qtablewidgetitem11 = self.table_qwk_new.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("sistema", u"Saldo", None));
        ___qtablewidgetitem12 = self.table_qwk_new.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("sistema", u"Tipo de trabajo", None));
        ___qtablewidgetitem13 = self.table_qwk_new.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("sistema", u"Lote", None));
        ___qtablewidgetitem14 = self.table_qwk_new.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("sistema", u"Responsable", None));
        ___qtablewidgetitem15 = self.table_qwk_new.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("sistema", u"Observaciones", None));
        ___qtablewidgetitem16 = self.table_qwk_new.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("sistema", u"Firma", None));
        self.label_45.setText(QCoreApplication.translate("sistema", u"MES", None))
        self.comboBox_month.setItemText(0, QCoreApplication.translate("sistema", u"ENERO", None))
        self.comboBox_month.setItemText(1, QCoreApplication.translate("sistema", u"FEBRERO", None))
        self.comboBox_month.setItemText(2, QCoreApplication.translate("sistema", u"MARZO", None))
        self.comboBox_month.setItemText(3, QCoreApplication.translate("sistema", u"ABRIL", None))
        self.comboBox_month.setItemText(4, QCoreApplication.translate("sistema", u"MAYO", None))
        self.comboBox_month.setItemText(5, QCoreApplication.translate("sistema", u"JUNIO", None))
        self.comboBox_month.setItemText(6, QCoreApplication.translate("sistema", u"JULIO", None))
        self.comboBox_month.setItemText(7, QCoreApplication.translate("sistema", u"AGOSTO", None))
        self.comboBox_month.setItemText(8, QCoreApplication.translate("sistema", u"SETIEMBRE", None))
        self.comboBox_month.setItemText(9, QCoreApplication.translate("sistema", u"OCTUBRE", None))
        self.comboBox_month.setItemText(10, QCoreApplication.translate("sistema", u"NOVIEMBRE", None))
        self.comboBox_month.setItemText(11, QCoreApplication.translate("sistema", u"DICIEMBRE", None))

        self.label_47.setText(QCoreApplication.translate("sistema", u"A\u00d1O", None))
        self.label_34.setText(QCoreApplication.translate("sistema", u"CODIGO DE PROYECTO", None))
        self.pushButton_15.setText(QCoreApplication.translate("sistema", u"Buscar", None))
        ___qtablewidgetitem17 = self.table_payments.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("sistema", u"DNI", None));
        ___qtablewidgetitem18 = self.table_payments.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("sistema", u"Nombres", None));
        ___qtablewidgetitem19 = self.table_payments.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("sistema", u"Apellidos", None));
        ___qtablewidgetitem20 = self.table_payments.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("sistema", u"Cargo", None));
        ___qtablewidgetitem21 = self.table_payments.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("sistema", u"Salario diario", None));
        ___qtablewidgetitem22 = self.table_payments.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("sistema", u"Total de dias", None));
        ___qtablewidgetitem23 = self.table_payments.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("sistema", u"Total Girar", None));
        ___qtablewidgetitem24 = self.table_payments.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("sistema", u"Adelantos", None));
        ___qtablewidgetitem25 = self.table_payments.horizontalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("sistema", u"Por pagar", None));
        ___qtablewidgetitem26 = self.table_payments.horizontalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("sistema", u"Observaciones", None));
        ___qtablewidgetitem27 = self.table_payments.horizontalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("sistema", u"Estado", None));
        self.label_9.setText(QCoreApplication.translate("sistema", u"Obtenga los datos de trabajadores, materiales o asistencia", None))
        self.label_11.setText(QCoreApplication.translate("sistema", u"Nombres o DNI:", None))
        self.label_12.setText(QCoreApplication.translate("sistema", u"Codigo material \n"
" o nombre :", None))
        self.label_10.setText(QCoreApplication.translate("sistema", u"Codigo proyecto\n"
" o nombre:", None))
        self.pushButton_11.setText(QCoreApplication.translate("sistema", u"Ver detalles", None))
        self.pushButton_10.setText(QCoreApplication.translate("sistema", u"Ver detalles", None))
        self.pushButton_8.setText(QCoreApplication.translate("sistema", u"Ver detalles", None))
        self.label_3.setText(QCoreApplication.translate("sistema", u"C\u00f3digo o nombre del Proyecto :", None))
        self.lineEdit_buscar_pro.setPlaceholderText(QCoreApplication.translate("sistema", u"Escriba el codigo o nombre proyecto", None))
        self.btn_agregar_pro.setText(QCoreApplication.translate("sistema", u"Agregar", None))
        self.label_5.setText(QCoreApplication.translate("sistema", u"Realiza actividades de administrador, \n"
"es necesario introducir contrase\u00f1a", None))
        self.btn_changes_password.setText(QCoreApplication.translate("sistema", u"\n"
" Cambiar Contrase\u00f1a \n"
"", None))
        self.btn_add_admin_ctrl.setText(QCoreApplication.translate("sistema", u"\n"
" Agregar administrador \n"
"", None))
        self.btn_delete_admin_ctrl.setText(QCoreApplication.translate("sistema", u"\n"
" Eliminar administrador \n"
"", None))
        self.pushButton_7.setText(QCoreApplication.translate("sistema", u"\n"
" Generar una copia de seguridad \n"
"", None))
    # retranslateUi

