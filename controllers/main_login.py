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
		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		#acceder a las paginas
		#self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))			
		self.btn_proyectos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_proyectos))
		self.btn_registro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registro))	
		self.btn_asistencia.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_asistencia))
		self.btn_trabajadores.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trabajadores))			
		self.btn_pagos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_pagos))
		self.btn_reportes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_reportes))
		self.btn_admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_adminstracion))	
		# realiza que los table view se ajusten a los datos de entrada
		self.table_qwt_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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
		self.frame_encabezados=[self.frame_registro,self.frame_asistencia,self.frame_trabajador,self.frame_pagos,self.frame_reportes,self.frame_proyectos,self.frame_administrador]
		# deberia cerrar la ventana
		
		#self.frm_superior_min.connect(self.this_double_click)
		#self.click_count = 0
		self.valor_x=0
	def add_control_frame(self):
		height=250
		width=250
		height_cont=int(self.frame_contenedor_pro.height()/270)
		width_cont=int(self.frame_contenedor_pro.width()/270)
		if(self.valor_x<=3):
			self.valor_x+=1
			if(len(self.control_proyecto)>=1):
				frame=self.control_proyecto[-1]
				x=frame.x()
				y=frame.y()
				height=frame.height()
				width=frame.width()
				self.control_proyecto.append(self.crear_qframe(x+width+20,y,height,width))
			else:
				x=10
				y=10
				self.control_proyecto.append(self.crear_qframe(x,y,height,width))
		else:
			if(len(self.control_proyecto)>=1):
				frame=self.control_proyecto[-1]
				x=frame.x()
				y=frame.y()
				height=frame.height()
				width=frame.width()
				self.control_proyecto.append(self.crear_qframe(x,y+height+20,height,width))
			else:
				x=10
				y=10
				self.control_proyecto.append(self.crear_qframe(x,y,height,width))

	def crear_qframe(self,x,y,height,width):
		# Crear un QFrame y establecer su geometr
		qframe = QFrame(self.frame_contenedor_pro)
		#qframe.setObjectName("frame_new"+str(x))
		qframe.setGeometry(QRect(x, y, height,width))
		qframe.setStyleSheet("background-color: rgb(103, 105, 255);")
		#qframe.setFrameShape(QFrame.StyledPanel)
		#qframe.setFrameShadow(QFrame.Raised)
		lbl_frame = QLabel(qframe)
		lbl_frame.setText("Hola mundo")
		lbl_frame.show()
		qframe.show()
		return qframe

	def set_pass(self,txt1,txt2):
		self.txt_users=txt1
		self.txt_password=txt2
		#print(self.txt_users,self.txt_password)

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
		height = self.frame_trabajador.height()
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




