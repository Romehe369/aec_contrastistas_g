# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuJEVKcH.ui'
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


class Ui_sistema(object):
    def setupUi(self, sistema):
        if sistema.objectName():
            sistema.setObjectName(u"sistema")
        sistema.resize(914, 789)
        sistema.setMinimumSize(QSize(400, 0))
        sistema.setStyleSheet(u"background-color: rgb(117, 117, 117);")
        self.centralwidget = QWidget(sistema)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 50))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
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
        self.bt_menu.setMinimumSize(QSize(200, 50))
        self.bt_menu.setMaximumSize(QSize(200, 50))
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
        icon.addFile(u"./assets/icons/configuracion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.btn_ocultar = QPushButton(self.frame_superior)
        self.btn_ocultar.setObjectName(u"btn_ocultar")
        self.btn_ocultar.setMinimumSize(QSize(150, 50))
        self.btn_ocultar.setMaximumSize(QSize(200, 50))
        self.btn_ocultar.setSizeIncrement(QSize(200, 50))
        self.btn_ocultar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(117, 117, 117);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_ocultar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_titulo = QLabel(self.frame_superior)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_titulo.setFont(font1)
        self.label_titulo.setStyleSheet(u"color: rgb(170, 255, 0);")

        self.horizontalLayout_2.addWidget(self.label_titulo)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(35, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"\n"
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
        self.bt_restaurar.setMaximumSize(QSize(35, 35))
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
        self.bt_maximizar.setMaximumSize(QSize(35, 35))
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
"\n"
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

        self.btn_registro = QPushButton(self.frame_lateral)
        self.btn_registro.setObjectName(u"btn_registro")
        self.btn_registro.setMinimumSize(QSize(0, 40))
        self.btn_registro.setToolTipDuration(0)
        self.btn_registro.setStyleSheet(u"")
        self.btn_registro.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_registro)

        self.btn_asistencia = QPushButton(self.frame_lateral)
        self.btn_asistencia.setObjectName(u"btn_asistencia")
        self.btn_asistencia.setMinimumSize(QSize(0, 40))
        self.btn_asistencia.setStyleSheet(u"")
        self.btn_asistencia.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_asistencia)

        self.btn_trabajadores = QPushButton(self.frame_lateral)
        self.btn_trabajadores.setObjectName(u"btn_trabajadores")
        self.btn_trabajadores.setMinimumSize(QSize(0, 40))
        self.btn_trabajadores.setStyleSheet(u"")
        self.btn_trabajadores.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_trabajadores)

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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stackedWidget.addWidget(self.page)
        self.page_registro = QWidget()
        self.page_registro.setObjectName(u"page_registro")
        self.page_registro.setStyleSheet(u"QFrame{\n"
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
        self.verticalLayout_4 = QVBoxLayout(self.page_registro)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_registro = QFrame(self.page_registro)
        self.frame_registro.setObjectName(u"frame_registro")
        self.frame_registro.setFrameShape(QFrame.StyledPanel)
        self.frame_registro.setFrameShadow(QFrame.Raised)
        self.frame_registro.setLineWidth(1)
        self.verticalLayout_16 = QVBoxLayout(self.frame_registro)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.frame_registro)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_registro)

        self.frame_4 = QFrame(self.page_registro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:0.386, x2:1, y2:0, stop:0 rgba(116, 157, 152, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 15, 15, 15)
        self.btn_agregar_trabajador = QPushButton(self.frame_4)
        self.btn_agregar_trabajador.setObjectName(u"btn_agregar_trabajador")
        self.btn_agregar_trabajador.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_agregar_trabajador)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.pushButton_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 8)
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
        self.frame_asistencia.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.frame_asistencia.setFrameShape(QFrame.StyledPanel)
        self.frame_asistencia.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_asistencia)

        self.frame_6 = QFrame(self.page_asistencia)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font3 = QFont()
        font3.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.tableWidget.setAutoScrollMargin(16)

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_asistencia)
        self.page_trabajadores = QWidget()
        self.page_trabajadores.setObjectName(u"page_trabajadores")
        self.page_trabajadores.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_6 = QVBoxLayout(self.page_trabajadores)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_trabajador = QFrame(self.page_trabajadores)
        self.frame_trabajador.setObjectName(u"frame_trabajador")
        self.frame_trabajador.setFrameShape(QFrame.StyledPanel)
        self.frame_trabajador.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_trabajador)

        self.frame_tra_contenedor = QFrame(self.page_trabajadores)
        self.frame_tra_contenedor.setObjectName(u"frame_tra_contenedor")
        self.frame_tra_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_tra_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_tra_contenedor)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.table_qwt_new = QTableWidget(self.frame_tra_contenedor)
        if (self.table_qwt_new.columnCount() < 10):
            self.table_qwt_new.setColumnCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255));
        self.table_qwt_new.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font3);
        self.table_qwt_new.setHorizontalHeaderItem(9, __qtablewidgetitem14)
        self.table_qwt_new.setObjectName(u"table_qwt_new")
        self.table_qwt_new.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.table_qwt_new.setAutoScrollMargin(16)

        self.verticalLayout_17.addWidget(self.table_qwt_new)


        self.verticalLayout_6.addWidget(self.frame_tra_contenedor)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_trabajadores)
        self.page_pagos = QWidget()
        self.page_pagos.setObjectName(u"page_pagos")
        self.page_pagos.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_7 = QVBoxLayout(self.page_pagos)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_pagos = QFrame(self.page_pagos)
        self.frame_pagos.setObjectName(u"frame_pagos")
        self.frame_pagos.setFrameShape(QFrame.StyledPanel)
        self.frame_pagos.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_pagos)

        self.frame_10 = QFrame(self.page_pagos)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_10)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 8)
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
        self.frame_reportes.setFrameShape(QFrame.StyledPanel)
        self.frame_reportes.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_reportes)

        self.frame_12 = QFrame(self.page_reportes)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_12)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_reportes)
        self.page_proyectos = QWidget()
        self.page_proyectos.setObjectName(u"page_proyectos")
        self.verticalLayout_10 = QVBoxLayout(self.page_proyectos)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_proyectos = QFrame(self.page_proyectos)
        self.frame_proyectos.setObjectName(u"frame_proyectos")
        self.frame_proyectos.setMaximumSize(QSize(16777215, 100))
        self.frame_proyectos.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:0.386, x2:1, y2:0, stop:0 rgba(116, 157, 152, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.frame_proyectos.setFrameShape(QFrame.StyledPanel)
        self.frame_proyectos.setFrameShadow(QFrame.Raised)
        self.btn_Buscar_pro = QPushButton(self.frame_proyectos)
        self.btn_Buscar_pro.setObjectName(u"btn_Buscar_pro")
        self.btn_Buscar_pro.setGeometry(QRect(370, 20, 131, 51))
        self.lineEdit_buscar_pro = QLineEdit(self.frame_proyectos)
        self.lineEdit_buscar_pro.setObjectName(u"lineEdit_buscar_pro")
        self.lineEdit_buscar_pro.setGeometry(QRect(20, 40, 291, 31))
        self.lineEdit_buscar_pro.setFont(font3)
        self.lineEdit_buscar_pro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame_proyectos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 181, 21))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0%);")

        self.verticalLayout_10.addWidget(self.frame_proyectos)

        self.frame_contenedor_pro = QFrame(self.page_proyectos)
        self.frame_contenedor_pro.setObjectName(u"frame_contenedor_pro")
        self.frame_contenedor_pro.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_contenedor_pro.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor_pro.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_contenedor_pro)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 7)
        self.stackedWidget.addWidget(self.page_proyectos)
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
        self.frame_administrador.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.frame_administrador.setFrameShape(QFrame.StyledPanel)
        self.frame_administrador.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_administrador)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.frame_administrador)
        self.label_5.setObjectName(u"label_5")
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

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_14.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_14.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_14.addWidget(self.pushButton_7)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 8)
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
        self.stackedWidget.setCurrentIndex(6)


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
        self.btn_registro.setText(QCoreApplication.translate("sistema", u"AGREGAR  TRABAJORES \n"
" MATERIALES", None))
        self.btn_asistencia.setText(QCoreApplication.translate("sistema", u"ASISTENCIA", None))
        self.btn_trabajadores.setText(QCoreApplication.translate("sistema", u"TRABAJADORES", None))
        self.btn_pagos.setText(QCoreApplication.translate("sistema", u"PAGOS Y OTROS", None))
        self.btn_reportes.setText(QCoreApplication.translate("sistema", u"REPORTES", None))
        self.btn_admin.setText(QCoreApplication.translate("sistema", u"ADMINISTRADOR", None))
        self.label_2.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS \n"
