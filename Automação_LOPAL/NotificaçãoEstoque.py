import smtplib
import csv
from email.mime.text import MIMEText

# Extraindo as informações do arquivo csv
with open('DadosEsp.csv', 'r') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        coluna_1 = linha[0:1]
        coluna_2 = linha[1:2]
        coluna_3 = linha[2:3]
        coluna_4 = linha[3:4]
        coluna_5 = linha[4:5]

        data = coluna_1
        tempo = coluna_2
        esteira_1 = coluna_3
        esteira_2 = coluna_4
        esteira_3 = coluna_5

# Configurações do servidor de email
servidor_smtp = 'smtp.gmail.com'
porta = 587
usuario = 'juliarobertslaurindodasilva@gmail.com'
senha = "rlah lzbb vphm uurj"

# Conectando ao servidor
servidor = smtplib.SMTP(servidor_smtp, porta)
servidor.starttls()
servidor.login(usuario, senha)

# Criando a mensagem
assunto = "Status de Monitoramento do Estoque - As Terezas"
corpo = f"""Siga abaixo as informações em tempo real do sistema de estoque:

- Data: {data}
- Horário: {tempo}
- Esteira 1: {esteira_1}
- Esteira 2: {esteira_2}
- Esteira 3: {esteira_3}
"""
mensagem = MIMEText(corpo)
mensagem['Subject'] = assunto
mensagem['From'] = usuario
mensagem['To'] = 'bernardisenzo09@gmail.com'

# Enviando o email
servidor.send_message(mensagem)

# Fechando a conexão com o servidor
servidor.quit()