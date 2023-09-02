import sys
import time 
import random
from datetime import datetime, timedelta
from PySide2.QtCore import (QEasingCurve,QDate,QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from db.conexion  import Registro_datos
from views.ui_login import Ui_login
from views.ui_menu import Ui_sistema

from controllers.change_password import changed_password_uad
from controllers.add_trabajador import new_trabajador
from controllers.control_project import add_project

class MiApp(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # evento click para acceder al sistema
        self.bt_ingresar.clicked.connect(self.iniciar_sesion)
        self.btn_close.clicked.connect(self.close)
        # Realizamos una petición a la base de datos de ussers
        self.datos = Registro_datos()
        self.frame_infoaccces.hide()
        self.frame_clave.hide()
        self.estado_btn=False
        self.btn_accessclave.clicked.connect(self.show_setclave)
        self.btn_acceder.clicked.connect(self.verificate_access)
        self.lindt_clave.textChanged.connect(self.upper_clave)
        # Esta clave solo se ejecuta al inicio, cuando no haya ningun usuario 
        self.clave = "AEC99-223P@-3ROTY-MN@97"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.iniciar_sesion()
    def upper_clave(self):
        tex=self.lindt_clave.text()
        self.lindt_clave.setText(tex.upper())

    def show_setclave(self):
        if(self.estado_btn): 
            self.estado_btn=False
            self.frame_ctrl.show()
            self.frame_clave.hide()
        else:
            self.estado_btn=True
            self.frame_ctrl.hide()
            self.frame_clave.show()

    def verificate_access(self):
        tex=self.lindt_clave.text()
        if(self.clave==tex):
            self.ventana = control_aec()
            self.ventana.show()
            self.close()
        else:
            QMessageBox.critical(self, "Acceder", "Clave invalida.", QMessageBox.Ok)

    def iniciar_sesion(self):
        # Los labels de contraseña y usuario ponemos en blanco
        users = self.users.text()
        password_entry = self.password.text()
        users_entry = users
        users_all_information = self.datos.busca_users(users_entry)
        sql = "SELECT * FROM tlogin_data" 
        datos_full=self.datos.get_datos(sql)
        # Cuando no existe ninguna informacion
        if(users_all_information is None and len(datos_full)>0):
            QMessageBox.about(self, "Error al iniciar sesion", "<font color='#3D59AB'><h3> Contraseña o usuario incorrecto <br> intentelo de nuevo por favor</h3></font>")
        else:
            if(len(datos_full)==0):
                self.frame_infoaccces.show()
            else:
                users=users_all_information[2]
                password=users_all_information[3]
                id_access=users_all_information[0]
                if(password_entry==password and users==users_entry):
                    for i in range(0,99):
                        self.progressBar.setValue(i)
                    self.ventana = control_aec()
                    self.ventana.set_pass(users,password,id_access)
                    self.ventana.show()
                    self.close()
                else:
                    QMessageBox.about(self, "Error al iniciar sesion", "<font color='#3D59AB'><h3> Contraseña o usuario incorrecto <br> intentelo de nuevo por favor</h3></font>")

class ClickableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        QMessageBox.about(self, "SISTEMA AEC CONTRATISTAS GENERALES", "<center><h3>SISTEMA DESARROLLADO PARA<br>AEC CONTRATISTAS GENERALES IRL</h3></center>")

class control_aec(QMainWindow,Ui_sistema):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        icon = QIcon()
        icon.addFile("./assets/icono.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.users=""
        self.password=""
        self.alto_qfadd_project=0
        self.code_project=""
        self.name_project=""
        self.datos = Registro_datos()
        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.page_inicio_new()
        self.icnon_menssage()
        #acceder a las paginas
        self.btn_proyectos.clicked.connect(self.click_btn_proyectos)
        self.btn_registro.clicked.connect(self.get_datosregistros)  
        self.btn_kardex.clicked.connect(self.page_kardex)           
        self.btn_pagos.clicked.connect(self.page_pagos)
        self.btn_reportes.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_reportes))
        self.btn_admin.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_adminstracion))
        self.btn_seetable.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_showtable))
        self.btn_add_admin_ctrl.clicked.connect(self.ctrl_frame_add_admin)  
        self.btn_delete_admin_ctrl.clicked.connect(self.ctrl_frame_delete_admin)
        self.table_combo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # btn controls
        self.btn_add_confirm_admin.clicked.connect(self.add_admin_new)
        self.delete_admin_ctrl_btn.clicked.connect(self.delete_bd_admin)
        #control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)        
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.btn_agregar_trabajador.clicked.connect(self.agregar_trabajador)
        self.btn_changes_password.clicked.connect(self.cambiar_password)
        self.btn_ocultar.clicked.connect(self.mover_arriba)
        self.bt_restaurar.hide()
        self.frame_details.hide()
        self.lstw_name.hide()
        self.btn_agregar_pro.clicked.connect(self.add_new_project)
        #self.btn_Buscar_pro.clicked.connect()
        self.lineEdit_add_users.textChanged.connect(self.verificar_users)
        self.v_ScrollBar_project.valueChanged.connect(self.scroll_frame)
        self.btn_search_iddni.clicked.connect(self.show_search_data)
        self.lndt_confirm_password_new.textChanged.connect(self.verificar_pass)
        self.lndt_add_password.textChanged.connect(self.validate_password)
        self.btn_show_admin.clicked.connect(self.show_admin)
        self.tableWidget_admin.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_admin.cellClicked.connect(self.onCellClicked)
        self.btn_add_options.clicked.connect(self.open_options)
        self.btn_add_row.clicked.connect(self.add_row)
        self.btn_save_options.clicked.connect(self.save_tableoptions)
        self.btn_returnsave.clicked.connect(self.get_datosregistros)
        self.btn_registrar_ie.clicked.connect(self.set_factura)
        self.lineEdit_detalle.textChanged.connect(self.this_upperf)
        self.lineEdit_nrodoc.textChanged.connect(self.nrodoc_upper)
        self.lineEdit_coddocu.textChanged.connect(self.change_idmatrial)
        self.btn_add_newmaterial.clicked.connect(self.add_dmaterial)
        self.lineEdit_cantidadmt.textChanged.connect(self.calcular_total)
        self.lineEdit_mntt.textChanged.connect(self.cal_igv)
        self.lineEdit_costounit.textChanged.connect(self.calcular_total)
        self.btn_searchdnipro.clicked.connect(self.show_searchdni)
        self.btn_seednidet.clicked.connect(self.see_detailsdni)
        self.lndt_responsablen.textChanged.connect(self.show_listwid)
        self.lstw_name.itemClicked.connect(self.selected_oneitem)
        self.id_options=[]
        self.list_posndni=[]
        self.list_posproject=[]
        # menu lateral
        self.borrar_elementos()
        self.bt_menu.clicked.connect(self.mover_menu)
        self.oculto=False
        self.code_add_registro=""
        self.reutizable=0
        self.add_busqueda_dni=None
        # Agregamos todos los frames e control ocultar y mostrar
        self.frame_encabezados=[self.frame_reportes,self.frame_proyectos,self.frame_administrador]
        self.valor_x=0
        self.update_date_now()
        self.bt_cerrar.clicked.connect(self.close)

    def closeEvent(self, event):
        cerrar = QMessageBox(self)
        cerrar.setWindowTitle("Salir del sistema AEC")
        cerrar.setIcon(QMessageBox.Question)
        cerrar.setText("¿Estás seguro que desea cerrar el sistema AEC?")
        botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
        botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)    
        cerrar.exec_()    
        if cerrar.clickedButton() == botonSalir:
            event.accept()
        else:
            event.ignore()
    # Asignamos ep dni a la variable dada
    def cal_igv(self):
        try:
            amount=float(self.lineEdit_mntt.text())
        except Exception as e:
            amount=0
        self.lineEdit_igv.setText(str(amount*0.18))

    def calcular_total(self):
        cantidad=self.lineEdit_cantidadmt.text()
        precio=self.lineEdit_costounit.text()
        if(len(cantidad)>0 and len(precio)>0):
            try:
                this_cantidad=float(cantidad)
                this_precio=float(precio)
            except Exception as e:
                this_cantidad=0
                this_precio=0
                QMessageBox.information(self, "Calcular total", "Los datos cantidad o precio son invalido.", QMessageBox.Ok)
            finally:
                total=this_cantidad*this_precio
                self.label_allmt.setText(str(total))
    def show_listwid(self):
        self.lstw_name.show()
        self.obtener_similar()

    def obtener_similar(self):
        param=self.lndt_responsablen.text()
        sql="SELECT nombres,apellidos FROM ttrabajador WHERE nombres LIKE %s"
        results=self.datos.phrases_similares(sql,param)
        if(results!=[]):
            self.lstw_name.clear()
            for row in results:
                self.lstw_name.addItem(row[0]+" "+row[1])

    def selected_oneitem(self):
        selected_items = self.lstw_name.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            dato = selected_item.text()
            self.lndt_responsablen.setText(str(dato))
        self.lstw_name.hide()

    # metodo para agregar un material, va depender si ya existe en la base de datos
    # dicho articulo
    def add_dmaterial(self):
        fecha=self.date_emision.text()
        name_material=self.lineEdit_namematrial.text()
        cantidad=self.lineEdit_cantidadmt.text()
        cantidad_aux=cantidad
        precio=self.lineEdit_costounit.text()
        guia_remision=self.lineEdit_guiaremision.text()
        code_search=self.lineEdit_codefin.text()
        checkBox_reutizable=1
        medida=self.comboBox_medida.currentText()
        month=self.comboBox_mothn.currentText()
        responsable=self.lndt_responsablen.text()
        total=self.label_allmt.text()
        code_material=month[:3]+"."+self.aleatorio_value(6)
        if(self.code_add_registro==""):
            QMessageBox.critical(self, "Registrar material", "Primero registre la factura\n para registrar el material.", QMessageBox.Ok)
        else:
            # Agregamos el material en la bd material
            act=self.datos.add_material(self.code_add_registro, name_material, guia_remision, cantidad, precio, total,checkBox_reutizable)
            if(act):
                # Si existe este material en nuestra bd de tmarial_distrubucion actualizamos solo la cantidad
                sql1="SELECT code_material,cantidad FROM tmaterial_distribution WHERE name_material=%s"
                val1=(name_material,)
                data_exists=self.datos.get_data(sql1,val1)
                if(data_exists):
                    cantidad=data_exists[1]+float(cantidad)
                    add_datos=self.datos.insert_tkardex(data_exists[0], medida, fecha, cantidad_aux,0,0,cantidad,"","",responsable,"","")
                    sql= """UPDATE tmaterial_distribution SET cantidad = %s  WHERE name_material= %s"""
                    val = (cantidad,name_material,)
                    dat=self.datos.set_datos(sql,val)
                else:
                    agregar_new = QMessageBox(self)
                    agregar_new.setWindowTitle("Este material es nuevo")
                    agregar_new.setIcon(QMessageBox.Question)
                    agregar_new.setText("¿Estás seguro que desea agregar?")
                    botonSalir = agregar_new.addButton("SI", QMessageBox.YesRole)
                    botonCancelar = agregar_new.addButton("NO", QMessageBox.NoRole)    
                    agregar_new.exec_()    
                    if agregar_new.clickedButton() == botonSalir:
                        sql= """INSERT INTO tmaterial_distribution(code_material , name_material, cantidad, medida) VALUES(%s,%s,%s,%s)"""
                        val = (code_material,name_material, cantidad, medida,)
                        add_material=self.datos.set_datos(sql,val)
                        if(add_material):
                            sql1="SELECT code_material FROM tmaterial_distribution WHERE name_material=%s"
                            val1=(name_material,)
                            data_exists=self.datos.get_data(sql1,val1)
                            add_datos=self.datos.insert_tkardex(data_exists[0], medida, fecha, cantidad,0,0,cantidad,"","",responsable,"","")
                        else:
                            QMessageBox.critical(self, "Registrar material", "Se genero un error al registrar el material.", QMessageBox.Ok)
                    else:
                        event.ignore()
                    
                QMessageBox.information(self, "Registrar material", "Se ha registrado el material.", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Registrar material", "No se pudo registrar el material.", QMessageBox.Ok)
        
    def check_reutilizable(self):
        if(self.checkBox_reutizable.isChecked()):
            return 1
        else:
            return 0

    def change_idmatrial(self):
        tex=self.lineEdit_coddocu.text()
        self.lineEdit_codefin.setText(tex)

    def this_upperf(self):
        tex=self.lineEdit_detalle.text()
        self.lineEdit_detalle.setText(tex.upper())
        self.lineEdit_namematrial.setText(tex.upper())
    def nrodoc_upper(self):
        tex=self.lineEdit_nrodoc.text()
        self.lineEdit_nrodoc.setText(tex.upper())

    def aleatorio_value(self,dim):
        code=""
        for l in range(0,dim):
            rand=random.randint(0,9)
            if(rand%2==0):
                code+=chr(random.randint(ord('A'), ord('Z')))
            else:
                code+=str(random.randint(0, 9))
        return code
        
    def set_factura(self):
        code_factura=""
        month=self.comboBox_mothn.currentText()
        document_type=self.cmbbox_documents.currentText()
        date_emision=self.date_emision.text()
        rotated_to=self.cmbbox_rotated.currentText()
        name_material=self.lineEdit_detalle.text()
        # Tratamos de convertir en un numero el monto
        try:
            amount=float(self.lineEdit_mntt.text())
        except Exception as e:
            amount=0
        payment_method=self.cmbbox_mediopay.currentText()
        # Obtenemos el indice para recuperar de la lista
        cost_cname=self.cmbbox_costcenter.currentIndex()
        cost_center=self.list_posproject[cost_cname][0]
        expense_dni=self.cmbbox_responsable.currentIndex()
        expense_made=self.list_posndni[expense_dni][0]
        document_number=self.lineEdit_nrodoc.text()
        date_payments=self.datetime_decline.text()
        igv=self.lineEdit_igv.text()
        check_number=self.check_number.text()
        type_expenditure=self.cmbbox_egreso.currentText()
        observation=self.lineEdit_observation.text()
        code_docuemts=self.lineEdit_coddocu.text() 
        if(len(code_docuemts)==0):
            code_docuemts="0000"
        code_factura=month[:3]+self.aleatorio_value(5)+code_docuemts
        if(name_material=="" or amount==0 or cost_center=="" or expense_made==""):
            QMessageBox.critical(self, "Registrar factura", "Hay espacios vacios.", QMessageBox.Ok)
        else:
            act=self.datos.add_factura(code_factura, date_emision, name_material, date_payments, document_type, document_number, payment_method, check_number, rotated_to, type_expenditure, cost_center, amount, expense_made, igv, observation)
            if(act):
                self.code_add_registro=code_factura
                QMessageBox.information(self, "Registrar factura", "Se ha registrado la factura.", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Registrar factura", "No se ha podido registrar la factura.", QMessageBox.Ok)

    def get_datosregistros(self):
        self.list_posndni=[]
        self.pages.setCurrentWidget(self.page_registro)
        datos=self.datos.get_option()
        self.cmbbox_documents.clear()
        self.cmbbox_rotated.clear()
        self.cmbbox_mediopay.clear()
        self.cmbbox_costcenter.clear()
        self.cmbbox_responsable.clear()
        self.cmbbox_egreso.clear()
        self.comboBox_medida.clear()
        #Agregamos la lista de tipo de documentos
        for i in datos:
            tex=i[1]
            if tex is not None:
                self.cmbbox_documents.addItems([i[1]])
        # Agregamos los nombres de girado a
        for i in datos:
            tex=i[2]
            if tex is not None:
                self.cmbbox_rotated.addItems([i[2]])
        for i in datos:
            tex=i[3]
            if tex is not None:
                self.cmbbox_mediopay.addItems([i[3]])
        # Agregamos los dni de los responsable 
        for i in datos:
            tex=i[4]
            sql = "SELECT dni,nombres,apellidos FROM ttrabajador WHERE dni=%s" 
            val = (tex,)
            datos_bd=self.datos.get_data(sql,val)
            self.list_posndni=self.list_posndni+[datos_bd]
            if(datos_bd is not None):
                self.cmbbox_responsable.addItems([datos_bd[1]+" "+datos_bd[2]])
        for i in datos:
            tex=i[5]
            if tex is not None:
                self.cmbbox_egreso.addItems([i[5]])
        for i in datos:
            tex=i[6]
            if tex is not None:
                self.comboBox_medida.addItems([i[6]])
        sql = "SELECT code_project,name FROM tproject GROUP BY code_project" 
        datos_bd=self.datos.get_datos(sql)
        self.list_posproject=datos_bd
        for i in datos_bd:
            tex=i[1]
            if tex is not None:
                self.cmbbox_costcenter.addItems([tex])
    def show_searchdni(self):
        self.show_search_data()
        self.btn_seednidet.show()
        self.frame_details.hide()

    def see_detailsdni(self):
        self.lineEdit_gettingdni.setText(self.lineEdit_dni_admin.text())
        self.frame_details.show()
        self.btn_seednidet.hide()
    # Agregar una fila al evento btn
    def add_row(self):
        current_row_count = self.table_combo.rowCount()
        self.table_combo.setRowCount(current_row_count + 1)
    # Dar formato de tamanio de las tabla
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
    # Obtenemos los de la base de datos
    def open_options(self):
        # Realizamos la conexion con la db
        datos=self.datos.get_option()
        self.id_options=[]
        self.pages.setCurrentWidget(self.page_add_combo)
        self.table_combo.setRowCount(len(datos))
        # Indicamos el tamnio de la table
        self.table_combo.setColumnCount(7)
        self.change_header(self.table_combo)
        if(datos!=[]):
            for row in range(len(datos)):
                self.id_options.append(datos[row][0])
                for column in range(1,8):
                    item = QTableWidgetItem(datos[row][column])
                    self.table_combo.setItem(row, column-1, item)

    def save_tableoptions(self):
        # Obtenemos el umero de filas
        i=self.table_combo.rowCount()
        # Obtenemos el numero de columnas
        j=self.table_combo.columnCount()
        for row in range(i):
            column=[]
            for col in range(j):
                item = self.table_combo.item(row, col)
                # get data only that value is different of None
                if(item is not None):
                    info=item.text()
                    if(info!=""):
                        column.append(info)
                    else:
                        column.append(None)
                else:
                    column.append(None)
            # Verifica si todos los elementos de la fila son vacias
            result=all(element is None for element in column)
            # Si una fila esta vacia se elimina dicha fila
            if(result and i==len(self.id_options)):
                act=self.datos.delete_options(self.id_options[row])
            else:
                # No esta vacio pero se ha modificado
                if(row<len(self.id_options)):
                    act=self.datos.update_option(self.id_options[row],column[0],column[1],column[2],column[3],column[4],column[5],column[6])
                # Verifica que no este vacio y lo agrega
                elif(result==False):
                    act=self.datos.set_option(column[0],column[1],column[2],column[3],column[4],column[5],column[6])
        QMessageBox.information(self, "Agregar opciones de tabla", "Se guardo las modificaciones.", QMessageBox.Ok)
        self.get_datosregistros()

    def onCellClicked(self, row, col):
        item = self.tableWidget_admin.item(row, 3)
        self.lndt_delete_id.setText(item.text())

    def page_kardex(self):
        from controllers.t_karderctrl import tkardex
        tkardex_frame=tkardex(self)
        tkardex_frame.show()
        self.return_home()

    def page_pagos(self):
        from controllers.tpayments import tpaymentst
        payments=tpaymentst(self)
        self.pages.setCurrentWidget(self.page_inicio)
        self.return_home()
        payments.show()

    def show_search_data(self):
        from controllers.tsearch_dni import tsearch_dni
        self.add_busqueda_dni=tsearch_dni(self)
        self.add_busqueda_dni.show()
    # Retorna al anterior punto de llamada
    def return_home(self):
        self.lbl_name_welcome.setText("SISTEMA")
        self.lbl_mensaje_show.setText("La asistencia se controla desde menu proyectos")
        self.page_inicio_new()
    def open_attendance(self):
        from controllers.tcall_list import tasistencia
        self.table_attendece=tasistencia(self)
        self.table_attendece.show()
        self.table_attendece.call_list_data()
        #self.pages.setCurrentWidget(self.page_asistencia)

    def page_inicio_new(self):
        self.pages.setCurrentWidget(self.page_inicio)
    def icnon_menssage(self):
        self.label_nameaec = ClickableLabel(self.frame_lateral)
        self.label_nameaec.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_nameaec.setText("AEC CONTRATISTAS \n GENERALES")
        self.label_nameaec.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_nameaec)

    def update_date_now(self):
        now = datetime.now()
        d = QDate(now.year, now.month, now.day)
        self.date_emision.setDate(d)
        self.datetime_decline.setDate(d)
        self.comboBox_mothn.setCurrentIndex(now.month-1)

    def click_btn_proyectos(self):
        self.pages.setCurrentWidget(self.page_proyectos)
        self.add_control_frame()

    def borrar_elementos(self):
        self.datos = Registro_datos()
        while self.gridLayout_add_frame.count() > 0:
            child = self.gridLayout_add_frame.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def scroll_frame(self):
        width=self.frame_contenedor_proyec.width()-9
        height=self.frame_contenedor_proyec.height()-9
        self.frame_contexto.setFixedSize(width, height)
        self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.alto_qfadd_project*190)
        # Actualizar la posición vertical del QFrame según el valor de la QScrollBar
        value = self.v_ScrollBar_project.value()
        height_cont=int(self.frame_contenedor_pro.height()/100)
        self.frame_contenedor_pro.move(self.frame_contenedor_pro.x(), -value*height_cont)

    def show_admin(self):
        list_users=self.datos.showfull_admin()
        self.tableWidget_admin.setRowCount(len(list_users))
        self.tableWidget_admin.setColumnCount(5)
        for row in range(len(list_users)):
            dni_admin=list_users[row][0]
            act=self.datos.buscar_trabajador(dni_admin)
            pos=1
            for column in range(5):
                if(column<3):
                    item = QTableWidgetItem(act[column])
                    self.tableWidget_admin.setItem(row, column, item)
                else:
                    item = QTableWidgetItem(list_users[row][pos])
                    self.tableWidget_admin.setItem(row, column, item)
                    pos+=1

    # Eliminamos un administrador del sistema
    def delete_bd_admin(self):
        # Obtenemos el dni- o users
        users_dni=self.lndt_delete_id.text()
        # Verificamos que exista algun dato
        if(users_dni==""):
            QMessageBox.information(self, "Eliminar administrador", "Completa los datos correctamente.", QMessageBox.Ok)
        else:
            estado=self.datos.elimina_admin(users_dni)
            if(estado):
                QMessageBox.information(self, "Eliminar administrador", "Operacion exitosa.", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Eliminar administrador", "No existe el DNI o users\nen la base de datos.", QMessageBox.Ok)

    def add_admin_new(self):
        # Recuperamos los datos
        users=self.lineEdit_add_users.text()
        password=self.lndt_add_password.text()
        password_conf=self.lndt_confirm_password_new.text()
        dni=self.lineEdit_dni_admin.text()
        if(users=="" or password=="" or dni=="" or password_conf=="" or len(users)<=5):
            QMessageBox.information(self, "Agregar administrador", "Completa los datos correctamente.", QMessageBox.Ok)
        else:
            if(password==password_conf):
                self.datos.add_admin(dni,users, password)
                self.lineEdit_add_users.setText("")
                self.lndt_add_password.setText("")
                self.lndt_confirm_password_new.setText("")
                QMessageBox.information(self, "Agregar administrador", "Se agrego correctamente.", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Agregar administrador", "Error en confirmar contraseña.", QMessageBox.Ok)

    def verificar_pass(self):
        password=self.lndt_add_password.text()
        confirm=self.lndt_confirm_password_new.text()
        if(password!=confirm):
            self.label_confirmation.setText("No coincide la contraseña")
        else:
            self.label_confirmation.setText("")

    def validate_password(self):
        text=self.lndt_add_password.text()
        if(len(text)<8 and len(text)>=1):
            self.label_validate.setText("La contraseña debe\nser mayor a 7 caracteres")
        else:
            if(self.is_alnumver(text)==False and len(text)>=1):
                self.label_validate.setText("Debe contener\nnúmeros y letras")
            else:
                self.label_validate.setText("")

    def is_alnumver(self,password):
        numeric="0123456789"
        for i in password:
            if(i in numeric):
                return True
        return False

    def verificar_users(self):
        users=self.lineEdit_add_users.text()
        if(len(users)>5):
            self.label_validate_users.setText("")
            act = self.datos.busca_users(users)
            # Verifica si existe el users en la base de datos
            if act is not None:
                QMessageBox.information(self, "Verificar usuario", "El users ya existe.", QMessageBox.Ok)
                # Mostramos los mensajes y ponemos en blanco los datos
                self.lineEdit_add_users.setText("")
                self.lndt_add_password.setText("")
                self.label_validate_users.setText("")
        elif(len(users)>=1):
            self.label_validate_users.setText("El user debe tener mas de 5 caracteres")
    def ctrl_frame_delete_admin(self):
        self.pages.setCurrentWidget(self.page_delete)

    def ctrl_frame_add_admin(self):
        self.pages.setCurrentWidget(self.page_add_administrator)

    def add_new_project(self):
        self.ui_add_project=add_project(self)
        self.ui_add_project.show()
        
    def add_control_frame(self):
        self.frame_contenedor_data.setMaximumSize(QSize(self.frame_contexto.width(),self.frame_contexto.height()))
        self.borrar_elementos()
        # Aqui se define el ancho y alto de nuestro objeto
        width=200   # ancho del frame a crear
        height=150  # alto del frame a crear
        # Tamanio del conetenedor
        width_cont=int(self.frame_contexto.width()/220)
        height_cont=int(self.frame_contexto.height()/170)
        # obtenemos los datos
        valor=self.datos.show_tproject() 
        # Contador para detener el bucle while
        contador_bucle=0
        count_next_line=0
        # Crear la cantidad de elementos necesarios
        while(contador_bucle<len(valor)):
            count_column=0
            while(count_column<width_cont and contador_bucle<len(valor)):
                valor_add=valor[contador_bucle]
                frame_project=control_data(self,valor_add[0],valor_add[1],count_next_line,count_column)
                frame_project.crear_qframe()
                self.gridLayout_add_frame.addWidget(frame_project.get_frame(),count_next_line,count_column,1,1)
                #increment in each iter
                contador_bucle+=1
                count_column+=1
            count_next_line+=1
            if(self.alto_qfadd_project>1):
                self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.alto_qfadd_project*190)

            elif(count_next_line>=4):
                self.frame_contenedor_pro.setFixedSize(self.frame_contenedor_pro.width(),self.frame_contenedor_pro.height()+190)
        self.alto_qfadd_project=count_next_line

    def set_pass(self,users,password,id_access):
        self.users=users
        self.password=password
        self.id_access=id_access

    def cambiar_password(self):
        #from controllers.change_password import changed_password_uad
        self.cambiar=changed_password_uad(self)
        self.cambiar.show()

    def agregar_trabajador(self):
        self.trabajador= new_trabajador(self)
        self.trabajador.show()

    def control_bt_minimizar(self):
        self.showMinimized()        

    def  control_bt_normal(self): 
        self.showNormal()       
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def mover_menu(self):
        # Volvemos los objetos a su posicion
        if True:    
            width = self.frame_lateral.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
            self.animacion.start()

    def mover_arriba(self):
        # verifica si esta oculto
        if(self.oculto):
            for frame_i in self.frame_encabezados:
                frame_i.show()
            self.oculto=False
            self.btn_ocultar.setText("OCULTAR \n ENCABEZADO")

        else:
            self.oculto=True
            for frame_i in self.frame_encabezados:
                frame_i.hide()
            self.btn_ocultar.setText("MOSTRAR \n ENCABEZADO")
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
            
class CopyLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text())
            QMessageBox.information(self, "Copiar codigo", "Se ha copiado.", QMessageBox.Ok)
            
