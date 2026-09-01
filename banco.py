import sqlite3
# Importa o SQLite


def conectar():
    # Define a função responsável pela conexão
    conexao = sqlite3.connect("mini_wms.db")
    # Cria a conexão com o banco de dados
    return conexao
    # Retorna a conexão


def criar_tabelas():
    # Função responsável por criar a tabela
    conexao = conectar()
    # Obtém a conexão com o banco
    cursor = conexao.cursor()
    # Cria o cursor para executar comandos SQL

    # Testei o comando SQL para garantir que os dados da tabela
    # usuarios não seriam alterados e, em seguida, criei a tabela produtos

    comando_sql = """
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY,
            codigo_barras TEXT,
            sku TEXT,
            descricao TEXT,
            caixaria INTEGER,
            validade TEXT,
            lote TEXT,
            quantidade INTEGER,
            valor_unitario REAL 
         
        );
    
    """

    cursor.execute(comando_sql)
    # Executa o comando SQL criado acima
       
    comando_select = """
        SELECT  *  FROM produtos;

"""
    cursor.execute(comando_select)
    dados_exibir = cursor.fetchall()
    # Comando que traz os dados de forma organizada ao exibir
    print("=" * 130)
    print("RELATÓRIO ITENS CADASTRADOS".center(50))
    print("=" * 130)
    print(
         f"{'ID':<10}"
    f"{'CÓDIGO DE BARRAS':<20}"
    f"{'SKU'}"
    f"{'DESCRIÇÃO':<15}"
    f"{'CAIXARIA':<15}"
    f"{'VALIDADE':<15}"
    f"{'LOTE':<15}"
    f"{'QUANTIDADE':<15}"
    f"{'VALOR UNITÁRIO':<15}"


    )
    # Cria as informações que serão os títulos das colunas
    print("-" * 130)

    for p in dados_exibir:
    # Percorre cada registro retornado pelo fetchall()
    # e imprime o relatório
        print(
        f"{p[0]:<10}"
        f"{p[1]:<20}"
        f"{p[2]}"
        f"{p[3]:<15}"
        f"{p[4]:<15}"
        f"{p[5]:<15}"
        f"{p[6]:<15}"
        f"{p[7]:<15}"
        f"{p[8]:<15}"
            
        )
       
    conexao.commit()
   
    # Exibe uma mensagem de confirmação

    conexao.close()
    # Fecha a conexão para finalizar o acesso ao banco
    

def cadastrar_item():
    conexao = conectar()
    cursor = conexao.cursor()
    print("CADASTRAR ITEM:")
    codigo_barras = int(input("Código de Barras: "))
    sku = input("SKU: ")
    descricao = input("Descrição: ")
    caixaria = int(input("Caixaria: "))
    validade = input("Validade: ")
    lote = input("Lote: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor Unitário: "))

    cursor.execute(

        """INSERT INTO produtos(
            
            codigo_barras,
            sku,
            descricao,
            caixaria,
            validade,
            lote,
            quantidade,
            valor_unitario
    )
    VALUES( ?, ?, ?, ?, ?, ?, ?, ?)""",
    (
       
        codigo_barras,
        sku,
        descricao,
        caixaria,
        validade,
        lote,
        quantidade,
        valor_unitario 
    ))
    

    conexao.commit()
    print(f"'{descricao}'cadastrado com sucesso!")
    # Mensagem de confirmação de registro
    conexao.close()


def deletar_item():
    conexao = conectar()
        
    cursor = conexao.cursor()
    # Comando criado para apagar um item via ID
    # que estava gerando erro no código
    print("EXCLUIR ITEM VIA SKU:".center(50))
    sku_produto = input("\nSKU do produto que deseja excluir: ").strip().upper()

    cursor.execute(

        "DELETE FROM produtos WHERE sku = ?",(sku_produto,))
    
    if cursor.rowcount > 0:
        conexao.commit()
        print("Item excluído com sucesso!")
    else:
        print("SKU não encontrado.")

    conexao.close()
def atualizar_item():
    conexao = conectar()
    cursor = conexao.cursor()

    print("ATUALIZAR ITEM:")
    # Inicia a atualização do item via SKU
    sku_atualizar = input("SKU do produto: ").strip().upper()
    # Esse é o SKU atual, usado para localizar qual cadastro será alterado.
    codigo_barras = int(input("Código de Barras: "))
    descricao = input("Descrição: ")
    caixaria = int(input("Caixaria: "))
    validade = input("Validade: ")
    lote = input("Lote: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor Unitário: "))

    # ATUALIZA produtos.db e DEFINE os novos dados
    cursor.execute(

        """UPDATE produtos 
        SET 
            
            codigo_barras = ?,
            descricao= ?,
            caixaria= ?,
            validade= ?,
            lote= ?,
            quantidade= ?,
            valor_unitario = ?
    WHERE sku = ? 
    """,
    (
    
   
        codigo_barras,
        descricao,
        caixaria,
        validade,
        lote,
        quantidade,
        valor_unitario,
        sku_atualizar,
        
    )
    
    )
    if cursor.rowcount > 0:
    # informa quantas linhas foram afetadas pelo último comando SQL.
        conexao.commit()
        print("Item atualizado com sucesso!")
    else:
        print("SKU não encontrado.")
    
    # Tupla com os novos valores que serão gravados no produto.
    # O sku_atualizar é usado pelo WHERE para localizar o registro.
    conexao.commit()
    
    conexao.close()

deletar_item()
cadastrar_item()
atualizar_item()