" GENERALES", None))
        self.label_4.setText(QCoreApplication.translate("sistema", u"Registrar, agregar o eliminar trabajadores", None))
        self.btn_agregar_trabajador.setText(QCoreApplication.translate("sistema", u"\n"
" Aregar un trabajador \n"
"", None))
        self.pushButton_2.setText(QCoreApplication.translate("sistema", u"\n"
" Agregar materiales \n"
"", None))
        self.pushButton_3.setText(QCoreApplication.translate("sistema", u"\n"
" Agregar Adminitrador \n"
"", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sistema", u"Nro", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sistema", u"DNI", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sistema", u"Nombres", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sistema", u"Apellidos", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("sistema", u"Sexo", None));
        ___qtablewidgetitem5 = self.table_qwt_new.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("sistema", u"Fecha", None));
        ___qtablewidgetitem6 = self.table_qwt_new.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("sistema", u"Entradas", None));
        ___qtablewidgetitem7 = self.table_qwt_new.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("sistema", u"Salidas", None));
        ___qtablewidgetitem8 = self.table_qwt_new.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("sistema", u"Devoluciones", None));
        ___qtablewidgetitem9 = self.table_qwt_new.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("sistema", u"Saldo", None));
        ___qtablewidgetitem10 = self.table_qwt_new.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("sistema", u"Tipo de trabajo", None));
        ___qtablewidgetitem11 = self.table_qwt_new.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("sistema", u"Lote", None));
        ___qtablewidgetitem12 = self.table_qwt_new.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("sistema", u"Responsable", None));
        ___qtablewidgetitem13 = self.table_qwt_new.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("sistema", u"Observaciones", None));
        ___qtablewidgetitem14 = self.table_qwt_new.horizontalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("sistema", u"Firma", None));
        self.btn_Buscar_pro.setText(QCoreApplication.translate("sistema", u"Buscar", None))
        self.label_3.setText(QCoreApplication.translate("sistema", u"Nombre del Proyecto :", None))
        self.label_5.setText(QCoreApplication.translate("sistema", u"TextLabel", None))
        self.btn_changes_password.setText(QCoreApplication.translate("sistema", u"\n"
" Cambiar Contrase\u00f1a \n"
"", None))
        self.pushButton_5.setText(QCoreApplication.translate("sistema", u"\n"
" Cambiar Contrase\u00f1a \n"
"", None))
        self.pushButton_6.setText(QCoreApplication.translate("sistema", u"\n"
" Cambiar Contrase\u00f1a \n"
"", None))
        self.pushButton_7.setText(QCoreApplication.translate("sistema", u"\n"
" Cambiar Contrase\u00f1a \n"
"", None))
    # retranslateUi

