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


        
        
    comanod_select = """
        SELECT  *  FROM produtos;

"""
    cursor.execute(comanod_select)
    dados_exibir = cursor.fetchall()
    print(dados_exibir)
    conexao.commit()
    # Confirma e registra a alteração realizada no banco
    
    
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
inserir_produto('789000000020',
    'SKU020',
    'Mouse',
    12,
    '2032/09/10',
    'LOTE020',
    15,
    35.90)

# Chama a função para executar o processo

