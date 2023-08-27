from PySide2.QtWidgets import QApplication
from controllers.main_login import MiApp

if __name__ == "__main__":
    app = QApplication()
    window = MiApp()
    window.show()
    app.exec_()

