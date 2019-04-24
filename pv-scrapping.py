# Escrito por Alonso Canales basado en PythonSpot.
# @aecanales - aecanales@uc.cl
# https://pythonspot.com/extract-links-from-webpage-beautifulsoup/

import urllib
import bs4
import re
import os
import subprocess

WEBSITE = 'http://catalinacortazar.com/PensamientoVisual/?cat='

print("-" * 25 + "\n" + "DESCARGADOR TAREAS IDI1015" + "\n" + "-" * 25)

category = input("Indica la categoría de la tarea que deseas descargar.\n(Los dígitos en http://catalinacortazar.com/PensamientoVisual/?cat=XXX)\n")

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

with open(os.devnull, 'w') as devnull:
    for link in links[0:1]:
        print(f" {link}")
        subprocess.run(['wget', link], stdout=devnull, stderr=devnull)

print("¡Descargado!")