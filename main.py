import sys
import os
from src.images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from src.mymail import sendQuickMail, sendAttachEmail

def main(args):
    imagen = "https://images.pexels.com/photos/13940670/pexels-photo-13940670.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    imagen2 = "https://images.pexels.com/photos/3866557/pexels-photo-3866557.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    image_path = "test.jpg"
    new_image = "imagen1.jpg"

    showImageFromURL(imagen)
    downloadImageFromUrl(imagen2, new_image)
    grayScaleImage(image_path)

    subject = "Test asunto"
    message = "Test mensaje"
    destination = "artain04@gmail.com"
    path = "test.jpg"

    sendAttachEmail(subject, message, destination, path)
    sendQuickMail(subject, message, destination)
    pregunta = input("borrar imagen1.jpg? \nSi o no: ")
    if pregunta.upper() == "SI":
        os.remove("imagen1.jpg")


if __name__ == "__main__":
    main(sys.argv)
