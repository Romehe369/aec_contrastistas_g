# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuPNBpJm.ui'
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
        sistema.resize(914, 769)
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
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.frame_lateral.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_uno = QPushButton(self.frame_lateral)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setMinimumSize(QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/registrar3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon6)
        self.bt_uno.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_uno)

        self.bt_dos = QPushButton(self.frame_lateral)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setMinimumSize(QSize(0, 40))
        self.bt_dos.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/asistencia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_dos.setIcon(icon7)
        self.bt_dos.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_dos)

        self.bt_tres = QPushButton(self.frame_lateral)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setMinimumSize(QSize(0, 40))
        self.bt_tres.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"./assets/icons/empleados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_tres.setIcon(icon8)
        self.bt_tres.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_tres)

        self.bt_cuatro = QPushButton(self.frame_lateral)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setMinimumSize(QSize(0, 40))
        self.bt_cuatro.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"./assets/icons/pagos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cuatro.setIcon(icon9)
        self.bt_cuatro.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cuatro)

        self.bt_cinco = QPushButton(self.frame_lateral)
        self.bt_cinco.setObjectName(u"bt_cinco")
        self.bt_cinco.setMinimumSize(QSize(0, 40))
        self.bt_cinco.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u"./assets/icons/reportes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cinco.setIcon(icon10)
        self.bt_cinco.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cinco)

        self.bt_seis = QPushButton(self.frame_lateral)
        self.bt_seis.setObjectName(u"bt_seis")
        self.bt_seis.setMinimumSize(QSize(0, 40))
        self.bt_seis.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"./assets/icons/nuevo_proyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_seis.setIcon(icon11)
        self.bt_seis.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.bt_seis)

        self.bt_siete = QPushButton(self.frame_lateral)
        self.bt_siete.setObjectName(u"bt_siete")
        self.bt_siete.setMinimumSize(QSize(0, 40))
        self.bt_siete.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u"./assets/icons/adminitrador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_siete.setIcon(icon12)
        self.bt_siete.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_siete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_lateral)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_lateral, 0, Qt.AlignLeft)

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
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"./assets/icons/AEC.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(0)

        self.verticalLayout_9.addWidget(self.label)

        self.stackedWidget.addWidget(self.page)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        self.page_uno.setStyleSheet(u"QFrame{\n"
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
        self.verticalLayout_4 = QVBoxLayout(self.page_uno)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_uno)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_uno)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.426, y1:0.0170455, x2:1, y2:0, stop:0 rgba(142, 144, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"")
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
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        self.page_dos.setStyleSheet(u"background-color: rgb(140, 140, 140);")
        self.verticalLayout_5 = QVBoxLayout(self.page_dos)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_dos)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page_dos)
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
        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QWidget()
        self.page_tres.setObjectName(u"page_tres")
        self.page_tres.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_6 = QVBoxLayout(self.page_tres)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_tres)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page_tres)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.table_qwt_new = QTableWidget(self.frame_8)
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


        self.verticalLayout_6.addWidget(self.frame_8)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QWidget()
        self.page_cuatro.setObjectName(u"page_cuatro")
        self.page_cuatro.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_7 = QVBoxLayout(self.page_cuatro)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_cuatro)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_cuatro)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_10)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        self.page_cinco.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.verticalLayout_8 = QVBoxLayout(self.page_cinco)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_cinco)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_cinco)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_12)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 8)
        self.stackedWidget.addWidget(self.page_cinco)
        self.page_seis = QWidget()
        self.page_seis.setObjectName(u"page_seis")
        self.verticalLayout_10 = QVBoxLayout(self.page_seis)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_encabezado_pro = QFrame(self.page_seis)
        self.frame_encabezado_pro.setObjectName(u"frame_encabezado_pro")
        self.frame_encabezado_pro.setMaximumSize(QSize(16777215, 100))
        self.frame_encabezado_pro.setStyleSheet(u"background-color: rgb(148, 148, 148);")
        self.frame_encabezado_pro.setFrameShape(QFrame.StyledPanel)
        self.frame_encabezado_pro.setFrameShadow(QFrame.Raised)
        self.btn_Buscar_pro = QPushButton(self.frame_encabezado_pro)
        self.btn_Buscar_pro.setObjectName(u"btn_Buscar_pro")
        self.btn_Buscar_pro.setGeometry(QRect(230, 20, 75, 23))
        self.lineEdit_buscar_pro = QLineEdit(self.frame_encabezado_pro)
        self.lineEdit_buscar_pro.setObjectName(u"lineEdit_buscar_pro")
        self.lineEdit_buscar_pro.setGeometry(QRect(20, 40, 151, 21))
        self.lineEdit_buscar_pro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame_encabezado_pro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 121, 16))

        self.verticalLayout_10.addWidget(self.frame_encabezado_pro)

        self.frame_contenedor_pro = QFrame(self.page_seis)
        self.frame_contenedor_pro.setObjectName(u"frame_contenedor_pro")
        self.frame_contenedor_pro.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_contenedor_pro.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor_pro.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_contenedor_pro)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 7)
        self.stackedWidget.addWidget(self.page_seis)
        self.page_siete = QWidget()
        self.page_siete.setObjectName(u"page_siete")
        self.page_siete.setStyleSheet(u"QFrame{\n"
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
        self.verticalLayout_11 = QVBoxLayout(self.page_siete)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_siete)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:1 rgba(176, 183, 232, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)


        self.verticalLayout_11.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_siete)
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
        self.verticalLayout_11.setStretch(1, 9)
        self.stackedWidget.addWidget(self.page_siete)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        sistema.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(sistema)
        self.statusBar.setObjectName(u"statusBar")
        sistema.setStatusBar(self.statusBar)

        self.retranslateUi(sistema)

        self.bt_menu.setDefault(False)
        self.bt_uno.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(sistema)
    # setupUi

    def retranslateUi(self, sistema):
        sistema.setWindowTitle(QCoreApplication.translate("sistema", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("sistema", u"    MENU ", None))
        self.label_titulo.setText(QCoreApplication.translate("sistema", u"SISTEMA AEC CONTRATISTAS GENERALES", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("sistema", u"  INICIO             ", None))
        self.bt_uno.setText(QCoreApplication.translate("sistema", u"     REGISTRO", None))
        self.bt_dos.setText(QCoreApplication.translate("sistema", u"   ASISTENCIA", None))
        self.bt_tres.setText(QCoreApplication.translate("sistema", u"TRABAJADORES", None))
        self.bt_cuatro.setText(QCoreApplication.translate("sistema", u"PAGOS Y OTROS", None))
        self.bt_cinco.setText(QCoreApplication.translate("sistema", u"        REPORTES", None))
        self.bt_seis.setText(QCoreApplication.translate("sistema", u"    PROYECTOS", None))
        self.bt_siete.setText(QCoreApplication.translate("sistema", u"ADMINISTRADOR", None))
        self.label_2.setText(QCoreApplication.translate("sistema", u"AEC CONTRATISTAS \n"
" GENERALES", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("sistema", u"Registrar, agregar o eliminar trabajadores", None))
        self.btn_agregar_trabajador.setText(QCoreApplication.translate("sistema", u"Aregar un trabajador", None))
        self.pushButton_2.setText(QCoreApplication.translate("sistema", u"Agregar materiales", None))
        self.pushButton_3.setText(QCoreApplication.translate("sistema", u"Agregar Adminitrador", None))
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
        self.label_3.setText(QCoreApplication.translate("sistema", u"Nombre del Proyecto", None))
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

