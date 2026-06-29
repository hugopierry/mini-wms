class Produto():
    def __init__(self,codigo, descricao,quantidade,valor_unitario):
        self.codigo = codigo
        self.descricao = descricao 
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.total = valor_unitario * quantidade
    
    def exibir_produto(self):
        print(f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nValor Unitário: R${self.valor_unitario:.2f}\nTotal: R${self.total:.2f} ")

print("DADOS PRODUTO".center(30))
p1 = Produto(1234,"Paracetamol",137,2.90)
p1.exibir_produto()


