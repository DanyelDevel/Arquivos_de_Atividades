import sqlite3
import datetime
conn = sqlite3.connect('database.db')
print('Insira os dados do Pedido: ')
client_id = input('Qual o id do cliente: ')
hoje = datetime.date.today()
valores = [client_id, hoje]
sql_pedido = 'INSERT INTO pedido (cliente_id, data) values (?, ?)'
c = conn.cursor()
c.execute(sql_pedido, valores)
print('ID do pdeido: ', c.lastrowid)
pedido_id = c.lastrowid
quantidade_item = input("Quantos itens deseja adicionar? ")
quantidade_item = int(quantidade_item)

for i in range(quantidade_item):
    produto = input('Qual o produto? ')
    quantidade = input('Qual a quantidade? ')
    quantidade = int(quantidade)
    valor = input('Qual o valor? ')
    valor = float(valor)
    sql_item = '''
    INSERT INTO item_pedido (
    pedido_id, produto, valor, quantidade
    )
    values (?, ?, ?, ?)
    '''
    valores = [pedido_id, produto, valor, quantidade]
    c.execute(sql_item, valores)

conn.commit()
conn.close()
