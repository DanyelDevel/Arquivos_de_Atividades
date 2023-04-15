import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor (id INT, name VARCHAR(100), endereço VARCHAR(250));')
conexao.commit()
conexao.close()
