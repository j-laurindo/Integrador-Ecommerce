import smtplib
from email.mime.text import MIMEText

# Configurações do servidor de email
servidor_smtp = 'smtp.gmail.com'
porta = 587
usuario = 'jlaurindo0104@gmail.com'
senha = "chave de acesso do google"
# Conectando ao servidor
servidor = smtplib.SMTP(servidor_smtp, porta)
servidor.starttls()
servidor.login(usuario, senha)

# Criando a mensagem
assunto = "oi amg tudo bom?"
corpo = "Este email é um email enviado através de um script Python!"
mensagem = MIMEText