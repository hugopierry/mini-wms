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
def inserir_produto(codigo_barras, sku, descricao, caixaria,
                    validade, lote, quantidade, valor_unitario):
        
    conexao = conectar()
    cursor = conexao.cursor()


    comando_inserir = """

    INSERT INTO produtos (
            codigo_barras,
            sku,
            descricao,
            caixaria,
            validade,
            lote,
            quantidade,
            valor_unitario
        )
        VALUES (?,?,?,?,?,?,?,?);
""" 
    cursor.execute(comando_inserir,(
        codigo_barras,
        sku,
        descricao,
        caixaria,
        validade,
        lote,
        quantidade,
        valor_unitario))
    conexao.commit()
    conexao.close()
criar_tabelas()
inserir_produto('789000000021',
    'SKU021',
    'Headphone',
    15,
    '2032/09/10',
    'LOTE021',
    15,
    186.90)


# Chama a função para executar o processo

def deletar_item():
    conexao = conectar()
        
    cursor = conexao.cursor()
    # Comando criado para apagar um item via ID
    # que estava gerando erro no código
    comando_deletar = """
    DELETE FROM produtos
        WHERE id = 1
    """
    cursor.execute(comando_deletar)
    conexao.commit()
    conexao.close()
deletar_item()