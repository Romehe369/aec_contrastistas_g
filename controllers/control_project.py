from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from views.ui_cuadro_mensaje import Ui_add_cuadro

class ctrl_project(QMainWindow,Ui_add_cuadro):
    def __init__(self, parent):
        super(ctrl_project,self).__init__(parent)
        self.setupUi(self)
        #eliminar barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Cerrar la ventana principal
        self.btn_decline.clicked.connect(self.close)