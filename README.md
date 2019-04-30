# pv-scrapping
Script escrito en Python 3.6 para bajar trabajos de la página web del curso Pensamiento Visual. Requiere el módulo ``bs4`` el cuál se puede instalar mediante el comando en terminal ``pip install bs4``. Si no funciona, asegúrate que estas corriendo el terminal como administrador. 

Para correrlo, baja ambos archivos ``.py`` y ejecuta ``main.py``. Te preguntará el número de la categoría de la tarea en la página (los dígitos en http://catalinacortazar.com/PensamientoVisual/?cat=XXX) y el nombre del *.zip* final. Descargará todos los archivos automáticamente y los comprimirá en un *.zip* con el nombre que indicaste.

## Ideas para el futuro
* Poder descargar otros tipos de tareas (imágenes, enlaces a Youtube)
* Dividir automáticamente en dos *.zip* por sección según la lista de alumnos.