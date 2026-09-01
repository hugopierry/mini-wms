from produto import Produto
# Vem do arquivo produto e é importado
from banco import cadastrar_item
# vem do arquivo banco.py


class Estoque():
    def __init__(self):
        self.produtos = {}
        # # atualmente armazena em um dicionário, (na mémoria RAM), quando o sistema é fechado
        # os dados somem, pois foi um armazenamento temporáreo
        # por isso que o mesmo deverá ser integrado a um banco de dados
    
    def cadastrar_produto(self,codigo_barras,sku,descricao,caixaria,validade,lote,quantidade,valor_unitario):
        # função para cadastro. A mesma receberá atualização.
        if sku in  self.produtos:
            print("Produto já cadastrado!")
            # se o produto constar cadastrado, surge mensagem informanado isso e assim não se tornar possível o cadastramento.
        else:
                produto = Produto(
                    codigo_barras,
                    sku,
                    descricao,
                    caixaria,
                    validade,
                    lote,
                    quantidade,
                    valor_unitario
                )

                cadastrar_item(
                    codigo_barras,
                    sku,
                    descricao,
                    caixaria,
                    validade,
                    lote,
                    quantidade,
                    valor_unitario
                )
                self.produtos[sku] = produto 
                    # Recebe os parâmetros do método cadastrar_produto() 
                    # mantém o objeto no dicionário
    
    def retirar(self,codigo,quantidade):
        # função para retirar saldo, baseado em código e quantidade.
        try:
            if quantidade > self.produtos[codigo].quantidade:
                print("Saldo insuficinte para retirada.")
                # se o valor retirado for maior que o valor disponível, o sisitem não permite e, infomra via print o motivo
            else:
                self.produtos[codigo].quantidade -=quantidade
                # caso possua saldo suficiente, é realizado saída do estoque
        except KeyError:
            print("Produto não encontrado!")
            # se o produto não existir no cadastro, é infomrado via print
    
    def entrada(self, sku, quantidade):
        try:
            self.produtos[sku].quantidade +=quantidade
        except KeyError:
            print("Produto não cadastrado! Cadastre antes de dar entrada.")
            # função que gera entrada de saldo do produto via código. Se o produto não possui cadastro, não pode ser realziaod a entrada.
            # Isso é informado via print.
    
    def listar_produtos(self):
        for produto in self.produtos.values():
            produto.exibir_produto()
            # função para listar o que possui cadastrado na memória RAM.
            # O uso do FOR serve para organizar a exibição.






