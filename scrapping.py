# Escrito por Alonso Canales.
# @aecanales - aecanales@uc.cl
# https://github.com/aecanales/pv-scrapping

import os, re, shutil, subprocess, urllib, zipfile
import bs4  # BeautifulSoup4


def get_page_soup(website: str) -> bs4.BeautifulSoup:
    ''' Retorna un BeautifulSoup de la página web solicitada. '''
    html_page = urllib.request.urlopen(website)
    return bs4.BeautifulSoup(html_page, features='html5lib')

def gather_links(soup: bs4.BeautifulSoup) -> list:
    ''' 
    Recopila todos los enlances en el soup entregado.
    Si detecta un enlace a la página anterior de la misma categoría, 
    llama la función recursivamente para descargar los enlaces de esa página.
    '''
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

        if 'Older' in link.get_text():
            links.extend(gather_links(get_page_soup(link.get('href'))))

    return links

def filter_links(links: list) -> list:
    '''
    Filtra la lista de enlaces retornando sólo los que corresponden a una archivo.
    Es simple ahora pero se podria complejizar para descargar otros tipos de 
    contenido como videos de Youtube o imágenes.
    '''
    return [link for link in links if 'upload' in link]

def create_temporary_directory():
    ''' Crea un directorio temporal al cual descargar los archivos.'''
    os.mkdir('tmp')

def download_files_to_temporary_directory(links: list):
    ''' Descarga los archivos al directorio temporal usando wget. '''
    os.chdir('tmp')

    # Usar os.devnull nos permite usar el comando 'wget' sin que aparezca su output.
    # (en otras palabras, lo llamo sólo por razones estéticas)
    with open(os.devnull, 'w') as devnull:
        for link in links:
            print(f" {link}")
            subprocess.run(['wget', link], stdout=devnull, stderr=devnull)

    os.chdir('..')

def zip_files(zip_name: str):
    ''' Crea un ZIP de los archivos descargados. '''
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for file in os.listdir('tmp'):
            zip_file.write(os.path.join('tmp', file), file)

def delete_temporary_directory():
    ''' Elimina el directorio temporal y todos los archivos que contiene. '''
    shutil.rmtree('tmp')
