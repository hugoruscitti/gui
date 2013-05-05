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
    <td><img src='https://raw.github.com/hugoruscitti/gui/master/ventana.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
</pre>
    </td>
</tr>

<tr>
    <td><img src='https://raw.github.com/hugoruscitti/gui/master/boton.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
boton = gui.Boton(ventana, "Pulse")
</pre>
    </td>
</tr>

<tr>
    <td><img src='https://raw.github.com/hugoruscitti/gui/master/campo.png'></td>
    <td>
<pre>import gui

ventana = gui.Ventana("Hola!")
boton = gui.Boton(ventana, "Pulse")
campo = gui.Campo(ventana, 'ingrese su nombre', 'Pepe')
</pre>
    </td>
</tr>

</table>
