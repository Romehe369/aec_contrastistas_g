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
		icon = QIcon()
		icon.addFile("./assets/icono.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.datos = Registro_datos()
		self.gripSize = 10
		self.payments_table_data()
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.btn_close.clicked.connect(self.close)
		self.table_detalls.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.table_payments.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_close_pframe.clicked.connect(self.hide_frame)
		#self.btn_allow_pframe.clicked.connect(self.hide_frame)	
		self.table_payments.cellClicked.connect(self.onCellClicked)
		self.btn_show_table.clicked.connect(self.show_frame)
		self.lineEdit_year.textChanged.connect(self.verificar_year)
		self.lndt_adelantos.textChanged.connect(self.calcular)
		self.comboBox_month.currentIndexChanged.connect(self.verifcar_mes)
		self.table_detalls.hide()
		self.estado_btn=False
		self.btn_details.clicked.connect(self.show_information)
		self.btn_dar_adelantos.clicked.connect(self.give_advances)
	############################MOVIMIENTO CUADRO##############################
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
		col=0
		item = self.table_payments.item(row, col)
		self.lndt_sdni.setText(item.text())
		mes_elegido = self.comboBox_month.currentText()
		self.label_month_add.setText(mes_elegido)
		name = self.table_payments.item(row, col+1)
		self.label_name.setText(name.text())
		surname = self.table_payments.item(row, col+2)
		self.label_surnames.setText(surname.text())
		mounth = self.table_payments.item(row, col+4)
		self.label_days_pay.setText(mounth.text())
		self.contar_dias()

	def give_advances(self):
		give_advan = QMessageBox(self)
		periodo=self.label_periodo.text()
		mes=self.label_month_add.text()
		dni=self.lndt_sdni.text()
		total_dias=self.label_all_days.text()
		total_girar=self.label_total.text()
		adelantos=0
		try:
			adelantos=float(self.lndt_adelantos.text())
		except Exception as e:
			adelantos=0
		por_pagar=self.label_porpagar.text()
		observaciones="No especifica"
		estado=0
		if(adelantos<=0):
			QMessageBox.information(self, "Dar adelanto", "Elija un monto mayor.", QMessageBox.Ok)
		else:
			give_advan.setWindowTitle("Dar adelanto al trabajador")
			give_advan.setIcon(QMessageBox.Question)
			give_advan.setText("¿Esta seguro que desea dar adelanto a "+dni+" ? ")
			botonSi = give_advan.addButton("Si", QMessageBox.YesRole)
			botonCancelar = give_advan.addButton("Cancelar", QMessageBox.NoRole)
			give_advan.exec_()
			if give_advan.clickedButton() == botonSi:
				act=self.datos.add_tpagos(periodo,mes,dni,total_dias,total_girar,adelantos,por_pagar,observaciones,estado)
				if(act):
					QMessageBox.information(self, "Dar adelanto", "Se ha dado adelanto.", QMessageBox.Ok)
		
	def show_information(self):
		if(self.estado_btn):
			self.btn_details.setText("VER DETALLES")
			self.estado_btn=False
			self.table_detalls.hide()
			self.table_payments.show()
		else:
			self.btn_details.setText("RETORNAR")
			self.estado_btn=True
			self.table_detalls.show()
			self.table_payments.hide()
			sql="""SELECT * FROM tpagos"""
			act=self.datos.get_datos(sql)
			if(len(act)>0):
				self.show_paymentstable(act)


	def verificar_year(self):
		year=self.lineEdit_year.text()
		if(len(year)==4):
			self.label_periodo.setText(year)
			self.contar_dias()
	def verifcar_mes(self):
		self.label_month_add.setText(self.comboBox_month.currentText())
		self.contar_dias()
	def contar_dias(self):
		# Obtienes el mes
		month_d = self.comboBox_month.currentIndex()+1
		# Obteenmos el anio
		year_d=int(self.lineEdit_year.text())
		# Obtenemos el DNI
		dni=self.lndt_sdni.text()
		# El inicio de mes
		dia_inicio=date(year_d,month_d,1)
		# fin de mes
		if(month_d==12):
			dia_fin=date(year_d+1,1,1)
		else:
			dia_fin=date(year_d,month_d+1,1)
		fin_mes=dia_fin-timedelta(1)
		datos=self.datos.between_month(dia_inicio,fin_mes,dni)
		suma_dias=datos[0][0]
		self.label_all_days.setText(str(suma_dias))
		self.calcular()

	def calcular(self):
		total_dias=int(self.label_all_days.text())
		dia_pay=float(self.label_days_pay.text())
		try:
			adelanto=float(self.lndt_adelantos.text())
		except Exception as e:
			adelanto=0
		adelantos=adelanto
		total=dia_pay*total_dias
		self.label_total.setText(str(total))
		if(total>=adelantos):
			total=total-adelantos;
		else:
			total=0
		self.label_porpagar.setText(str(total))

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

	def show_paymentstable(self,datos):
		self.change_header(self.table_detalls)
		self.table_detalls.setRowCount(len(datos))
		self.table_detalls.setColumnCount(11)
		# We go through the array or matrix
		for row in range(len(datos)):
			# Obtenemos el dni de la bd
			dni_get=datos[row][3]
			# Buscamos los datos en la table trabajador
			get_dnid=self.datos.buscar_trabajador(dni_get)
			data_full=get_dnid+datos[row][4:]
			for column in range(11):
				item = QTableWidgetItem(str(data_full[column]))
				self.table_detalls.setItem(row, column, item)

	# Genera tabla de pagos
	def payments_table_data(self):
		now = datetime.now()
		self.comboBox_month.setCurrentIndex(now.month-1)
		self.change_header(self.table_payments)
		datos=self.datos.show_all_dni()
		# Create a table by 6 column and 100 row
		self.table_payments.setRowCount(len(datos))
		self.table_payments.setColumnCount(5)
		# We go through the array or matrix
		for row in range(len(datos)):
			for column in range(5):
				item = QTableWidgetItem(str(datos[row][column]))
				self.table_payments.setItem(row, column, item)