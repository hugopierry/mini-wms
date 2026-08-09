
from rich.console import Console
from rich.panel import Panel



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
    
    @staticmethod
    def formatar_moeda(valor):
        return f"R$ {valor:,.2f}".replace(",","X").replace(".",",").replace("X",".")
    
    def exibir_produto(self):
        console = Console()

        console.print(
            Panel(
                f"Código: {self.codigo}\n"
                f"Descrição: {self.descricao}\n"
                f"Quantidade: {self._quantidade}\n"
                f"Valor Unitário: R${self.valor_unitario:.2f}".replace(",","X").replace(".",",").replace("X",".") +"\n"
                f"Total:{self.formatar_moeda(self.total)}",
                title="PRODUTO",
                border_style="green",
                width = 40,
                style="on #202020"

            )

        )