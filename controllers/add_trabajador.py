from PySide2.QtCore import Qt, QDir
from PySide2.QtGui import  QPixmap
from PySide2.QtWidgets import *

from controllers.change_password import Dialogo
from db.conexion  import Registro_datos
from views.ui_add_worker import Ui_Dialog_add_Trabajador

class new_trabajador(QMainWindow, Ui_Dialog_add_Trabajador):
	def __init__(self, parent):
		super(new_trabajador,self).__init__(parent)
		self.setupUi(self)
		#eliminar barra
		self.setWindowFlag(Qt.FramelessWindowHint)
		# Hacer transparente
		self.setAttribute(Qt.WA_TranslucentBackground)
		# crear un mensaje
		self.dialogo = Dialogo()
		# Variables de control
		self.dni_true=False
		self.file_namepic=""
		self.btn_aceptar.clicked.connect(self.get_data_frame)
		self.btn_cancelar.clicked.connect(self.close)
		# Cuando hacemos click en el boton de cargar una imagen
		self.pushButton_cargar.clicked.connect(self.cargar)
		# Cuando hacemos click en el boton de eleminar una imagen
		self.pushButton_delete.clicked.connect(self.limpiar)
		self.lineEditDNI.textChanged.connect(self.verificar_dni)
		self.datos = Registro_datos()

	def verificar_dni(self):
		# Recuperamos los valores de lineeditdni
		dni=self.lineEditDNI.text()
		# verificamos que sea todo nuemrico
		if(dni.isdecimal()):
			# Buscamos en nuestra base de datos
			act = self.datos.buscar_trabajador(dni)
			# Si el dni  existe nos devuelve un valor diferente de none
			if act is not None:
				# Si el ya existe le mostramos un mensaje de que ya existe dicho dni
				self.dialogo.label_mensaje.setText("El nro dni ya existe")
				self.dialogo.show()
		elif(len(dni)>=1):
			# Si el valor ingresado no se asemeja a un dni le mostramos que el valro es invalido
			self.dialogo.label_mensaje.setText("El nro dni es invalido \n verifique por favor")
			self.dialogo.show()

	def get_data_frame(self):
		dni=self.lineEditDNI.text()
		nombres=self.lineEditName.text()
		apellidos=self.lineEditSurname.text()
		combo_sexo=self.comboBox_sexo.currentText()
		fecha_inicio=self.dateEdit_fecha_init.text()
		combo_categoria=self.comboBox_categoria.currentText()
		correo=self.lineEdit_Correo.text()
		nro_movil=self.lineEdit_celular.text()
		# Obetenmos las caracteristicas de las photos
		if(self.file_namepic!=""):
			photo=self.convertToBinaryData()
			if(dni!="" and nombres!="" and apellidos!=""):
				self.datos.insertar_trabajador(dni,nombres,apellidos,combo_sexo,fecha_inicio,correo,nro_movil,combo_categoria,photo)
				self.dialogo.label_mensaje.setText("Se agrego existosamente")
				self.file_namepic=""
				self.dialogo.show()
				self.close()
			else:
				self.dialogo.label_mensaje.setText("Hay espacios vacios \n por completar")
				self.dialogo.show()
		else:
			self.dialogo.label_mensaje.setText("Falta agregar \n la foto de DNI")
			self.dialogo.show()

	def convertToBinaryData(self):
	    # Convert digital data to binary format
	    with open(self.file_namepic, 'rb') as file:
	    	binaryData = file.read()
	    return binaryData

	def cargar(self):
		fileName=QFileDialog.getOpenFileName(self,"Abrir una imagen",QDir.homePath(),"Imagenes (*.png *.jpg *.jpeg)")
		self.file_namepic=fileName[0]
		if(fileName==""):
			return
		image=QPixmap(fileName[0])
		self.img_dni.setPixmap(image)

	def limpiar(self):
		self.img_dni.clear()