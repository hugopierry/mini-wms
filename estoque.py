from produto import Produto

class Estoque():
    def __init__(self):
        self.produtos = {}
    
    def cadastrar_produto(self,codigo,descricao,quantidade, valor_unitario):
        if codigo in  self.produtos:
            print("Produto já cadastrado!")
        else:
           produto = Produto(codigo,descricao,quantidade,valor_unitario)
           self.produtos[codigo] = produto 
    
    def retirar(self,codigo,quantidade):
        try:
            if quantidade > self.produtos[codigo].quantidade:
                print("Saldo insuficinte para retirada.")
            else:
                self.produtos[codigo].quantidade -=quantidade
        except KeyError:
            print("Produto não encontrado!")
    
    def entrada(self, codigo, quantidade):
        try:
            self.produtos[codigo].quantidade +=quantidade
        except KeyError:
            print("Produto não cadastrado! Cadastre antes de dar entrada.")
    
    def listar_produtos(self):
        for produto in self.produtos.values():
            produto.exibir_produto()
            






