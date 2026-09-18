from abc import ABC, abstractmethod

from numpy import quantile
from banco import entrada_item, retirar_item
import banco


class Movimentacao(ABC):
    """
    Classe abstrata: define o contrato que Entrada e Saída têm que seguir.
    Não dá para fazer Movimentação(produto, 10) direto, só via sunclasse.
    """
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    @abstractmethod
    def executar(self):
        pass 

class Entrada(Movimentacao):
    def executar(self):
        self.produto.quantidade += self.quantidade
        entrada_item(self.produto.sku, self.quantidade)
        return f"Entrada de {self.quantidade} un. em {self.produto.descricao}"

class Saida(Movimentacao):
    def executar(self):
        if self.quantidade > self.produto.quantidade:
            # se a quantidade de retirada for maior que o saldo disponível, segue memsagem:
            raise ValueError("Saldo insuficiente para retirada.")
        self.produto.quantidade -= self.quantidade
        # caso o saldo seja disponível, a retirada segue apra ser executada
        retirar_item(self.produto.sku, self.quantidade)
        return f"Retirada de {self.quantidade} un. de {self.produto.descricao}"
        # retorna mensagem de quantidade retirada do produto com sua descrição.



