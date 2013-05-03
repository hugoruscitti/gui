gui
===

Una biblioteca muy simple para ayudar a construir aplicaciones gráficas en clases de programación.


**gui** utiliza pyqt4 cómo bilioteca soporte, solo que traduce algunas de sus funciones
mas utilizadas.


<table>
<tr>
    <td>Resultado</td>
    <td>
<pre>Código</pre>
    </td>
</td>
</table>


Todo
----

- [X] Mejorar la API para enparentar widgets.
- [X] Crear un layout 
- [X] Crear el widget TextoLibre
- [ ] Implementar etiquetas para los widgets Campo y TextoLibre.
- [ ] Documentar los ejemplos en este mismo archivo README.


Ejemplo básico
--------------

    import gui

    gui.iniciar()

    v = gui.Ventana()
    b = gui.Boton()

    v.agregar(b)

    v.confirmar("Te parece una buena idea?")
