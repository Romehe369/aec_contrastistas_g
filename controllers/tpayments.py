from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import date, datetime, timedelta
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
		#self.frame_pagos_new()
		self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_close_pframe.clicked.connect(self.hide_frame)
		#self.btn_allow_pframe.clicked.connect(self.hide_frame)	
		self.table_payments.cellClicked.connect(self.onCellClicked)
		self.btn_show_table.clicked.connect(self.show_frame)
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
	#############################################MODULOS DE ACTIVIDAD###################
	def onCellClicked(self, row, col):
		item = self.table_payments.item(row, col)
		self.lndt_sdni.setText(item.text())
		mes_elegido = self.comboBox_month.currentText()
		self.label_month_add.setText(mes_elegido)

	def contar_dias(self):
		#self.label_all_days.setText("21")
		month_d = self.comboBox_month.currentIndex()+1
		year_d=int(self.lineEdit_year.text())
		dni="76174442"
		#month_d=dia.month
		#year_d=dia.year
		# El inicio de mes
		dia_inicio=date(year_d,month_d,1)
		# fin de mes
		if(month_d==12):
			dia_fin=date(year_d+1,1,1)
		else:
			dia_fin=date(year_d,month_d+1,1)
		fin_mes=dia_fin-timedelta(1)
		count=1
		suma_dias=0
		while(dia_inicio!=fin_mes):
			datos=self.datos.show_all_data(fin_mes)
			if(len(datos)>=1):
				suma_dias+=self.addition_days_new(datos,dni)
			fin_mes=fin_mes-timedelta(1)
			count+=1
		datos=self.datos.show_all_data(dia_inicio)
		if(len(datos)>=1):
			suma_dias+=self.addition_days_new(datos,dni)
		self.label_all_days.setText(str(suma_dias))

	def addition_days_new(self,this_table,dni):
		encontrado=0
		for i in this_table:
			if(dni==i[1] and i[2]):
				encontrado=1
				break
		return encontrado

	def show_frame(self):
		#self.contar_dias()
		self.btn_show_table.setText("TABLA DE DATOS")
		self.frame_princiapl.show()
		self.frame_pagos.show()

	def hide_frame(self):
		self.btn_show_table.setText("Haga click aqui, para mostrar cuadro de pagos")
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
		datos=self.datos.show_all_dni()
		# Create a table by 6 column and 100 row
		self.table_payments.setRowCount(len(datos))
		self.table_payments.setColumnCount(11)
		# We go through the array or matrix
		for row in range(len(datos)):
			for column in range(11):
				if(column<5):
					item = QTableWidgetItem(str(datos[row][column]))
					self.table_payments.setItem(row, column, item)