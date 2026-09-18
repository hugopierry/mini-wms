from numpy import quantile
import pandas as pd

from banco import buscar_produtos
# Python, traga para este arquivo a função buscar_produtos 
# que está dentro do arquivo banco.py

dados = buscar_produtos()
# a variável 'dados',  recebe a função criada, buscar_produtos, já importada

df = pd.DataFrame(dados, columns=['id','codigo_barras','sku','descricao','caixaria','validade','lote','quantidade','valor_unitario'])
# DataFrame estrutura os dados retornados do banco em uma estrutura tabular do Pandas,
# com linhas e colunas nomeadas
   
print(df)

print("=="*60)

print("VALOR TOTAL DOS ITENS EM ESTOQUE (R$)\n".center(50))

df["valor_total"] = df["quantidade"] * df["valor_unitario"]
# criação da coluna 'valor_total', para colocar o cáuculo desejado
print(df)

print("=="*60)
print("TOP5, ITENS QUE REPRESENTAM MAIOR VALOR FINANCEIRO DENTRO DO ESTOQUE (R$):\n".center(50))

top5_itens_caros = df.nlargest(5, "valor_total")
print(top5_itens_caros)