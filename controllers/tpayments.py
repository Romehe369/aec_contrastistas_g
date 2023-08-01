
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_tpayments import Ui_tpayments

class tpaymentst(QMainWindow, Ui_tpayments):
	def __init__(self, parent):
		super(tpaymentst,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.datos = Registro_datos()
		self.gripSize = 10
		self.payments_table_data()
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.btn_close.clicked.connect(self.close)
		self.frame_pagos_new()
		self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_close_pframe.clicked.connect(self.hide_frame)
		self.btn_allow_pframe.clicked.connect(self.hide_frame)	
		self.btn_pagar.clicked.connect(self.show_frame)
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
	def show_frame(self):
		self.frame_princiapl.hide()
		self.frame_pagos.show()

	def hide_frame(self):
		self.frame_princiapl.show()
		self.frame_pagos.hide()

	def frame_pagos_new(self):
		self.frame_pagos.hide()
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

	# Genera tabla de pagos
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