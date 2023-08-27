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
    def update_date(self):
        now = datetime.now()
        d = QDate(now.year, now.month, now.day)
        self.dateEdit.setDate(d)

    def onCellClicked(self, row, col):
        col=0
        item = self.table_showinfo.item(row, col)
        self.label_name.setText(item.text())
        cantidad = self.table_showinfo.item(row, col+1)
        self.label_saldo.setText(cantidad.text())
        medida = self.table_showinfo.item(row, col+2)
        self.label_medida.setText(medida.text())

    def add_infodata(self):
        sql = "SELECT name,cantidad,medida FROM tmarial_distribution"
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

    def table_setdata(self,datos):
        self.change_header(self.table_showinfo)
        self.table_showinfo.setRowCount(len(datos))
        self.table_showinfo.setColumnCount(3)
        for row in range(len(datos)):
            for column in range(3):
                item = QTableWidgetItem(str(datos[row][column]))
                self.table_showinfo.setItem(row, column, item)

    def table_qwk_new_data(self):
        self.frame_delete.hide()
        self.change_header(self.table_qwk_new)
        self.table_qwk_new.setRowCount(20)
        self.table_qwk_new.setColumnCount(11)
        for row in range(100):
            for column in range(11):
                item = QTableWidgetItem("Nombres full {}".format(row+1))
                self.table_qwk_new.setItem(row, column, item)
