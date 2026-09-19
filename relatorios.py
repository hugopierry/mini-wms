
import pandas as pd

from banco import buscar_produtos
# Python, traga para este arquivo a função buscar_produtos 
# que está dentro do arquivo banco.py

dados = buscar_produtos()
# a variável 'dados',  recebe a função criada, buscar_produtos, já importada

df = pd.DataFrame(
    dados,
    columns=[
        'id',
        'codigo_barras',
        'sku',
        'descricao',
        'caixaria',
        'validade',
        'lote',
        'quantidade',
        'valor_unitario'
    ]
)

# DataFrame estrutura os dados retornados do banco em uma estrutura tabular do Pandas,
# com linhas e colunas nomeadas
   
print(df)

print("=="*70)

print("\nVALOR TOTAL DOS ITENS EM ESTOQUE (R$)\n".center(50))

df["valor_total"] = df["quantidade"] * df["valor_unitario"]
# criação da coluna 'valor_total', para colocar o cáuculo desejado
print(df)

print("=="*70)
print("\nTOP5, ITENS QUE REPRESENTAM MAIOR VALOR FINANCEIRO DENTRO DO ESTOQUE (R$):\n".center(50))

top5_itens_caros = df.nlargest(5, "valor_total")
print(top5_itens_caros)

print("=="*70)
print("\n1O PRODUTOS COM MAIOR QUANTIDADE EM ESTOQUE:\n".center(50))
top10_itens_maior_estoque = df.nlargest(10,"quantidade")
print(top10_itens_maior_estoque)

print("=="*70)
print("10 PRODUTOS QUE POSSUEM MAIOR QUANTIDADE EM ESTOQUE, COM SUAS DESCRIÇÕES E QUANTIDADES:\n".center(50))
top10_itens_desc_quant = df.nlargest(10,"quantidade")[["descricao","quantidade"]]
# busca os 10 itens com maior quantiade como referência, e traz suas descrições e quantidade
print(top10_itens_desc_quant)

print("=="*70)
print("5 PRODUTOS COM MAIOR VALOR FINANCEIRO EM ESTOQUE,COM SUAS DESCRIÇÕES, QUANTIDADE E VALOR R$:\n".center(50))
top5_maior_valor_quant_desc = df.nlargest(5,"valor_total")[["descricao","quantidade","valor_total"]]
# Primeiro, nlargest() busca os 10 maiores valores da coluna "quantidade".
# Depois, [["descricao", "quantidade"]] seleciona apenas essas duas colunas do resultado.
print(top5_maior_valor_quant_desc)

print("=="*60)
print("5 PRODUTOS COM MENOR QUANTIDADE EM ESTOQUE, COM SUAS DESCRIÇÕES, SKU E QUANTIADE:\n".center(50))
top5_itens_menor_quant_sku_desc = df.nsmallest(5,"quantidade")[["sku","descricao","quantidade"]]
# nsmallest() busca os 5 menores valores usando "quantidade" como critério.
# Depois, seleciono apenas SKU, descrição e quantidade do resultado.
print(top5_itens_menor_quant_sku_desc)