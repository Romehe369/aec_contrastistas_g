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
        self.file_nameREpic=""
        self.estado_adni=False
        self.btn_tick.hide()
        self.btn_aceptar.clicked.connect(self.get_data_frame)
        # Cuando hacemos click en el boton de cargar una imagen
        self.pushButton_cargar.clicked.connect(self.cargar)
        # Cuando hacemos click en el boton de eleminar una imagen
        self.pushButton_delete.clicked.connect(self.limpiar)
        self.btn_deletere.clicked.connect(self.limpiar_re)
        self.lineEditDNI.textChanged.connect(self.verificar_dni)
        self.lineEditName.textChanged.connect(self.upper_name)
        self.lineEditSurname.textChanged.connect(self.upper_surname)
        self.btn_untick.clicked.connect(self.check_this)
        self.btn_tick.clicked.connect(self.uncheck_this)
        self.btn_uplouddni.clicked.connect(self.cargar_redni)
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
    def upper_name(self):
        tex=self.lineEditName.text()
        self.lineEditName.setText(tex.upper())
    def upper_surname(self):
        tex=self.lineEditSurname.text()
        self.lineEditSurname.setText(tex.upper())

    def check_this(self):
        self.estado_adni=True
        self.frame_dni.hide()
        self.btn_tick.show()
        self.btn_untick.hide()
    def uncheck_this(self):
        self.estado_adni=False
        self.btn_tick.hide()
        self.frame_dni.show()
        self.btn_untick.show()
    # verify of number the identid card is true, or is valid
    # number
    def verificar_dni(self):
        # Get of value the lineeditdni
        dni=self.lineEditDNI.text()
        # verify of size to equal 8
        if(len(dni)==8):
            # check the value is decimal
            if(dni.isdecimal()):
                # Buscamos en nuestra base de datos
                act = self.datos.buscar_trabajador(dni)
                # Si el dni  existe nos devuelve un valor diferente de []
                if act is not None:
                    # Si el ya existe le mostramos un mensaje de que ya existe dicho dni
                    QMessageBox.information(self, "Mensaje", "El nro dni ya existe.", QMessageBox.Ok)
                    return False
                else:
                    return True
            elif(len(dni)>=1):
                # Si el valor ingresado no se asemeja a un dni le mostramos que el valro es invalido
                QMessageBox.critical(self, "Mensaje", "El nro dni es invalido \n verifique por favor", QMessageBox.Ok)
                return False
        return False
    # Get of all value to add from Ttrabajdor
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
            salario=0
        finally:
            estado_dni=self.verificar_dni()
            # Obetenmos las caracteristicas de las photos
            if(estado_dni and self.estado_adni==False and salario>=1):
                photo=self.convertToBinaryData()
                photo2=self.convertToBinaryReverse()
                if(nombres!="" and apellidos!="" and self.file_namepic!="" and self.file_nameREpic!=""):
                    self.datos.insertar_trabajador(dni,nombres,apellidos,combo_sexo,fecha_inicio,correo,nro_movil,combo_categoria,salario,photo,photo2)
                    QMessageBox.information(self, "Agregar trabajador", "Se agrego existosamente", QMessageBox.Ok)
                    self.close()
                else:
                    QMessageBox.critical(self, "Agregar trabajador", "Falta agregar foto de DNI", QMessageBox.Ok)
            elif(salario==0 and estado_dni):
                QMessageBox.critical(self, "Agregar trabajador", "Salario invalido", QMessageBox.Ok)
            elif (estado_dni and self.estado_adni and nombres!="" and apellidos!=""):
                self.datos.insertar_trabajador(dni,nombres,apellidos,combo_sexo,fecha_inicio,correo,nro_movil,combo_categoria,salario,None,None)
                QMessageBox.information(self, "Agregar trabajador", "Se agrego existosamente", QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.critical(self, "Agregar trabajador", "No se pudo agregar", QMessageBox.Ok)
                
    def convertToBinaryData(self):
        # Convert digital data to binary format
        if(self.file_namepic!=""):
            with open(self.file_namepic, 'rb') as file:
                binaryData = file.read()
            return binaryData

    def convertToBinaryReverse(self):
        # Convert digital data to binary format
        if(self.file_nameREpic!=""):
            with open(self.file_nameREpic, 'rb') as file:
                binaryData = file.read()
            return binaryData

    def cargar(self):
        fileName=QFileDialog.getOpenFileName(self,"Abrir una imagen",QDir.homePath(),"Imagenes (*.png *.jpg *.jpeg)")
        self.file_namepic=fileName[0]
        if(fileName==""):
            return
        image=QPixmap(fileName[0])
        self.img_dni.setPixmap(image)

    def cargar_redni(self):
        fileName=QFileDialog.getOpenFileName(self,"Abrir una imagen",QDir.homePath(),"Imagenes (*.png *.jpg *.jpeg)")
        self.file_nameREpic=fileName[0]
        if(fileName==""):
            return
        image=QPixmap(fileName[0])
        self.img_dnireverse.setPixmap(image)

    def limpiar(self):
        self.img_dni.clear()

    def limpiar_re(self):
        self.img_dnireverse.clear()