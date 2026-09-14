import pandas as pd

from banco import conectar
# vá no arquivo banco.py e traga só a função conectar

conexao = conectar()
query = "SELECT * FROM produtos"
# FROM estoque significa "da tabela estoque".
# Guarda numa variável (query) só por organização

df = pd.read_sql(query, conexao)
# Aqui é o ponto central . pd.read_sql() recebe dois argumentos: 
# o que buscar (a query) e onde buscar (a conexão).
#  Ele executa esse SELECT no banco e já transforma o resultado direto num DataFrame — a estrutura de tabela do pandas (linhas e colunas, 
# tipo uma planilha em memória). 
# É por isso que chamamos a variável de df: é convenção pra "DataFrame".


print(df)
# Imprime no terminal as linhas, colunas bem alinhadas de forma otganizada

print(df.info())
# imprimi indícios de onde possa haver 'sujeiras' no arquivo

duplicados = df[df.duplicated(subset='codigo_barras', keep= False)]
print(f"Duplicados: {duplicados}")
