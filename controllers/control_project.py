import random
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
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
        self.datos = Registro_datos()
        self.allow_btn.clicked.connect(self.get_all_data)
        self.search_name_db.clicked.connect(self.search_db)
        self.decline_btn.clicked.connect(self.close)
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
        region=self.region_lineEdit.text()
        province=self.province_lineEdit.text()
        district=self.district_lineEdit.text()
        date_start=self.start_dateEdit.text()
        date_end=self.end_dateEdit.text()
        references=self.references_plainTextEdit.toPlainText()
        values=[code_project,name_project,dni_responsible,region,province,district]
        if(self.no_exist_null_value(values)):
            self.datos.insertar_project(code_project,name_project,dni_responsible,region,province,district,date_start,date_end,references)
            self.dialogo.label_mensaje.setText("Se agrego existosamente")
            self.dialogo.show()
            self.close()
        else:
            self.dialogo.label_mensaje.setText("Hay espacios vacios \n por completar")
            self.dialogo.show()


