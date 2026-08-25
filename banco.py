import sqlite3  



def conectar():
    conexao = sqlite3.connect("mini_wms.db")
    return conexao
            
def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

   
    comando_sql = """
    CREATE TABLE IF NOT EXISTS usuarios(
        matricula TEXT PRIMARY KEY,
        senha TEXT,
        nome TEXT
    );

"""
    cursor.execute(comando_sql)
    
    conexao.commit()
    conexao.close()
import os

def conectar():
    conexao = sqlite3.connect("mini_wms.db")
    print("Caminho do banco:", os.path.abspath("mini_wms.db"))
    return conexao