# -*- encoding: utf-8 -*-
#
# Desarrollado por: Hugo Ruscitti
# Licencia: GPL v3
#
# Basado en los ejemplos de: http://zetcode.com/tutorials/pyqt4/

import sys
import atexit
import signal

from PyQt4 import QtCore
from PyQt4 import QtGui


def ejecutar_main_loop():
    """Se asegura de detener el programa esperando al usuario."""
    sys.exit(Componente.app.exec_())

def iniciar():
    Componente.app = QtGui.QApplication(sys.argv)
    atexit.register(ejecutar_main_loop)
    # Se asegura de que las teclas "ctrl+c" puedan cerrar el programa.
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class Componente(object):
    """Representa el contexto de la aplicacion global."""
    app = False

    def obtener_centro_escritorio(kls):
        return QtGui.QDesktopWidget().availableGeometry().center()

    def mostrar(self):
        self.widget.show()

    def ocultar(self):
        self.widget.hide()

    def definir_posicion(self, x, y):
        self.widget.move(x, y)


class Ventana(Componente):

    def __init__(self, titulo="sin titulo", ancho=320, alto=240, posicion_x=100, posicion_y=100):
        self.widget = QtGui.QWidget()
        self.widget.resize(ancho, alto)
        self.widget.setWindowTitle(titulo)
        self.definir_posicion(posicion_x, posicion_y)
        self.mostrar()

    def definir_posicion(self, x, y):
        if not x and not y:
            x, y = Componente.obtener_centro_escritorio()
            x -= self.width() / 2
            y -= self.height() / 2

        Componente.definir_posicion(self, x, y)

    def agregar(self, componente):
        componente.widget.setParent(self.widget)
        componente.mostrar()

    def confirmar(self, mensaje='sin mensaje'):
        botones = QtGui.QMessageBox.Yes|QtGui.QMessageBox.No
        respuesta = QtGui.QMessageBox.question(self.widget, 'Confirmar', mensaje, botones)
        return respuesta == QtGui.QMessageBox.Yes


class Boton(Componente):

    def __init__(self, etiqueta="sin etiqueta"):
        self.widget = QtGui.QPushButton(etiqueta)
        self.mostrar()


class Campo(Componente):

    def __init__(self, etiqueta="sin etiqueta", valor_inicial=""):
        self.widget = QtGui.QLineEdit()
        self.mostrar()


if __name__ == "__main__":
    iniciar()
    v = Ventana()
    b = Boton()
    v.agregar(b)
    v.agregar(Campo("Ingrese nombre"))
    b.definir_posicion(200, 100)
    v.confirmar("hola?")
