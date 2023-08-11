# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuZTICCg.ui'
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
        sistema.resize(1193, 560)
        sistema.setMinimumSize(QSize(0, 0))
        sistema.setMaximumSize(QSize(16777215, 16777215))
        sistema.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(sistema)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
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
        icon.addFile(u"./assets/menu.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"./assets/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"./assets/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"./assets/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u"./assets/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_proyectos = QPushButton(self.frame_lateral)
        self.btn_proyectos.setObjectName(u"btn_proyectos")
        self.btn_proyectos.setMinimumSize(QSize(0, 40))
        self.btn_proyectos.setStyleSheet(u"")
        self.btn_proyectos.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.btn_proyectos)

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

        self.btn_asistencia = QPushButton(self.frame_lateral)
        self.btn_asistencia.setObjectName(u"btn_asistencia")
        self.btn_asistencia.setMinimumSize(QSize(0, 40))
        self.btn_asistencia.setStyleSheet(u"")
        self.btn_asistencia.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_asistencia)

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
        self.pages = QStackedWidget(self.frame_contenedor)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.pages.setFrameShape(QFrame.NoFrame)
        self.pages.setFrameShadow(QFrame.Plain)
        self.pages.setLineWidth(0)
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setStyleSheet(u"background-color: rgb(29, 151, 202);")
        self.verticalLayout_16 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.page_inicio)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_28)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_name_welcome = QLabel(self.frame_28)
        self.lbl_name_welcome.setObjectName(u"lbl_name_welcome")
        self.lbl_name_welcome.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbl_name_welcome.setFont(font3)
        self.lbl_name_welcome.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 255);")
        self.lbl_name_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_name_welcome)

        self.label_50 = QLabel(self.frame_28)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 255);")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_50)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_49 = QLabel(self.frame_29)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(300, 300))
        self.label_49.setMaximumSize(QSize(16777215, 16777215))
        self.label_49.setPixmap(QPixmap(u"./assets/icono.png"))
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_49.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.label_49)


        self.verticalLayout_6.addWidget(self.frame_29)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_mensaje_show = QLabel(self.frame_28)
        self.lbl_mensaje_show.setObjectName(u"lbl_mensaje_show")
        self.lbl_mensaje_show.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.lbl_mensaje_show.setFont(font5)
        self.lbl_mensaje_show.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 0);")
        self.lbl_mensaje_show.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_mensaje_show)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_16.addWidget(self.frame_28)

        self.pages.addWidget(self.page_inicio)
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
        self.verticalLayout_34.setContentsMargins(70, -1, 70, -1)
        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 40))
        self.label_38.setStyleSheet(u"background-color: rgb(255, 240, 125);")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_38)

        self.label_42 = QLabel(self.frame_26)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_42)

        self.frame_25 = QFrame(self.frame_26)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 32))
        self.frame_25.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_dni_admin = QLineEdit(self.frame_25)
        self.lineEdit_dni_admin.setObjectName(u"lineEdit_dni_admin")
        self.lineEdit_dni_admin.setMinimumSize(QSize(0, 31))
        self.lineEdit_dni_admin.setStyleSheet(u"border-radius:3px;")
        self.lineEdit_dni_admin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lineEdit_dni_admin)

        self.btn_search_iddni = QPushButton(self.frame_25)
        self.btn_search_iddni.setObjectName(u"btn_search_iddni")
        self.btn_search_iddni.setMinimumSize(QSize(200, 31))

        self.horizontalLayout_18.addWidget(self.btn_search_iddni)


        self.verticalLayout_34.addWidget(self.frame_25)

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

        self.label_validate_users = QLabel(self.frame_26)
        self.label_validate_users.setObjectName(u"label_validate_users")
        self.label_validate_users.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_validate_users.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_validate_users)

        self.label_41 = QLabel(self.frame_26)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_41)

        self.lndt_add_password = QLineEdit(self.frame_26)
        self.lndt_add_password.setObjectName(u"lndt_add_password")
        self.lndt_add_password.setMinimumSize(QSize(0, 31))
        self.lndt_add_password.setEchoMode(QLineEdit.Normal)
        self.lndt_add_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.lndt_add_password)

        self.label_validate = QLabel(self.frame_26)
        self.label_validate.setObjectName(u"label_validate")
        self.label_validate.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_validate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_validate)

        self.label_43 = QLabel(self.frame_26)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 0))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_43)

        self.lndt_confirm_password_new = QLineEdit(self.frame_26)
        self.lndt_confirm_password_new.setObjectName(u"lndt_confirm_password_new")
        self.lndt_confirm_password_new.setMinimumSize(QSize(0, 31))
        self.lndt_confirm_password_new.setEchoMode(QLineEdit.Normal)
        self.lndt_confirm_password_new.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.lndt_confirm_password_new)

        self.label_confirmation = QLabel(self.frame_26)
        self.label_confirmation.setObjectName(u"label_confirmation")
        self.label_confirmation.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_confirmation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_confirmation)

        self.btn_add_confirm_admin = QPushButton(self.frame_26)
        self.btn_add_confirm_admin.setObjectName(u"btn_add_confirm_admin")
        self.btn_add_confirm_admin.setMinimumSize(QSize(0, 40))

        self.verticalLayout_34.addWidget(self.btn_add_confirm_admin)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_11)


        self.horizontalLayout_14.addWidget(self.frame_26)


        self.verticalLayout_32.addWidget(self.add_admin_frame)


        self.verticalLayout_9.addWidget(self.frame_23)

        self.pages.addWidget(self.page_add_administrator)
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
        self.frame.setMaximumSize(QSize(16777215, 40))
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

        self.btn_add_options = QPushButton(self.frame)
        self.btn_add_options.setObjectName(u"btn_add_options")
        self.btn_add_options.setMinimumSize(QSize(0, 35))
        self.btn_add_options.setMaximumSize(QSize(16777215, 35))
        self.btn_add_options.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.btn_add_options)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"}\n"
