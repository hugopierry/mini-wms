

import pandas as pd

from banco import conectar, buscar_produtos
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
# Verifica se existem SKUs duplicados

print("="*60)
print("Usando Loc[]")

dados_produto = df.loc[0,["descricao","quantidade","valor_unitario"]]
print(dados_produto)

print("\nDESAFIO".center(50))
print("\n1 - Quero todos os produtos cuja quantidade seja maior que 400:")

maior_que_400 = df["quantidade"] > 400


estoque_alto = df.loc[maior_que_400]
print(estoque_alto)


print("\n2 - Quero todos os produtos cuja quantidade seja menor que 50:")

menor_que_50 = df["quantidade"] <50
estoque_baixo = df.loc[menor_que_50]
print(estoque_baixo)

print("\n3 - Encontrar um produto pelo SKU e retornar sua descrição, quantidade e valor unitário:")

# variável
cond_sku = df["sku"] == "SKU004"

                    # loc[] condição pela variável  |              colunas
busca_pelo_sku = df.loc[cond_sku,["descricao","quantidade","valor_unitario"]]
print(busca_pelo_sku)

print("\n4 - Encontrar produtos com quantidade maior que 10 E valor unitário maior que R$ 50,00.")

est_maior_10 = df["quantidade"] > 10
valor_maior_50 = df["valor_unitario"] > 50

prod_filtrados = est_maior_10 & valor_maior_50

resultado = df.loc[prod_filtrados, ["sku","descricao","quantidade","valor_unitario"]]
print(resultado)

print("""\n5 - Preciso identificar os produtos que têm estoque acima de 100 unidades
E valor unitário acima de R$ 5,00.
Quero visualizar apenas SKU, descrição, quantidade e valor unitário.""")

estoque_acima_100 = df["quantidade"] > 100
valor_unit_5 = df["valor_unitario"] > 5

prod_novo_filtro = estoque_acima_100 & valor_unit_5

novo_resultado = df.loc[prod_novo_filtro,["sku","descricao","quantidade","valor_unitario"]]
print(novo_resultado)
