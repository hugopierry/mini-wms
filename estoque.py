

from produto import Produto
# Vem do arquivo produto e é importado
from banco import cadastrar_item, entrada_item, retirar_item , buscar_produtos # nunca esquecer de chamar o método criado no módulo anterior
# vem do arquivo banco.py


class Estoque():
    def __init__(self):
        self.produtos = {}

        produtos = buscar_produtos()

        for produto in produtos:
            novo_produto = Produto(
                produto[1],
                produto[2],
                produto[3],
                produto[4],
                produto[5],
                produto[6],
                produto[7],
                produto[8]
            )

            self.produtos[produto[2]] = novo_produto
            # usa o SKU (produto[2]) como chave do dicionário
            # e armazena o objeto novo_produto como valor
        


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
    
    def retirar(self,sku,quantidade):
        # função para retirar saldo, baseado em código e quantidade.
        try:
            if quantidade > self.produtos[sku].quantidade:
                print("Saldo insuficinte para retirada.")
                
                # se o valor retirado for maior que o valor disponível, o sisitem não permite e, infomra via print o motivo
            else:
                self.produtos[sku].quantidade -=quantidade
                retirar_item(sku, quantidade)
                # caso possua saldo suficiente, é realizado saída do estoque
        except KeyError:
            print("Produto não encontrado!")
            # se o produto não existir no cadastro, é infomrado via print
    
    def entrada(self, sku, quantidade):
        try:
            self.produtos[sku].quantidade += quantidade
            # Procura o SKU no dicionário e aumenta a quantidade em memória.
            entrada_item(sku, quantidade)
            # atualiza a quantidade no banco de dados.
        # Se o SKU não existir, informa ao usuário.
        except KeyError:
            print("Produto não encontrado!")
            
       
        
        

    def listar_produtos(self):
        for produto in self.produtos.values():
            produto.exibir_produto()
            # função para listar o que possui cadastrado na memória RAM.
            # O uso do FOR serve para organizar a exibição.


estoque = Estoque() 




