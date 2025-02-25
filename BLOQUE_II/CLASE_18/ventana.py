import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/PyQt5/Qt5/plugins"

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QSlider, QProgressBar
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.w = 600
        self.h = 500
        self.x = 100
        self.y = 100
        self.titulo = "PROYECTO"
        self.initUI()
    def initUI(self):
        self.setGeometry(self.x,self.y,self.w,self.h)
        self.setWindowTitle(self.titulo)
        #Creamos Label
        self.label1 = QLabel("PROTOTIPO - I", self)
        self.label1.move(230, 100)
        p = "font-size: 20px; color: orange"
        self.label1.setStyleSheet(p)

        self.label2 = QLabel("VALOR: 0", self)
        self.label2.move(230, 230)
        p = "font-size: 20px; color: orange"
        self.label2.setStyleSheet(p)

        #Creamos Boton
        boton1 = QPushButton("ACTIVAR", self)
        boton1.move(200, 150)
        boton1.clicked.connect(self.activar)

        boton2 = QPushButton("DESACTIVAR", self)
        boton2.move(300, 150)
        boton2.clicked.connect(self.desactivar)

        #Creamos Slider
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(230, 200, 200, 30)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.valueChanged.connect(self.datos)

        #Creamos Barra de progreso
        self.bar = QProgressBar(self)
        self.bar.setGeometry(230, 250, 200, 30)
        self.bar.setValue(0)

        self.show()

    def activar(self):
        print("Activado")
        self.label1.setText("Activado")
        self.label1.adjustSize()

    def desactivar(self):
        print("Desactivado")
        self.label1.setText("Desactivado")
        self.label1.adjustSize()

    def datos(self, data):
        print(data)
        self.label2.setText("Valor: " + str(data))
        self.label2.adjustSize()
        self.bar.setValue(data)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    app.exec_()

#help(PyQt5)
#def setGeometry(self, ax: int, ay: int, aw: int, ah: int) -> None: ...
#def setWindowTitle(self, a0: typing.Optional[str]) -> None: ...
#def show(self) -> None: ...

#Crear dos botones con PyQt5 Si se presiona el boton A imprimir "activado" si se presiona el boton B imprimir "desactivado"