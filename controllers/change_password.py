import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_change_password import Ui_changes_password

class changed_password_uad(QMainWindow,Ui_changes_password):
    def __init__(self, parent):
        super(changed_password_uad,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Recuperamos password del sistema
        self.users=self.parent().users;
        self.password=self.parent().password;
        # Aqui guardamos la nueva contraseña
        self.change_new_password=""
        # Creamos un cuadro de mensaje
        self.btn_cancelar.clicked.connect(self.close)
        self.btn_aceptar.clicked.connect(self.verificar)
        self.label_verificate.hide()
        self.change_valido=False
        self.new_password.textChanged.connect(self.verifacte_pass)
        self.confirm_new_password.textChanged.connect(self.verificar_confirm_pass)
        self.datos = Registro_datos()
        self.start()
        self.frame_superior.mouseMoveEvent = self.mover_ventana

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if self.isMaximized() == False:         
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
    def start(self):
        self.label_users_name.setText(self.users)

    def verifacte_pass(self):
        text=self.new_password.text()
        if(len(text)<8):
            self.label_verificate.show()
            self.change_valido=False
            self.label_verificate.setText("La contraseña debe\nser mayor a 7 caracteres")
        else:
            if(self.is_alnumver(text)==False):
                self.label_verificate.show()
                self.change_valido=False
                self.label_verificate.setText("Debe contener\nnúmeros y letras")
            else:
                self.label_verificate.hide()
                self.change_valido=True
        self.verificar_confirm_pass()

    def is_alnumver(self,password):
        numeric="0123456789"
        for i in password:
            if(i in numeric):
                return True
        return False

    def is_true_change(self):
        new_password=self.new_password.text()
        password_confirm=self.confirm_new_password.text()
        if(len(new_password)>1 and len(password_confirm)>1):
            return new_password==password_confirm
        else:
            return False

    def verificar_confirm_pass(self):
        # Las nuevas contraseñas coinciden
        if(self.is_true_change()):
            self.change_valido=True
            self.confirm_contrasena_incorrecta.setText("La contraseña coincide")
            self.confirm_contrasena_incorrecta.setStyleSheet("color:rgb(0, 255, 0)")
            self.change_new_password=self.confirm_new_password.text()
        # Las contraseñas son diferentes
        else:
            self.change_valido=False
            self.confirm_contrasena_incorrecta.setStyleSheet("color:rgb(255, 0, 0)")
            self.confirm_contrasena_incorrecta.setText("La contraseña no coincide")
        

    def verificar(self):
        # Obtenemos el password de acceso al sistema
        password_old =self.lndt_password.text()
        # Verificamos que el password de anterior conincida
        if(password_old != self.password):
            QMessageBox.information(self, "Cambiar contraseña", "Contraseña principal incorrecto.", QMessageBox.Ok)
            self.lndt_password.setStyleSheet("""
            border-radius:10px;
            font: 75 12pt \"Arial\";
            border:0px;
            background-color: rgb(255, 170, 255);
            """)
        else:
            if(self.is_true_change()):
                act = self.datos.actualiza_password(self.parent().id_access,self.change_new_password)
                self.parent().password=self.change_new_password
                QMessageBox.information(self, "Cambiar contraseña", "Las contraseña se cambio correctamente.", QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.information(self, "Cambiar contraseña", "Las contraseña no se pudo modificar.", QMessageBox.Ok)