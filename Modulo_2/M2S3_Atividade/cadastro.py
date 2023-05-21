import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
print('Insira os dados do cliente: ')
nome = input('Qual o nome do cliente? ')
cpf = input('Qual o cpf do cliente? ')
valores = [nome, cpf]
sql_inserir = 'INSERT INTO cliente (nome, cpf) values (?, ?)'
c.execute(sql_inserir, valores)
conn.commit()
conn.close()