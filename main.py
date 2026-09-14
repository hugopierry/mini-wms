from estoque import Estoque
# Importa a classe Estoque do arquivo estoque.py.
from log_in_oficial import Criar_acesso_usuario, Acesso_usuario, login
# Importa as funções do login oficial.
from rich.console import Console
from rich.panel import Panel

console = Console()
estoque = Estoque()

acesso = login()

if acesso is False:
    exit()


while True:
    console.print(
        Panel(
        
        "\n1 - Cadastrar produto\n"
        "2 - Inserir produto\n"
        "3 - Retirar produto\n"
        "4 - Listar produto\n"
        "0 - Sair",
        title="[bold white]MINI WMS[/bold white]",
        border_style="cyan",
        width=30,
        style="on #1e293b"
        )
    )
    
    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":
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
    elif opcao == "2":
        sku = input("Informe o SKU em letras maiúsculas: ") 
        quantidade = int(input("Quantidade: "))
        estoque.entrada(sku,quantidade)
        # Condição que insere quantida via sku

    elif opcao == "3":
        sku = input("Informe o SKU em letras maiúsculas: ").strip()
        quantidade = int(input("Quantidade: "))
        estoque.retirar(sku,quantidade)
        # condição que retira saldo via código
    
    elif opcao == "4":
        estoque.listar_produtos()
        # condição que lista os dados atualizados, mesmo que em memória RAM
        
    elif opcao == "0":
        print("Saindo...")
        # condição que encerra o loop com break
        break
    else:
        print("Opção inválida!")
        # se for digita uma opção inexistente, é avisado via print




input("\nPressione ENTER para fechar...")