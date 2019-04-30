# Escrito por Alonso Canales.
# @aecanales - aecanales@uc.cl

import urllib
import bs4
import re
import os
import subprocess
import shutil
import zipfile

def get_page_soup(website: str) -> bs4.BeautifulSoup:
    ''' Retorna un BeautifulSoup de la página web solicitada. '''
    html_page = urllib.request.urlopen(website)
    return bs4.BeautifulSoup(html_page, features='html5lib')

def gather_links(soup: bs4.BeautifulSoup) -> list:
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

        if 'Older' in link.get_text():
            links.extend(gather_links(get_page_soup(link.get('href'))))

    return links

def filter_links(links: list) -> list:
    return [link for link in links if 'upload' in link]

if __name__ == "__main__":

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


