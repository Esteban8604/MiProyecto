import unittest
import os
from ProyectoPython.images import grayScaleImage, downloadImageFromUrl, showImageFromURL
from ProyectoPython.mymail import sendAttachEmail, sendQuickMail

class TestProyecto(unittest.TestCase,):

    def testdownload(self):

        url = "https://images.pexels.com/photos/4187560/pexels-photo-4187560.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        nombre = "imagetest.jpg"
        downloadImageFromUrl(url, nombre)
        self.assertTrue(
            os.path.exists(nombre)
        )

    def testgray(self):
        path = "test.jpg"
        test = grayScaleImage(path)
        self.assertTrue(
            os.path.exists(test)
        )

    def testshow(self):
        url = "https://images.pexels.com/photos/12312763/pexels-photo-12312763.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        test = showImageFromURL(url)
        self.assertTrue(
            os.path.exists(test)
        )

    def testquick(self):
        subject = "test subject"
        message = "test message"
        destination = "artain04@gmail.com"
        sendQuickMail(subject, message, destination)
        self.assertTrue(True)


    def testattach(self):
        subject = "test subject"
        message = "test message"
        destination = "artain04@gmail.com"
        path = "test.jpg"
        sendAttachEmail(subject, message, destination, path)
        self.assertTrue(True)

    def tearDown(self):
        images = [
            "imagetest.jpg",
            "imagedownload.jpg",
            "grayscaleimage.jpg"
        ]
        for imagenes in images:
            if os.path.exists(imagenes):
                os.remove(imagenes)
        return super().tearDown()


if __name__=="__main__":
    unittest.main()