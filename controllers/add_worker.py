from PySide2 import QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from views.ui_add_worker import Ui_Dialog_add_Trabajador
import re
import shutil
import os

class new_trabajador(QMainWindow):
    def __init__(self, parent):
        super(new_trabajador,self).__init__(parent)
        self.ventana_worker = Ui_Dialog_add_Trabajador() 
        self.ventana_worker.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        #transparente
        # evento click para acceder al sistema
        self.ventana_worker.btn_aceptar.clicked.connect(self.retorno)

    def retorno(self):
        self.close()
        self.parent().show()
