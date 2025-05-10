import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Configurações
remetente = 'raphaa.m.oliveira@gmail.com'  # seu Gmail
senha_app = 'jdkixrtemgpqkkpe'     # sua senha de aplicativo do Gmail
destinatario = 'raphael.macedo.oliveira@hotmail.com'  # destinatário

# Caminho do anexo
caminho_arquivo = r'C:\Users\usuario\Documents\PESSOAL\TI\EMAIL AUT RAPHAEL-PADRAO\RAPHAEL MACEDO TI.pdf'
nome_arquivo = os.path.basename(caminho_arquivo)

# Mensagem
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = 'Relatório Automático - TI'

# Corpo do e-mail
mensagem.attach(MIMEText('Olá,\n\nSegue em anexo o relatório de TI.\n\nAtenciosamente,\nRaphael Macedo', 'plain'))

# Anexa o PDF
with open(caminho_arquivo, 'rb') as anexo:
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(anexo.read())
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition', f'attachment; filename="{nome_arquivo}"')
    mensagem.attach(parte)

# Enviando o e-mail
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha_app)
    servidor.send_message(mensagem)
    servidor.quit()
    print("✅ E-mail enviado com sucesso!")
    
except Exception as e:
    print("❌ Erro ao enviar e-mail:", e)
