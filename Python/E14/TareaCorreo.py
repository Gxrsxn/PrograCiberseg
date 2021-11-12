import argparse
import smtplib
import getpass
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email import encoders

#Gerson Hiram Alcocer Jimenez

correo1 = input("Ingresa el correo desde donde se enviara el meme: ")
pwd = getpass.getpass()
correo2 = input("Ingresa el destinatario: ")
asunto = input("Ingresa el asunto: ")
text = input("Ingresa el cuerpo del correo: ")
mensaje = MIMEText(text)
msg = MIMEMultipart()
msg['From']=correo1
msg['To']=correo2
msg['Subject']=asunto
imagen = input("Ingresa el nombre de la imagen: ")
file = open(imagen, "rb")
attach_image = MIMEImage(file.read())
attach_image.add_header('Content-Disposition', 'attachment; filename = "imagen.jpg"')
msg.attach(attach_image)
msg.attach(mensaje)


#Se auntentifica el correo, se envia y luego se cierra la conexión 

mailServer = smtplib.SMTP('smtp.office365.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(correo1,pwd)

mailServer.sendmail(correo1, correo2, msg.as_string())

mailServer.close()



