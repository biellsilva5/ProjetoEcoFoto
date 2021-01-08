from app import app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import timedelta, datetime
import jwt

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# username ou email para logar no servidor
username = 'coordenacaodeextensao@eco.ufrj.br'
password = 'triplex2016'

# enviar 
from_addr = 'Extensão EcoFoto<coordenacaodeextensao@eco.ufrj.br>'

def send_email(rementente:list, token):
    
    try:
        dec = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return 'Assinatura invalida.'
    except jwt.exceptions.ExpiredSignatureError:
        return 'Link expirado.'

    to_addrs = rementente
    message = MIMEMultipart('alternative')
    message['subject'] = 'Recuperação de senha.'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)


    html = """\
    <html>
    <head></head>
    <body>
        <p>Olá!<br>
        Recebemos uma solicitação para redefinir a senha de acesso a sua conta EcoFoto.<br>
        Use o link abaixo para finalizar a alteração:<br>
        <a href='http://agora.labnet.nce.ufrj.br/recuperar-senha?token="""+token+ """ 'target='_blank'>Alterar senha.</a><br>
        Caso o link acima não funcione, copie e cole no seu navegador:<br>
        http://agora.labnet.nce.ufrj.br/recuperar-senha?token="""+ token + """<br>

        
        
        </p>
    </body>
    </html>
    """

    part2 = MIMEText(html, 'html')

    message.attach(part2)


    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    try:
        server.sendmail(from_addr, to_addrs, message.as_string())
    except smtplib.SMTPRecipientsRefused:
        return 'Email invalido'
    server.quit()
    return token











