from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from db.conexion  import Registro_datos
from views.ui_add_worker import Ui_add_Trabajador

class new_trabajador(QMainWindow, Ui_add_Trabajador):
    def __init__(self, parent):
        super(new_trabajador,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Hacer transparente
        icon = QIcon()
        icon.addFile("./assets/icono.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # crear un mensaje
        # Variables de control
        self.dni_true=False
        self.file_namepic=""
        self.btn_aceptar.clicked.connect(self.get_data_frame)
        # Cuando hacemos click en el boton de cargar una imagen
        self.pushButton_cargar.clicked.connect(self.cargar)
        # Cuando hacemos click en el boton de eleminar una imagen
        self.pushButton_delete.clicked.connect(self.limpiar)
        self.lineEditDNI.textChanged.connect(self.verificar_dni)
        self.btn_close.clicked.connect(self.close)
        self.datos = Registro_datos()
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
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

    def verificar_dni(self):
        # Recuperamos los valores de lineeditdni
        dni=self.lineEditDNI.text()
        # Verificamos que sea de dimension 8
        if(len(dni)==8):
            # verificamos que sea todo nuemrico
            if(dni.isdecimal()):
                # Buscamos en nuestra base de datos
                act = self.datos.buscar_trabajador(dni)
                # Si el dni  existe nos devuelve un valor diferente de []
                if act is not None:
                    # Si el ya existe le mostramos un mensaje de que ya existe dicho dni
                    QMessageBox.information(self, "Mensaje", "El nro dni ya existe.", QMessageBox.Ok)
            elif(len(dni)>=1):
                # Si el valor ingresado no se asemeja a un dni le mostramos que el valro es invalido
                QMessageBox.information(self, "Mensaje", "El nro dni es invalido \n verifique por favor", QMessageBox.Ok)

    def get_data_frame(self):
        dni=self.lineEditDNI.text()
        nombres=self.lineEditName.text()
        apellidos=self.lineEditSurname.text()
        combo_sexo=self.comboBox_sexo.currentText()
        fecha_inicio=self.dateEdit_fecha_init.text()
        combo_categoria=self.comboBox_categoria.currentText()
        correo=self.lineEdit_Correo.text()
        nro_movil=self.lineEdit_celular.text()
        try:
            salario=float(self.lineEdit_salario.text())
        except Exception as e:
            QMessageBox.information(self, "Mensaje", "Escriba el salario de los\n decimales con punto", QMessageBox.Ok)
        else:
            # Obetenmos las caracteristicas de las photos
            if(self.file_namepic!="" and len(dni)==8):
                photo=self.convertToBinaryData()
                if(dni!="" and nombres!="" and apellidos!=""):
                    self.datos.insertar_trabajador(dni,nombres,apellidos,combo_sexo,fecha_inicio,correo,nro_movil,combo_categoria,salario,photo)
                    QMessageBox.information(self, "Mensaje", "Se agrego existosamente", QMessageBox.Ok)
                    self.file_namepic=""
                    self.close()
                else:
                    QMessageBox.information(self, "Mensaje", "Hay espacios vaciospor completar", QMessageBox.Ok)
            elif (len(dni)<8):
                QMessageBox.information(self, "Mensaje", "El número de DNI debe ser de 8 digitos", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Mensaje", "Falta agregar la foto de DNI", QMessageBox.Ok)

    def convertToBinaryData(self):
        # Convert digital data to binary format
        if(self.file_namepic!=""):
            with open(self.file_namepic, 'rb') as file:
                binaryData = file.read()
            return binaryData

    def cargar(self):
        fileName=QFileDialog.getOpenFileName(self,"Abrir una imagen",QDir.homePath(),"Imagenes (*.png *.jpg *.jpeg)")
        self.file_namepic=fileName[0]
        if(fileName==""):
            return
        image=QPixmap(fileName[0])
        self.img_dni.setPixmap(image)

    def limpiar(self):
        self.img_dni.clear()