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
		self.table_qwk_new_data()
		self.gripSize = 10
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_close.clicked.connect(self.close)
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
