import sqlite3
# importa o sql


def conectar():
# Define a função de conexão
    conexao = sqlite3.connect("mini_wms.db")
    # conexão que integra ao banco de dados
    return conexao
    # após isso, é retornado a conexão.

def criar_tabelas():
# função para criar a tabela
    conexao = conectar()
    # define a conexão e inicia
    cursor = conexao.cursor()
    # cria o cursor para executar comandos SQL

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
    conexao.commit()
    print("Banco de dados para Produtos criado com sucesso!")
    conexao.close()

criar_tabelas()