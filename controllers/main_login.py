import sys
import time 
import random
from datetime import datetime, timedelta
from PySide2 import QtCore
from PySide2.QtCore import (QDate,QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_login import Ui_login
from views.ui_menu import Ui_sistema

from controllers.change_password import (changed_password_uad, Dialogo)
from controllers.add_trabajador import new_trabajador
from controllers.control_project import add_project

class MiApp(QMainWindow, Ui_login):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#eliminar barra
		self.setWindowFlag(Qt.FramelessWindowHint)
		#transparente
		self.setAttribute(Qt.WA_TranslucentBackground)
		# evento click para acceder al sistema
		self.bt_ingresar.clicked.connect(self.iniciar_sesion)
		self.btn_close.clicked.connect(self.close)
     	
     	# Realizamos una petición a la base de datos de ussers
		self.datos = Registro_datos()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			self.iniciar_sesion()

	def iniciar_sesion(self):
		# Los labels de contraseña y usuario ponemos en blanco
		self.contrasena_incorrecta.clear()
		self.usuario_incorrecto.clear()
		users = self.users.text()
		password_entry = self.password.text()
		users_entry = users
		users_all_information = self.datos.busca_users(users_entry)
		if(len(users_all_information)==0):
			self.usuario_incorrecto.setText('Usuario incorrecto')
		else:
			users1=users_all_information[2]
			password=users_all_information[3]
			if(password_entry==password and users==users_entry):
				for i in range(0,99):
					time.sleep(0.000)
					self.progressBar.setValue(i)
					self.cargando.setText('Cargando...')

				self.ventana = control_aec()
				self.ventana.set_pass(users,password)
				self.ventana.show()
				self.close()
			else:
				self.contrasena_incorrecta.setText('Contraseña incorrecta')
			
class control_aec(QMainWindow,Ui_sistema):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		#SizeGrip
		self.gripSize = 10
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.txt_users=""
		self.txt_password=""
		self.alto_qfadd_project=0
		self.code_project=""
		self.name_project=""
		self.datos = Registro_datos()
		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.page_inicio_new()
		#acceder a las paginas
		#self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))			
		self.btn_proyectos.clicked.connect(self.click_btn_proyectos)
		self.btn_registro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registro))	
		self.btn_asistencia.clicked.connect(self.return_home)
		#self.btn_kardex.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_kardex))			
		self.btn_pagos.clicked.connect(self.page_pagos)
		self.btn_reportes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_reportes))
		self.btn_admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_adminstracion))
		#self.pushButton_get_dni.clicked.connect(self.retornar_origen)
		self.btn_add_admin_ctrl.clicked.connect(self.ctrl_frame_add_admin)	
		self.btn_delete_admin_ctrl.clicked.connect(self.ctrl_frame_delete_admin)
		# realiza que los table view se ajusten de entrada de datos
		#self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		#self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		# btn controls
		self.btn_add_confirm_admin.clicked.connect(self.add_admin_new)
		##self.add_admin_btn_ctrls.clicked.connect(self.es_null)
		self.delete_admin_ctrl_btn.clicked.connect(self.delete_bd_admin)
		#control barra de titulos
		self.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.btn_agregar_trabajador.clicked.connect(self.agregar_trabajador)
		self.btn_changes_password.clicked.connect(self.cambiar_password)
		self.btn_ocultar.clicked.connect(self.mover_arriba)
		self.bt_restaurar.hide()
		self.dialogo=Dialogo()
		self.btn_agregar_pro.clicked.connect(self.add_new_project)
		#self.btn_Buscar_pro.clicked.connect()
		self.lndt_add_password.textChanged.connect(self.verificar_users)
		self.v_ScrollBar_project.valueChanged.connect(self.scroll_frame)
		self.btn_search_iddni.clicked.connect(self.show_search_data)
		# menu lateral
		self.borrar_elementos()
		self.bt_menu.clicked.connect(self.mover_menu)
		self.oculto=False
		self.add_busqueda_dni=None
		# Agregamos todos los frames e control ocultar y mostrar
		self.frame_encabezados=[self.frame_reportes,self.frame_proyectos,self.frame_administrador]
		self.valor_x=0
		self.update_date_now()
		self.bt_cerrar.clicked.connect(self.close)
	def page_pagos(self):
		from controllers.tpayments import tpaymentst
		payments=tpaymentst(self)
		self.return_home()
		payments.show()

	def show_search_data(self):
		from controllers.tsearch_dni import tsearch_dni
		self.add_busqueda_dni=tsearch_dni(self)
		self.add_busqueda_dni.show()
	# Retorna al anterior punto de llamada
	def return_home(self):
		self.lbl_name_welcome.setText("SISTEMA")
		#self.lbl_mensaje_show.setText("La asistencia se controla\ndesde menu proyectos")
		self.page_inicio_new()
	def open_attendance(self):
		from controllers.tcall_list import tasistencia
		self.table_attendece=tasistencia(self)
		self.table_attendece.show()
		self.table_attendece.call_list_data()
		#self.stackedWidget.setCurrentWidget(self.page_asistencia)

	def page_inicio_new(self):
		self.stackedWidget.setCurrentWidget(self.page_inicio)

	def update_date_now(self):
		now = datetime.now()
		d = QDate(now.year, now.month, now.day)
		self.date_emision.setDate(d)
		self.datetime_decline.setDate(d)

	def click_btn_proyectos(self):
		self.stackedWidget.setCurrentWidget(self.page_proyectos)
		self.add_control_frame()

	def borrar_elementos(self):
		self.datos = Registro_datos()
		while self.gridLayout_add_frame.count() > 0:
			child = self.gridLayout_add_frame.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def scroll_frame(self):
		self.frame_contenedor_pro.resize(self.frame_contenedor_pro.width(),self.alto_qfadd_project*190)
		# Actualizar la posición vertical del QFrame según el valor de la QScrollBar
		value = self.v_ScrollBar_project.value()
		height_cont=int(self.frame_contenedor_pro.height()/100)
		self.frame_contenedor_pro.move(self.frame_contenedor_pro.x(), -value*height_cont)
	
	# Eliminamos un administrador del sistema
	def delete_bd_admin(self):
		# Obtenemos el dni- o users
		users_dni=self.lndt_delete_id.text()
		# Verificamos que exista algun dato
		if(users_dni==""):
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("Completa los datos\ncorrectamente")
		else:
			estado=self.datos.elimina_admin(users_dni)
			if(estado):
				self.dialogo.show()
				self.dialogo.label_mensaje.setText("Operacion\nExitosa")
			else:
				self.dialogo.show()
				self.dialogo.label_mensaje.setText("No existe el DNI\no users en la\nbase de datos")

	def add_admin_new(self):
		# Recuperamos los datos
		users=self.lineEdit_add_users.text()
		password=self.lndt_add_password.text()
		if(users=="" or password==""):
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("Completa los datos \n correctamente")
		else:
			self.datos.add_admin(users, password)
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("Se agrego\ncorrectamente")

	def verificar_users(self):
		users=self.lineEdit_add_users.text()
		act = self.datos.busca_users(users)
		# Verifica si existe el users en la base de datos
		if act is not None:
			self.dialogo.label_mensaje.setText("El users ya existe")
			# Mostramos los mensajes y ponemos en blanco los datos
			self.lineEdit_add_users.setText("")
			self.lndt_add_password.setText("")
			self.dialogo.show()

	def ctrl_frame_delete_admin(self):
		self.add_admin_frame.hide()
		self.delete_admin_frame.show()
		self.stackedWidget.setCurrentWidget(self.page_add_administrator)

	def ctrl_frame_add_admin(self):
		self.add_admin_frame.show()
		self.delete_admin_frame.hide()
		self.stackedWidget.setCurrentWidget(self.page_add_administrator)

	def add_new_project(self):
		self.ui_add_project=add_project(self)
		self.ui_add_project.show()
		
	def add_control_frame(self):
		self.borrar_elementos()
		# Aqui se define el ancho y alto de nuestro objeto
		width=200	# ancho del frame a crear
		height=150  # alto del frame a crear
		# Tamanio del conetenedor
		width_cont=int(self.frame_contenedor_pro.width()/220)
		height_cont=int(self.frame_contenedor_pro.height()/170)
		# obtenemos los datos
		valor=self.datos.show_tproject() 
		# Contador para detener el bucle while
		contador_bucle=0
		count_next_line=0
		# Crear la cantidad de elementos necesarios
		while(contador_bucle<len(valor)):
			count_column=0
			while(count_column<width_cont and contador_bucle<len(valor)):
				valor_add=valor[contador_bucle]
				frame_project=control_data(self,valor_add[0],valor_add[1],count_next_line,count_column)
				frame_project.crear_qframe()
				self.gridLayout_add_frame.addWidget(frame_project.get_frame(),count_next_line,count_column,1,1)
				#increment in each iter
				contador_bucle+=1
				count_column+=1
			count_next_line+=1
		self.alto_qfadd_project=count_next_line

	def set_pass(self,txt1,txt2):
		self.txt_users=txt1
		self.txt_password=txt2

	def cambiar_password(self):
		#from controllers.change_password import changed_password_uad
		self.cambiar=changed_password_uad(self)
		self.cambiar.show()

	def agregar_trabajador(self):
		self.trabajador= new_trabajador(self)
		self.trabajador.show()

	def control_bt_minimizar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.bt_restaurar.hide()
		self.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.bt_maximizar.hide()
		self.bt_restaurar.show()

	def mover_menu(self):
		# Volvemos los objetos a su posicion
		if True:	
			width = self.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 200
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	def mover_arriba(self):
		# verifica si esta oculto
		if(self.oculto):
			for frame_i in self.frame_encabezados:
				frame_i.show()
			self.oculto=False
			self.btn_ocultar.setText("OCULTAR \n ENCABEZADO")

		else:
			self.oculto=True
			for frame_i in self.frame_encabezados:
				frame_i.hide()
			self.btn_ocultar.setText("MOSTRAR \n ENCABEZADO")
	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()
				
