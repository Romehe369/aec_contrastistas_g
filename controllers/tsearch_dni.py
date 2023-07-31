from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_tsearch_data import Ui_tsearch_dni

class tsearch_dni(QMainWindow, Ui_tsearch_dni):
	def __init__(self, parent):
		super(tsearch_dni,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.btn_close_search.clicked.connect(self.close)
		self.btn_decline.clicked.connect(self.close)
		self.datos = Registro_datos()
		self.dni_admin=""
		self.validate=False
		self.listWidget_show_s.clear()
		self.lineEdit_data_search.textChanged.connect(self.obtener_similar)
		self.listWidget_show_s.itemClicked.connect(self.itemClicked_event)
		self.pushButton_get_dni.clicked.connect(self.asignar_dni)
		self.btn_ampliar.clicked.connect(self.showNormal)
		self.gripSize = 10
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana
	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
	def mover_ventana(self, event):
		if self.isMaximized() == False:         
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()
		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()

	def asignar_dni(self):
		if(self.validate):
			self.parent().lineEdit_dni_admin.setText(self.dni_admin)
			self.dni_admin=""
			self.close()
		else:
			self.lbl_seleccionado_dni.setText("SELECCIONE UN ELEMENTO")

	def obtener_similar(self):
		param=self.lineEdit_data_search.text()
		sql="SELECT * FROM ttrabajador WHERE nombres LIKE %s"
		results=self.datos.phrases_similares(sql,param)
		if(results==[]):
			self.lbl_seleccionado_dni.setText("NO EXISTE COINCIDENCIA DE LA BUSQUEDA")
		else:
			self.listWidget_show_s.clear()
			self.listWidget_show_s.addItem("DNI\t"+"   NOMBRES Y APELLIDOS")
			for row in results:
				tex=row[0]+" : "+row[1]+" "+row[2]
				self.listWidget_show_s.addItem(tex)
	def itemClicked_event(self):
		selected_items = self.listWidget_show_s.selectedItems()
		if selected_items:
			selected_item = selected_items[0]
			dato = selected_item.text()
			if("DNI" in dato):
				self.lbl_seleccionado_dni.setText("DNI : ")
				self.validate=False
			else:
				txt_dni=dato[:8]
				self.dni_admin=txt_dni
				self.validate=True
				self.lbl_seleccionado_dni.setText("DNI : "+txt_dni+"   NOMBRE"+dato[8:])
