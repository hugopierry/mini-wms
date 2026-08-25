import sqlite3

conexao = sqlite3.connect(r"C:\Users\hugop\OneDrive\Desktop\MINI WMS\mini_wms.db")
cursor = conexao.cursor()

cursor.execute("""
   UPDATE usuarios
   SET nome = ?
   WHERE matricula = ?

""", ("Freeza", 10011,))



conexao.commit()

print("Banco de dados criado com sucesso!")

conexao.close()