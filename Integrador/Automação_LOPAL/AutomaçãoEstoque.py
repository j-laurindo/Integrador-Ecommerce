import csv
import pandas as pd

# Leitura dos dados CSV
df = pd.read_csv("DadosEsp.csv", sep=",")
tabela_html = df.to_html()

with open('status.html', 'w') as f:
    tabela = f.write(tabela_html)
    print("Tabela HTML escrito com sucesso!")

#Criação da Página HTML
pagina_html = f"""<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Teste</title>
    </head>
    <body>
        <h1>Status das Esteiras - Monitoramento de Estoque</h1>
        <section>{tabela}</section>
    </body>
    </html>
"""

with open("status.html", "w", encoding="UTF-8") as f:
    f.write(pagina_html)

with open("status.html", "r", encoding="UTF-8") as f:
    conteudo_pagina = f.read()
    print(conteudo_pagina)





"""
with open("DadosEsp.csv", "r") as csvfile:
    arquivo_csv = csv.reader(csvfile, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print(str(linha))
        else:
            print(str(linha))
"""
