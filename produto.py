class Produto():
    def __init__(self,codigo, descricao,quantidade,valor_unitario):
        self.codigo = codigo
        self.descricao = descricao 
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.total = valor_unitario * quantidade
        # Essa variável recebe o valor unitário e multiplica pela quantidade, apresentando o total do item.
        # Será revisto, e terá essa informação atualzada.
    
    def exibir_produto(self):
        print(f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nValor Unitário: R${self.valor_unitario:.2f}\nTotal: R${self.total:.2f} ")

    """
    A classe Produto representa os dados de cada produto.
    A função exibir_produto() apresenta esses dados
    de forma organizada.
    """



