import requests
from PIL import Image
import uuid

def main():
    """Inicializador del codigo.

    """
    valor = input("Para descargar una imagen y mostrarla, digite 1.\n"
                  "Para descargar una imagen y guardarla en una ruta indicada, digite 2.\n"
                  "Para convertir una imagen a blanco y negro, digite 3.\n")
    if valor == "1":
        url = input("ingrese la url de la imagen: ")
        showImageFromURL(url)

    elif valor == "2":
        url = input("ingrese la url de la imagen: ")
        path = input("ingrese la ubicacion de la imagen. Ej: imagen1.jpg: ")
        downloadImageFromUrl(url, path)

    elif valor == "3":
        path = input("ingrese la ubicacion de la imagen: ")
        grayScaleImage(path)
    else:
        print("que?")


def showImageFromURL(url):
    """Descarga una imagen desde una URL y la muestra.

        Args:
        ^^^^^
            :url (str): URL que se usara para descargar la imagen.

        Returns:
        ^^^^^^^^
            :Nombre_archivo (str): Nombre de la imagen que se descargó.
    """
    respuesta = requests.get(url)
    nombre_archivo = "imagedownload.jpg"
    with open(nombre_archivo, mode="wb") as imagen:
        imagen.write(respuesta.content)
    imagen_descargada = Image.open(nombre_archivo)
    imagen_descargada.show()
    return nombre_archivo



def downloadImageFromUrl(url, path):
    """Descarga una imagen y la guarda en la ruta indicada.

        Args:
        ^^^^^
            :url (str): URL que se usara para descargar la imagen.

            :path (str): ruta en la que desea descargar la imagen.

    """
    respuesta = requests.get(url)
    with open(path, "wb") as file:
        file.write(respuesta.content)



def grayScaleImage(path):
    """Convierte una imagen a blanco y negro.

        Args:
        ^^^^^
            :path (str): Nombre de la imagen a convertir.

        Returns:
        ^^^^^^^^
            :Name (str): Nombre de la imagen en blanco y negro
    """
    name = "grayscaleimage.jpg"
    imagen = Image.open(path)
    grayscale_image = imagen.convert("L")
    grayscale_image.save(name)

    return name



if __name__=="__main__":
    main()