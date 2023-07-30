# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tsearch_dataWFunDN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tsearch_dni(object):
    def setupUi(self, tsearch_dni):
        if not tsearch_dni.objectName():
            tsearch_dni.setObjectName(u"tsearch_dni")
        tsearch_dni.resize(865, 557)
        self.centralwidget = QWidget(tsearch_dni)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 3px solid rgb(0, 0, 127);\n"
"background-color: rgb(170, 170, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox{\n"
"border: none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"border: none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, 9, -1)
        self.frame_des = QFrame(self.frame)
        self.frame_des.setObjectName(u"frame_des")
        self.frame_des.setStyleSheet(u"border:none;")
        self.frame_des.setFrameShape(QFrame.StyledPanel)
        self.frame_des.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_des)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.comboBox_name_s = QComboBox(self.frame_des)
        self.comboBox_name_s.addItem("")
        self.comboBox_name_s.addItem("")
        self.comboBox_name_s.addItem("")
        self.comboBox_name_s.setObjectName(u"comboBox_name_s")
        self.comboBox_name_s.setMinimumSize(QSize(200, 0))
        self.comboBox_name_s.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")

        self.horizontalLayout.addWidget(self.comboBox_name_s)

        self.lineEdit_data_search = QLineEdit(self.frame_des)
        self.lineEdit_data_search.setObjectName(u"lineEdit_data_search")
        self.lineEdit_data_search.setMinimumSize(QSize(300, 0))
        self.lineEdit_data_search.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineEdit_data_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame_des, 1, 0, 1, 1)

        self.lbl_description = QLabel(self.frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setStyleSheet(u"")
        self.lbl_description.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_description, 2, 0, 1, 1)

        self.listWidget_show_s = QListWidget(self.frame)
        QListWidgetItem(self.listWidget_show_s)
        QListWidgetItem(self.listWidget_show_s)
        self.listWidget_show_s.setObjectName(u"listWidget_show_s")
        self.listWidget_show_s.setMinimumSize(QSize(0, 100))
        self.listWidget_show_s.setLayoutDirection(Qt.LeftToRight)
        self.listWidget_show_s.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:1px;\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.listWidget_show_s, 3, 0, 1, 1)

        self.lbl_seleccionado_dni = QLabel(self.frame)
        self.lbl_seleccionado_dni.setObjectName(u"lbl_seleccionado_dni")
        self.lbl_seleccionado_dni.setMinimumSize(QSize(0, 40))
        self.lbl_seleccionado_dni.setStyleSheet(u"")
        self.lbl_seleccionado_dni.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_seleccionado_dni, 4, 0, 1, 1)

        self.horizontalFrame = QFrame(self.frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(170, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_get_dni = QPushButton(self.horizontalFrame)
        self.pushButton_get_dni.setObjectName(u"pushButton_get_dni")
        self.pushButton_get_dni.setMinimumSize(QSize(0, 31))
        self.pushButton_get_dni.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_get_dni)

        self.btn_decline = QPushButton(self.horizontalFrame)
        self.btn_decline.setObjectName(u"btn_decline")
        self.btn_decline.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_2.addWidget(self.btn_decline)


        self.gridLayout.addWidget(self.horizontalFrame, 5, 0, 1, 1)

        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}")
        self.layout_principal = QHBoxLayout(self.frame_superior)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setObjectName(u"layout_principal")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_principal.addItem(self.horizontalSpacer_3)

        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.lbl_title)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_principal.addItem(self.horizontalSpacer_4)

        self.btn_ampliar = QPushButton(self.frame_superior)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        self.btn_ampliar.setMaximumSize(QSize(31, 16777215))
        self.btn_ampliar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_ampliar)

        self.btn_close_search = QPushButton(self.frame_superior)
        self.btn_close_search.setObjectName(u"btn_close_search")
        self.btn_close_search.setMaximumSize(QSize(31, 16777215))
        self.btn_close_search.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_close_search)


        self.gridLayout.addWidget(self.frame_superior, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame)

        tsearch_dni.setCentralWidget(self.centralwidget)

        self.retranslateUi(tsearch_dni)

        QMetaObject.connectSlotsByName(tsearch_dni)
    # setupUi

    def retranslateUi(self, tsearch_dni):
        tsearch_dni.setWindowTitle(QCoreApplication.translate("tsearch_dni", u"MainWindow", None))
        self.comboBox_name_s.setItemText(0, QCoreApplication.translate("tsearch_dni", u"Nombres", None))
        self.comboBox_name_s.setItemText(1, QCoreApplication.translate("tsearch_dni", u"Apellidos", None))
        self.comboBox_name_s.setItemText(2, QCoreApplication.translate("tsearch_dni", u"Nro celular", None))

        self.lbl_description.setText(QCoreApplication.translate("tsearch_dni", u"Liste de nombres o apellidos que coinciden", None))

        __sortingEnabled = self.listWidget_show_s.isSortingEnabled()
        self.listWidget_show_s.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_show_s.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("tsearch_dni", u"Hello world", None));
        ___qlistwidgetitem1 = self.listWidget_show_s.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("tsearch_dni", u"Never mind", None));
        self.listWidget_show_s.setSortingEnabled(__sortingEnabled)

        self.lbl_seleccionado_dni.setText(QCoreApplication.translate("tsearch_dni", u"Se ha seleccionado el DNI :", None))
        self.pushButton_get_dni.setText(QCoreApplication.translate("tsearch_dni", u"Obtener el DNI", None))
        self.btn_decline.setText(QCoreApplication.translate("tsearch_dni", u"Cancelar", None))
        self.lbl_title.setText(QCoreApplication.translate("tsearch_dni", u"Mostrar datos", None))
        self.btn_ampliar.setText(QCoreApplication.translate("tsearch_dni", u"\u25a0", None))
        self.btn_close_search.setText(QCoreApplication.translate("tsearch_dni", u"X", None))
    # retranslateUi

