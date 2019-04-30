# Escrito por Alonso Canales.
# @aecanales - aecanales@uc.cl

import scrapping

WEBSITE = 'http://catalinacortazar.com/PensamientoVisual/?cat='

print("-" * 25 + "\n" + "DESCARGADOR TAREAS IDI1015" + "\n" + "-" * 25)

category = input("Indica la categoría de la tarea que deseas descargar.\n(Los dígitos en http://catalinacortazar.com/PensamientoVisual/?cat=XXX)\n")
zip_name = input("Indica el nombre que deseas para el .zip.\n")

print("Buscando página...")

soup = scrapping.get_page_soup(WEBSITE + category)

print("Recopilando enlaces...")

links = scrapping.gather_links(soup)

print("Filtrando enlaces...")

links = scrapping.filter_links (links)

for link in links:
    print(link)
