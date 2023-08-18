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
		#self.setWindowFlag(Qt.FramelessWindowHint)
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
		users = self.users.text()
		password_entry = self.password.text()
		users_entry = users
		users_all_information = self.datos.busca_users(users_entry)
		# Cuando no existe ninguna informacion
		if(users_all_information is None):
			#self.usuario_incorrecto.setText('Usuario no registrado')
			QMessageBox.about(self, "Error al iniciar sesion", "<font color='#3D59AB'><h3> Contraseña o usuario incorrecto <br> intentelo de nuevo por favor</h3></font>")
		else:
			users=users_all_information[2]
			password=users_all_information[3]
			id_access=users_all_information[0]
			if(password_entry==password and users==users_entry):
				for i in range(0,99):
					self.progressBar.setValue(i)
				self.ventana = control_aec()
				self.ventana.set_pass(users,password,id_access)
				self.ventana.show()
				self.close()
			else:
				QMessageBox.about(self, "Error al iniciar sesion", "<font color='#3D59AB'><h3> Contraseña o usuario incorrecto <br> intentelo de nuevo por favor</h3></font>")
			
class control_aec(QMainWindow,Ui_sistema):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		icon = QIcon()
		icon.addFile("./assets/icono.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		#SizeGrip
		self.gripSize = 10
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.users=""
		self.password=""
		self.alto_qfadd_project=0
		self.code_project=""
		self.name_project=""
		self.datos = Registro_datos()
		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.page_inicio_new()
		#acceder a las paginas
		#self.bt_inicio.clicked.connect(lambda: self.pages.setCurrentWidget(self.page))			
		self.btn_proyectos.clicked.connect(self.click_btn_proyectos)
		self.btn_registro.clicked.connect(self.get_datosregistros)	
		self.btn_asistencia.clicked.connect(self.view_configuration)
		self.btn_kardex.clicked.connect(self.page_kardex)			
		self.btn_pagos.clicked.connect(self.page_pagos)
		self.btn_reportes.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_reportes))
		self.btn_admin.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_adminstracion))
		#self.pushButton_get_dni.clicked.connect(self.retornar_origen)
		self.btn_add_admin_ctrl.clicked.connect(self.ctrl_frame_add_admin)	
		self.btn_delete_admin_ctrl.clicked.connect(self.ctrl_frame_delete_admin)
		# realiza que los table view se ajusten de entrada de datos
		#self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		#self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.table_combo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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
		self.lineEdit_add_users.textChanged.connect(self.verificar_users)
		self.v_ScrollBar_project.valueChanged.connect(self.scroll_frame)
		self.btn_search_iddni.clicked.connect(self.show_search_data)
		self.lndt_confirm_password_new.textChanged.connect(self.verificar_pass)
		self.lndt_add_password.textChanged.connect(self.validate_password)
		self.btn_show_admin.clicked.connect(self.show_admin)
		self.tableWidget_admin.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.tableWidget_admin.cellClicked.connect(self.onCellClicked)
		self.btn_add_options.clicked.connect(self.open_options)
		self.btn_add_row.clicked.connect(self.add_row)
		self.btn_save_options.clicked.connect(self.save_tableoptions)
		self.btn_returnsave.clicked.connect(self.get_datosregistros)
		self.btn_registrar_ie.clicked.connect(self.set_factura)
		self.btn_add_newgasto.clicked.connect(self.clear_resgitros)
		self.lineEdit_detalle.textChanged.connect(self.this_upperf)
		self.lineEdit_coddocu.textChanged.connect(self.change_idmatrial)
		self.btn_updatemat.clicked.connect(self.update_dbmaterial)
		self.lineEdit_cantidadmt.textChanged.connect(self.calcular_total)
		self.lineEdit_costounit.textChanged.connect(self.calcular_total)
		self.id_options=[]
		# menu lateral
		self.borrar_elementos()
		self.bt_menu.clicked.connect(self.mover_menu)
		self.oculto=False
		self.code_add_registro=""
		self.add_busqueda_dni=None
		# Agregamos todos los frames e control ocultar y mostrar
		self.frame_encabezados=[self.frame_reportes,self.frame_proyectos,self.frame_administrador]
		self.valor_x=0
		self.update_date_now()
		self.bt_cerrar.clicked.connect(self.close)

	def closeEvent(self, event):
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("Salir del sistema AEC")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar el sistema AEC?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)    
		cerrar.exec_()    
		if cerrar.clickedButton() == botonSalir:
			event.accept()
		else:
			event.ignore()

	def calcular_total(self):
		self.update_dbmaterial()
		code_material=self.label_codematerial.text()
		name_material=self.lineEdit_namematrial.text()
		cantidad=self.lineEdit_cantidadmt.text()
		precio=self.lineEdit_costounit.text()
		guia_remision=self.lineEdit_guiaremision.text()
		code_search=self.lineEdit_codefin.text()
		checkBox_reutizable=1
		medida=self.comboBox_medida.currentText()
		if(len(cantidad)>0 and len(precio)>0):
			try:
				this_cantidad=float(cantidad)
				this_precio=float(precio)
			except Exception as e:
				self.dialogo.show()
				this_cantidad=0
				this_precio=0
				self.dialogo.label_mensaje.setText("Los datos cantidad o\nprecion invalido")
			finally:
				total=this_cantidad*this_precio
				self.label_allmt.setText(str(total))
			act=self.datos.add_material(code_material, self.code_add_registro, name_material, guia_remision, cantidad, precio, total,checkBox_reutizable)

	def update_dbmaterial(self):
		code_material=""
		month=self.comboBox_mothn.currentText()
		code_material=month[:3]+"."+self.aleatorio_value(6)
		self.label_codematerial.setText(code_material)

	def change_idmatrial(self):
		tex=self.lineEdit_coddocu.text()
		self.lineEdit_codefin.setText(tex)

	def this_upperf(self):
		tex=self.lineEdit_detalle.text()
		self.lineEdit_detalle.setText(tex.upper())
		self.lineEdit_namematrial.setText(tex.upper())
	def aleatorio_value(self,dim):
		code=""
		for l in range(0,dim):
			rand=random.randint(0,9)
			if(rand%2==0):
				code+=chr(random.randint(ord('A'), ord('Z')))
			else:
				code+=str(random.randint(0, 9))
		return code
		
	def set_factura(self):
		code_factura=""
		month=self.comboBox_mothn.currentText()
		document_type=self.cmbbox_documents.currentText()
		date_emision=self.date_emision.text()
		rotated_to=self.cmbbox_rotated.currentText()
		detalle=self.lineEdit_detalle.text()
		amount=self.lineEdit_mntt.text()
		payment_method=self.cmbbox_mediopay.currentText()
		cost_center=self.cmbbox_costcenter.currentText()
		expense_made=self.cmbbox_responsable.currentText()
		document_number=self.lineEdit_nrodoc.text()
		date_payments=self.datetime_decline.text()
		igv=self.lineEdit_igv.text()
		check_number="14555665"
		type_expenditure=self.cmbbox_egreso.currentText()
		observation=self.lineEdit_observation.text()
		code_docuemts=self.lineEdit_coddocu.text()
		code_factura=month[:3]+self.aleatorio_value(4)+code_docuemts
		self.code_add_registro=code_factura
		act=self.datos.add_factura(code_factura,date_emision, date_payments, document_type, document_number, payment_method, check_number, rotated_to, type_expenditure, cost_center, amount, expense_made, igv, observation,detalle)

	def clear_resgitros(self):
		print("Borrado ")
	def view_configuration(self):
		print("No ha procedimiento")

	def get_datosregistros(self):
		self.pages.setCurrentWidget(self.page_registro)
		datos=self.datos.get_option()
		self.cmbbox_documents.clear()
		self.cmbbox_rotated.clear()
		self.cmbbox_mediopay.clear()
		self.cmbbox_costcenter.clear()
		self.cmbbox_responsable.clear()
		self.cmbbox_egreso.clear()
		for i in datos:
			tex=i[1]
			if tex is not None:
				self.cmbbox_documents.addItems([i[1]])
		for i in datos:
			tex=i[2]
			if tex is not None:
				self.cmbbox_rotated.addItems([i[2]])
		for i in datos:
			tex=i[3]
			if tex is not None:
				self.cmbbox_mediopay.addItems([i[3]])
		for i in datos:
			tex=i[4]
			if tex is not None:
				self.cmbbox_costcenter.addItems([i[4]])
		for i in datos:
			tex=i[5]
			if tex is not None:
				self.cmbbox_responsable.addItems([i[5]])
		for i in datos:
			tex=i[6]
			if tex is not None:
				self.cmbbox_egreso.addItems([i[6]])

	def add_row(self):
		current_row_count = self.table_combo.rowCount()
		self.table_combo.setRowCount(current_row_count + 1)

	def change_header(self,table_properties):
		# Cahenged the size of contents of Qtablwidget to 12
		font = QFont()
		# set valor
		font.setPointSize(12)
		table_properties.setFont(font)
		font = QFont()
		font.setPointSize(12);
		# Change the size of leters about horizontal header of table assitencia
		table_properties.horizontalHeader().setFont(font);
		table_properties.verticalHeader().setFont(font);
		table_properties.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)

	def open_options(self):
		datos=self.datos.get_option()
		self.id_options=[]
		self.pages.setCurrentWidget(self.page_add_combo)
		self.table_combo.setRowCount(len(datos))
		self.table_combo.setColumnCount(6)
		self.change_header(self.table_combo)
		if(datos!=[]):
			for row in range(len(datos)):
				self.id_options.append(datos[row][0])
				for column in range(1,7):
					item = QTableWidgetItem(datos[row][column])
					self.table_combo.setItem(row, column-1, item)

	def save_tableoptions(self):
		# Obtenemos el umero de filas
		i=self.table_combo.rowCount()
		# Obtenemos el numero de columnas
		j=self.table_combo.columnCount()
		for row in range(i):
			column=[]
			for col in range(j):
				item = self.table_combo.item(row, col)
				# get data only that value is different of None
				if(item is not None):
					info=item.text()
					if(info!=""):
						column.append(info)
					else:
						column.append(None)
				else:
					column.append(None)
			result=all(element is None for element in column)
			# Si una fila esta vacia se elimina la posicion
			if(result and i==len(self.id_options)):
				act=self.datos.delete_options(self.id_options[row])
			else:
				# No esta vacio pero se ha modificado
				if(row<len(self.id_options)):
					act=self.datos.update_option(self.id_options[row],column[0],column[1],column[2],column[3],column[4],column[5])
				# Verifica que no este vacio y lo agrega
				elif(result==False):
					act=self.datos.set_option(column[0],column[1],column[2],column[3],column[4],column[5])
		self.dialogo.show()
		self.dialogo.label_mensaje.setText("Se guardo las modificaciones")
		self.get_datosregistros()

	def onCellClicked(self, row, col):
		item = self.tableWidget_admin.item(row, 3)
		self.lndt_delete_id.setText(item.text())

	def page_kardex(self):
		from controllers.t_karderctrl import tkardex
		tkardex_frame=tkardex(self)
		tkardex_frame.show()
		self.return_home()

	def page_pagos(self):
		from controllers.tpayments import tpaymentst
		payments=tpaymentst(self)
		self.pages.setCurrentWidget(self.page_inicio)
		self.return_home()
		payments.show()

	def show_search_data(self):
		from controllers.tsearch_dni import tsearch_dni
		self.add_busqueda_dni=tsearch_dni(self)
		self.add_busqueda_dni.show()
	# Retorna al anterior punto de llamada
	def return_home(self):
		self.lbl_name_welcome.setText("SISTEMA")
		self.lbl_mensaje_show.setText("La asistencia se controla desde menu proyectos")
		self.page_inicio_new()
	def open_attendance(self):
		from controllers.tcall_list import tasistencia
		self.table_attendece=tasistencia(self)
		self.table_attendece.show()
		self.table_attendece.call_list_data()
		#self.pages.setCurrentWidget(self.page_asistencia)

	def page_inicio_new(self):
		self.pages.setCurrentWidget(self.page_inicio)

	def update_date_now(self):
		now = datetime.now()
		d = QDate(now.year, now.month, now.day)
		self.date_emision.setDate(d)
		self.datetime_decline.setDate(d)
		self.comboBox_mothn.setCurrentIndex(now.month-1)

	def click_btn_proyectos(self):
		self.pages.setCurrentWidget(self.page_proyectos)
		self.add_control_frame()

	def borrar_elementos(self):
		self.datos = Registro_datos()
		while self.gridLayout_add_frame.count() > 0:
			child = self.gridLayout_add_frame.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def scroll_frame(self):
		width=self.frame_contenedor_proyec.width()-9
		height=self.frame_contenedor_proyec.height()-9
		self.frame_contexto.setFixedSize(width, height)
		self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.alto_qfadd_project*190)
		# Actualizar la posición vertical del QFrame según el valor de la QScrollBar
		value = self.v_ScrollBar_project.value()
		height_cont=int(self.frame_contenedor_pro.height()/100)
		self.frame_contenedor_pro.move(self.frame_contenedor_pro.x(), -value*height_cont)

	def show_admin(self):
		list_users=self.datos.showfull_admin()
		self.tableWidget_admin.setRowCount(len(list_users))
		self.tableWidget_admin.setColumnCount(5)
		for row in range(len(list_users)):
			dni_admin=list_users[row][0]
			act=self.datos.buscar_trabajador(dni_admin)
			pos=1
			for column in range(5):
				if(column<3):
					item = QTableWidgetItem(act[column])
					self.tableWidget_admin.setItem(row, column, item)
				else:
					item = QTableWidgetItem(list_users[row][pos])
					self.tableWidget_admin.setItem(row, column, item)
					pos+=1

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
		dni=self.lineEdit_dni_admin.text()
		if(users=="" or password=="" or dni=="" or len(users)<=5):
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("Completa los datos \n correctamente")
		else:
			self.datos.add_admin(dni,users, password)
			self.dialogo.show()
			self.dialogo.label_mensaje.setText("Se agrego\ncorrectamente")

	def verificar_pass(self):
		password=self.lndt_add_password.text()
		confirm=self.lndt_confirm_password_new.text()
		if(password!=confirm):
			self.label_confirmation.setText("No coincide la contraseña")
		else:
			self.label_confirmation.setText("")

	def validate_password(self):
		text=self.lndt_add_password.text()
		if(len(text)<8):
			self.label_validate.setText("La contraseña debe\nser mayor a 7 caracteres")
		else:
			if(self.is_alnumver(text)==False):
				self.label_validate.setText("Debe contener\nnúmeros y letras")
			else:
				self.label_validate.setText("")

	def is_alnumver(self,password):
		numeric="0123456789"
		for i in password:
			if(i in numeric):
				return True
		return False

	def verificar_users(self):
		users=self.lineEdit_add_users.text()
		if(len(users)>5):
			self.label_validate_users.setText("")
			act = self.datos.busca_users(users)
			# Verifica si existe el users en la base de datos
			if act is not None:
				self.dialogo.label_mensaje.setText("El users ya existe")
				# Mostramos los mensajes y ponemos en blanco los datos
				self.lineEdit_add_users.setText("")
				self.lndt_add_password.setText("")
				self.label_validate_users.setText("")
				self.dialogo.show()
		else:
			self.label_validate_users.setText("El user debe tener mas de 5 caracteres")
	def ctrl_frame_delete_admin(self):
		self.pages.setCurrentWidget(self.page_delete)

	def ctrl_frame_add_admin(self):
		self.pages.setCurrentWidget(self.page_add_administrator)

	def add_new_project(self):
		self.ui_add_project=add_project(self)
		self.ui_add_project.show()
		
	def add_control_frame(self):
		self.frame_contenedor_data.setMaximumSize(QSize(self.frame_contexto.width(),self.frame_contexto.height()))
		self.borrar_elementos()
		# Aqui se define el ancho y alto de nuestro objeto
		width=200	# ancho del frame a crear
		height=150  # alto del frame a crear
		# Tamanio del conetenedor
		width_cont=int(self.frame_contexto.width()/220)
		height_cont=int(self.frame_contexto.height()/170)
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
			if(self.alto_qfadd_project>1):
				self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.alto_qfadd_project*190)

			elif(count_next_line>=4):
				self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.frame_contenedor_pro.height()+190)
		self.alto_qfadd_project=count_next_line

	def set_pass(self,users,password,id_access):
		self.users=users
		self.password=password
		self.id_access=id_access

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





