gui
===

Una biblioteca muy simple para ayudar a construir aplicaciones gráficas en clases de programación.


**gui** utiliza pyqt4 cómo bilioteca soporte, solo que traduce algunas de sus funciones
mas utilizadas.

Ejemplo básico
--------------

    import gui

    gui.iniciar()

    v = gui.Ventana()
    b = gui.Boton()

    v.agregar(b)

    v.confirmar("Te parece una buena idea?")
