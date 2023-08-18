from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime, timedelta
import random
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
        self.lista_table=[]
        self.list_id_distribution=[]
        self.datos=Registro_datos()
        self.seleccionado=False
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.table_asistencia.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btn_guardar_asistencia.clicked.connect(self.save_list)
        self.btn_add_new.clicked.connect(self.add_newdistribucion)
        self.btn_search_dni.clicked.connect(self.get_dni)
        self.btn_delete.clicked.connect(self.delete_onelist)
        self.table_asistencia.cellClicked.connect(self.onCellClicked)
        self.dt_fecha_list.dateChanged.connect(self.clear_data)

    def clear_data(self):
        self.call_list_data()

    def delete_onelist(self):
        if(self.seleccionado):
            # Obtenemos el dni de QLineEdit
            dni=self.lineEdit_dni_admin.text()
            pos=0
            for i in range(0,len(self.list_id_distribution)):
                if(dni==self.list_id_distribution[i][1]):
                    pos=i
            id_distr=self.list_id_distribution[pos][0]
            act=self.datos.update_dispresence(id_distr,0)
            if(act):
                self.dialogo.label_mensaje.setText("Se ha quitado\nde la lista")
                self.dialogo.show()
                self.call_list_data()
            else:
                self.dialogo.label_mensaje.setText("No se puedo realizar\nla operación")
                self.dialogo.show()

        else:
            self.dialogo.label_mensaje.setText("Seleccione un\nnro de DNI")
            self.dialogo.show()

    def delete_fromtasistencia(self,dni):
        date_now=self.dt_fecha_list.text()
        # Intersectamos  dni y con la fecha
        datos=self.datos.datemonth_and_dni(date_now,dni)
        if(len(datos)>0):
            this_info=datos[0][0]
            act=self.datos.delete_asistence(this_info)

    def add_exists_dni(self):
        dni=self.lineEdit_dni_admin.text()
        pos=0
        for i in range(0,len(self.list_id_distribution)):
            if(dni==self.list_id_distribution[i][1]):
                pos=i
        id_distr=self.list_id_distribution[pos][0]
        act=self.datos.update_dispresence(id_distr,1)
        if(act):
            return True
        else:
            return False

    def onCellClicked(self, row, col):
        col=1
        item = self.table_asistencia.item(row, col)
        dni=item.text()
        self.lineEdit_dni_admin.setText(dni)
        if(len(dni)==8):
            self.seleccionado=True
        else:
            self.seleccionado=False
        
    def get_dni(self):
        from controllers.tsearch_dni import tsearch_dni
        add_busqueda_dni=tsearch_dni(self)
        add_busqueda_dni.show()

    def add_newdistribucion(self):
        # Se genera el codigo de distribucion
        id_distribucion=self.random_generate()
        code_project=self.parent().code_project
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
                if(self.add_exists_dni()):
                    self.dialogo.label_mensaje.setText("Operacion Exitosa")
                    self.dialogo.show()
                    self.call_list_data()
                else:
                    # Si el ya existe le mostramos un mensaje de que ya existe dicho dni
                    self.dialogo.label_mensaje.setText("El nro dni ya existe")
                    self.dialogo.show()
                    #self.lineEdit_dni_admin.setText("")
            else:
                act = self.datos.buscar_trabajador(dni)
                # Si el dni  existe nos devuelve un valor diferente de []
                if act is not None:
                    act=self.datos.add_distribution_presence(id_distribucion,code_project,dni,1)
                    #self.dialogo.label_mensaje.setText("Operacion Exitosa")
                    #self.dialogo.show()
                    self.call_list_data()
                else:
                    self.dialogo.label_mensaje.setText("El DNI no esta registrado,\nregistre por favor")
                    self.dialogo.show()
        else:
            self.dialogo.label_mensaje.setText("Seleccione un\nnro de DNI")
            self.dialogo.show()

    def exists_inthismonth(self,this_object,dni):
        date_now=self.dt_fecha_list.text()
        # Intersectamos  dni y con la fecha
        datos=self.datos.datemonth_and_dni(date_now,dni)
        if(len(datos)>0):
            this_object.change_state()

    # Si el dni existe en el mes dato, ya no se vuelve ha agregar 
    # A la table asistencia     
    def noexists_this_iddni(self,dni):
        # Obtenemos la fecha
        date_now=self.dt_fecha_list.text()
        # Obtenemos los datos de la fecha de ahora
        datos=self.datos.datemonth_and_dni(date_now,dni)
        # Existe en la bd esta informacion
        if(len(datos)>0):
            return False
        else:
            return True # cuando no hay datos

    def random_generate(self):
        value=""
        # Genera un numero aleatorio de 11 cifras
        for i in range(11):
            value+=str(random.randint(0, 9))
        return value
    # Guarda la lista de los datos
    def save_list(self):
        # Obtenemos el umero de filas
        i=self.table_asistencia.rowCount()
        # Obtenemos el numero de columnas
        j=self.table_asistencia.columnCount()
        # Obetenmos la fecha
        date=self.dt_fecha_list.text()
        # El codigo del proyecto
        code_project=self.parent().code_project
        table=[]
        for row in range(i):
            pos=0
            dni=self.table_asistencia.item(row, 1).text()
            for i in range(0,len(self.list_id_distribution)):
                if(dni==self.list_id_distribution[i][1]):
                    pos=i
            id_distribucion=self.list_id_distribution[pos][0]
            k=self.lista_table[row]
            # Se crea las primeras lineas de la tabla de distribucion
            columna=[id_distribucion,code_project]
            for col in range(j):
                item = self.table_asistencia.item(row, col)
                # get data only that value is different of None
                if(item is not None):
                    columna.append(item.text())
            # Only exist in the data in added
            this_dni=columna[2]
            # (True,True) status le indica si esta pintado
            # Si es (True, True), se agrega el resultado, se crea un nuevo registro
            if(k.status and self.noexists_this_iddni(this_dni)):
                columna.append(1)
                columna.append(None)
                columna.append(None)
                act=self.datos.add_presence(date,columna[0],columna[1],this_dni,columna[5],columna[6],columna[7])
                if(act):
                    self.dialogo.label_mensaje.setText("Se guardo la lista")
                    self.close()
                    self.dialogo.show()
                else:
                    self.dialogo.label_mensaje.setText("No se pudo guardar la lista")
                    self.dialogo.show()
            # El dni existe en la tabla, no se vuelve a gregar el resgistro
            else:
                # Se elimina dicho registro de asitencia, porque se ha descheaqueado
                if(k.status==False):
                    # eliminar por dni un registro de la fecha
                    self.delete_fromtasistencia(this_dni)
                    #act=self.datos.delete_asistence()
                self.dialogo.label_mensaje.setText("Se guardo la lista")
                self.close()
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
        # Solo procesamos cuando los datos sea mayor a 0
        if(len(datos)>0):
            # Recorremos la lista de asistencias
            for i in datos:
                # Agregamos el id_distribucion mas el dni
                self.list_id_distribution.append((i[0],i[2]))
                #Verificamos que no este eliminado de la lista
                if(i[3]):
                    # Obtenemos la informacion del dni de dicho trabajador
                    act = self.datos.buscar_trabajador(i[2])
                    if act!=[]:
                        # Aqui agregamos los nombres y aplelidos despues del DNI
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
            self.exists_inthismonth(checkBoxWidget,datos_fila[1])
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

    def change_state(self):
        # Cambia el estado a checkeado
        self.checkbox.setChecked(True)
        self.btnstate()

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