# Se crea un control de la tabla
class control_data(QDialog):
	def __init__(self, parent,code_project,name_project,row,column):
		super(control_data,self).__init__(parent)
		self.code_project=code_project
		self.name_project=name_project
		self.row=row
		self.column=column
		self.qframe=QFrame()
		self.dialogo=Dialogo()
		from controllers.control_project import ctrl_project
		self.ui_add=ctrl_project(self)
		from controllers.change_password import dialogo_delete
		self.view_delete=dialogo_delete(self)
		self.ui_add.btn_call_list.clicked.connect(self.call_list)
		self.ui_add.btn_delete_project.clicked.connect(self.delete_project)

	def delete_project(self):
		self.view_delete.show()
		self.view_delete.btn_alow.clicked.connect(self.delete_frame)

	def delete_frame(self):
		# se cierra el menu de opciones
		self.view_delete.close()
		item = self.parent().gridLayout_add_frame.itemAtPosition(self.row, self.column)
		datos = Registro_datos()
		# elimina el objeto seleccionado
		item.widget().deleteLater()
		if(datos.delete_project_bcode(self.code_project)):
			# Actualiza los datos visibles
			self.parent().add_control_frame()
			self.dialogo.show()
			self.ui_add.close()
			self.dialogo.label_mensaje.setText("Se elimino \n correctamente")
		else:
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("No se pudo realizar\nla operacion")

	def call_list(self):
		self.ui_add.close()
		self.parent().code_project=self.code_project
		self.parent().name_project=self.name_project
		self.parent().open_attendance()
		self.close()

	def get_frame(self):
		return self.qframe

	def crear_qframe(self):
		# Crear un QFrame y establecer su geometr
		self.qframe = QFrame(self.parent().frame_contenedor_pro)
		self.qframe.setMinimumSize(QSize(200, 170))
		self.v_layout_frame = QVBoxLayout(self.qframe)
		self.qframe.setStyleSheet("background-color: rgb(103, 105, 255);")
		self.lbl_frame = QLabel(self.qframe)
		self.lbl_frame.setText("Cod. proyecto:\n"+self.code_project)
		#self.lbl_frame.setGeometry(QRect(10, 10, 180, 90))
		self.lbl_frame.setStyleSheet("font: 75 16pt Arial")
		self.lbl_frame.setAlignment(Qt.AlignCenter)
		self.v_layout_frame.addWidget(self.lbl_frame)
		self.lbl_fr_name = QLabel(self.qframe)
		self.lbl_fr_name.setText("Nombre :\n"+self.ui_add.line_break())
		#self.lbl_fr_name.setGeometry(QRect(10, 10, 180, 90))
		self.lbl_fr_name.setStyleSheet("font: 75 16pt Arial")
		self.lbl_fr_name.setAlignment(Qt.AlignCenter)
		self.v_layout_frame.addWidget(self.lbl_fr_name)


		self.view_details = QPushButton(self.qframe)
		#self.view_details.setGeometry(QRect(10, 110, 180, 30))
		self.view_details.setMinimumSize(QSize(0, 31))
		self.view_details.setText("VER DETALLES")
		self.view_details.setStyleSheet("QPushButton{ border: 1px solid rgb(0, 0, 127);\n"
		"border-radius:5px;\n"
		"background-color: rgb(255, 170, 0);\n"
		"font: 75 12pt \"MS Shell Dlg 2\";}\n"
		"QPushButton:hover{ background-color: white;\n"
		"border-radius:5px;}")
		self.v_layout_frame.addWidget(self.view_details)
		self.view_details.clicked.connect(self.open_project)
		self.view_details.show()
		self.lbl_frame.show()
		self.qframe.show()
	
	def open_project(self):
		self.ui_add.show()





