gui
===

Una biblioteca muy simple para ayudar a construir aplicaciones gráficas en clases de programación.


**gui** utiliza pyqt4 cómo bilioteca soporte, solo que traduce algunas de sus funciones
mas utilizadas.


Primeros pasos
--------------

Puedes ingresar en una consola y descargar la biblioteca con este comando:

    wget https://raw.github.com/hugoruscitti/gui/master/gui.py


Luego puedes abrir un intérprete de python y comenzar a escribir:


<table>
<tr>
    <td><img style='img {box-shadow: 0px 0px 10px gray;}' src='https://raw.github.com/hugoruscitti/gui/master/imagenes/ventana.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
</pre>
    </td>
</tr>

<tr>
    <td><img style='img {box-shadow: 0px 0px 10px gray;}' src='https://raw.github.com/hugoruscitti/gui/master/imagenes/boton.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
boton = gui.Boton(ventana, "Pulse")
</pre>
    </td>
</tr>

<tr>
    <td><img style='img {box-shadow: 0px 0px 10px gray;}' src='https://raw.github.com/hugoruscitti/gui/master/imagenes/campo.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
boton = gui.Boton(ventana, "Pulse")
campo = gui.Campo(ventana, 'ingrese su nombre', 'Pepe')
</pre>
    </td>
</tr>

</table>

Integración con QtDesigner
--------------------------

Una forma mas sencilla de construir la interfaz de usuario es utilizar
QtDesigner, generar un archivo .ui y luego cargarlo desde gui:


    >>> import gui
    >>> ventana = gui.abrir("archivo.ui")

