from PySide2.QtWidgets import (QLabel, QPushButton, QDialog)
from PySide2.QtCore import (QRect,Qt,QFont)
import sys
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #self.resize(300, 300)
        self.setWindowTitle("Cuadro de diálogo")
        #self.etiqueta = QLabel(self)
        self.resize(268, 259)
        self.setStyleSheet(u"QDialog{\n"
		"background-color: rgb(138, 138, 138);\n"
		"border: 2px solid rgb(0, 0, 0) ;\n"
		"}\n"
		"QLabel{\n"
		"color: rgb(255, 255, 255);\n"
		"}\n"
		"\n"
		"QPushButton{\n"
		"background-color: rgb(83, 152, 255);\n"
		"border-radius:10px;\n"
		"border:1px solid rgb(0, 0, 0) ;\n"
		"font: 87 10pt \"Segoe UI Black\"}\n"
		"QPushButton:hover{\n"
		"border-radius:10px;\n"
		"border:1px solid rgb(0, 0, 0) ;\n"
		"background-color:white;\n"
		"font: 87 10pt \"Segoe UI Black\"}")
        self.pButton_alow = QPushButton(self)
        self.pButton_alow.setObjectName(u"pButton_alow")
        self.pButton_alow.setGeometry(QRect(60, 210, 141, 31))
        self.label_mensaje = QLabel(self)
        self.label_mensaje.setObjectName(u"label_mensaje")
        self.label_mensaje.setGeometry(QRect(20, 20, 231, 161))
        font = QFont()
        font.setPointSize(12)
        self.label_mensaje.setFont(font)
        self.label_mensaje.setAlignment(Qt.AlignCenter)
        self.pButton_alow.setText("Aceptar")
