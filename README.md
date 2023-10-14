# ProyectoPython
Hola, bienvenido a mi biblioteca de python

# Instalación
Esta sección muestra como instalar el paquete **ProyectoPython**

Para instalar el paquete es necesario crear un entorno virtual:
```terminal
python -m venv venv
env\scripts\activate
pip install -r requirements.txt
```
Para utilizarlo solo debe importar las funciones al inicio de su módulo
```python
from ProyectoPython.images import showImageFromURL
from ProyectoPython.images import downloadImageFromUrl
from ProyectoPython.images import grayScaleImage

from ProyectoPython.mymail import sendAttachEmail
from ProyectoPython.mymail import sendQuickMail
```

## Funciones en images.py
* #### showImageFromURL
###### muestra y descarga una imagen desde una url.
* #### downloadImageFromUrl
###### descarga una imagen y la guarda en una ruta especifica desde una url.
* #### grayScaleImage
###### Convierte una imagen en blanco y negro.

## Funciones en mymail.py
* sendQuickMail
###### Envia un correo rapido.
* sendAttachEmail
###### Envia un correo con un archivo adjunto

## Referencias
Para ver el codigo fuente vaya a el repositorio de [Github](https://github.com/Esteban8604/MiProyecto)

Para ver la biblioteca vaya a [Testpypi](https://test.pypi.org/project/ProyectoPython/)

| Lenguaje | %   |
|----------| --- |
|Python    | 100%