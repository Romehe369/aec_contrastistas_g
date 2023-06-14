import sys
import time 
from PySide2 import QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
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


g_users=""
g_password=""

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
		self.contrasena_incorrecta.setText('')
		self.usuario_incorrecto.setText('')
		users_entry = self.users.text()
		password_entry = self.password.text()

		users_entry = str("'" + users_entry + "'")
		password_entry = str("'" + password_entry + "'")

		dato1 = self.datos.busca_users(users_entry)
		dato2 = self.datos.busca_password(password_entry)

		fila1 = dato1
		fila2 = dato2

		if fila1 == fila2:	
			if dato1 == [] and dato2 ==[]:
				self.contrasena_incorrecta.setText('Contraseña incorrecta')
				self.usuario_incorrecto.setText('Usuario incorrecto')
			else:
				if dato1 ==[]:
					self.usuario_incorrecto.setText('Usuario incorrecto')
				else:
					dato1 = dato1[0][1]
				if dato2 ==[]:
					self.contrasena_incorrecta.setText('Contraseña incorrecta')
				else:
					dato2 = dato2[0][2]
				

				if dato1 != [] and dato2 != []:
					for i in range(0,99):
						time.sleep(0.02)
						self.progressBar.setValue(i)
						self.cargando.setText('Cargando...')

					self.hide()
					self.ventana = control_aec()
					self.ventana.set_pass(dato1,dato2)
					self.ventana.show()
		else:
			self.contrasena_incorrecta.setText(' Error ')
			self.usuario_incorrecto.setText(' Error ')
			
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
		self.datos = Registro_datos()
		self.call_list_data()
		self.payments_table_data()
		self.table_qwk_new_data()
		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		#acceder a las paginas
		#self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))			
		self.btn_proyectos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_proyectos))
		self.btn_registro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registro))	
		self.btn_asistencia.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_asistencia))
		self.btn_kardex.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_kardex))			
		self.btn_pagos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_pagos))
		self.btn_reportes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_reportes))
		self.btn_admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_adminstracion))	
		# realiza que los table view se ajusten a los datos de entrada
		self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.table_asistencia.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		#control barra de titulos
		self.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.btn_agregar_trabajador.clicked.connect(self.agregar_trabajador)
		self.btn_changes_password.clicked.connect(self.cambiar_password)
		self.bt_cerrar.clicked.connect(lambda: self.close())
		self.btn_ocultar.clicked.connect(self.mover_arriba)
		self.bt_restaurar.hide()
		self.btn_Buscar_pro.clicked.connect(self.add_control_frame)
		# menu lateral
		self.control_proyecto=[]
		self.bt_menu.clicked.connect(self.mover_menu)
		self.oculto=False
		# Agregamos todos los frames e control ocultar y mostrar
		self.frame_encabezados=[self.frame_registro,self.frame_asistencia,self.frame_kardex,self.frame_pagos,self.frame_reportes,self.frame_proyectos,self.frame_administrador]
		# deberia cerrar la ventana
		
		#self.frm_superior_min.connect(self.this_double_click)
		#self.click_count = 0
		self.valor_x=0
		self.name_proyecto=""
		self.proyectos_cod={"PRYCT001":"Valor1","PRYCT002":"Valor2","PRYCT003":"Valor3","PRYCT004":"Valor4"}

	def add_control_frame(self):
		width=200	# ancho
		height=150  # alto
		width_cont=int(self.frame_contenedor_pro.width()/220)
		height_cont=int(self.frame_contenedor_pro.height()/170)
		# Valores de inicio de graficos
		x=10
		y=10
		if(self.valor_x < width_cont):
			if(len(self.control_proyecto)>=1):
				frame=(self.control_proyecto[-1]).get_frame()
				x=frame.x()
				y=frame.y()
				height=frame.height()
				width=frame.width()
				frame_project=control_data(self,"Hola para siempre","Mundo dos",x+width+20,y,width,height)
				frame_project.crear_qframe()
				self.control_proyecto.append(frame_project)
			else:
				frame_project=control_data(self,"Hola","Mundo",x,y,width,height)
				frame_project.crear_qframe()
				self.control_proyecto.append(frame_project)
			self.valor_x+=1

		elif(self.valor_x==width_cont):
			frame=(self.control_proyecto[-1]).get_frame()
			x=10
			y=frame.y()
			height=frame.height()
			width=frame.width()
			frame_project=control_data(self,"Hola variable","Mundo new",x,y+height+20,width,height)
			frame_project.crear_qframe()
			self.control_proyecto.append(frame_project)
			self.valor_x=1

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
		height = self.frame_kardex.height()
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
	def table_qwk_new_data(self):
		self.change_header(self.table_qwk_new)
		self.table_qwk_new.setRowCount(20)
		self.table_qwk_new.setColumnCount(11)
		for row in range(100):
			for column in range(11):
				item = QTableWidgetItem("Nombres full {}".format(row+1))
				self.table_qwk_new.setItem(row, column, item)


	def payments_table_data(self):
		self.change_header(self.table_payments)
		# Create a table by 6 column and 100 row
		self.table_payments.setRowCount(20)
		self.table_payments.setColumnCount(11)
		# We go through the array or matrix
		for row in range(100):
			for column in range(11):
				item = QTableWidgetItem("Nombres full {}".format(row+1))
				self.table_payments.setItem(row, column, item)

	def call_list_data(self):
		# Create a table by 6 column and 100 row
		self.table_asistencia.setRowCount(100)
		self.table_asistencia.setColumnCount(6)
		self.change_header(self.table_asistencia)
		# We go through the array or matrix
		for row in range(100):
			# Create a checkbox and add the table
			checkBoxWidget = CheckBoxWidget()
			self.table_asistencia.setCellWidget(row, 0, checkBoxWidget)
			for column in range(1,6):
				item = QTableWidgetItem("Nombres full {}".format(row+1))
				self.table_asistencia.setItem(row, column, item)
				
class CheckBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxWidget, self).__init__(parent)
        # We give it a style of greater size of Qcheckbox
        self.setStyleSheet("""
        QCheckBox{
        background-color: none;
        }
        QCheckBox:indicator {
        width:40px; 
        height:25 px;
        background-color: white;
        border-radius : 12px;
	    }
	    QCheckBox:indicator:checked {
	        background-color: #00ff00;
	        border-radius : 12px;
	    }""")
        self.checkbox = QCheckBox(self)
        self.checkbox.setMinimumSize(QSize(0, 0))
        layout = QVBoxLayout(self)
        layout.addWidget(self.checkbox)
        # This is necesary about center the object checkbox
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class control_data(QDialog):
	def __init__(self, parent,code_project,name,x,y,width,height):
		super(control_data,self).__init__(parent)
		self.code_project=code_project
		self.name=name
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.qframe=None
		from controllers.control_project import ctrl_project
		self.ui_add=ctrl_project(self)
		self.ui_add.btn_call_list.clicked.connect(self.call_list)

	def call_list(self):
		self.ui_add.close()
		self.parent().stackedWidget.setCurrentWidget(self.parent().page_asistencia)

	def get_frame(self):
		return self.qframe

	def crear_qframe(self):
		# Crear un QFrame y establecer su geometr
		self.qframe = QFrame(self.parent().frame_contenedor_pro)
		self.qframe.setGeometry(QRect(self.x, self.y,self.width, self.height))
		self.qframe.setStyleSheet("background-color: rgb(103, 105, 255);")
		self.lbl_frame = QLabel(self.qframe)
		self.lbl_frame.setText("Proyecto en \n desarrollo \n place")
		self.lbl_frame.setObjectName("txt")
		self.lbl_frame.setGeometry(QRect(10, 10, 180, 90))
		self.lbl_frame.setStyleSheet("font: 75 16pt Arial")
		self.lbl_frame.setAlignment(Qt.AlignCenter)

		self.view_details = QPushButton(self.qframe)
		self.view_details.setObjectName("view_details")
		self.view_details.setGeometry(QRect(10, 110, 180, 30))
		self.view_details.setText("VER DETALLES")
		self.view_details.setStyleSheet("QPushButton{ border: 1px solid rgb(0, 0, 127);\n"
		"border-radius:5px;\n"
		"background-color: rgb(255, 170, 0);\n"
		"font: 75 12pt \"MS Shell Dlg 2\";}\n"
		"QPushButton:hover{ background-color: white;\n"
		"border-radius:5px;}")
		self.view_details.clicked.connect(self.open_project)
		self.view_details.show()
		self.lbl_frame.show()
		self.qframe.show()
		#http://portal.apci.gob.pe/index.php/registros-de-proyectos/item/449-departamento-provincia-distrito
	def open_project(self):
		self.ui_add.show()





