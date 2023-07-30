from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime, timedelta

from db.conexion  import Registro_datos
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
		self.frame_superior.mouseMoveEvent = self.mover_ventana
		self.table_asistencia.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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
		code_project=self.parent().code_project
		datos=self.datos.list_tasistencia(code_project)
		info_dni=[]
		if(len(datos)>0):
			for i in datos:
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
        layout = QVBoxLayout(self)
        layout.addWidget(self.checkbox)
        # This is necesary about center the object checkbox
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
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