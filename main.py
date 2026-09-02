from estoque import Estoque
# Importa a classe Estoque do arquivo estoque.py.
from log_in_oficial import Criar_acesso_usuario, Acesso_usuario
# Importa as funções do login oficial.
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
        width=30,
        style="on #1e293b"
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
        codigo_barras = input("Código de barras: ")
        sku = input("SKU: ")
        descricao = input("Descrição: ")
        caixaria = int(input("Caixaria: "))
        validade = input("Validade: ")
        lote = input("Lote: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: ").replace(".","").replace(",","."))
        estoque.cadastrar_produto(
                                    codigo_barras,
                                    sku,
                                    descricao,
                                    caixaria,
                                    validade,
                                    lote,
                                    quantidade,
                                    valor_unitario
                                )
        # Integração do cadastro de produtos com o banco de dados.
        # Os dados recebidos pelo usuário são enviados ao estoque.py
        # e posteriormente gravados no SQLite através do INSERT.
    elif opcao == "4":
        sku = input("sku: ") 
        quantidade = int(input("Quantidade: "))
        estoque.entrada(sku,quantidade)
        # Condição que insere quantida via sku

    elif opcao == "5":
        codigo = input("Código: ")
        quantidade = int(input("Quantidade: "))
        estoque.retirar(codigo,quantidade)
        # condição que retira saldo via código
    
    elif opcao == "6":
        estoque.listar_produtos()
        # condição que lista os dados atualizados, mesmo que em memória RAM
        
    elif opcao == "7":
        print("Saindo...")
        # condição que encerra o loop com break
        break
    else:
        print("Opção inválida!")
        # se for digita uma opção inexistente, é avisado via print




