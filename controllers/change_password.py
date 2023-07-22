import sys
from PySide2 import QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_change_password import Ui_changes_password
from views.ui_dialogo_delete import Ui_Dialog_delete

class dialogo_delete(QDialog,Ui_Dialog_delete):
	def __init__(self,parent):
		super(dialogo_delete,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.estado=False
		self.btn_decline.clicked.connect(self.close)

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #self.resize(300, 300)
        self.setWindowTitle(" Mensaje ")
        #self.etiqueta = QLabel(self)
        self.resize(268, 259)
        self.setStyleSheet(u"QDialog{\n"
		"background-color: rgb(138, 138, 138);\n"
		"border: 2px solid rgb(0, 0, 0) ;\n"
		"}\n"
		"QLabel{\n"
		"color: rgb(255, 255, 255);\n"
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
        self.pButton_alow = QPushButton(self)
        self.pButton_alow.setObjectName(u"pButton_alow")
        self.pButton_alow.setGeometry(QRect(60, 210, 141, 31))
        self.label_mensaje = QLabel(self)
        self.label_mensaje.setObjectName(u"label_mensaje")
        self.label_mensaje.setGeometry(QRect(20, 20, 231, 161))
        font = QFont()
        font.setPointSize(12)
        self.label_mensaje.setFont(font)
        self.label_mensaje.setAlignment(Qt.AlignCenter)
        self.pButton_alow.setText("Aceptar")
        self.pButton_alow.clicked.connect(self.close)


class changed_password_uad(QMainWindow,Ui_changes_password):
	def __init__(self, parent):
		super(changed_password_uad,self).__init__(parent)
		self.setupUi(self)
		#eliminar barra
		self.setWindowFlag(Qt.FramelessWindowHint)
		# Recuperamos password del sistema
		#self.txt_users=self.parent().txt_users;
		self.txt_password=self.parent().txt_password;
		# Aqui guardamos la nueva contraseña
		self.change_new_password=""
		# Creamos un cuadro de mensaje
		self.dialogo = Dialogo()
		#self.btn_aceptar.clicked.connect(self.aceptar)
		self.btn_cancelar.clicked.connect(self.close)
		self.btn_aceptar.clicked.connect(self.verificar)
		self.confirm_new_password.textChanged.connect(self.verificar_confirm_pass)
		#self.dialogo.pButton_alow.clicked.connect(self.dialogo.close)
		self.datos = Registro_datos()

	def is_true_change(self):
		new_password=self.new_password.text()
		password_confirm=self.confirm_new_password.text()
		return new_password==password_confirm

	def verificar_confirm_pass(self):
		# Las nuevas contraseñas coinciden
		if(self.is_true_change()):
			self.confirm_contrasena_incorrecta.setText("La contraseña coincide")
			self.confirm_contrasena_incorrecta.setStyleSheet("color:rgb(0, 255, 0)")
			self.change_new_password=self.confirm_new_password.text()
		# Las contraseñas son diferentes
		else:
			self.confirm_contrasena_incorrecta.setStyleSheet("color:rgb(255, 0, 0)")
			self.confirm_contrasena_incorrecta.setText("La Contraseña no coincide")
		

	def verificar(self):
		# Obtenemos el password de acceso al sistema
		password_old =self.password.text()
		# Verificamos que el password de anterior conincida
		if(password_old != self.txt_password):
			self.dialogo.label_mensaje.setText("Contraseña anterior \n incorrecto")
			self.dialogo.show()
		else:
			if(self.is_true_change()):
				act = self.datos.actualiza_password(self.parent().txt_users,self.change_new_password)
				self.dialogo.show()
				self.dialogo.label_mensaje.setText("Las contraseña se\ncambio correctamente")
				self.close()

