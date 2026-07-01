from estoque import Estoque

from login import fazer_login

fazer_login()

estoque = Estoque()

while True:
    print("="*30)
    print("MINI WMS".center(30))
    print("="*30)
    print("1 - Cadastrar produto")
    print("2 - Dar entrada")
    print("3 - Retirar")
    print("4 - Listar produtos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Código: ")
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))
        estoque.cadastrar_produto(codigo, descricao, quantidade, valor_unitario)

    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        estoque.listar_produtos()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")



