import random
from datetime import datetime, timedelta
from PySide2.QtCore import (QDate,QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from views.ui_cuadro_mensaje import Ui_add_cuadro
from db.conexion  import Registro_datos
from views.ui_add_proyecto import Ui_add_project_new
from controllers.change_password import Dialogo

class ctrl_project(QMainWindow,Ui_add_cuadro):
    def __init__(self, parent):
        super(ctrl_project,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Cerrar la ventana principal
        self.btn_decline.clicked.connect(self.close)
        self.label_code_project.setText(self.parent().code_project)
        self.line_break()

    def line_break(self):
        name_project=self.parent().name_project
        split_text=name_project.split(" ")
        len_text=int(len(split_text)/2)+1
        split_text.insert(len_text,"\n")
        text_formal=" ".join(split_text)
        self.label_title.setText(text_formal)

class add_project(QMainWindow,Ui_add_project_new):
    def __init__(self, parent):
        super(add_project,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Cerrar la ventana principal
        self.code_project=self.random_value()
        self.dialogo=Dialogo()
        self.date_now()
        self.number_of_days.setEnabled(False)
        self.datos = Registro_datos()
        self.allow_btn.clicked.connect(self.get_all_data)
        self.search_name_db.clicked.connect(self.search_db)
        self.decline_btn.clicked.connect(self.close)
        self.number_of_days.textChanged.connect(self.validator_check)
        self.checkBox_numbers_of_days.stateChanged.connect(self.activate_num_days)
        self.agregar_datos()
        self.id_region=0
        self.comboBox_region.currentIndexChanged.connect(self.agregar_province)
        self.comboBox_province.currentIndexChanged.connect(self.agregar_distritos)
        #self.region_lineEdit.textChanged.connect(self.set_upper)
        #self.province_lineEdit.textChanged.connect(self.set_upper)
        #self.district_lineEdit.textChanged.connect(self.set_upper)

    def agregar_datos(self):
        act = self.datos.get_region()
        list_new=["-Seleccione-"]+[n[1] for n in act]
        self.comboBox_region.addItems(list_new)
        #self.region_lineEdit.setText(self.region_lineEdit.text().upper())
        #self.province_lineEdit.setText(self.province_lineEdit.text().upper())
        #self.district_lineEdit.setText(self.district_lineEdit.text().upper())
        
    def agregar_province(self):
        self.comboBox_province.clear()
        region = self.datos.get_region()
        index=self.comboBox_region.currentIndex()-1
        id_region=(region[index])[0]
        self.id_region=id_region
        act = self.datos.get_provinces(id_region)
        list_new=["-Seleccione-"]+[n[1] for n in act]
        self.comboBox_province.addItems(list_new)
        
    def agregar_distritos(self):
        self.comboBox_district.clear()
        provinces=self.datos.get_provinces(self.id_region)
        index=self.comboBox_province.currentIndex()-1
        id_province=(provinces[index])[0]
        act = self.datos.get_districts(id_province)
        list_new=["-Seleccione-"]+[n[1] for n in act]
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

    def addition_days(self):
        if(len(self.number_of_days.text())>=1):
            try:
                number_of_days=int(self.number_of_days.text())
            except Exception as e:
                self.dialogo.label_mensaje.setText("Dígite un número válido")
                self.dialogo.show()
            else:
                now = datetime.now()
                time_future = now + timedelta(days=number_of_days)
                d = QDate(time_future.year, time_future.month, time_future.day)
                self.end_dateEdit.setDate(d)

    def validator_check(self):
        if(self.checkBox_numbers_of_days.isChecked()):
            self.addition_days()

    # Search of base data about information of key code_project
    def search_db(self):
        print("No se encontro")
    # generate a random value about existing repetiton
    def random_value(self):
        values_random=self.random_generate()
        self.lbl_code_pro_random.setText(values_random)

    def random_generate(self):
        value=""
        for i in range(8):
            value+=str(random.randint(0, 9))
        return "PRO"+value
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
        dni_responsible=self.id_res_linetext.text()
        region=self.comboBox_region.currentText()
        province=self.comboBox_province.currentText()
        district=self.comboBox_district.currentText()
        date_start=self.start_dateEdit.text()
        date_end=self.end_dateEdit.text()
        references=self.references_plainTextEdit.toPlainText()
        values=[code_project,name_project,dni_responsible,region,province,district]
        if(self.no_exist_null_value(values)):
            self.datos.insertar_project(code_project,name_project,dni_responsible,region,province,district,date_start,date_end,references)
            self.dialogo.label_mensaje.setText("Se agrego existosamente")
            self.parent().add_control_frame()
            self.dialogo.show()
            self.close()
        else:
            self.dialogo.label_mensaje.setText("Hay espacios vacios \n por completar")
            self.dialogo.show()


