from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime, timedelta
import random
from db.conexion  import Registro_datos
from controllers.change_password import Dialogo
from views.ui_table_asistencia import Ui_tasistencia

class tasistencia(QMainWindow, Ui_tasistencia):
	def __init__(self, parent):
		super(tasistencia,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.btn_close.clicked.connect(self.close)
		self.datos = Registro_datos()
		self.gripSize = 10
		self.grip = QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.start_value()
		self.dialogo = Dialogo()
		self.lista_table=[]
		self.list_id_distribution=[]
		self.datos=Registro_datos()
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.table_asistencia.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.btn_guardar_asistencia.clicked.connect(self.save_list)
		self.btn_add_new.clicked.connect(self.add_newdistribucion)
		self.btn_search_dni.clicked.connect(self.get_dni)

	def get_dni(self):
		from controllers.tsearch_dni import tsearch_dni
		add_busqueda_dni=tsearch_dni(self)
		add_busqueda_dni.show()

	def add_newdistribucion(self):
		id_distribucion=self.random_generate()
		code_project=self.parent().code_project
		status=1
		dni=self.lineEdit_dni_admin.text()
		# Verificar que exista en la base de datos de trabajador
		if(len(dni)==8):
			datos=self.datos.list_tasistencia(code_project)
			exists=False
			for i in datos:
				dni_distribution=i[2]
				if(dni_distribution==dni):
					exists=True
					break
			if exists:
				# Si el ya existe le mostramos un mensaje de que ya existe dicho dni
				self.dialogo.label_mensaje.setText("El nro dni ya existe")
				self.dialogo.show()
				#self.lineEdit_dni_admin.setText("")
			else:
				act = self.datos.buscar_trabajador(dni)
				# Si el dni  existe nos devuelve un valor diferente de []
				if act is not None:
					act=self.datos.add_distribution_presence(id_distribucion,code_project,dni,status)
					#self.dialogo.label_mensaje.setText("Operacion Exitosa")
					#self.dialogo.show()
					self.call_list_data()
				else:
					self.dialogo.label_mensaje.setText("El DNI no esta registrado,\nregistre por favor")
					self.dialogo.show()
				
	def random_generate(self):
		value=""
		for i in range(11):
			value+=str(random.randint(0, 9))
		return value

	def save_list(self):
		i=self.table_asistencia.rowCount()
		j=self.table_asistencia.columnCount()
		date=self.dt_fecha_list.text()
		code_project=self.parent().code_project
		table=[]
		for row in range(i):
			id_distribucion=self.list_id_distribution[row]
			k=self.lista_table[row]
			columna=[id_distribucion,code_project]
			for col in range(j):
				item = self.table_asistencia.item(row, col)
				# get data only that value is different of None
				if(item is not None):
					columna.append(item.text())
			if(k.status):
				columna.append(1)
			else:
				columna.append(0)
			columna.append(None)
			columna.append(None)
			act=self.datos.add_presence(date,columna[0],columna[1],columna[2],columna[5],columna[6],columna[7])
			if(act):
				self.dialogo.label_mensaje.setText("Se guardo la lista")
				self.close()
				self.dialogo.show()
			else:
				self.dialogo.label_mensaje.setText("No se pudo guardar la lista")
				self.dialogo.show()


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
	def start_value(self):
		self.change_code_project.setText(self.parent().code_project)
		self.change_name_project.setText(self.parent().name_project)
		self.update_date_now()
	def update_date_now(self):
		now = datetime.now()
		d = QDate(now.year, now.month, now.day)
		self.dt_fecha_list.setDate(d)

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

	def disanable_column(self,size_t):
		for row in range(size_t):
			for col in range(1, 4):
				item = self.table_asistencia.item(row, col)
				item.setFlags(item.flags() & ~Qt.ItemIsEditable)

	def call_list_data(self):
		self.lista_table=[]
		self.list_id_distribution=[]
		code_project=self.parent().code_project
		datos=self.datos.list_tasistencia(code_project)
		info_dni=[]
		if(len(datos)>0):
			for i in datos:
				self.list_id_distribution.append(i[0])
				act = self.datos.buscar_trabajador(i[2])
				if act!=[]:
					info_dni.append(["",i[2],act[1],act[2]])
		# Create a table by 6 column and 100 row
		self.table_asistencia.setRowCount(len(info_dni))
		self.table_asistencia.setColumnCount(6)
		self.change_header(self.table_asistencia)
		# We go through the array or matrix
		for row in range(0,len(info_dni)):
			# Create a checkbox and add the table
			checkBoxWidget = CheckBoxWidget()
			self.lista_table.append(checkBoxWidget)
			self.table_asistencia.setCellWidget(row, 0, checkBoxWidget)
			datos_fila=info_dni[row]
			for column in range(1,len(datos_fila)):
				item = QTableWidgetItem(datos_fila[column])
				self.table_asistencia.setItem(row, column, item)
		self.disanable_column(len(info_dni))


class CheckBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxWidget, self).__init__(parent)
        # We give it a style of greater size of Qcheckbox
        self.status=False
        self.checkbox = QCheckBox(self)
        self.checkbox.setStyleSheet("""
        QCheckBox{
        background-color: none;
        }
        QCheckBox:indicator {
        width:40px; 
        height:26px;
        background-color: white;
        border-radius : 0px;
	    }
	    QCheckBox:indicator:checked {
	        background-color: #00ff00;
	        border-radius : 0px;
	    }""")
        self.checkbox.setMinimumSize(QSize(0, 0))
        self.checkbox.stateChanged.connect(self.btnstate)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.checkbox)
        # This is necesary about center the object checkbox
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self.setLayout(layout)
    def btnstate(self):
    	if self.checkbox.isChecked() == True:
    		self.status=True
    		self.checkbox.setStyleSheet("""
	        QCheckBox{
	        background-color: #00ff00;
	        }
	        QCheckBox:indicator {
	        width:40px; 
	        height:26px;
	        background-color: white;
	        border-radius : 0px;
		    }
		    QCheckBox:indicator:checked {
		        background-color: #00ff00;
		        border-radius : 0px;
		    }""")
    	else:
    		self.status=False
    		self.checkbox.setStyleSheet("""
	        QCheckBox{
	        background-color: none;
	        }
	        QCheckBox:indicator {
	        width:40px; 
	        height:26px;
	        background-color: white;
	        border-radius : 0px;
		    }
		    QCheckBox:indicator:checked {
		        background-color: #00ff00;
		        border-radius : 0px;
		    }""")