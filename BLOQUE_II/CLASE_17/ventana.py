import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.w = 600
        self.h = 300
        self.x = 100
        self.y = 100
        self.titulo = "PROYECTO"
        self.initUI()
    def initUI(self):
        self.setGeometry(self.x,self.y,self.w,self.h)
        self.setWindowTitle(self.titulo)
        #Creamos Label
        label = QLabel("PROTOTIPO - I", self)
        label.move(230, 100)
        p = "font-size: 20px; color: orange"
        label.setStyleSheet(p)

        #Creamos Boton
        boton1 = QPushButton("ACTIVAR", self)
        boton1.move(250, 150)
        boton1.clicked.connect(self.activar)

        #Creamos Slider
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(230, 200, 200, 30)
        slider.valueChanged.connect(self.datos)

        self.show()

    def activar(self):
        print("Activado")

    def datos(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    app.exec_()

#help(PyQt5)
#def setGeometry(self, ax: int, ay: int, aw: int, ah: int) -> None: ...
#def setWindowTitle(self, a0: typing.Optional[str]) -> None: ...
#def show(self) -> None: ...

#Crear dos botones con PyQt5 Si se presiona el boton A imprimir "activado" si se presiona el boton B imprimir "desactivado"