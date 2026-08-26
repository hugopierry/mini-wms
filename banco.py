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

    conexao.commit()
    # Confirma e registra a alteração realizada no banco

    print("Banco de dados para Produtos criado com sucesso!")
    # Exibe uma mensagem de confirmação

    conexao.close()
    # Fecha a conexão para finalizar o acesso ao banco


criar_tabelas()
# Chama a função para executar o processo