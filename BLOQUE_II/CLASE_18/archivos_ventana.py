import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.w = 500
        self.h = 250
        self.x = 100
        self.y = 100
        self.titulo = "PROYECTO"
        self.initUI()
    def initUI(self):
        self.setGeometry(self.x,self.y,self.w,self.h)
        self.setWindowTitle(self.titulo)
        #Creamos QLabel
        self.label = QLabel("Esperando...", self)
        self.label.setGeometry(100, 80, 150, 30)


        #Creamos Temporizador
        timer = QTimer(self)
        timer.timeout.connect(self.mostrar_mensaje)
        timer.start(1000)
        self.contador = 0
        self.show()

    def mostrar_mensaje(self):
        self.contador += 1
        print("Hola:", self.contador)
        self.label.setText(str(self.contador))

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    app.exec_()

#help(PyQt5)
#def setGeometry(self, ax: int, ay: int, aw: int, ah: int) -> None: ...
#def setWindowTitle(self, a0: typing.Optional[str]) -> None: ...
#def show(self) -> None: ...

#Crear dos botones con PyQt5 Si se presiona el boton A imprimir "activado" si se presiona el boton B imprimir "desactivado"