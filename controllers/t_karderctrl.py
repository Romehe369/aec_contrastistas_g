from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import date, datetime, timedelta
from db.conexion  import Registro_datos
from views.ui_tkardex import Ui_tkarded

class tkardex(QMainWindow, Ui_tkarded):
    def __init__(self, parent):
        super(tkardex,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.datos = Registro_datos()
        self.gripSize = 10
        self.estado_buttton=False
        self.estado_btnreturn=False
        self.grip = QSizeGrip(self)
        self.frame_delete.hide()
        self.btn_confirm_delete.hide()
        self.table_qwk_new.hide()
        self.add_infodata()
        self.update_date()
        self.lstw_name.hide()
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.table_showinfo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_qwk_new.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btn_close.clicked.connect(self.close)
        #################METODOS##############
        self.btn_delete_rmaterial.clicked.connect(self.close_menu)
        #self.lndt_codemat.textChanged.connect(self.add_infodata)
        self.btn_viewdetals.clicked.connect(self.show_info)
        self.table_showinfo.cellClicked.connect(self.onCellClicked)
        self.btn_out_material.clicked.connect(self.out_material)
        self.lndt_responsable.textChanged.connect(self.show_listwid)
        self.lstw_name.itemClicked.connect(self.itemClicked_event)
        self.btn_add_devoluciones.clicked.connect(self.devoluciones_add)
    ###########################################Mover ventana###########################
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
    ###########################################Mover ventana###########################
    def show_info(self):
        if(self.estado_buttton):
            self.btn_viewdetals.setText("VER DETALLES")
            self.estado_buttton=False
            self.table_showinfo.show()
            self.table_qwk_new.hide()
        else:
            self.btn_viewdetals.setText("RETORNAR")
            self.estado_buttton=True
            self.table_showinfo.hide()
            self.table_qwk_new.show()
            self.show_tdtable()

    def show_listwid(self):
        self.lstw_name.show()
        self.obtener_similar()

    def update_date(self):
        now = datetime.now()
        d = QDate(now.year, now.month, now.day)
        self.dateEdit.setDate(d)
    def get_dataact(self):
        # Paramets of default
        salidas=0
        entradas=0
        devoluciones=0
        code_material=self.label_codemat.text()
        unidad_medida=self.label_medida.text()
        name_material=self.label_name.text()
        fecha=self.dateEdit.text()
        type_of_word=self.lndt_typeword.text()
        lote=self.lndt_lote.text()
        name_responsable=self.lndt_responsable.text()
        observation=self.observations_ledt.text()
        firma=""
        return [code_material, unidad_medida, fecha, entradas,salidas,devoluciones,type_of_word,lote,name_responsable,observation,firma]

    def devoluciones_add(self):
        name_material=self.label_name.text()
        name_responsable=self.lndt_responsable.text()
        list_atrib=self.get_dataact()
        try:
            cantidad=float(self.label_saldo.text())
            edit_cantidad=float(self.edit_cantidad.text())
        except Exception as e:
            cantidad=0
            edit_cantidad=0
            QMessageBox.critical(self, "Registrar devoluciones", "Cantidad Invalida.", QMessageBox.Ok)
        cantidad=cantidad+edit_cantidad
        saldo=cantidad
        devoluciones=edit_cantidad
        if(cantidad>0 and name_responsable!=""):
            add_datos=self.datos.insert_tkardex(list_atrib[0], list_atrib[1], list_atrib[2], list_atrib[3],list_atrib[4],devoluciones,saldo,list_atrib[6],list_atrib[7],list_atrib[8],list_atrib[9],list_atrib[10])
            if(add_datos):
                sql= """UPDATE tmaterial_distribution SET cantidad = %s  WHERE name_material = %s"""
                val = (cantidad,name_material,)
                dat=self.datos.set_datos(sql,val)
                if(dat):
                    QMessageBox.information(self, "Registrar devoluciones", "Se ha registrado con exito.", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "Registrar devoluciones", "No se pudo registrar, intentelo de nuevo.", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Registrar devoluciones", "No se pudo registrar, intentelo de nuevo.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Registrar devoluciones", "Cantidad invalida o responsable.", QMessageBox.Ok)

    def out_material(self):
        name_material=self.label_name.text()
        name_responsable=self.lndt_responsable.text()
        list_atrib=self.get_dataact()
        try:
            cantidad=float(self.label_saldo.text())
            edit_cantidad=float(self.edit_cantidad.text())
        except Exception as e:
            cantidad=0
            edit_cantidad=0
            QMessageBox.critical(self, "Registrar salidas", "Cantidad Invalida.", QMessageBox.Ok)
        cantidad=cantidad-edit_cantidad
        saldo=cantidad
        salidas=edit_cantidad
        if(cantidad>0 and name_responsable!=""):
            add_datos=self.datos.insert_tkardex(list_atrib[0], list_atrib[1], list_atrib[2], list_atrib[3],salidas,list_atrib[5],saldo,list_atrib[6],list_atrib[7],list_atrib[8],list_atrib[9],list_atrib[10])
            if(add_datos):
                sql= """UPDATE tmaterial_distribution SET cantidad = %s  WHERE name_material = %s"""
                val = (cantidad,name_material,)
                dat=self.datos.set_datos(sql,val)
                if(dat):
                    QMessageBox.information(self, "Registrar salidas", "Se ha registrado con exito.", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "Registrar salidas", "No se pudo registrar, intentelo de nuevo.", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Registrar salidas", "No se pudo registrar, intentelo de nuevo.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Registrar salidas", "Cantidad invalida o responsable.", QMessageBox.Ok)
    def onCellClicked(self, row, col):
        col=0
        code=self.table_showinfo.item(row,col)
        self.label_codemat.setText(code.text())
        item = self.table_showinfo.item(row, col+1)
        self.label_name.setText(item.text())
        cantidad = self.table_showinfo.item(row, col+2)
        self.label_saldo.setText(cantidad.text())
        medida = self.table_showinfo.item(row, col+3)
        self.label_medida.setText(medida.text())

    def add_infodata(self):
        sql = "SELECT * FROM tmaterial_distribution"
        act=self.datos.get_datos(sql)
        self.table_setdata(act)

    def close_menu(self):
        if(self.estado_btnreturn):
            self.btn_delete_rmaterial.setText("IR A ELIMINAR")
            self.estado_btnreturn=False
            self.frame_hide.show()
            self.frame_show_btn.show()
            self.frame_delete.hide()
            self.btn_confirm_delete.hide()
        else:
            self.btn_delete_rmaterial.setText("RETORNAR")
            self.estado_btnreturn=True
            self.frame_hide.hide()
            self.frame_show_btn.hide()
            self.frame_delete.show()
            self.btn_confirm_delete.show()

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

    def obtener_similar(self):
        param=self.lndt_responsable.text()
        sql="SELECT nombres,apellidos FROM ttrabajador WHERE nombres LIKE %s"
        results=self.datos.phrases_similares(sql,param)
        if(results!=[]):
            self.lstw_name.clear()
            for row in results[:3]:
                self.lstw_name.addItem(" "+row[0]+" "+row[1])

    def itemClicked_event(self):
        selected_items = self.lstw_name.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            dato = selected_item.text()
            self.lndt_responsable.setText(str(dato))
        self.lstw_name.hide()

    def table_setdata(self,datos):
        self.change_header(self.table_showinfo)
        self.table_showinfo.setRowCount(len(datos))
        self.table_showinfo.setColumnCount(4)
        for row in range(len(datos)):
            for column in range(0,4):
                item = QTableWidgetItem(str(datos[row][column]))
                self.table_showinfo.setItem(row, column, item)
    def show_tdtable(self):
        label_codemat=self.label_codemat.text()
        if(len(label_codemat)>0):
            query="""SELECT * FROM tkardex WHERE code_material = %s;"""
            val=(label_codemat,)
            act=self.datos.get_datasfull(query,val)
            if(len(act)>0):
                self.table_qwk_new_data(act)
        else:
            self.table_showinfo.setRowCount(0)
            QMessageBox.information(self, "Ver detalles", "Seleccione un material.", QMessageBox.Ok)

    def table_qwk_new_data(self,datos):
        self.frame_delete.hide()
        self.change_header(self.table_qwk_new)
        self.table_qwk_new.setRowCount(len(datos))
        self.table_qwk_new.setColumnCount(10)
        for row in range(len(datos)):
            for column in range(10):
                item = QTableWidgetItem(str(datos[row][column+3]))
                self.table_qwk_new.setItem(row, column, item)
