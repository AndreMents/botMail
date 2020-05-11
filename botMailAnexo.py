import smtplib
import mimetypes 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
import os
import time


fromaddr = "cpd@metalurgicaimac.com.br" 
toaddr = "cpd@metalurgicaimac.com.br" 

msg = MIMEMultipart() 

msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "E-mail autimatico botMailImac"

body = ('''E-mail enviado automáticamente pelo botMailImac. Este é um E-mail de teste, desconsidere o mesmo.

Enviado por:botMailImac by André Oliveira''')
msg.attach(MIMEText(body)) 

filename = r'enviar\*.*' 
attachment = open(filename, "rb") 

mimetypes_anexo = mimetypes.guess_type(filename)[0].split('/') 
part = MIMEBase(mimetypes_anexo[0],mimetypes_anexo[1]) 

part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s"% filename)

msg.attach(part)

server = smtplib.SMTP('smtp.metalurgicaimac.com.br',587) 
server.starttls() 
server.login(fromaddr, open('senha.txt').read().strip()) 
text = msg.as_string() 
server.sendmail(fromaddr, toaddr, text)
server.quit()

from subprocess import Popen
p = Popen("move.bat", cwd=r"C:\Users\suporte-01\Desktop\botMailImac")
stdout, stderr = p.communicate()
