# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_passwordUZBMBr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_changes_password(object):
    def setupUi(self, changes_password):
        if not changes_password.objectName():
            changes_password.setObjectName(u"changes_password")
        changes_password.resize(432, 531)
        changes_password.setStyleSheet(u"")
        self.frame_contenedor = QFrame(changes_password)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setGeometry(QRect(0, 10, 421, 511))
        self.frame_contenedor.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(0, 0, 0) ;\n"
"background-color: qlineargradient(spread:pad, x1:0.409318, y1:0.636, x2:0.432, y2:0.0454545, stop:0 rgba(59, 123, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"	border: 0px ;\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgba( 255, 255, 255, 0% );\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(83, 152, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(0, 0, 0) ;\n"
"font: 87 10pt \"Segoe UI Black\"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"border:1px solid rgb(0, 0, 0) ;\n"
"background-color:white;\n"
"font: 87 10pt \"Segoe UI Black\"}")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame_contenedor)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_control = QFrame(self.frame_contenedor)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setStyleSheet(u"border:none;")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_control)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, 15)
        self.label_5 = QLabel(self.frame_control)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 31))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_users_name = QLabel(self.frame_control)
        self.label_users_name.setObjectName(u"label_users_name")
        self.label_users_name.setMinimumSize(QSize(0, 31))
        self.label_users_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_users_name)

        self.label_2 = QLabel(self.frame_control)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 31))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lndt_password = QLineEdit(self.frame_control)
        self.lndt_password.setObjectName(u"lndt_password")
        self.lndt_password.setMinimumSize(QSize(0, 31))
        self.lndt_password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;\n"
"\n"
"")
        self.lndt_password.setEchoMode(QLineEdit.Normal)
        self.lndt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lndt_password)

        self.label_3 = QLabel(self.frame_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 31))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.new_password = QLineEdit(self.frame_control)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setMinimumSize(QSize(0, 31))
        self.new_password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.new_password.setEchoMode(QLineEdit.Normal)
        self.new_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.new_password)

        self.label_verificate = QLabel(self.frame_control)
        self.label_verificate.setObjectName(u"label_verificate")
        self.label_verificate.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_verificate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_verificate)

        self.label_4 = QLabel(self.frame_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 31))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.confirm_new_password = QLineEdit(self.frame_control)
        self.confirm_new_password.setObjectName(u"confirm_new_password")
        self.confirm_new_password.setMinimumSize(QSize(0, 31))
        self.confirm_new_password.setStyleSheet(u"border-radius:10px;\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px;")
        self.confirm_new_password.setEchoMode(QLineEdit.Normal)
        self.confirm_new_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.confirm_new_password)

        self.confirm_contrasena_incorrecta = QLabel(self.frame_control)
        self.confirm_contrasena_incorrecta.setObjectName(u"confirm_contrasena_incorrecta")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.confirm_contrasena_incorrecta.setFont(font)
        self.confirm_contrasena_incorrecta.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.confirm_contrasena_incorrecta.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.confirm_contrasena_incorrecta)

        self.btn_aceptar = QPushButton(self.frame_control)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setMinimumSize(QSize(0, 35))
        self.btn_aceptar.setStyleSheet(u"border: 1px solid rgb(0, 0, 0) ;")

        self.verticalLayout_2.addWidget(self.btn_aceptar)

        self.btn_cancelar = QPushButton(self.frame_control)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(0, 35))
        self.btn_cancelar.setStyleSheet(u"border: 1px solid rgb(0, 0, 0) ;")

        self.verticalLayout_2.addWidget(self.btn_cancelar)


        self.verticalLayout.addWidget(self.frame_control)


        self.retranslateUi(changes_password)

        QMetaObject.connectSlotsByName(changes_password)
    # setupUi

    def retranslateUi(self, changes_password):
        changes_password.setWindowTitle(QCoreApplication.translate("changes_password", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("changes_password", u"Cambiar contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("changes_password", u"USERS", None))
        self.label_users_name.setText(QCoreApplication.translate("changes_password", u"No especifica", None))
        self.label_2.setText(QCoreApplication.translate("changes_password", u"Contrase\u00f1a:", None))
        self.lndt_password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Ingrese tu contrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("changes_password", u"Contrase\u00f1a nueva :", None))
        self.new_password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Ingrese  contrase\u00f1a nueva", None))
        self.label_verificate.setText("")
        self.label_4.setText(QCoreApplication.translate("changes_password", u"Confirmar contrase\u00f1a :", None))
        self.confirm_new_password.setPlaceholderText(QCoreApplication.translate("changes_password", u"Confirma la nueva contrase\u00f1a", None))
        self.confirm_contrasena_incorrecta.setText("")
        self.btn_aceptar.setText(QCoreApplication.translate("changes_password", u"Aceptar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("changes_password", u"Cancelar", None))
    # retranslateUi

