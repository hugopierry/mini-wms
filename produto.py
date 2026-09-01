class Produto():
    def __init__(self, codigo_barras, sku,descricao,caixaria, validade, lote, quantidade, valor_unitario):
        
        self.codigo_barras = codigo_barras
        self.sku = sku
        self.descricao = descricao
        self.caixaria = caixaria
        self.validade = validade
        self.lote = lote
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def exibir_produto(self):
        print(f"Código de barras: {self.codigo_barras}\n"
              f"SKU: {self.sku}\n"
              f"Descrição: {self.descricao}\n"
              f"Caixaria: {self.caixaria}\n"
              f"Validade: {self.validade}\n"
              f"Lote: {self.lote}\n"
              f"Quantidade: {self.quantidade}\n"
              f"Valor unitário: {self.valor_unitario}")

    """
    A classe Produto representa os dados de cada produto.
    A função exibir_produto() apresenta esses dados
    de forma organizada.
    """

   


