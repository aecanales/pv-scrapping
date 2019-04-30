# Escrito por Alonso Canales.
# @aecanales - aecanales@uc.cl

import urllib
import bs4
import re
import os
import subprocess
import shutil
import zipfile

WEBSITE = 'http://catalinacortazar.com/PensamientoVisual/?cat='

print("-" * 25 + "\n" + "DESCARGADOR TAREAS IDI1015" + "\n" + "-" * 25)

category = input("Indica la categoría de la tarea que deseas descargar.\n(Los dígitos en http://catalinacortazar.com/PensamientoVisual/?cat=XXX)\n")
zip_name = input("Indica el nombre que deseas para el .zip.\n")

print("Buscando página...")

html_page = urllib.request.urlopen("http://catalinacortazar.com/PensamientoVisual/?cat=" + category)
soup =  bs4.BeautifulSoup(html_page, features='html5lib')

print("Recopilando enlaces...")

links = []
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

# Probalemente podria realizar el filtro en el comando previo pero no entiendo bien como funciona findAll :c
print("Filtrando enlaces...")

links = [link for link in links if 'upload' in link]

print(f"{len(links)} archivos encontrados. Descargando...")

os.mkdir('tmp')
os.chdir('tmp')

# Usar os.devnull nos permite usar el comando 'wget' sin que aparezca su output.
# (en otras palabras, lo llamo sólo por razones estéticas)
with open(os.devnull, 'w') as devnull:
    for link in links:
        print(f" {link}")
        subprocess.run(['wget', link], stdout=devnull, stderr=devnull)

os.chdir('..')

print("Comprimiendo...")

with zipfile.ZipFile(zip_name, 'w') as zip_file:
    for file in os.listdir('tmp'):
        zip_file.write(os.path.join('tmp', file), file)

print("Borrando archivos temporales...")

shutil.rmtree('tmp')

input('Listo! Apriete cualquier botón para cerrar.')


