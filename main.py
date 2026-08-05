from estoque import Estoque
from login_robusto.log_in import login, Criar_acesso_usuario, Acesso_usuario
from rich.console import Console
from rich.panel import Panel

console = Console()
estoque = Estoque()
cadastro = None



while True:
    console.print(
        Panel(
        "\n1 - Acessar o sistema\n"
        "2 - Criar usuário\n"
        "3 - Cadastrar produto\n"
        "4 - Inserir produto\n"
        "5 - Retirar produto\n"
        "6 - Listar produto\n"
        "7 - Sair",
        title="[bold white]MINI WMS[/bold white]",
        border_style="cyan",
        width=30
        )
    )

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if cadastro is None:
            console.print(
            Panel(
                "❌     Nenhum usuário \n       cadastrado.",
                border_style="red",
                width=30
            )
        ) 
            
        else:
            acesso = Acesso_usuario(cadastro)
    elif opcao == "2":
        cadastro = Criar_acesso_usuario()

    elif opcao == "3":
        codigo = input("Código: ")
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))
        estoque.cadastrar_produto(codigo, descricao, quantidade, valor_unitario)

    elif opcao == "4":
        codigo = input("Código: ") 
        quantidade = int(input("Quantidade: "))
        estoque.entrada(codigo,quantidade)

    elif opcao == "5":
        codigo = input("Código: ")
        quantidade = int(input("Quantidade: "))
        estoque.retirar(codigo,quantidade)
    
    elif opcao == "6":
        estoque.listar_produtos()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")



