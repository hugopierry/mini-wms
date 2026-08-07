from rich.table import Table
from rich.console import Console



class Produto():
    def __init__(self, codigo, descricao, quantidade, valor_unitario):
        self.codigo = codigo
        self.descricao = descricao 
        self._quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.total = valor_unitario * quantidade
        
    @property
    def quantidade(self):
        return self._quantidade
    
    def exibir_produto(self):
        print(f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self._quantidade}\nValor Unitário: R${self.valor_unitario:.2f}\nTotal: R${self.total:.2f} ")



