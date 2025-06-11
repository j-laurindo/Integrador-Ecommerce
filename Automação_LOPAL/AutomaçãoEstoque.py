import csv
import pandas as pd, openpyxl

# Leitura dos dados CSV
dados = pd.read_csv("DadosEsp.csv", sep=",")
dados.to_excel('DadosEsp.xlsx', index=False)
tabela_html = dados.to_html()

#Criação da Página HTML
pagina_html = f"""<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Teste</title>
    </head>
    <body>
        <h1>Status das Esteiras - Monitoramento de Estoque</h1>
        <section>{tabela_html}</section>
    </body>
    </html>
"""

with open("status.html", "w", encoding="UTF-8") as f:
    f.write(pagina_html)

with open("status.html", "r", encoding="UTF-8") as f:
    conteudo_pagina = f.read()
    print(conteudo_pagina)





