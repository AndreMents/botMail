#coding: utf-8
# Developer: Derxs
# Version: 1.2
from tkinter import *
from functools import partial
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import smtplib, os

def main():
	janela = Tk()

	def clickBtn(botao):
		if botao['text'] == 'Entrar':
			global servidor, email, senha

			email = "cpd@metalurgicaimac.com.br"
			senha = "sup@18"
			
			servidor = smtplib.SMTP('smtp.metalurgicaimac.com.br:587')
			servidor.starttls()
			servidor.ehlo()
			
			try:
				servidor.login(email, senha)
				status_code['foreground'] = '#00CD00'
				status_code['text'] = 'online'

				bt2['text'] = 'Enviar e-mail'
				bt['text'] = 'Sair'
			except smtplib.SMTPAuthenticationError:
				status_code['text'] = 'e-mail ou senha inválidos'
				servidor.quit()
			except TypeError:
				status_code['text'] = 'preencha os campos abaixo'
			except:
				status_code['text'] = 'você conseguiu me bugar, parabéns!'
		
		elif botao['text'] == 'Ativar':
			if os.name == 'posix':
				os.system('x-www-browser https://myaccount.google.com/lesssecureapps?pli=1')
			else:
				os.system('start iexplore.exe https://myaccount.google.com/lesssecureapps?pli=1')
		
		elif botao['text'] == 'Sair':
			servidor.quit()
			status_code['text'] = 'offline'
			status_code['foreground'] = '#EE0000'

			email_input.delete(0, END)
			senha_input.delete(0, END)
			
			bt2['text'] = 'Entrar'
			bt['text'] = 'Ativar'

		elif botao['text'] == 'Enviar e-mail':
			envia = Tk()

			def click(botao):
				if botao['text'] == 'Enviar':
					try:
						titulo_vai = titulo_input.get()
						email_vai = destino_input.get()
						msg = mensagem_input.get()
						arquivo_vai = arquivo_input.get()
						arquivo_tipo = arquivo_tipo_input.get()

						if(arquivo_vai != '') and (arquivo_tipo_input != ''):
							miemail = MIMEMultipart()
							miemail["From"] = email
							miemail["To"] = email_vai
							miemail["Subject"] = titulo_vai
							msgText = MIMEText('{}<br><img src="cid:{}"><br>'.format(msg, arquivo_vai), 'html')

							msg_file = MIMEBase('application', arquivo_tipo)

							msg_file.set_payload(open(arquivo_vai, 'rb').read())
							
							encode_base64(msg_file)

							msg_file.add_header('Content-Disposition', 'attachment', filename=arquivo_vai)

							miemail.attach(msgText)
							miemail.attach(msg_file)

							servidor.sendmail(email, miemail["To"].split(", "), miemail.as_string())
						else:
							miemail = MIMEMultipart()
							miemail["From"] = email
							miemail["To"] = email_vai
							miemail["Subject"] = titulo_vai
							msgText = MIMEText('{}'.format(msg), 'html')
							miemail.attach(msgText)

							servidor.sendmail(email, miemail["To"].split(", "), miemail.as_string())
						
							status_code_envio['text'] = 'e-mail enviado com sucesso'
							status_code_envio['foreground'] = '#00CD00'
					except:
						status_code_envio['text'] = 'e-mail não enviado'
						status_code_envio['foreground'] = '#EE0000'
				else:
					envia.destroy()

			status_envio = Label(envia, text='Status:', background='#E8E8E8')
			status_envio.place(x=1, y=1)

			status_code_envio = Label(envia, text='nenhum e-mail enviado', background='#E8E8E8')
			status_code_envio.place(x=60, y=1)

			destino = Label(envia, text='Destino: ', background='#E8E8E8')
			destino.place(x=55, y=100)

			titulo = Label(envia, text='Título: ', background='#E8E8E8')
			titulo.place(x=55, y=130)

			mensagem = Label(envia, text='Mensagem: ', background='#E8E8E8')
			mensagem.place(x=55, y=160)

			arquivo = Label(envia, text='Arquivo: ', background='#E8E8E8')
			arquivo.place(x=55, y=190)

			arquivo_tipo = Label(envia, text='Tipo de arquivo:', background='#E8E8E8')
			arquivo_tipo.place(x=55, y=220)
			
			destino_input = Entry(envia)
			destino_input.place(x=190, y=100)

			titulo_input = Entry(envia)
			titulo_input.place(x=190, y=130)

			mensagem_input = Entry(envia)
			mensagem_input.place(x=190, y=160)

			arquivo_input = Entry(envia)
			arquivo_input.place(x=190, y=190)

			arquivo_tipo_input = Entry(envia)
			arquivo_tipo_input.place(x=190, y=220)

			envia_botao = Button(envia, text='Enviar')
			envia_botao['command'] = partial(click, envia_botao)
			envia_botao.place(x=190, y=280)

			cancela = Button(envia, text='Cancelar envio')
			cancela['command'] = partial(click, cancela)
			cancela.place(x=190, y=320)

			envia_botao.configure(font='10', border=0, foreground='#FFF', background='#00FF7F', activebackground='#FFF', activeforeground='#00FF7F',  width=18)
			cancela.configure(font='10', border=0, foreground='#FFF', background='#00FF7F', activebackground='#FFF', activeforeground='#00FF7F',  width=18)

			arquivo_input.configure(font='10', highlightbackground='#00FF7F')
			arquivo_tipo_input.configure(font='10', highlightbackground='#00FF7F')
			destino_input.configure(font='10', highlightbackground='#00FF7F')
			titulo_input.configure(font='10', highlightbackground='#00FF7F')
			mensagem_input.configure(font='10', highlightbackground='#00FF7F')

			status_envio.configure(font='5')
			status_code_envio.configure(font='5')
			destino.configure(font='10')
			titulo.configure(font='10')
			mensagem.configure(font='10')
			arquivo.configure(font='10')
			arquivo_tipo.configure(font='10')
			envia.configure(background='#E8E8E8')

			envia.title('MailPy - Enviar e-mail')
			envia.geometry("420x400+500+150")
			envia.mainloop()


	status = Label(janela, text='Status:', background='#E8E8E8')
	status.place(x=1, y=1)

	status_code = Label(janela, text='offline', background='#E8E8E8')
	status_code.place(x=60, y=1)

	email = Label(janela, text='E-mail: ', background='#E8E8E8')
	email.place(x=55, y=100)

	senha = Label(janela, text='Senha: ', background='#E8E8E8')
	senha.place(x=55, y=130)

	email_input = Entry(janela)
	email_input.place(x=120, y=100)

	senha_input = Entry(janela)
	senha_input.place(x=120, y=130)

	bt2 = Button(janela, text='Entrar')
	bt2['command'] = partial(clickBtn, bt2)
	bt2.place(x=120, y=180)

	bt = Button(janela, text='Ativar')
	bt['command'] = partial(clickBtn, bt)
	bt.place(x=120, y=220)

	bt2.configure(font='10', border=0, foreground='#FFF', background='#00FF7F', activebackground='#FFF', activeforeground='#00FF7F',  width=18)
	bt.configure(font='10', border=0, foreground='#FFF', background='#00FF7F', activebackground='#FFF', activeforeground='#00FF7F',  width=18)

	email.configure(font='10')
	email_input.configure(font='10', highlightbackground='#00FF7F')
	senha.configure(font='10')
	senha_input.configure(font='10', show='*', highlightbackground='#00FF7F')
	status.configure(font='5')
	status_code.configure(font='5', foreground='#EE0000')
	janela.configure(background='#E8E8E8')

	janela.title("MailPy - Gmail")
	janela.geometry("420x300+500+150")
	janela.mainloop()

main()