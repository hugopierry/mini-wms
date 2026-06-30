from produto import Produto

class Estoque():
    def __init__(self):
        self.produtos = {}
    
    def cadastrar_produto(self,codigo,descricao,quantidade):
        if codigo in  self.produtos:
            print("Produto já cadastrado!")
        else:
           produto = Produto(codigo,descricao,quantidade)
           self.produtos[codigo] = produto 
    
    def retirar(self,codigo,quantidade):
        if quantidade > self.produtos[codigo].quantidade:
            print("Saldo insuficinte para retirada.")
        else:
            self.produtos[codigo].quantidade -=quantidade


