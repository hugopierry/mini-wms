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

df.info()
# inspeção geral
tipos_dados = df.dtypes
print(f"Todos os tipos de dados: \n{tipos_dados}")
# Mostra o tipo de dado de cada coluna
duplicados = df[df.duplicated(subset='sku', keep= False)]
print(f"Duplicados: {duplicados}")
# Verifica se existem códigos de barras duplicados

input("Pressione ENTER para sair do programa")