"QCalendarWidget QWidget {\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color : lightgreen;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    /* delete default icons */\n"
"    min-width: 50px;\n"
"    max-height: 33px;\n"
"	/* set background transparent */\n"
"}\n"
"#qt_calendar_navigationbar {\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	width: 110px;\n"
"	height: 31px;\n"
"}\n"
"#qt_calendar_yearbutton {\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	width: 70px;\n"
"	height: 31px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setStyleSheet(u"QLabel{\n"
"border: 0px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setSpacing(9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_mothn = QComboBox(self.frame_5)
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.addItem("")
        self.comboBox_mothn.setObjectName(u"comboBox_mothn")
        self.comboBox_mothn.setMinimumSize(QSize(0, 31))
        self.comboBox_mothn.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.comboBox_mothn, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 31))
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_30, 4, 2, 1, 1)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 31))
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_31, 0, 2, 1, 1)

        self.lineEdit_25 = QLineEdit(self.frame_5)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(0, 31))
        font6 = QFont()
        font6.setPointSize(12)
        self.lineEdit_25.setFont(font6)

        self.gridLayout_3.addWidget(self.lineEdit_25, 2, 3, 1, 1)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 31))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 31))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_14.setFont(font7)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 31))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 31))
        self.lineEdit_11.setFont(font6)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 31))
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_29, 3, 2, 1, 1)

        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 31))
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_28, 5, 2, 1, 1)

        self.lineEdit_24 = QLineEdit(self.frame_5)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(0, 31))
        self.lineEdit_24.setFont(font6)

        self.gridLayout_3.addWidget(self.lineEdit_24, 5, 3, 1, 1)

        self.lineEdit_23 = QLineEdit(self.frame_5)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(0, 31))
        self.lineEdit_23.setFont(font6)

        self.gridLayout_3.addWidget(self.lineEdit_23, 0, 3, 1, 1)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 31))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.btn_registrar_ie = QPushButton(self.frame_5)
        self.btn_registrar_ie.setObjectName(u"btn_registrar_ie")
        self.btn_registrar_ie.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.btn_registrar_ie, 6, 3, 1, 1)

        self.cmbbox_egreso = QComboBox(self.frame_5)
        self.cmbbox_egreso.setObjectName(u"cmbbox_egreso")
        self.cmbbox_egreso.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_egreso, 3, 3, 1, 1)

        self.cmbbox_mediopay = QComboBox(self.frame_5)
        self.cmbbox_mediopay.setObjectName(u"cmbbox_mediopay")
        self.cmbbox_mediopay.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_mediopay, 6, 1, 1, 1)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 31))
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_22, 8, 0, 1, 1)

        self.cmbbox_documents = QComboBox(self.frame_5)
        self.cmbbox_documents.setObjectName(u"cmbbox_documents")
        self.cmbbox_documents.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_documents, 1, 1, 1, 1)

        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 31))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_32, 1, 2, 1, 1)

        self.cmbbox_costcenter = QComboBox(self.frame_5)
        self.cmbbox_costcenter.setObjectName(u"cmbbox_costcenter")
        self.cmbbox_costcenter.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_costcenter, 7, 1, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 31))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_20, 6, 0, 1, 1)

        self.cmbbox_rotated = QComboBox(self.frame_5)
        self.cmbbox_rotated.setObjectName(u"cmbbox_rotated")
        self.cmbbox_rotated.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_rotated, 3, 1, 1, 1)

        self.datetime_decline = QDateEdit(self.frame_5)
        self.datetime_decline.setObjectName(u"datetime_decline")
        self.datetime_decline.setMinimumSize(QSize(0, 31))
        self.datetime_decline.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.datetime_decline.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.datetime_decline, 1, 3, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 31))
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_21, 7, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 31))
        self.lineEdit_12.setFont(font6)
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_12, 5, 1, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 31))
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.frame_5)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 31))
        self.lineEdit_20.setFont(font6)

        self.gridLayout_3.addWidget(self.lineEdit_20, 4, 3, 1, 1)

        self.date_emision = QDateEdit(self.frame_5)
        self.date_emision.setObjectName(u"date_emision")
        self.date_emision.setMinimumSize(QSize(0, 31))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(9)
        self.date_emision.setFont(font8)
        self.date_emision.setStyleSheet(u"")
        self.date_emision.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.date_emision, 2, 1, 1, 1)

        self.cmbbox_responsable = QComboBox(self.frame_5)
        self.cmbbox_responsable.setObjectName(u"cmbbox_responsable")
        self.cmbbox_responsable.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.cmbbox_responsable, 8, 1, 1, 1)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 31))
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.btn_add_newgasto = QPushButton(self.frame_5)
        self.btn_add_newgasto.setObjectName(u"btn_add_newgasto")
        self.btn_add_newgasto.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.btn_add_newgasto, 9, 1, 1, 1)

        self.label_51 = QLabel(self.frame_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 31))
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_51, 2, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"QLabel{\n"
"border: 0px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setSpacing(9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 0)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_8)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.frame_7)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 31))
        self.lineEdit_22.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_22, 4, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_7)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 31))
        self.lineEdit_17.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_17, 3, 1, 1, 1)

        self.lineEdit_21 = QLineEdit(self.frame_7)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 31))
        self.lineEdit_21.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_21, 0, 1, 1, 1)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_27, 6, 0, 1, 1)

        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_52 = QLabel(self.frame_7)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_52, 4, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.frame_7)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 31))
        self.lineEdit_18.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_18, 5, 1, 1, 1)

        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_26, 5, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.frame_7)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 31))
        self.lineEdit_15.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_7)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 31))
        self.lineEdit_16.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_16, 2, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.frame_7)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 31))
        self.lineEdit_19.setFont(font6)

        self.gridLayout_2.addWidget(self.lineEdit_19, 6, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_2)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_33)

        self.checkBox = QCheckBox(self.frame_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 31))
        self.checkBox.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)

        self.verticalLayout_18.addWidget(self.checkBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_updatemat = QPushButton(self.frame_7)
        self.btn_updatemat.setObjectName(u"btn_updatemat")
        self.btn_updatemat.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_9.addWidget(self.btn_updatemat)

        self.btn_add_newmaterial = QPushButton(self.frame_7)
        self.btn_add_newmaterial.setObjectName(u"btn_add_newmaterial")
        self.btn_add_newmaterial.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_9.addWidget(self.btn_add_newmaterial)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_13.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalLayout_4.setStretch(0, 11)
        self.pages.addWidget(self.page_registro)
        self.page_delete = QWidget()
        self.page_delete.setObjectName(u"page_delete")
        self.page_delete.setStyleSheet(u"QWidget{\n"
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
"}\n"
"QFrame{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(0, 0, 127);\n"
"	border-radius:10px;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.page_delete)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.delete_admin_frame = QFrame(self.page_delete)
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
        self.lndt_delete_id.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lndt_delete_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.lndt_delete_id)

        self.btn_show_admin = QPushButton(self.delete_admin_frame)
        self.btn_show_admin.setObjectName(u"btn_show_admin")
        self.btn_show_admin.setMinimumSize(QSize(0, 40))

        self.verticalLayout_33.addWidget(self.btn_show_admin)

        self.tableWidget_admin = QTableWidget(self.delete_admin_frame)
        if (self.tableWidget_admin.columnCount() < 5):
            self.tableWidget_admin.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_admin.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_admin.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_admin.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_admin.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_admin.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_admin.setObjectName(u"tableWidget_admin")
        self.tableWidget_admin.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_admin.setTextElideMode(Qt.ElideRight)
        self.tableWidget_admin.setRowCount(0)
        self.tableWidget_admin.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_33.addWidget(self.tableWidget_admin)

        self.delete_admin_ctrl_btn = QPushButton(self.delete_admin_frame)
        self.delete_admin_ctrl_btn.setObjectName(u"delete_admin_ctrl_btn")
        self.delete_admin_ctrl_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_33.addWidget(self.delete_admin_ctrl_btn)

        self.verticalSpacer_13 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_13)


        self.verticalLayout_17.addWidget(self.delete_admin_frame)

        self.pages.addWidget(self.page_delete)
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
        self.lbl_title_reportes = QLabel(self.frame_reportes)
        self.lbl_title_reportes.setObjectName(u"lbl_title_reportes")
        self.lbl_title_reportes.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lbl_title_reportes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.lbl_title_reportes)


        self.verticalLayout_8.addWidget(self.frame_reportes)

        self.frame_contenedor_reports = QFrame(self.page_reportes)
        self.frame_contenedor_reports.setObjectName(u"frame_contenedor_reports")
        self.frame_contenedor_reports.setStyleSheet(u"QFrame{\n"
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
"}\n"
"QLineEdit{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_contenedor_reports.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor_reports.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_contenedor_reports)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_9 = QComboBox(self.frame_contenedor_reports)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(200, 31))
        self.comboBox_9.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 255);")

        self.gridLayout.addWidget(self.comboBox_9, 0, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.frame_contenedor_reports)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMinimumSize(QSize(200, 31))
        self.comboBox_11.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 255);")

        self.gridLayout.addWidget(self.comboBox_11, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_contenedor_reports)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.comboBox_10 = QComboBox(self.frame_contenedor_reports)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(200, 31))
        self.comboBox_10.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 255);")

        self.gridLayout.addWidget(self.comboBox_10, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_contenedor_reports)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_contenedor_reports)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_contenedor_reports)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(200, 35))
        self.pushButton_11.setFont(font6)

        self.gridLayout.addWidget(self.pushButton_11, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_contenedor_reports)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(200, 35))
        self.pushButton_10.setFont(font6)

        self.gridLayout.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_contenedor_reports)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(200, 35))
        self.pushButton_8.setFont(font6)

        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 695, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.verticalLayout_8.addWidget(self.frame_contenedor_reports)

        self.verticalLayout_8.setStretch(0, 1)
        self.pages.addWidget(self.page_reportes)
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
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0%);")

        self.horizontalLayout_15.addWidget(self.label_3)

        self.lineEdit_buscar_pro = QLineEdit(self.frame_proyectos)
        self.lineEdit_buscar_pro.setObjectName(u"lineEdit_buscar_pro")
        self.lineEdit_buscar_pro.setFont(font7)
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
        self.pages.addWidget(self.page_proyectos)
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
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_5.setFont(font9)
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
        self.pages.addWidget(self.page_adminstracion)
        self.page_add_combo = QWidget()
        self.page_add_combo.setObjectName(u"page_add_combo")
        self.page_add_combo.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(170, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.page_add_combo)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.table_combo = QTableWidget(self.page_add_combo)
        if (self.table_combo.columnCount() < 6):
            self.table_combo.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_combo.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.table_combo.setObjectName(u"table_combo")
        self.table_combo.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.table_combo)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add_row = QPushButton(self.page_add_combo)
        self.btn_add_row.setObjectName(u"btn_add_row")
        self.btn_add_row.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_4.addWidget(self.btn_add_row)

        self.pushButton_edit = QPushButton(self.page_add_combo)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_4.addWidget(self.pushButton_edit)

        self.btn_save_options = QPushButton(self.page_add_combo)
        self.btn_save_options.setObjectName(u"btn_save_options")
        self.btn_save_options.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_4.addWidget(self.btn_save_options)

        self.btn_returnsave = QPushButton(self.page_add_combo)
        self.btn_returnsave.setObjectName(u"btn_returnsave")
        self.btn_returnsave.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_4.addWidget(self.btn_returnsave)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.pages.addWidget(self.page_add_combo)

        self.verticalLayout_3.addWidget(self.pages)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        sistema.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(sistema)
        self.statusBar.setObjectName(u"statusBar")
        sistema.setStatusBar(self.statusBar)

        self.retranslateUi(sistema)

        self.bt_menu.setDefault(False)
        self.btn_registro.setDefault(False)
        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(sistema)
    # setupUi

    def retranslateUi(self, sistema):
        sistema.setWindowTitle(QCoreApplication.translate("sistema", u"Project", None))
        self.bt_menu.setText(QCoreApplication.translate("sistema", u"    MENU ", None))
        self.btn_ocultar.setText(QCoreApplication.translate("sistema", u"OCULTAR \n"
" ENCABEZADO", None))
        self.label_titulo.setText(QCoreApplication.translate("sistema", u"SISTEMA AEC CONTRATISTAS GENERALES", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.btn_proyectos.setText(QCoreApplication.translate("sistema", u"PROYECTOS", None))
        self.btn_kardex.setText(QCoreApplication.translate("sistema", u"KARDEX", None))
        self.btn_pagos.setText(QCoreApplication.translate("sistema", u"TAREO Y OTROS", None))
        self.btn_reportes.setText(QCoreApplication.translate("sistema", u"REPORTES", None))
        self.btn_registro.setText(QCoreApplication.translate("sistema", u"AGREGAR  TRABAJORES \n"
" MATERIALES", None))
        self.btn_admin.setText(QCoreApplication.translate("sistema", u"ADMINISTRADOR", None))
        self.btn_asistencia.setText(QCoreApplication.translate("sistema", u"CONFIGURACI\u00d3N", None))
        self.label_2.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS \n"
" GENERALES", None))
        self.lbl_name_welcome.setText(QCoreApplication.translate("sistema", u"BIENVENIDO", None))
        self.label_50.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS GENERALES", None))
        self.label_49.setText("")
        self.lbl_mensaje_show.setText("")
        self.label_35.setText(QCoreApplication.translate("sistema", u"Agregar un administrador", None))
        self.label_38.setText(QCoreApplication.translate("sistema", u"Agregar un administrador del sistema:", None))
        self.label_42.setText(QCoreApplication.translate("sistema", u"DNI", None))
        self.lineEdit_dni_admin.setPlaceholderText(QCoreApplication.translate("sistema", u"Ingrese DNI", None))
        self.btn_search_iddni.setText(QCoreApplication.translate("sistema", u"    Buscar por nombre o apellidos    ", None))
        self.label_46.setText(QCoreApplication.translate("sistema", u"Usuario", None))
        self.lineEdit_add_users.setPlaceholderText(QCoreApplication.translate("sistema", u"Ingrese usuario", None))
        self.label_validate_users.setText("")
        self.label_41.setText(QCoreApplication.translate("sistema", u"Contrase\u00f1a", None))
        self.lndt_add_password.setPlaceholderText(QCoreApplication.translate("sistema", u"Ingrese contrase\u00f1a", None))
        self.label_validate.setText("")
        self.label_43.setText(QCoreApplication.translate("sistema", u"Confirmar contrase\u00f1a", None))
        self.lndt_confirm_password_new.setPlaceholderText(QCoreApplication.translate("sistema", u"Confirmar contrase\u00f1a", None))
        self.label_confirmation.setText("")
        self.btn_add_confirm_admin.setText(QCoreApplication.translate("sistema", u"Agregar administrador", None))
        self.btn_agregar_trabajador.setText(QCoreApplication.translate("sistema", u"Aregar un trabajador", None))
        self.pushButton_2.setText(QCoreApplication.translate("sistema", u"Requerimientos de materiales", None))
        self.btn_add_options.setText(QCoreApplication.translate("sistema", u"Agrega opciones", None))
        self.label.setText(QCoreApplication.translate("sistema", u"Registrar egresos y salidas", None))
        self.comboBox_mothn.setItemText(0, QCoreApplication.translate("sistema", u"ENERO", None))
        self.comboBox_mothn.setItemText(1, QCoreApplication.translate("sistema", u"FEBRERO", None))
        self.comboBox_mothn.setItemText(2, QCoreApplication.translate("sistema", u"MARZO", None))
        self.comboBox_mothn.setItemText(3, QCoreApplication.translate("sistema", u"ABRIL", None))
        self.comboBox_mothn.setItemText(4, QCoreApplication.translate("sistema", u"MAYO", None))
        self.comboBox_mothn.setItemText(5, QCoreApplication.translate("sistema", u"JUNIO", None))
        self.comboBox_mothn.setItemText(6, QCoreApplication.translate("sistema", u"JULIO", None))
        self.comboBox_mothn.setItemText(7, QCoreApplication.translate("sistema", u"AGOSTO", None))
        self.comboBox_mothn.setItemText(8, QCoreApplication.translate("sistema", u"SETIEMBRE", None))
        self.comboBox_mothn.setItemText(9, QCoreApplication.translate("sistema", u"OCTUBRE", None))
        self.comboBox_mothn.setItemText(10, QCoreApplication.translate("sistema", u"NOVIEMBRE", None))
        self.comboBox_mothn.setItemText(11, QCoreApplication.translate("sistema", u"DICIEMBRE", None))

        self.label_30.setText(QCoreApplication.translate("sistema", u"Observacion :", None))
        self.label_31.setText(QCoreApplication.translate("sistema", u"Nro de documento :", None))
        self.lineEdit_25.setText(QCoreApplication.translate("sistema", u"18", None))
        self.label_15.setText(QCoreApplication.translate("sistema", u"Tipo de documento :", None))
        self.label_14.setText(QCoreApplication.translate("sistema", u"Mes :", None))
        self.label_19.setText(QCoreApplication.translate("sistema", u"Monto total (S/) :", None))
        self.label_29.setText(QCoreApplication.translate("sistema", u"Tipo de egreso :", None))
        self.label_28.setText(QCoreApplication.translate("sistema", u"Codigo de documento :", None))
        self.label_17.setText(QCoreApplication.translate("sistema", u"Girado A :", None))
        self.btn_registrar_ie.setText(QCoreApplication.translate("sistema", u"Registrar", None))
        self.label_22.setText(QCoreApplication.translate("sistema", u"Responsable :", None))
        self.label_32.setText(QCoreApplication.translate("sistema", u"Fecha de cancelacion :", None))
        self.label_20.setText(QCoreApplication.translate("sistema", u"Medio de pago :", None))
        self.label_21.setText(QCoreApplication.translate("sistema", u"Centro de costo :", None))
        self.label_18.setText(QCoreApplication.translate("sistema", u"Detalle :", None))
        self.label_16.setText(QCoreApplication.translate("sistema", u"Fecha de emision :", None))
        self.btn_add_newgasto.setText(QCoreApplication.translate("sistema", u"Ingresar nuevo gasto", None))
        self.label_51.setText(QCoreApplication.translate("sistema", u"IGV(%):", None))
        self.label_8.setText(QCoreApplication.translate("sistema", u"Registro de materiales", None))
        self.label_23.setText(QCoreApplication.translate("sistema", u"Nombre material :", None))
        self.lineEdit_21.setText("")
        self.label_27.setText(QCoreApplication.translate("sistema", u"Codigo financiero:", None))
        self.label_48.setText(QCoreApplication.translate("sistema", u"Codigo material :", None))
        self.label_52.setText(QCoreApplication.translate("sistema", u"TOTAL :", None))
        self.label_26.setText(QCoreApplication.translate("sistema", u"Guia de remision :", None))
        self.label_25.setText(QCoreApplication.translate("sistema", u"Costo Unitario :", None))
        self.label_24.setText(QCoreApplication.translate("sistema", u"Cantidad:", None))
        self.label_33.setText(QCoreApplication.translate("sistema", u"Se utiliza en fracciones:", None))
        self.checkBox.setText(QCoreApplication.translate("sistema", u"REUTILIZABLE", None))
        self.btn_updatemat.setText(QCoreApplication.translate("sistema", u"ActualizarMaterial", None))
        self.btn_add_newmaterial.setText(QCoreApplication.translate("sistema", u"Nuevo", None))
        self.label_40.setText(QCoreApplication.translate("sistema", u"Eliminar un administrador del sistema o controlador de asistencia en la web", None))
        self.label_44.setText(QCoreApplication.translate("sistema", u"Usuario", None))
        self.btn_show_admin.setText(QCoreApplication.translate("sistema", u"Ver lista de administradores", None))
        ___qtablewidgetitem = self.tableWidget_admin.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sistema", u"DNI", None));
        ___qtablewidgetitem1 = self.tableWidget_admin.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sistema", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget_admin.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sistema", u"Apellidos", None));
        ___qtablewidgetitem3 = self.tableWidget_admin.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sistema", u"Usuario", None));
        ___qtablewidgetitem4 = self.tableWidget_admin.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("sistema", u"Contrase\u00f1a", None));
        self.delete_admin_ctrl_btn.setText(QCoreApplication.translate("sistema", u"Eliminar administrador", None))
        self.lbl_title_reportes.setText(QCoreApplication.translate("sistema", u"Obtenga los datos de trabajadores, materiales o asistencia", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("sistema", u"DNI", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("sistema", u"NOMBRES", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("sistema", u"APELLIDOS", None))

        self.comboBox_11.setItemText(0, QCoreApplication.translate("sistema", u"CODIGO MATERIAL", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("sistema", u"NOMBRE", None))

        self.comboBox_10.setItemText(0, QCoreApplication.translate("sistema", u"CODIGO PROYECTO", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("sistema", u"NOMBRE", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("sistema", u"RESPONSABLE", None))

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
        ___qtablewidgetitem5 = self.table_combo.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("sistema", u"Tipo de documento ", None));
        ___qtablewidgetitem6 = self.table_combo.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("sistema", u"Girado A ", None));
        ___qtablewidgetitem7 = self.table_combo.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("sistema", u"Medio de pago", None));
        ___qtablewidgetitem8 = self.table_combo.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("sistema", u"Centro de costo", None));
        ___qtablewidgetitem9 = self.table_combo.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("sistema", u"(DNI) Responsable", None));
        ___qtablewidgetitem10 = self.table_combo.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("sistema", u"Tipo de egreso", None));
        self.btn_add_row.setText(QCoreApplication.translate("sistema", u"Agregar una fila", None))
        self.pushButton_edit.setText(QCoreApplication.translate("sistema", u"Editar", None))
        self.btn_save_options.setText(QCoreApplication.translate("sistema", u"Guardar", None))
        self.btn_returnsave.setText(QCoreApplication.translate("sistema", u"RETORNAR", None))
    # retranslateUi

