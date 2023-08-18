from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_tkardex import Ui_tkarded

class tkardex(QMainWindow, Ui_tkarded):
	def __init__(self, parent):
		super(tkardex,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)
		#self.setAttribute(Qt.WA_TranslucentBackground)
		self.datos = Registro_datos()
		#self.table_qwk_new_data()
		self.gripSize = 10
		self.estado_buttton=False
		self.estado_btnreturn=False
		self.grip = QSizeGrip(self)
		self.frame_delete.hide()
		self.btn_confirm_delete.hide()
		self.table_qwk_new.hide()
		self.grip.resize(self.gripSize, self.gripSize)
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_close.clicked.connect(self.close)
		#################METODOS##############
		self.btn_delete_rmaterial.clicked.connect(self.close_menu)
		self.lndt_codemat.textChanged.connect(self.add_infodata)
		self.btn_viewdetals.clicked.connect(self.show_info)
	###########################################Mover ventana###########################
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
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
	###########################################Mover ventana###########################
	def show_info(self):
		if(self.estado_buttton):
			self.btn_viewdetals.setText("VER DETALLES")
			self.estado_buttton=False
			self.table_showinfo.show()
			self.table_qwk_new.hide()
		else:
			self.btn_viewdetals.setText("RETORNAR")
			self.estado_buttton=True
			self.table_showinfo.hide()
			self.table_qwk_new.show()

	def add_infodata(self):
		print("Hello world")
		"""param=self.lndt_codemat.text()
		sql="SELECT * FROM ttrabajador WHERE nombres LIKE %s"
		results=self.datos.phrases_similares(sql,param)
		if(results==[]):
			self.lbl_seleccionado_dni.setText("NO EXISTE COINCIDENCIA DE LA BUSQUEDA")
		else:
			self.listWidget_show_s.clear()
			self.listWidget_show_s.addItem("DNI\t"+"   NOMBRES Y APELLIDOS")
			for row in results:
				tex=row[0]+" : "+row[1]+" "+row[2]
				self.listWidget_show_s.addItem(tex)"""

	def close_menu(self):
		if(self.estado_btnreturn):
			self.btn_delete_rmaterial.setText("IR A ELIMINAR")
			self.estado_btnreturn=False
			self.frame_hide.show()
			self.frame_show_btn.show()
			self.frame_delete.hide()
			self.btn_confirm_delete.hide()
		else:
			self.btn_delete_rmaterial.setText("RETORNAR")
			self.estado_btnreturn=True
			self.frame_hide.hide()
			self.frame_show_btn.hide()
			self.frame_delete.show()
			self.btn_confirm_delete.show()

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
		self.frame_delete.hide()
		self.change_header(self.table_qwk_new)
		self.table_qwk_new.setRowCount(20)
		self.table_qwk_new.setColumnCount(11)
		for row in range(100):
			for column in range(11):
				item = QTableWidgetItem("Nombres full {}".format(row+1))
				self.table_qwk_new.setItem(row, column, item)