# Se crea un control de la tabla
class control_data(QDialog):
    def __init__(self, parent,code_project,name_project,row,column):
        super(control_data,self).__init__(parent)
        self.code_project=code_project
        self.name_project=name_project
        self.row=row
        self.column=column
        self.qframe=QFrame()
        from controllers.control_project import ctrl_project
        self.ui_add=ctrl_project(self)
        self.ui_add.btn_decline.clicked.connect(self.ui_add.close)
        self.ui_add.btn_call_list.clicked.connect(self.call_list)
        self.ui_add.btn_delete_project.clicked.connect(self.delete_project)

    def delete_project(self):
        delete_pro = QMessageBox(self)
        delete_pro.setWindowTitle("Eliminar proyecto")
        delete_pro.setIcon(QMessageBox.Question)
        delete_pro.setText("¿Esta seguro que desea eliminar este proyecto?")
        button_yes = delete_pro.addButton("Si", QMessageBox.YesRole)
        button_decline = delete_pro.addButton("Cancelar", QMessageBox.NoRole)
        delete_pro.exec_()
        if delete_pro.clickedButton() == button_yes:
            self.delete_frame()

    def delete_frame(self):
        item = self.parent().gridLayout_add_frame.itemAtPosition(self.row, self.column)
        datos = Registro_datos()
        # elimina el objeto seleccionado
        item.widget().deleteLater()
        if(datos.delete_project_bcode(self.code_project)):
            # Actualiza los datos visibles
            self.parent().add_control_frame()
            self.ui_add.close()
            QMessageBox.information(self, "Eliminar proyecto", "Se elimino  correctamente.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Eliminar proyecto", "No se pudo realizar la operacion.", QMessageBox.Ok)

    def call_list(self):
        self.ui_add.close()
        self.parent().code_project=self.code_project
        self.parent().name_project=self.name_project
        self.parent().open_attendance()

    def get_frame(self):
        return self.qframe

    def crear_qframe(self):
        # Crear un QFrame y establecer su geometr
        self.qframe = QFrame(self.parent().frame_contenedor_pro)
        self.qframe.setMinimumSize(QSize(200, 170))
        self.v_layout_frame = QVBoxLayout(self.qframe)
        self.qframe.setStyleSheet("background-color: rgb(103, 105, 255);")

        self.lbl_frame = QLabel(self.qframe)
        self.lbl_frame.setText("Cod. proyecto:")
        self.lbl_frame.setStyleSheet("font: 75 16pt Arial")
        self.lbl_frame.setAlignment(Qt.AlignCenter)
        self.v_layout_frame.addWidget(self.lbl_frame)

        self.lbl_code = CopyLabel(self.qframe)
        self.lbl_code.setText(self.code_project)
        self.lbl_code.setStyleSheet("font: 75 16pt Arial")
        self.lbl_code.setAlignment(Qt.AlignCenter)
        self.v_layout_frame.addWidget(self.lbl_code)

        self.lbl_fr_name = QLabel(self.qframe)
        self.lbl_fr_name.setText("Nombre :\n"+self.ui_add.line_break())
        self.lbl_fr_name.setStyleSheet("font: 75 16pt Arial")
        self.lbl_fr_name.setAlignment(Qt.AlignCenter)
        self.v_layout_frame.addWidget(self.lbl_fr_name)
        self.view_details = QPushButton(self.qframe)
        self.view_details.setMinimumSize(QSize(0, 31))
        self.view_details.setText("VER DETALLES")
        self.view_details.setStyleSheet("QPushButton{ border: 1px solid rgb(0, 0, 127);\n"
        "border-radius:5px;\n"
        "background-color: rgb(255, 170, 0);\n"
        "font: 75 12pt \"MS Shell Dlg 2\";}\n"
        "QPushButton:hover{ background-color: white;\n"
        "border-radius:5px;}")
        self.v_layout_frame.addWidget(self.view_details)
        self.view_details.clicked.connect(self.open_project)
        self.view_details.show()
        self.lbl_frame.show()
        self.qframe.show()
    
    def open_project(self):
        self.ui_add.show()





