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

    def __init__(self, padre=None):
        if not Componente.app:
            iniciar()
        if padre:
            padre.agregar_a_grilla(self.widget)
            padre.mostrar()

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
        Componente.__init__(self)
        self.widget = QtGui.QWidget()

        self._grid = QtGui.QGridLayout()
        self._grid.setSpacing(10)
        self.widget.setLayout(self._grid)
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

    def confirmar(self, mensaje='sin mensaje'):
        botones = QtGui.QMessageBox.Yes|QtGui.QMessageBox.No
        respuesta = QtGui.QMessageBox.question(self.widget, 'Confirmar', mensaje, botones)
        return respuesta == QtGui.QMessageBox.Yes

    def alertar(self, mensaje=''):
        QtGui.QMessageBox.information(self.widget, 'Alerta', mensaje)

    def obtener_titulo(self):
        return str(self.widget.windowTitle())

    def definir_titulo(self, titulo):
        self.widget.setWindowTitle(titulo)

    titulo = property(obtener_titulo, definir_titulo)

    def agregar_a_grilla(self, widget):
        self._grid.addWidget(widget, self._grid.rowCount(), 0)



class Boton(Componente):

    def __init__(self, padre, etiqueta="sin etiqueta"):
        self.widget = QtGui.QPushButton(etiqueta)
        Componente.__init__(self, padre)

    def obtener_texto(self):
        return str(self.widget.text())

    def definir_texto(self, nuevo_valor):
        return self.widget.setText(nuevo_valor)

    texto = property(obtener_texto, definir_texto)

    def conectar_cuando_pulsa(self, funcion):
        QtCore.QObject.connect(self.widget, QtCore.SIGNAL('clicked()'), funcion)

    cuando_pulsa = property(None, conectar_cuando_pulsa)

class Campo(Componente):

    def __init__(self, padre, etiqueta="sin etiqueta", valor_inicial=""):
        layout = QtGui.QFormLayout()
        self.widget = QtGui.QWidget()
        self.input = QtGui.QLineEdit()
        self.label = QtGui.QLabel(etiqueta)
        layout.addRow(self.label, self.input)

        self.widget.setLayout(layout)
        Componente.__init__(self, padre)

class TextoLibre(Componente):

    def __init__(self, padre, etiqueta="sin etiqueta", valor_inicial=""):

        layout = QtGui.QFormLayout()
        self.widget = QtGui.QWidget()
        self.input = QtGui.QTextEdit()
        self.label = QtGui.QLabel(etiqueta)
        layout.addRow(self.label, self.input)

        self.widget.setLayout(layout)

        Componente.__init__(self, padre)



if __name__ == "__main__":
    iniciar()
    v = Ventana()
    a = Boton(v, "hola !")
    c = Boton(v, "Hacer una pregunta")
    b = Boton(v, "Emitir un saludo")

    def hacer_una_pregunta():
        respuesta = v.confirmar("Esta seguro?")
        print "Ha contestado", respuesta

    c.cuando_pulsa = hacer_una_pregunta

    def saludar():
        v.alertar("Hola!!!")

    b.cuando_pulsa = saludar

    texto = TextoLibre(v)
    campo = Campo(v)
