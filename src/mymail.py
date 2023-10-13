import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

def main():
    """Funcion main
    """
    valor = input("1 para enviar correo rapido o 2 para enviar correo adjunto: ")
    subject = input(str("ingrese el asunto del correo: "))
    message = input(str("ingrese el mensaje del correo: "))
    destino = input(str("ingrese la direccion a la que quiere enviar el correo: "))
    if valor == "1":
        sendQuickMail(subject, message, destino)
    else:
        path = input(str("ingrese el nombre del archivo: "))
        sendAttachEmail(subject, message, destino, path)


    
def sendQuickMail(subject:str, message:str, destination:str):
    """Envía un correo electrónico rápido al destino indicado.
        Args:
            subject (str): Asunto del correo electronico
            message (str): Mensaje que se enviara en el correo
            destination (str): direccion a la cual se enviara el correo
    """

    mail = input(str("Ingrese su correo electronico: "))
    password = input(str("Ingrese su contraseña: "))

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject
    mensaje["From"] = mail
    mensaje["To"] = destination
    mensaje.attach(MIMEText(message, 'plain'))
    
    hilo = threading.Thread(target=enviar_correo, args=(mail, password, mensaje, destination))
    hilo.start()
    
    

def sendAttachEmail(subject:str, message:str, destination:str, path:str):
    """Envía un correo electrónico con un archivo adjunto a la dirección indicada.
        Args:
            subject (str): Asunto del correo electronico
            message (str): Mensaje que se enviara en el correo
            destination (str): direccion a la cual se enviara el correo
            path (str): Direccion del archivo que se enviara en el correo
    """
    mail = input(str("Ingrese su correo electronico: "))
    password = input(str("Ingrese su contraseña: "))

    mensaje = MIMEMultipart()

    mensaje["Subject"] = subject
    mensaje["From"] = mail
    mensaje["To"] = destination 

    mensaje.attach(MIMEText(message, 'plain'))

    adjunto = MIMEBase("application", "octet-stream")

    with open(path, mode= "rb") as archivo:
        adjunto.set_payload(archivo.read())

    encoders.encode_base64(adjunto)

    adjunto.add_header(
        "Content-Disposition",
        f"attachment; filename={path}",
    )

    mensaje.attach(adjunto)

    hilo = threading.Thread(target=enviar_correo, args=(mail, password, mensaje, destination))
    hilo.start()
    


def enviar_correo(mail:str, password:str, message:str, destination:str):
    """Envia un correo electronico
        Args:
            mail (str): Correo con el que se iniciara sesion.
            password (str): Contraseña para ingresar al correo previamente solicitado
            message (str): El mensaje que se enviara en el correo
            destination (str): direccion a la cual se enviara el correo
            """
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(mail, password)

            server.sendmail(mail, destination, message.as_string())

    except smtplib.SMTPAuthenticationError as e:
        raise Exception("Error de autenticación: Verifica tu correo y contraseña.")
    except smtplib.SMTPException as e:
        raise Exception("Error al enviar el correo.")


if __name__=="__main__":
    main()