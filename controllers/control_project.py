import random
from datetime import datetime, timedelta
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from views.ui_cuadro_mensaje import Ui_add_cuadro
from db.conexion  import Registro_datos
from views.ui_add_proyecto import Ui_add_project_new

class ctrl_project(QMainWindow,Ui_add_cuadro):
    def __init__(self, parent):
        super(ctrl_project,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Cerrar la ventana principal
        self.label_code_project.setText(self.parent().code_project)
        self.label_title.setText(self.line_break())
        self.frame.mouseMoveEvent = self.mover_ventana

    def line_break(self):
        name_project=self.parent().name_project
        split_text=name_project.split(" ")
        len_text=int(len(split_text)/2)+1
        split_text.insert(len_text,"\n")
        text_formal=" ".join(split_text)
        return text_formal

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if self.isMaximized() == False:         
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

class add_project(QMainWindow,Ui_add_project_new):
    def __init__(self, parent):
        super(add_project,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Cerrar la ventana principal
        self.date_now()
        self.number_of_days.setEnabled(False)
        self.datos = Registro_datos()
        self.allow_btn.clicked.connect(self.get_all_data)
        self.search_name_db.clicked.connect(self.search_db)
        self.btn_close.clicked.connect(self.close)
        self.number_of_days.textChanged.connect(self.validator_check)
        self.checkBox_numbers_of_days.stateChanged.connect(self.activate_num_days)
        self.agregar_datos() #frame_contenedor
        self.id_region=0
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.comboBox_region.currentIndexChanged.connect(self.agregar_province)
        self.comboBox_province.currentIndexChanged.connect(self.agregar_distritos)
        self.code_project=self.random_value()
        self.start_dateEdit.dateChanged.connect(self.random_value)

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

    def agregar_datos(self):
        act = self.datos.get_region()
        list_new=["-Seleccione-"]+[n[1] for n in act]
        self.comboBox_region.addItems(list_new)
        self.comboBox_province.addItems(["-Seleccione-"])
        self.comboBox_district.addItems(["-Seleccione-"])

    def agregar_province(self):
        self.comboBox_province.clear()
        region = self.datos.get_region()
        index=self.comboBox_region.currentIndex()-1
        if(index>-1 and len(region)>0):
            id_region=(region[index])[0]
            self.id_region=id_region
            act = self.datos.get_provinces(id_region)
            list_new=["-Seleccione-"]+[n[1] for n in act]
        else:
            list_new=["-Seleccione-"]
        self.comboBox_province.addItems(list_new)
        
    def agregar_distritos(self):
        self.comboBox_district.clear()
        provinces=self.datos.get_provinces(self.id_region)
        index=self.comboBox_province.currentIndex()-1
        if(index>-1 and len(provinces)>0):
            id_province=(provinces[index])[0]
            act = self.datos.get_districts(id_province)
            list_new=["-Seleccione-"]+[n[1] for n in act]
        else:
            list_new=["-Seleccione-"]
        self.comboBox_district.addItems(list_new)

    def activate_num_days(self):
        if(self.checkBox_numbers_of_days.isChecked()):
            self.number_of_days.setEnabled(True)
            self.number_of_days.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.number_of_days.setPlaceholderText("Ingrese el número de días")
        else:
            self.number_of_days.clear()
            self.number_of_days.setStyleSheet("background-color: rgb(0, 255, 255);")
            self.number_of_days.setPlaceholderText("Active cantidad de días")
            self.number_of_days.setEnabled(False)

    def date_now(self):
        now = datetime.now()
        d = QDate(now.year, now.month, now.day)
        self.start_dateEdit.setDate(d)
        self.end_dateEdit.setDate(d)

    def random_value(self):
        self.lbl_code_pro_random.clear()
        values_random=self.random_generate()
        self.lbl_code_pro_random.setText(values_random)

    def random_generate(self):
        date=self.start_dateEdit.date()
        year = date.year()
        fecha=[date.month(),date.day()]
        A=[str(0)+str(n) if len(str(n)) == 1 else n for n in fecha]
        value="PRO"+str(year)+str(A[0])+str(A[1])
        for i in range(3):
            value+=str(random.randint(0, 9))
        return value

    def addition_days(self):
        if(len(self.number_of_days.text())>=1):
            try:
                number_of_days=int(self.number_of_days.text())
            except Exception as e:
                QMessageBox.information(self, "Calcular días", "Dígite un número válido.", QMessageBox.Ok)
            else:
                date=self.start_dateEdit.date()
                now = datetime(date.year(), date.month(), date.day())
                time_future = now + timedelta(days=number_of_days)
                d = QDate(time_future.year, time_future.month, time_future.day)
                self.end_dateEdit.setDate(d)

    def validator_check(self):
        if(self.checkBox_numbers_of_days.isChecked()):
            self.addition_days()

    # Search of base data about information of key code_project
    def search_db(self):
        from controllers.tsearch_dni import tsearch_dni
        add_busqueda_dni=tsearch_dni(self)
        add_busqueda_dni.show()
    # Check the exist value of null
    def no_exist_null_value(self,list_value):
        for i in list_value:
            if(i==""):
                return False
        return True
    # get data of the line edit text
    def get_all_data(self):
        code_project=self.lbl_code_pro_random.text()
        name_project=self.name_project_lineEdit.text()
        dni_responsible=self.lineEdit_dni_admin.text()
        region=self.comboBox_region.currentText()
        province=self.comboBox_province.currentText()
        district=self.comboBox_district.currentText()
        date_start=self.start_dateEdit.text()
        date_end=self.end_dateEdit.text()
        references=self.references_plainTextEdit.toPlainText()
        values=[code_project,name_project,dni_responsible,region,province,district]
        if(self.no_exist_null_value(values)):
            self.datos.insertar_project(code_project,name_project,dni_responsible,region,province,district,date_start,date_end,references)
            QMessageBox.information(self, "Agregar proyecto", "Se agrego existosamente.", QMessageBox.Ok)
            self.parent().ui_add_project=None
            self.parent().add_control_frame()
            self.close()
        else:
            QMessageBox.information(self, "Agregar proyecto", "Hay espacios vacios por completar.", QMessageBox.Ok)



