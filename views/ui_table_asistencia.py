# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_asistenciajwZaOh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tasistencia(object):
    def setupUi(self, tasistencia):
        if not tasistencia.objectName():
            tasistencia.setObjectName(u"tasistencia")
        tasistencia.resize(908, 523)
        self.centralwidget = QWidget(tasistencia)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 3px solid rgb(0, 0, 127);\n"
"background-color: rgb(170, 170, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox{\n"
"border: none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"border: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";}\n"
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
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 15)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"	background-color: rgb(158, 158, 158);\n"
"}")
        self.layout_principal = QHBoxLayout(self.frame_superior)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setObjectName(u"layout_principal")
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.frame_superior)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.lbl_title)

        self.btn_ampliar = QPushButton(self.frame_superior)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        self.btn_ampliar.setMaximumSize(QSize(35, 31))
        self.btn_ampliar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_ampliar)

        self.btn_close = QPushButton(self.frame_superior)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(35, 31))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"}")

        self.layout_principal.addWidget(self.btn_close)


        self.verticalLayout_4.addWidget(self.frame_superior)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(0, 31))
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.btn_delete, 4, 3, 1, 1)

        self.change_code_project = QLabel(self.frame)
        self.change_code_project.setObjectName(u"change_code_project")
        self.change_code_project.setMinimumSize(QSize(0, 30))
        self.change_code_project.setStyleSheet(u"color: rgb(85, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.change_code_project, 0, 1, 1, 1)

        self.change_name_project = QLabel(self.frame)
        self.change_name_project.setObjectName(u"change_name_project")
        self.change_name_project.setMinimumSize(QSize(0, 30))
        self.change_name_project.setStyleSheet(u"color: rgb(85, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.change_name_project, 3, 1, 1, 1)

        self.dt_fecha_list = QDateEdit(self.frame)
        self.dt_fecha_list.setObjectName(u"dt_fecha_list")
        self.dt_fecha_list.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dt_fecha_list.setFont(font)
        self.dt_fecha_list.setStyleSheet(u"background-color: rgb(0, 135, 203);\n"
"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.dt_fecha_list.setCalendarPopup(True)
        self.dt_fecha_list.setDate(QDate(2023, 1, 1))

        self.gridLayout.addWidget(self.dt_fecha_list, 0, 3, 1, 1)

        self.label_37 = QLabel(self.frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 30))
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_37, 4, 0, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 30))
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_33, 3, 0, 1, 1)

        self.lineEdit_delete_dni = QLineEdit(self.frame)
        self.lineEdit_delete_dni.setObjectName(u"lineEdit_delete_dni")
        self.lineEdit_delete_dni.setMinimumSize(QSize(0, 31))
        self.lineEdit_delete_dni.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_delete_dni.setMaxLength(8)

        self.gridLayout.addWidget(self.lineEdit_delete_dni, 4, 2, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.change_responsible_name = QLabel(self.frame)
        self.change_responsible_name.setObjectName(u"change_responsible_name")
        self.change_responsible_name.setMinimumSize(QSize(0, 30))
        self.change_responsible_name.setStyleSheet(u"color: rgb(85, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.change_responsible_name, 4, 1, 1, 1)

        self.label_36 = QLabel(self.frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 30))
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_36, 0, 2, 1, 1)

        self.btn_add_new = QPushButton(self.frame)
        self.btn_add_new.setObjectName(u"btn_add_new")
        self.btn_add_new.setMinimumSize(QSize(0, 31))
        self.btn_add_new.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:0px;\n"
"}")

        self.gridLayout.addWidget(self.btn_add_new, 3, 3, 1, 1)

        self.lineEdit_dni_add = QLineEdit(self.frame)
        self.lineEdit_dni_add.setObjectName(u"lineEdit_dni_add")
        self.lineEdit_dni_add.setMinimumSize(QSize(0, 31))
        self.lineEdit_dni_add.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_dni_add.setMaxLength(8)

        self.gridLayout.addWidget(self.lineEdit_dni_add, 3, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.table_asistencia = QTableWidget(self.frame)
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
        self.table_asistencia.setStyleSheet(u"border: 1px solid rgb(0, 0, 127);\n"
"border-radius:1px;\n"
"background-color: rgb(255, 255, 255);")
        self.table_asistencia.setAutoScrollMargin(16)
        self.table_asistencia.setRowCount(0)
        self.table_asistencia.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.table_asistencia)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.btn_guardar_asistencia = QPushButton(self.frame)
        self.btn_guardar_asistencia.setObjectName(u"btn_guardar_asistencia")
        self.btn_guardar_asistencia.setMinimumSize(QSize(0, 31))
        self.btn_guardar_asistencia.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_guardar_asistencia)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        tasistencia.setCentralWidget(self.centralwidget)

        self.retranslateUi(tasistencia)

        QMetaObject.connectSlotsByName(tasistencia)
    # setupUi

    def retranslateUi(self, tasistencia):
        tasistencia.setWindowTitle(QCoreApplication.translate("tasistencia", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("tasistencia", u"LLAMAR ASISTENCIA", None))
        self.btn_ampliar.setText(QCoreApplication.translate("tasistencia", u"\u25a0", None))
        self.btn_close.setText(QCoreApplication.translate("tasistencia", u"X", None))
        self.btn_delete.setText(QCoreApplication.translate("tasistencia", u"Eliminar", None))
        self.change_code_project.setText(QCoreApplication.translate("tasistencia", u"Hello", None))
        self.change_name_project.setText("")
        self.label_37.setText(QCoreApplication.translate("tasistencia", u"Responsable:", None))
        self.label_33.setText(QCoreApplication.translate("tasistencia", u"Nombre del proyecto:", None))
        self.lineEdit_delete_dni.setPlaceholderText(QCoreApplication.translate("tasistencia", u"Ingrese el DNI", None))
        self.label_13.setText(QCoreApplication.translate("tasistencia", u"Codigo de proyecto:", None))
        self.change_responsible_name.setText("")
        self.label_36.setText(QCoreApplication.translate("tasistencia", u"Fecha:", None))
        self.btn_add_new.setText(QCoreApplication.translate("tasistencia", u"Agregar nuevo", None))
        self.lineEdit_dni_add.setPlaceholderText(QCoreApplication.translate("tasistencia", u"Ingrese el DNI", None))
        ___qtablewidgetitem = self.table_asistencia.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tasistencia", u"Asistencia", None));
        ___qtablewidgetitem1 = self.table_asistencia.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tasistencia", u"DNI", None));
        ___qtablewidgetitem2 = self.table_asistencia.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tasistencia", u"Nombres", None));
        ___qtablewidgetitem3 = self.table_asistencia.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tasistencia", u"Apellidos", None));
        ___qtablewidgetitem4 = self.table_asistencia.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tasistencia", u"Observaci\u00f3n", None));
        ___qtablewidgetitem5 = self.table_asistencia.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tasistencia", u"Justificaci\u00f3n", None));
        self.btn_guardar_asistencia.setText(QCoreApplication.translate("tasistencia", u"Guardar lista", None))
    # retranslateUi

